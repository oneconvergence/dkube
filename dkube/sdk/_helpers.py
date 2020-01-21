import os
import random
import string
import time

from .env import *
from .schema import *
from .lib import *

def upload_to_dkube(env:Environment, fspath:str, name:str):
    if env.type == EnvironmentType.INTERNAL:
        client = minio_client(env.endpoint, env.key, env.secret)
    if env.type == EnvironmentType.EXTERNAL:
        client = minio_client(env.endpoint, env.key, env.secret, proxy=True, token=env.token)
    bucket = env.bucket
    prefix = "users/{}/model".format(env.user)
    access_token = env.token

    prefix = "{}/{}".format(prefix, name)

    for path, subdirs, files in os.walk(fspath):
        path = path.replace("\\","/")
        directory = path.replace(fspath,"")
        for filee in files:
            target = "{}/{}/{}".format(prefix, directory, filee)
            target = os.path.normpath(target)
            client.fput_object(bucket, target, os.path.join(path, filee), 'text/plain')

def create_model(env:Environment, model:Model):
    url = "{}/dkube/v2/controller/users/{}/datums".format(env.url, env.user)
    post(url, env.token, data=model.to_json())

def create_training_job(env:Environment, job:DkubeJob):
    url = "{}/dkube/v2/controller/users/{}/jobs".format(env.url, env.user)
    post(url, env.token, data=job.to_json())

def create_serving_job(env:Environment, job:DkubeJob):
    url = "{}/dkube/v2/controller/users/{}/jobs".format(env.url, env.user)
    post(url, env.token, data=job.to_json())

def wait_for_training_job(env:Environment, name:str):
    state = State.UNKNOWN.value
    reason = 'unknown'
    while State.is_final_state(state) == False:
        time.sleep(10)
        job = get_training_job(env, name)
        state = job.params.value.generated.status.state.value
        reason = job.params.value.generated.status.reason
        logger.info("user {}, job {}, state {}, reason {}".format(env.user, job.name, state, reason))

    return state, reason

def wait_for_serving_job(env:Environment, name:str):
    state = State.UNKNOWN.value
    reason = 'unknown'
    while State.is_running_state(state) == False:
        time.sleep(10)
        job = get_serving_job(env, name)
        state = job.params.value.generated.status.state.value
        reason = job.params.value.generated.status.reason
        logger.info("user {}, job {}, state {}, reason {}".format(env.user, job.name, state, reason))

    return state, reason

def get_training_job(env:Environment, name:str):
    job = DkubeJob()
    job.name = name
    url = "{}/dkube/v2/controller/users/{}/jobs/class/{}/job/{}/collection".format(env.url, env.user, "training", job.name)
    data = get(url, env.token)
    job.from_json(data['data']['job'])
    return job

def get_serving_job(env:Environment, name:str):
    job = DkubeJob()
    job.name = name
    url = "{}/dkube/v2/controller/users/{}/jobs/class/{}/job/{}/collection".format(env.url, env.user, "inference", job.name)
    data = get(url, env.token)
    job.from_json(data['data']['job'])
    return job

    
def generate_version():
    return ''.join([random.choice(string.digits) for n in range(10)])

def get_tfmodel_version(fspath: str):
    #For models generated using Tensorflow Estimator - version will be present in the path
    #Expected path is <basepath>/modelversion
    if os.path.isdir(fspath):
        fspath = fspath + "/"
        version = os.path.split(os.path.dirname(fspath))[1]
        #version can only be a number
        if version.isdigit() == True:
            return version
    return ""
