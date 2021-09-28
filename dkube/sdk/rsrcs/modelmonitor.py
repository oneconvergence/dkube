from __future__ import print_function

import sys
import time
import json
from pprint import pprint
from .util import *

from dkube.sdk.internal import dkube_api

from dkube.sdk.internal.dkube_api.models.modelmonitor_status_def import ModelmonitorStatusDef
from dkube.sdk.internal.dkube_api.models.modelmonitor_schema_feature import ModelmonitorSchemaFeature
from dkube.sdk.internal.dkube_api.models.modelmonitor_default_threshold_def import ModelmonitorDefaultThresholdDef
from dkube.sdk.internal.dkube_api.models.modelmonitor_features_spec_def import ModelmonitorFeaturesSpecDef
from dkube.sdk.internal.dkube_api.models.modelmonitor_component_def import ModelmonitorComponentDef
from dkube.sdk.internal.dkube_api.models.modelmonitor_dataset_def import ModelmonitorDatasetDef
from dkube.sdk.internal.dkube_api.models.modelmonitor_alert_cond_def import ModelmonitorAlertCondDef
from dkube.sdk.internal.dkube_api.models.modelmonitor_alert_def import ModelmonitorAlertDef
from dkube.sdk.internal.dkube_api.models.modelmonitor_def import ModelmonitorDef


class DkubeModelMonitor(object):
    def __init__(self, user, name=generate("mm"),model_name="",description = '',tags=None):

       # self.features = []
        #self.features.append(ModelmonitorSchemaFeature(selected=None, label=None, _class='Categorical', type='InputFeature'))
        #self.schema = ModelmonitorFeaturesSpecDef(features=self.features)
        self.schema = {}
        self.default_thresholds = []
        self.train_metrics = None

        self.datasets = []

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
            default_thresholds = self.default_thresholds,
            datasets=self.datasets,
            alerts=self.alerts)

        self.update_basic(user,name,model_name, description, tags)
        #self.add_default_thresholds()
        #self.update_schema()

    def update_basic(self, user,name,model_name,description, tags):
        """
            Method to update the attributes specified at creation. Description and tags can be updated. tags is a list of string values.
        """
        tags = list_of_strs(tags)

        self.user = user
        self.name = name
        self.modelmonitor.name = name
        self.modelmonitor.owner = user
        self.modelmonitor.description = description
        self.modelmonitor.model = model_name+":"+self.user
        self.modelmonitor.tags = tags
        ## Defaults
        self.modelmonitor.drift_detection_run_frequency_hrs = 1
        self.modelmonitor.drift_detection_algorithm = 'Kolmogorov-Smirnov & Chi Squared'
        
        return self
    
    def add_dataset(self,name,data_class,version=None,data_format='csv',s3_subpath=None,gt_col=None,predict_col=None,sql_query=None):
        name = name + ":"+ self.user
        mm_dataset = ModelmonitorDatasetDef(id=None, _class=data_class, transformer_script=None, name=name, sql_query=sql_query,
                                               s3_subpath=s3_subpath, version=version, data_format=data_format, groundtruth_col=gt_col,
                                               predict_col=predict_col, created_at=None, updated_at=None)
        
        self.modelmonitor.datasets.append(mm_dataset)
        
    def add_alert(self,name,alert_class,feature=None,op='>',threshold=None):
        self.conditions = []
        self.conditions.append(ModelmonitorAlertCondDef(feature=feature, op=op, threshold=threshold))
        mm_alert = ModelmonitorAlertDef(_class=alert_class,email=None,name=name,conditions=self.conditions)
        
        self.modelmonitor.alerts.append(mm_alert)
        
    def add_default_thresholds(self,thtype='performance_threshold',threshold=0,percent_threshold=0):
        
        self.modelmonitor.default_thresholds.append(ModelmonitorDefaultThresholdDef(id=None,type=thtype,threshold=threshold,percent_threshold=percent_threshold))
    def update_schema(self,label,selected=None,schema_class='Categorical',schema_type='InputFeature'):
        self.features=[]
        self.features.append(ModelmonitorSchemaFeature(selected=selected, label=label, _class=schema_class, type=schema_type))
        self.modelmonitor.schema = ModelmonitorFeaturesSpecDef(features=self.features)
        
            
    def update_modelmonitor_details(self,model_type='Regression',model_category='TimeSeries',model_framework='Tensorflow-1x',version=None,run_freq=1,drift_algo='Kolmogorov-Smirnov & Chi Squared',emails=None,train_metrics=None):
        self.modelmonitor.model_type = model_type
        self.modelmonitor.model_category = model_category
        self.modelmonitor.model_framework = model_framework
        self.modelmonitor.version = version
        self.modelmonitor.drift_detection_run_frequency_hrs = run_freq
        self.modelmonitor.drift_detection_algorithm = drift_algo
        self.modelmonitor.emails = emails
        self.modelmonitor.train_metrics = train_metrics
        #self.modelmonitor.default_thresholds = default_thresholds
        #self.modelmonitor.schema = schema
    
    def update_transformer_script(self,data_name,script):
        for index,data in enumerate(self.modelmonitor.datasets):
            if (data.name == data_name+":"+self.user):
                self.modelmonitor.datasets[index].transformer_script = script
        
    def to_JSON(self):
        return json.dumps(self,default=lambda o: o.__dict__)


class DkubeModelMonitorDataset(object):
    def __init__(self, user, name=generate("mm-data")):
        self.user = user
        self._class = None
        self.transformer_script = None
        self.name = name
        self.sql_query = None
        self.s3_subpath = None
        self.version = None
        self.data_format = 'csv'
        self.groundtruth_col = None
        self.predict_col = None


    def to_JSON(self):
        return json.dumps(self,default=lambda o: o.__dict__)

    def update_dataset(self,data_class=None,transformer_script=None,sql_query=None,groundtruth_col=None,predict_col=None,data_format='csv'):
        self.name = self.name+":"+self.user
        self._class = data_class
        self.transformer_script = transformer_script
        self.sql_query = sql_query
        self.groundtruth_col = groundtruth_col
        self.predict_col = predict_col
        self.data_format = data_format

class DkubeModelMonitorAlert(object):
    def __init__(self,name=generate("mm-alert")):
        self._class = None
        self.name = name
        self.email = None
        self.feature = None
        self.op = '>'
        self.threshold = None 

    def to_JSON(self):
        return json.dumps(self,default=lambda o: o.__dict__)

    def update_alert(self,alert_class=None,feature=None,op=None,threshold=None):
        self.name = self.name
        self._class = alert_class
        self.feature = feature
        self.op = op
        self.threshold = threshold
        
        


