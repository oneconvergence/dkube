from minio import Minio

import os

from .env import *
from .schema import *
from .rest import client as d3c

def _upload_to_dkube(env:Environment, fspath:str, name:str):
    client = Minio(env.endpoint,
               access_key=env.key,
               secret_key=env.secret, secure=False)
    bucket = env.bucket
    prefix = "users/{}/model".format(env.user)
    access_token = env.token

    prefix = "{}/{}".format(prefix, name)

    for path, subdirs, files in os.walk(fspath):
        path = path.replace("\\","/")
        directory = path.replace(fspath,"")
        for filee in files:
            target = "{}/{}/{}".format(prefix, directory, filee)
            client.fput_object(bucket, target, os.path.join(path, filee), 'text/plain')

def _create_model(env:Environment, model:Model):
    url = "{}/dkube/v2/users/{}/datums".format(env.url, env.user)
    d3c.post(url, model, env.token)
    
def _generate_version():
    import random

    return ''.join([random.choice(string.digits) for n in range(10)])

def _get_tfmodel_version(fspath: str):
    import os

    #For models generated using Tensorflow Estimator - version will be present in the path
    #Expected path is <basepath>/modelversion
    if os.path.isdir(fspath):
        fspath = fspath + "/"
        version = os.path.split(os.path.dirname(fspath))[1]
        #version can only be a number
        if version.isdigit() == True:
            return version
    return ""
