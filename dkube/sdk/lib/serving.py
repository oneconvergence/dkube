from __future__ import print_function
import time
import sys

from dkube.sdk.internal import dkube_client
from dkube_client.rest import ApiException
from dkube_client.models.job_model import JobModel
from dkube_client.models.job_model_parameters import JobModelParameters
from dkube_client.models.inference_job_model import InferenceJobModel
from dkube_client.models.custom_container_model import CustomContainerModel
from dkube_client.models.custom_container_model_image import CustomContainerModelImage
from pprint import pprint

class ServingBase(object):
    def __init__(self):
        self.custom_container = CustomContainerModelImage(path=None, username=None, password=None, runas=None)
        self.transformer = CustomContainerModel(image=self.custom_container)
        self.serving_def = InferenceJobModel(model=None, version=None, owner=None, device=None, preprocessing=self.transformer)
        self.run_def = JobModelParametersRun(template=None, group='default')
        self.job_parameters = JobModelParameters(_class='inference', inference=self.serving_def, run=self.run_def)
        self.job = JobModel(name=None, parameters=self.job_parameters)
