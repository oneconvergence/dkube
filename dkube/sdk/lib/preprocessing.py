from __future__ import print_function
import time
import sys

from dkube.sdk.internal import dkube_client
from dkube_client.rest import ApiException
from dkube_client.models.job_model import JobModel
from dkube_client.models.job_model_parameters import JobModelParameters
from dkube_client.models.preprocessing_job_model import PreprocessingJobModel
from dkube_client.models.preprocessing_job_model_executor import PreprocessingJobModelExecutor
from dkube_client.models.job_config_model import JobConfigModel
from dkube_client.models.custom_container_model import CustomContainerModel
from dkube_client.models.custom_container_model_image import CustomContainerModelImage
from dkube_client.models.job_datum_model import JobDatumModel
from dkube_client.models.job_datum_model_workspace import JobDatumModelWorkspace
from dkube_client.models.job_input_datum_model import JobInputDatumModel
from dkube_client.models.job_model_parameters_run  import JobModelParametersRun
from dkube_client.models.custom_kv_model import CustomKVModel
from dkube_client.models.config_file_model import ConfigFileModel
from pprint import pprint

class PreprocessingBase(object):
    def __init__(self):
        self.repo = JobInputDatumModel #class assignment, caller creates objects

        self.custom_container = CustomContainerModelImage(path='', username=None, password=None, runas=None)
        self.executor_custom = CustomContainerModel(image=self.custom_container)
        self.executor_def =PreprocessingJobModelExecutor(choice='custom', custom=self.executor_custom)
        self.input_project_data = JobInputDatumModel(name=None, version=None, mountpath=None)
        self.input_project = JobDatumModelWorkspace(data=self.input_project_data, script=None)
        self.output_datasets = []
        self.input_datasets = []
        self.input_datums = JobDatumModel(workspace=self.input_project, datasets=self.input_datasets, outputs=self.output_datasets)
        self.customkv = CustomKVModel()
        self.configfile = ConfigFileModel()
        self.config = JobConfigModel(envs=None, file=self.configfile)
        self.pp_def = PreprocessingJobModel(kind='preprocessing', executor=self.executor_def, datums=self.input_datums, config=self.config)
        self.run_def = JobModelParametersRun(template=None, group='default')
        self.job_parameters = JobModelParameters(_class='preprocessing', preprocessing=self.pp_def, run=self.run_def)
        self.job = JobModel(name=None, parameters=self.job_parameters)
