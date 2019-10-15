"""Dkube Pipeline Component Launcher

Usage:
    cmd.py [--name=NAME] [--token=TOKEN] [--container=CONTAINER] [--script=SCRIPT] [--envs=ENVS] [--program=PROGRAM] [--datasets=DATASETS] [--models=MODELS] [--ngpus=NGPUS] [--distributeopts=DISTRIBUTEOPTS] [--config=CONFIG] [--tuning=TUNING] [--runid=RUNID]
    cmd.py (-h | --help)
    cmd.py --version

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
    --distributeopts=DISTRIBUTEOPTS     Distribution options. Format: '{'workers':<count>, 'ps':<ps>, 'strategy':<default/auto>}'
    --config=CONFIG                     Configuration for the program.
    --tuning=TUNING                     Hyperparameter search domain for the program.
    --runid=RUNID                       Unique ID of the pipeline run for back reference.
"""

from .docopt import docopt
from pyfiglet import Figlet
import json

def validate_container(container):
    container = json.loads(container)
    assert type(container) == dict, "container argument invalid format. See help"
    assert 'image' in container.keys(), "Container argument invalid format. Missing image key. See help"

def validate_distributeopts(opts):
    allowed_strategy = ['default', 'auto']
    opts = json.loads(opts)
    assert type(opts) == dict, "distributeopts argument invalid format. See help"
    assert 'workers' in opts.keys(), "distributeopts argument invalid format. Missing workers key. see help"
    assert 'strategy' in opts.keys(), "distributeopts argument invalid format. Missing strategy key. see help"
    assert opts['strategy'] in allowed_strategy, "distributeopts argument invalid format. unsupported strategy key val. see help"

def validate(**kwargs):
    #There are some parameters which are mandatory
    assert kwargs['--name'] != None, "--name is missing. Must be specified."
    assert kwargs['--token'] != None, "--token is missing. Must be specified."
    assert kwargs['--runid'] != None, "--runid is missing. Must be specified."

    assert kwargs['--container'] != None, "--container is missing, Must be specified."
    validate_container(kwargs['--container'])

    if json.loads(kwargs['--distributeopts']):
        validate_distributeopts(kwargs['--distributeopts'])


def transform(**kwargs):
    data = {}
    for key, val in kwargs.items():
        data[key.lstrip('--')] = val

    data['container'] = json.loads(data['container'])

    data['envs'] = json.loads(data['envs']) if data['envs'] else None
    data['datasets'] = json.loads(data['datasets']) if data['datasets'] else None
    data['models'] = json.loads(data['models']) if data['models'] else None
    data['distributeopts'] = json.loads(data['distributeopts']) if data['distributeopts'] else None
    return data

import os

from dkube.sdk.dkube import *
from dkube.sdk._types import *

def training(**kwargs):
    #extract user from supplied token
    #_extract_user_from_token(token)
    user = 'ocdkube'
    env = Environment(ip="http://dkube-d3api.dkube:5000", user=user, token=kwargs['token'])
    args = {}
    args.update({
            'container':ContainerImage.from_dict(kwargs['container']),
            'workspace':kwargs['program'] or '',
            'script':kwargs['script'] or '',
            'models':kwargs['models'] or [],
            'datasets':kwargs['datasets'] or [],
            'hptuning':kwargs['tuning'] or '',
            'ngpus':kwargs['ngpus'] or 0
            })

    if kwargs.get('envs', None):
        envs = kwargs['envs']
        if 'steps' in envs.keys():
            args.update({'steps': envs['steps']})
            del envs['steps']
        if 'epochs' in envs.keys():
            args.update({'epochs': envs['epochs']})
            del envs['epochs']
        if 'batchsize' in envs.keys():
            args.update({'batchsize': envs['batchsize']})
            del envs['batchsize']

    if kwargs.get('distributeopts', None):
        dopts = kwargs['distributeopts']
        args.update({'distributeopts': DistributeOpts().from_dict(dopts)})


    launch_training_job(kwargs['name'], autogenerate=True, environ=env.external, **args)

#if __name__ == '__main__':
def main():
    args = docopt(__doc__, version='1.4')
    print(**args)
    validate(**args)
    args = transform(**args)

    f = Figlet(font='slant')
    print(f.renderText('Dkube Training'))

    training(**args)

