from __future__ import print_function

import json
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
from dkube.sdk.internal.dkube_api.models.dkube_container_model import \
    DkubeContainerModel
from dkube.sdk.internal.dkube_api.models.dkube_container_model_framework import \
    DkubeContainerModelFramework
from dkube.sdk.internal.dkube_api.models.dkube_container_model_framework_details import \
    DkubeContainerModelFrameworkDetails
from dkube.sdk.internal.dkube_api.models.ds_job_model import DSJobModel
from dkube.sdk.internal.dkube_api.models.ds_job_model_executor import \
    DSJobModelExecutor
from dkube.sdk.internal.dkube_api.models.ds_job_model_hptuning import \
    DSJobModelHptuning
from dkube.sdk.internal.dkube_api.models.ds_job_model_hyperparams import \
    DSJobModelHyperparams
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
from dkube.sdk.internal.dkube_api.rest import ApiException

from .util import *


class DkubeTraining(object):

    """

        This class defines DKube Training Run with helper functions to set properties of Training Run.::

            from dkube.sdk import *
            training = DkubeTraining("oneconv", name="mnist-run")

            Where first argument is the user of the Training Run. User should be a valid onboarded user in dkube.

    """
    
    FRAMEWORK_OPTS = ["custom"]
    """
	List of valid frameworks for the training images
        Framework is used to derive the image used for Model Serving

	:bash:`custom` :- Custom framework
    """
    DISTRIBUTION_OPTS = ["manual", "auto"]
    """
	Options for GPU jobs configured to run on multiple nodes
        Default option is 'auto' where distribution is configured by the framework

	:bash:`auto` :- Framework configures the distribution mechanism

	:bash:`manual` :- User configures the distribution mechanism

    """

    def __init__(self, user, name=generate('train'), description='', tags=[]):
        self.repo = JobInputDatumModel  # class assignment, caller creates objects

        self.dkube_framework_details = DkubeContainerModelFrameworkDetails(
            version='v2.0.0')
        self.executor_dkube_framework = DkubeContainerModelFramework(
            choice='tensorflow', details=self.dkube_framework_details)
        self.executor_dkube = DkubeContainerModel(
            framework=self.executor_dkube_framework)
        self.custom_container = CustomContainerModelImage(
            path='', username=None, password=None, runas=None)
        self.executor_custom = CustomContainerModel(
            image=self.custom_container)
        self.executor_def = DSJobModelExecutor(
            choice='dkube', dkube=self.executor_dkube, custom=self.executor_custom)
        self.input_project_data = JobInputDatumModel(
            name=None, version=None, mountpath=None)
        self.input_project = JobDatumModelWorkspace(
            data=self.input_project_data, script=None)
        self.output_models = []
        self.input_datasets = []
        self.input_datums = JobDatumModel(
            workspace=self.input_project, datasets=self.input_datasets, outputs=self.output_models)
        self.input_featuresets = []
        self.output_featuresets = []
        self.featuresets = JobFeaturesetModel(inputs=self.input_featuresets, outputs=self.output_featuresets)
        self.configfile = ConfigFileModel()
        self.customenv = {}
        self.hyperparameters = DSJobModelHyperparams(file=self.configfile)
        self.hptuning = DSJobModelHptuning()
        
        self.training_def = DSJobModel(executor=self.executor_def, datums=self.input_datums,
                                       rdma=False, hyperparams=self.hyperparameters, hptuning=self.hptuning, featuresets=self.featuresets)
        self.run_def = JobModelParametersRun(template=None, group='default')
        self.job_parameters = JobModelParameters(
            _class='training', training=self.training_def, run=self.run_def)
        self.job = JobModel(name=None, parameters=self.job_parameters)

        self.update_basic(user, name, description, tags)
        self.execute = True
        self.FRAMEWORK_OPTS =  self.FRAMEWORK_OPTS + get_frameworks()

    def update_basic(self, user, name, description, tags):
        """
            Method to update the attributes specified at creation. Description and tags can be updated. tags is a list of string values.
        """
        tags = list_of_strs(tags)

        self.user = user
        self.name = name

        self.job.name = name
        self.job.description = description
        self.training_def.tags = tags

        # Defaults
        self.dkube_framework_details.version = '2.0.0'
        self.executor_def.custom = None
        self.input_project.script = 'python model.py'
        return self

    def update_group(self, group='default'):
        """
            Method to update the group to place the Training Run.
        """
        self.run_def.group = group

    def update_container(self, framework=FRAMEWORK_OPTS[0],
                         image_url="", login_uname="", login_pswd=""):
        """
            Method to update the framework and image to use for the training run.

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

        framework = framework.lower()
        framework_opts = DkubeTraining.FRAMEWORK_OPTS
        assert framework in framework_opts, "Invalid choice for framework, select oneof(" + str(
            framework_opts) + ")"

        if framework == "custom":
            framework_str = "custom"
            version_str = ""
        else:
            framework_str = framework.split("_")[0]
            version_str = framework.split("_")[1]

        self.executor_dkube_framework.choice = framework_str
        self.dkube_framework_details.version = version_str

        self.dkube_framework_details.image = image_url
        self.dkube_framework_details.username = login_uname
        self.dkube_framework_details.password = login_pswd
        self.dkube_framework_details.private = False

        if login_uname != "":
            self.dkube_framework_details.private = True
        return self

    def update_startupscript(self, startup_script=None):
        """
            Method to update startup command for the training run

            *Inputs*

                startup_script
                    Startup command for the training run pod. Relative path from the root of the code repository should be specified.
        """
        self.input_project.script = startup_script
        return self

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
        envs = []
        for k, v in vars.items():
            envs.append({"key": k, "value": v})

        self.hyperparameters.customkv = envs
        return self

    def add_code(self, name, commitid=None):
        """
            Method to update Code Repo for training run

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
            Method to update Dataset Repo input for training run

            *Inputs*

                name
                    Name of Dataset Repo

                version
                    Version (unique id) to use from Dataset

                mountpath
                    Path at which the Dataset contents are made available in the training run pod.
                    For local Dataset, mountpath points to the contents of Dataset.
                    For remote Dataset, mounpath contains the metadata for the Dataset.
        """
        if ":" not in name:
            name = self.user + ':' + name
        repo = self.repo(name=name, version=version, mountpath=mountpath)
        self.input_datasets.append(repo)

    def add_input_model(self, name, version=None, mountpath=None):
        """
            Method to update Model Repo input for training run

            *Inputs*

                name
                    Name of Model Repo

                version
                    Version (unique id) to use from Model

                mountpath
                    Path at which the Model contents are made available in the training run pod
        """
        if ":" not in name:
            name = self.user + ':' + name
        repo = self.repo(name=name, version=version, mountpath=mountpath)
        self.input_models.append(repo)

    def add_output_model(self, name, version=None, mountpath=None):
        """
            Method to update Model Repo output for training run

            *Inputs*

                name
                    Name of Model Repo

                version
                    Version (unique id) to use from Model (TODO)

                mountpath
                    Path to write model files in the training run. A new version is created in the Model Repo with files written to this path.
        """
        name = self.user + ':' + name
        repo = self.repo(name=name, version=version, mountpath=mountpath)
        self.output_models.append(repo)

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

    def update_hptuning(self, name, body=None):
        """
            Method to update hyperparameter tuning file for training run

            *Inputs*

                name
                    Name of hyperparameter tuning file

                body
                    Hyperparameter tuning data in yaml format which is made available as file with the specified name to the training pod under /mnt/dkube/config
        """
        self.hptuning.name = name
        self.hptuning.body = body

    def update_resources(self, cpus=None, mem=None, ngpus=0):
        """
            Method to update resource requirements for training run

            *Inputs*

                cpus
                    Number of required cpus

                mem
                    Memory requied in MB (TODO)

                gpus
                    Number of required gpus
        """
        self.training_def.ngpus = ngpus

    def update_distribution(self, opt=DISTRIBUTION_OPTS[0], nworkers=0):
        """
            Method to update gpu distribution method for training run

            *Inputs*

                opt
                    GPU distribution method specified as one of **DISTRIBUTION_OPTS**

                nworkers
                    Number of required workers
        """
        self.training_def.nworkers = nworkers
        if opt == "auto":
            self.training_def.gpus_override = True

    def add_input_featureset(self, name, version=None, mountpath=None):
        """
            Method to update Featureset input for training run

            *Inputs*

                name
                    Name of Featureset

                version
                    Version (unique id) to use from Featureset

                mountpath
                    Path at which the Featureset contents are made available in the training run pod
        """
        featureset_model = JobInputFeaturesetModel(name=name, version=version, mountpath=mountpath)
        self.input_featuresets.append(featureset_model)

    def list_frameworks(self):
        """
            Method to list frameworks available for training run
        """
        return json.dumps(self.FRAMEWORK_OPTS)
    
    def disable_execution(self):
        """
            Method to create Run with no execution to track external execution
        """
        self.execute = False
