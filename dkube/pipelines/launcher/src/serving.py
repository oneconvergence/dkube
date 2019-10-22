"""Dkube Pipeline Component Launcher

Usage:
    serving.py [--name=NAME] [--token=TOKEN] [--container=CONTAINER] [--script=SCRIPT] [--envs=ENVS] [--program=PROGRAM] [--datasets=DATASETS] [--models=MODELS] [--ngpus=NGPUS] [--config=CONFIG] [--runid=RUNID]
    training.py (-h | --help)
    training.py --version

Options:
    -h --help                           Show this screen.
    --version                           Show version.
    --name=NAME                         User specified name of the pipeline stage
    --token=TOKEN                       Authentication token of logged in user
    --container=CONTAINER               Container to be launched for the job. 
                                        Format: '{'image':<path>,'username':<user>,'password':<password>}'
    --script=SCRIPT                     Startup script to be executed inside container
    --envs=ENVS                         Env variables to be passed to the DL program
    --program=PROGRAM                   Selected program to be executed inside container
    --datasets=DATASETS                 List of input datasets for DL program. Format: '['<dataset>', '<dataset>']'
    --models=MODELS                     List of input models for DL program. Format: '['<model>', '<model>']'
    --ngpus=NGPUS                       Number of gpus required for the program.
    --config=CONFIG                     Configuration for the program.
    --runid=RUNID                       Unique ID of the pipeline run for back reference.
"""

from .docopt import docopt
from pyfiglet import Figlet
import json

def validate_container(container):
    container = json.loads(container)
    assert type(container) == dict, "container argument invalid format. See help"
    assert 'image' in container.keys(), "Container argument invalid format. Missing image key. See help"

def validate(**kwargs):
    #There are some parameters which are mandatory
    assert kwargs['--name'] != None, "--name is missing. Must be specified."
    assert kwargs['--token'] != None, "--token is missing. Must be specified."
    assert kwargs['--runid'] != None, "--runid is missing. Must be specified."

    assert kwargs['--container'] != None, "--container is missing, Must be specified."
    validate_container(kwargs['--container'])


def transform(**kwargs):
    data = {}
    for key, val in kwargs.items():
        data[key.lstrip('--')] = val

    data['container'] = json.loads(data['container'])

    data['envs'] = json.loads(data['envs']) if data['envs'] else None
    data['datasets'] = json.loads(data['datasets']) if data['datasets'] else None
    data['models'] = json.loads(data['models']) if data['models'] else None
    data['ngpus'] = int(data['ngpus'])
    return data

import os

from dkube.sdk.dkube import *
from dkube.sdk._types import *

def generate_outputs(env, name):
    model = get_trained_model(env, name)
    with open("/tmp/trainedmodel") as op:
        op.write(model)

    job = training_job(env, name)
    with open("/tmp/rundetails") as op:
        op.write(job.to_json())

def serving(**kwargs):
    #extract user from supplied token
    #_extract_user_from_token(token)
    user = 'ocdkube'
    env = Environment(host='dkube-d3api.dkube', port=5000, user=user, token=kwargs['token'])
    args = {}
    args.update({
            'container':ContainerImage.from_dict(kwargs['container']),
            'workspace':kwargs['program'] or '',
            'script':kwargs['script'] or '',
            'models':kwargs['models'] or [],
            'datasets':kwargs['datasets'] or [],
            'ngpus':kwargs['ngpus'] or 0
            })

    #this will also wait for job to complete (success/failed)
    launch_serving_job(kwargs['name'], autogenerate=True, environ=env.external, **args)

    #generate the outputs, next stage can pick from here
    generate_outputs(env.external, kwargs['name'])

def main():
    args = docopt(__doc__, version='1.4')
    validate(**args)
    args = transform(**args)

    f = Figlet(font='slant')
    print(f.renderText('Dkube Serving'))

    serving(**args)
