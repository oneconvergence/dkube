from minio import Minio
import os
import random
import string

from .env import *
from .schema import *
from .rest.client import *

def upload_to_dkube(env:Environment, fspath:str, name:str):
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

def create_model(env:Environment, model:Model):
    url = "{}/dkube/v2/users/{}/datums".format(env.url, env.user)
    post(url, model, env.token)
    
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
