from __future__ import print_function
import time
import sys

from dkube.sdk.internal import dkube_client
from dkube_client.rest import ApiException
from dkube_client.models.job_model import JobModel
from dkube_client.models.job_model_parameters import JobModelParameters
from dkube_client.models.ds_job_model import DSJobModel
from dkube_client.models.ds_job_model_executor import DSJobModelExecutor
from dkube_client.models.dkube_container_model import DkubeContainerModel
from dkube_client.models.dkube_container_model_framework import DkubeContainerModelFramework
from dkube_client.models.dkube_container_model_framework_details import DkubeContainerModelFrameworkDetails
from dkube_client.models.job_datum_model import JobDatumModel
from dkube_client.models.job_datum_model_workspace import JobDatumModelWorkspace
from dkube_client.models.job_input_datum_model import JobInputDatumModel
from dkube_client.models.job_model_parameters_run  import JobModelParametersRun
from dkube_client.models.ds_job_model_hyperparams import DSJobModelHyperparams
from dkube_client.models.custom_kv_model import CustomKVModel
from dkube_client.models.config_file_model import ConfigFileModel
from dkube_client.models.custom_container_model import CustomContainerModel
from dkube_client.models.custom_container_model_image import CustomContainerModelImage
from pprint import pprint

class TrainingBase(object):
    def __init__(self):
        self.repo = JobInputDatumModel #class assignment, caller creates objects

        self.tf_framework_details = DkubeContainerModelFrameworkDetails(tfversion='v1.14')
        self.executor_dkube_framework = DkubeContainerModelFramework(choice='tensorflow', details=self.tf_framework_details)
        self.executor_dkube = DkubeContainerModel(framework=self.executor_dkube_framework)
        self.custom_container = CustomContainerModelImage(path='', username=None, password=None, runas=None)
        self.executor_custom = CustomContainerModel(image=self.custom_container)
        self.executor_def = DSJobModelExecutor(choice='dkube', dkube=self.executor_dkube, custom=self.executor_custom)
        self.input_project_data = JobInputDatumModel(name=None, version=None, mountpath=None)
        self.input_project = JobDatumModelWorkspace(data=self.input_project_data, script=None)
        self.output_models = []
        self.input_datasets = []
        self.input_datums = JobDatumModel(workspace=self.input_project, datasets=self.input_datasets, outputs=self.output_models)
        self.customkv = CustomKVModel()
        self.configfile = ConfigFileModel()
        self.hyperparameters = DSJobModelHyperparams(file=self.configfile)
        self.training_def = DSJobModel(executor=self.executor_def, datums=self.input_datums, rdma=False, hyperparams=self.hyperparameters)
        self.run_def = JobModelParametersRun(template=None, group='default')
        self.job_parameters = JobModelParameters(_class='training', training=self.training_def, run=self.run_def)
        self.job = JobModel(name=None, parameters=self.job_parameters)
