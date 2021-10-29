from __future__ import print_function

import sys
import time
from pprint import pprint

from dkube.sdk.internal import dkube_api
from dkube.sdk.internal.dkube_api.models.config_file_model import \
    ConfigFileModel
from dkube.sdk.internal.dkube_api.models.custom_container_model import \
    CustomContainerModel
from dkube.sdk.internal.dkube_api.models.custom_container_model_image import \
    CustomContainerModelImage
from dkube.sdk.internal.dkube_api.models.custom_kv_model import CustomKVModel
from dkube.sdk.internal.dkube_api.models.job_config_model import JobConfigModel
from dkube.sdk.internal.dkube_api.models.job_datum_model import JobDatumModel
from dkube.sdk.internal.dkube_api.models.job_datum_model_workspace import \
    JobDatumModelWorkspace
from dkube.sdk.internal.dkube_api.models.job_featureset_model import \
    JobFeaturesetModel
from dkube.sdk.internal.dkube_api.models.job_input_datum_model import \
    JobInputDatumModel
from dkube.sdk.internal.dkube_api.models.job_input_featureset_model import \
    JobInputFeaturesetModel
from dkube.sdk.internal.dkube_api.models.job_model import JobModel
from dkube.sdk.internal.dkube_api.models.job_model_parameters import \
    JobModelParameters
from dkube.sdk.internal.dkube_api.models.job_model_parameters_run import \
    JobModelParametersRun
from dkube.sdk.internal.dkube_api.models.preprocessing_job_model import \
    PreprocessingJobModel
from dkube.sdk.internal.dkube_api.models.preprocessing_job_model_executor import \
    PreprocessingJobModelExecutor
from dkube.sdk.internal.dkube_api.rest import ApiException

from .util import *


class DkubePreprocessing(object):
    """

        This class defines DKube Preprocessing Run with helper functions to set properties of Preprocessing Run.::

            from dkube.sdk import *
            preprocessing = DkubePreprocessing("oneconv", name="mnist-run")

            Where first argument is the user of the Preprocessing Run. User should be a valid onboarded user in dkube.

    """

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
            workspace=self.input_project, datasets=self.input_datasets, models=self.input_models, outputs=self.output_datasets)
        self.input_featuresets = []
        self.output_featuresets = []
        self.featuresets = JobFeaturesetModel(
            inputs=self.input_featuresets, outputs=self.output_featuresets)
        self.customkv = CustomKVModel()
        self.configfile = ConfigFileModel()
        self.customenv = {}
        self.envs = []
        self.config = JobConfigModel(envs=self.envs, file=self.configfile)
        self.pp_def = PreprocessingJobModel(
            kind='preprocessing', executor=self.executor_def, datums=self.input_datums, config=self.config, featuresets=self.featuresets)
        self.run_def = JobModelParametersRun(template=None, group='default')
        self.job_parameters = JobModelParameters(
            _class='preprocessing', preprocessing=self.pp_def, run=self.run_def)
        self.job = JobModel(name=None, parameters=self.job_parameters)

        self.update_basic(user, name, description, tags)
        self.execute = True

    def update_basic(self, user, name, description, tags):
        """
            Method to update the attributes specified at creation. Description and tags can be updated. tags is a list of string values.
        """
        tags = list_of_strs(tags)

        self.user = user
        self.name = name

        self.job.name = name
        self.job.description = description
        self.pp_def.tags = tags

        # defaults
        self.custom_container.path = 'docker.io/ocdr/dkube-datascience-tf-cpu:v1.14'

    def update_group(self, group='default'):
        """
            Method to update the group to place the Preprocessing Run.
        """
        self.run_def.group = group

    def update_container(self, image_url=None, login_uname=None, login_pswd=None):
        """
            Method to update the framework and image to use for the Preprocessing run.

            *Inputs*

                framework
                    One of the frameworks from **FRAMEWORK_OPTS**

                image_url
                    url for the image repository |br|
                    e.g, docker.io/ocdr/dkube-datascience-tf-cpu:v2.0.0

                login_uname
                    username to access the image repository

                login_pswd
                    password to access the image repository
        """
        self.custom_container.path = image_url
        self.custom_container.username = login_uname
        self.custom_container.password = login_pswd

    def update_startupscript(self, startup_script=None):
        """
            Method to update startup command for the Preprocessing run

            *Inputs*

                startup_script
                    Startup command for the Preprocessing run pod. Relative path from the root of the code repository should be specified.
        """
        self.input_project.script = startup_script

    def update_envvars(self, envs={}):
        """
            Method to update env variables for the Preprocessing run

            *Inputs*

                envs
                    Dictionary of env variable name and value
        """
        self.customkv = [envs]

    def add_code(self, name, commitid=""):
        """
            Method to update Code Repo for Preprocessing run

            *Inputs*

                name
                    Name of Code Repo

                commitid
                    commit id to retreive from code repository
        """
        if ":" not in name:
            name = self.user + ':' + name
        self.input_project_data.name = name
        self.input_project_data.version = commitid

    def add_input_dataset(self, name, version=None, mountpath=None):
        """
            Method to update Dataset Repo input for Preprocessing run

            *Inputs*

                name
                    Name of Dataset Repo

                version
                    Version (unique id) to use from Dataset

                mountpath
                    Path at which the Dataset contents are made available in the Preprocessing run pod.
                    For local Dataset, mountpath points to the contents of Dataset.
                    For remote Dataset, mounpath contains the metadata for the Dataset.
        """
        if ":" not in name:
            name = self.user + ':' + name
        repo = self.repo(name=name, version=version, mountpath=mountpath)
        self.input_datasets.append(repo)

    def add_input_model(self, name, version=None, mountpath=None):
        """
            Method to update Model Repo input for Preprocessing run

            *Inputs*

                name
                    Name of Model Repo

                version
                    Version (unique id) to use from Model

                mountpath
                    Path at which the Model contents are made available in the Preprocessing run pod
        """
        if ":" not in name:
            name = self.user + ':' + name
        repo = self.repo(name=name, version=version, mountpath=mountpath)
        self.input_models.append(repo)

    def add_output_dataset(self, name, version=None, mountpath=None):
        """
            Method to update Dataset Repo output for Preprocessing run

            *Inputs*

                name
                    Name of Dataset Repo

                version
                    Version (unique id) to use from Model (TODO)

                mountpath
                    Path to write model files in the Preprocessing run. A new version is created in the Dataset Repo with files written to this path.
        """
        name = self.user + ':' + name
        repo = self.repo(name=name, version=version, mountpath=mountpath)
        self.output_datasets.append(repo)

    def add_input_featureset(self, name, version=None, mountpath=None):
        """
            Method to update Featureset input for Preprocessing run

            *Inputs*

                name
                    Name of Featureset

                version
                    Version (unique id) to use from Featureset

                mountpath
                    Path at which the Featureset contents are made available in the Preprocessing run pod

        """
        featureset_model = JobInputFeaturesetModel(
            name=name, version=version, mountpath=mountpath)
        self.input_featuresets.append(featureset_model)

    def add_output_featureset(self, name, version=None, mountpath=None):
        """
            Method to update Featureset output for Preprocessing run

            *Inputs*

                name
                    Name of Featureset

                version
                    Version (unique id) to use from Featureset (TODO)

                mountpath
                    Path to write Featureset files in the Preprocessing run. A new version is created in the Featureset with files written to this path.
        """
        featureset_model = JobInputFeaturesetModel(
            name=name, version=version, mountpath=mountpath)
        self.output_featuresets.append(featureset_model)

    def disable_execution(self):
        self.execute = False

    def update_config_file(self, name, body=None):
        """
            Method to update config file for training run
            *Inputs*

                name
                    Name of config file

                body
                    Config data which is made available as file with the specified name to the training pod under /mnt/dkube/config
        """
        self.configfile.name = name
        self.configfile.body = body

    def add_envvar(self, key, value):
        """
            Method to add env variable for the training run

            *Inputs*

                key
                    Name of env variable

                value
                    Value of env variable
        """
        self.customenv[key] = value
        return self.add_envvars(self.customenv)

    def add_envvars(self, vars={}):
        """
            Method to add env variables for the training run
            *Inputs*
                vars
                    Dictionary of env variable name and value
        """
        for k, v in vars.items():
            self.envs.append({"key": k, "value": v})
