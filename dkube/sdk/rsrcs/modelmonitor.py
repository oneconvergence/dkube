from __future__ import print_function

import sys
import time
from pprint import pprint
from .util import *

from dkube.sdk.internal import dkube_api

from dkube.sdk.internal.dkube_api.models.modelmonitor_status_def import ModelmonitorStatusDef
from dkube.sdk.internal.dkube_api.models.modelmonitor_schema_feature import ModelmonitorSchemaFeature
from dkube.sdk.internal.dkube_api.models.modelmonitor_features_spec_def import ModelmonitorFeaturesSpecDef
from dkube.sdk.internal.dkube_api.models.modelmonitor_component_def import ModelmonitorComponentDef
from dkube.sdk.internal.dkube_api.models.modelmonitor_dataset_def import ModelmonitorDatasetDef
from dkube.sdk.internal.dkube_api.models.modelmonitor_alert_cond_def import ModelmonitorAlertCondDef
from dkube.sdk.internal.dkube_api.models.modelmonitor_alert_def import ModelmonitorAlertDef
from dkube.sdk.internal.dkube_api.models.modelmonitor_def import ModelmonitorDef


class DkubeModelMonitor(object):
    def __init__(self, user, name=generate("mm"), description = '',tags=None):

        self.features = ModelmonitorSchemaFeature(selected=None, label=None, _class=None, type=None)
        self.schema = ModelmonitorFeaturesSpecDef(features=self.features)

        self.datasets = []

        self.conditions = ModelmonitorAlertCondDef(
            id=None, feature=None, op=None, threshold=None)

        self.alerts = []

        self.modelmonitor = ModelmonitorDef(
            id=None,
            schema=None,
            pipeline_component=None,
            owner=None,
            emails=None,
            name=None,
            description=None,
            tags=None,
            model=None,
            version=None,
            endpoint_url=None,
            model_type=None,
            model_framework=None,
            drift_detection_run_frequency_hrs=None,
            drift_detection_algorithm=None,
            performance_metrics_template=None,
            datasets=list(self.datasets),
            alerts=self.alerts)

        self.update_basic(user, name, description, tags)

    def update_basic(self, user, name, description, tags):
        """
            Method to update the attributes specified at creation. Description and tags can be updated. tags is a list of string values.
        """
        tags = list_of_strs(tags)

        self.user = user
        self.name = name
        self.modelmonitor.name = name
        self.modelmonitor.owner = user
        self.modelmonitor.description = description
        self.modelmonitor.tags = tags
        
        ## Defaults
        self.modelmonitor.drift_detection_run_frequency_hrs = 1
        self.modelmonitor.drift_detection_algorithm = 'Kolmogorov-Smirnov Divergence'
        
        return self
    
    def add_dataset(self,name,data_class,version=None):
        mm_dataset = ModelmonitorDatasetDef(id=None, _class=data_class, transformer_script=None, name=name, sql_query=None,
                                               s3_subpath=None, version=version, data_format=None, groundtruth_col=None,
                                               predict_col=None, created_at=None, updated_at=None)
        
        self.modelmonitor.datasets.append(mm_dataset)
        
    def add_alert(self,name,alert_class):
        mm_alert = ModelmonitorAlertDef(id=None,_class=alert_class,email=None,name=name,conditions=self.conditions)
        
        self.modelmonitor.alerts.append(mm_alert)
    
    def update_datasets(self,name,data_class,transformer_script=None,sql_query=None,groundtruth_col=None,predict_col=None):
        self.datasets.name = name
        self.datasets._class = data_class
        self.datasets.transformer_script = transformer_script
        self.datasets.sql_query = sql_query
        self.datasets.groundtruth_col = groundtruth_col
        self.datasets.predict_col = predict_col
        
    
    def update_alerts(self,name,alert_class,conditions=None):
        self.alerts.name = name
        self.alerts._class = alert_class
        self.alerts.conditions = conditions
        

            
    def add_modelmonitor(self,name,model_name,model_type,model_category,model_framework,version,run_freq,drift_algo,emails):
        self.modelmonitor.name = name
        self.modelmonitor.model= model_name
        self.modelmonitor.model_type = model_type
        self.modelmonitor.model_category = model_category
        self.modelmonitor.model_framework = model_framework
        self.modelmoniotr.version = version
        self.modelmonitor.drift_detection_run_frequency_hrs = run_freq
        self.modelmonitor.drift_detecttion_algorithm = drift_algo
        self.modelmonitor.emails = emails
