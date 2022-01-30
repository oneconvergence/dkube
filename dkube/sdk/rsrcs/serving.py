from __future__ import print_function

import sys
import time
from pprint import pprint

from dkube.sdk.internal import dkube_api
from dkube.sdk.internal.dkube_api.models.custom_container_model import \
    CustomContainerModel
from dkube.sdk.internal.dkube_api.models.custom_container_model_image import \
    CustomContainerModelImage
from dkube.sdk.internal.dkube_api.models.inference_job_model import \
    InferenceJobModel
from dkube.sdk.internal.dkube_api.models.job_model import JobModel
from dkube.sdk.internal.dkube_api.models.job_model_parameters import \
    JobModelParameters
from dkube.sdk.internal.dkube_api.models.job_model_parameters_run import \
    JobModelParametersRun
from dkube.sdk.internal.dkube_api.rest import ApiException

from .util import *


class DkubeServing(object):

    """

        This class defines Model Deployment with helper functions to set properties of Model Deployment.::

            from dkube.sdk import *
            serving = DkubeServing("oneconv", name="mnist-serving")

            Where first argument is the user of the Model Deployment. User should be a valid onboarded user in dkube.

    """

    def __init__(self, user, name=generate('serving'), description='', tags=[]):
        self.predictor_container = CustomContainerModelImage(
            path='', username=None, password=None, runas=None)
        self.predictor = CustomContainerModel(image=None)
        self.transformer_container = CustomContainerModelImage(
            path='', username=None, password=None, runas=None)
        self.transformer = CustomContainerModel(image=None)

        self.serving_def = InferenceJobModel(model=None, version=None, owner=None, device=None, deploy=None,
                                             serving_image=self.predictor, transformer=False,
                                             transformer_image=self.transformer, transformer_project=None,
                                             transformer_commit_id=None, transformer_code=None,
                                             min_replicas=0, max_concurrent_requests=0)
        self.run_def = JobModelParametersRun(template=None, group='default')
        self.job_parameters = JobModelParameters(
            _class='inference', inference=self.serving_def, run=self.run_def)
        self.job = JobModel(name=None, parameters=self.job_parameters)

        self.update_basic(user, name, description, tags)

    def update_basic(self, user, name, description, tags):
        """
            Method to update the attributes specified at creation. Description and tags can be updated. tags is a list of string values.
        """
        tags = list_of_strs(tags)

        self.user = user
        self.name = name
        self.description = description

        self.job.name = name
        self.job.description = description
        self.serving_def.tags = tags
        self.serving_def.device = "cpu"
        self.serving_def.transformer = False

    def set_transformer(self, transformer: bool = False, script=None):
        """
            Method to specify if a transformer is required for pre/post processing of Inference requests and the script to run from the Transformer Code Repo.

            *Inputs*

                transformer
                    True or False

                script
                    Script command to run in the transformer pod from Transformer Code Repo
        """
        self.serving_def.transformer = transformer
        self.serving_def.transformer_code = script

    def update_transformer_code(self, code=None, commitid=None):
        """
            Method to update Code Repo to use for the Transformer.

            *Inputs*

                code
                    Code Repo containing the script for Transformer

                commitid
                    commit id used to retrieve the transformer Code Repo
        """
        if ':' not in code:
            self.serving_def.transformer_project = self.user + ':' + code
        else:
            self.serving_def.transformer_project = code
        self.serving_def.transformer_commit_id = commitid

    def update_transformer_image(self, image_url='', login_uname=None, login_pswd=None):
        """
            Method to update the image to use for the transformer

            *Inputs*

                image_url
                    url for the image repository |br|
                    e.g, docker.io/ocdr/dkube-datascience-tf-cpu:v2.0.0

                login_uname
                    username to access the image repository

                login_pswd
                    password to access the image repository
        """
        self.transformer_container.path = image_url
        self.transformer_container.username = login_uname
        self.transformer_container.password = login_pswd
        self.transformer.image = self.transformer_container

    def update_serving_model(self, model, owner=None, version=None):
        """
            Method to update Model Repo input for Model Serving

            *Inputs*

                name
                    Name of Model Repo containing the model files

                owner
                    Owner of Model Repo containing the model files

                version
                    Version (unique id) to use from Model Repo
        """
        self.serving_def.model = model
        self.serving_def.version = version
        if owner is not None:
            self.serving_def.owner = owner
        else:
            self.serving_def.owner = self.user

    def update_serving_image(self, deploy=None, image_url='', login_uname=None, login_pswd=None):
        """
            Method to update the image to use for Model Serving

            *Inputs*

                deploy
                    Flag to specify Serving for Test or Production (TODO)

                image_url
                    url for the image repository |br|
                    e.g, docker.io/ocdr/tensorflowserver:2.0.0

                login_uname
                    username to access the image repository

                login_pswd
                    password to access the image repository
        """
        self.predictor_container.path = image_url
        self.predictor_container.username = login_uname
        self.predictor_container.password = login_pswd
        self.serving_def.deploy = deploy
        self.predictor.image = self.predictor_container

    def set_production_deploy(self):
        """
            Method to update the mode to use for Model Serving

            *Inputs*

                deploy
                    Flag to specify Serving for Test or Production (TODO)
        """
        self.serving_def.deploy = True

    def update_autoscaling_config(self, min_replicas, max_concurrent_requests):
        """
            Method to update the autocale config to use for Model Serving

            *Inputs*

                min_replicas
                    Min number of pods to be running for Serving

                max_concurrent_requests
                    Soft target threshold value for number of concurrent requests to trigger scale up of Serving pods
        """
        self.serving_def.min_replicas = min_replicas
        self.serving_def.max_concurrent_requests = max_concurrent_requests
