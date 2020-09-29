from __future__ import print_function
import time
import sys

from dkube.sdk.internal import dkube_api
from dkube.sdk.internal.dkube_api.rest import ApiException
from dkube.sdk.internal.dkube_api.models.job_model import JobModel
from dkube.sdk.internal.dkube_api.models.job_model_parameters import JobModelParameters
from dkube.sdk.internal.dkube_api.models.inference_job_model import InferenceJobModel
from dkube.sdk.internal.dkube_api.models.custom_container_model import CustomContainerModel
from dkube.sdk.internal.dkube_api.models.custom_container_model_image import CustomContainerModelImage
from pprint import pprint

from .util import *

class DkubeServing(object):
    def __init__(self, user, name=generate('serving'), description='', tags=[]):
        self.predictor_container = CustomContainerModelImage(
            path=None, username=None, password=None, runas=None)
        self.predictor = CustomContainerModel(image=self.predictor_container)
        self.transformer_container = CustomContainerModelImage(
            path=None, username=None, password=None, runas=None)
        self.transformer = CustomContainerModel(
            image=self.transformer_container)
        self.serving_def = InferenceJobModel(
            model=None, version=None, owner=None, device=None, preprocessing=self.transformer)
        self.run_def = JobModelParametersRun(template=None, group='default')
        self.job_parameters = JobModelParameters(
            _class='inference', inference=self.serving_def, run=self.run_def)
        self.job = JobModel(name=None, parameters=self.job_parameters)

        self.update_basic(user, name, description, tags)

    def update_basic(self, name, description, tags):
        self.user = user
        self.name = name

        self.job.name = name
        self.job.description = description
        self.serving_def.tags = tags

    def update_transformer_code(self, project=None, commitid=None, code=None):
        self.serving_def.transformer = True
        self.serving_def.transformer_project = project
        self.serving_def.transformer_commit_id = commitid
        self.serving_def.transformer_code = code

    def update_tranformer_image(self, image_url=None, login_uname=None, login_pswd=None):
        self.serving_def.transformer = True
        self.transformer_container.path = image_url
        self.transformer_container.username = login_uname
        self.transformer_container.password = login_pswd

    def update_serving_model(self, model, version=None):
        self.serving_def.model = model
        self.serving_def.version = version
        self.serving_dev.owner = self.user

    def update_serving_image(self, image_url=None, login_uname=None, login_pswd=None):
        self.serving_container.path = image_url
        self.serving_container.username = login_uname
        self.serving_container.password = login_pswd
