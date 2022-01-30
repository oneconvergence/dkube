import kfp.compiler as compiler
import kfp
import kfp.components as kfplc
import json
import ast

from dkube.sdk import *
from dkube.remote.job_properties import *
from dkube.pipelines import *

from typing import NamedTuple

from dkube.remote._kfpl import componentize


def create_and_launch_slurmjob(cluster: str, cluster_kind: str, props,
        token: str, code: str, dataset:str, model: str) -> NamedTuple(

        'outputs',
        [
            ('artifacts', str),
            ('run_details', str)
        ]):

    import requests

    from dkube.sdk import DkubeTraining
    from dkube.sdk import generate
    from dkube.remote import launch_remotejob

    auth_url = "http://dkube-auth-server.dkube:3001/verifyToken"
    headers = {"accept":"application/json"}
    assert token != "", "Token is empty"
    resp = requests.post(auth_url, data=token, headers=headers)
    assert resp.status_code == 200, "Got non 200 response from auth server while token validation"
    user = resp.json()['username']
    assert user != "", "Got empty user name from token"

    training_name = generate('mnist')
    training = DkubeTraining(
        str(user), name=training_name, description='triggered from dkube pl launcher')
    training.update_container(
        framework="tensorflow_2.0.0", image_url="ocdr/dkube-datascience-tf-cpu:v2.0.0-9")
    training.update_startupscript("python mnist/train.py")
    training.add_code(str(code))
    training.add_input_dataset(str(dataset), mountpath='/mnist')
    training.add_output_model(str(model), mountpath='/model')
    return launch_remotejob(cluster, cluster_kind, props, user, token, training.job)


dkube_slurmjob_op = componentize(create_and_launch_slurmjob,
                                 "dkube_slurmjob_launcher",
                                 "Launcher for slurmjob using DKube APIs.",
                                 "ocdr/dkube_launcher:remote",
                                 {
                                     'platform': 'Dkube'
                                 },
                                 {
                                     'platform': 'Dkube',
                                     'stage': 'training',
                                     'logger': 'dkubepl',
                                     'dkube.garbagecollect': 'true',
                                     'dkube.garbagecollect.policy':
                                     'all'
                                 })

dkube_servingop = kfplc.load_component_from_url(
    "https://raw.githubusercontent.com/oneconvergence/dkube/2.2/components/serving/component.yaml")


@kfplc.create_component_from_func
def extract_version(artifacts: str) -> str:
    import json
    print(artifacts)
    artifacts = json.loads(artifacts)
    version = artifacts[0]["version"]
    return version


@kfp.dsl.pipeline(
    name='slurm job pipeline',
    description='An example pipeline for launching slurm job.'
)
def slurm_pipeline(
        token=None,
        code=None,
        dataset=None,
        model=None,
        slurm_cluster=None,
        slurm_jobprops: type(SLURM_JobProperties) = SLURM_JobProperties()):

    slurm_task = dkube_slurmjob_op(
        slurm_cluster, "slurm-remote", slurm_jobprops, str(token), code, dataset, model).set_display_name("training")

    extract_task = extract_version(
        slurm_task.outputs['artifacts']).after(slurm_task).set_display_name("extract_version")
    serving_task = dkube_servingop(
        str(token), str(model),
        model_version=extract_task.output,
        serving_image=json.dumps({'image': 'ocdr/tensorflowserver:2.0.0'}),
        transformer_image=json.dumps(
            {'image': 'docker.io/ocdr/dkube-datascience-tf-cpu:v2.0.0-9'}),
        transformer_project=str(code),
        transformer_code='mnist/transformer.py').after(extract_task).set_display_name("serving")


compiler.Compiler().compile(slurm_pipeline, __file__ + '.tar.gz')
