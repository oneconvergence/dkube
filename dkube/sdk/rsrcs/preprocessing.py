from __future__ import print_function
import time
import sys

from dkube.sdk.internal import dkube_api
from dkube.sdk.internal.dkube_api.rest import ApiException
from dkube.sdk.internal.dkube_api.models.job_model import JobModel
from dkube.sdk.internal.dkube_api.models.job_model_parameters import JobModelParameters
from dkube.sdk.internal.dkube_api.models.preprocessing_job_model import PreprocessingJobModel
from dkube.sdk.internal.dkube_api.models.preprocessing_job_model_executor import PreprocessingJobModelExecutor
from dkube.sdk.internal.dkube_api.models.job_config_model import JobConfigModel
from dkube.sdk.internal.dkube_api.models.custom_container_model import CustomContainerModel
from dkube.sdk.internal.dkube_api.models.custom_container_model_image import CustomContainerModelImage
from dkube.sdk.internal.dkube_api.models.job_datum_model import JobDatumModel
from dkube.sdk.internal.dkube_api.models.job_datum_model_workspace import JobDatumModelWorkspace
from dkube.sdk.internal.dkube_api.models.job_input_datum_model import JobInputDatumModel
from dkube.sdk.internal.dkube_api.models.job_model_parameters_run import JobModelParametersRun
from dkube.sdk.internal.dkube_api.models.custom_kv_model import CustomKVModel
from dkube.sdk.internal.dkube_api.models.config_file_model import ConfigFileModel
from pprint import pprint

from .util import *

class DkubePreprocessing(object):
    def __init__(self, user, name=generate('data'), description='', tags=[]):

        self.repo = JobInputDatumModel  # class assignment, caller creates objects

        self.custom_container = CustomContainerModelImage(
            path='', username=None, password=None, runas=None)
        self.executor_custom = CustomContainerModel(
            image=self.custom_container)
        self.executor_def = PreprocessingJobModelExecutor(
            choice='custom', custom=self.executor_custom)
        self.input_project_data = JobInputDatumModel(
            name=None, version=None, mountpath=None)
        self.input_project = JobDatumModelWorkspace(
            data=self.input_project_data, script=None)
        self.output_datasets = []
        self.input_datasets = []
        self.input_models = []
        self.input_datums = JobDatumModel(
            workspace=self.input_project, datasets=self.input_datasets, outputs=self.output_datasets)
        self.customkv = CustomKVModel()
        self.configfile = ConfigFileModel()
        self.config = JobConfigModel(envs=None, file=self.configfile)
        self.pp_def = PreprocessingJobModel(
            kind='preprocessing', executor=self.executor_def, datums=self.input_datums, config=self.config)
        self.run_def = JobModelParametersRun(template=None, group='default')
        self.job_parameters = JobModelParameters(
            _class='preprocessing', preprocessing=self.pp_def, run=self.run_def)
        self.job = JobModel(name=None, parameters=self.job_parameters)

        self.update_basic(user, name, description, tags)

    def update_basic(self, name, description, tags):
        self.user = user
        self.name = name

        self.job.name = name
        self.job.description = description
        self.pp_def.tags = tags

        # defaults
        self.custom_container.path = 'docker.io/ocdr/dkube-datascience-tf-cpu:v1.14'

    def update_group(self, group='default'):
        self.run_def.group = group

    def update_container(self, image_url=None, login_uname=None, login_pswd=None):
        self.custom_container.path = image_url
        self.custom_container.username = login_uname
        self.custom_container.password = login_pswd

    def update_startupscript(self, startup_script=None):
        self.input_project.script = startup_script

    def update_envvars(self, envs={}):
        self.customkv = [envs]

    def add_project(self, name, commitid=None):
        name = self.user + ':' + name
        self.input_project_data.name = name
        self.input_project_data.version = commitid

    def add_input_dataset(self, name, version=None, mountpath=None):
        name = self.user + ':' + name
        repo = self.repo(name=name, version=version, mountpath=mountpath)
        self.input_datasets.append(repo)

    def add_input_model(self, name, version=None, mountpath=None):
        name = self.user + ':' + name
        repo = self.repo(name=name, version=version, mountpath=mountpath)
        self.input_models.append(repo)

    def add_output_dataset(self, name, version=None, mountpath=None):
        name = self.user + ':' + name
        repo = self.repo(name=name, version=version, mountpath=mountpath)
        self.output_datasets.append(repo)
