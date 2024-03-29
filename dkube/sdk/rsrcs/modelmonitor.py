from __future__ import print_function

import json
import sys
import time
from enum import Enum
from pprint import pprint

from dkube.sdk.internal import dkube_api
from dkube.sdk.internal.dkube_api.models.modelmonitor_alert_cond_def import (
    ModelmonitorAlertCondDef,
)
from dkube.sdk.internal.dkube_api.models.modelmonitor_alert_def import (
    ModelmonitorAlertDef,
)
from dkube.sdk.internal.dkube_api.models.modelmonitor_component_def import (
    ModelmonitorComponentDef,
)
from dkube.sdk.internal.dkube_api.models.modelmonitor_dataset_def import (
    ModelmonitorDatasetDef,
)
from dkube.sdk.internal.dkube_api.models.modelmonitor_def import ModelmonitorDef
from dkube.sdk.internal.dkube_api.models.modelmonitor_default_threshold_def import (
    ModelmonitorDefaultThresholdDef,
)
from dkube.sdk.internal.dkube_api.models.modelmonitor_features_spec_def import (
    ModelmonitorFeaturesSpecDef,
)
from dkube.sdk.internal.dkube_api.models.modelmonitor_schema_feature import (
    ModelmonitorSchemaFeature,
)
from dkube.sdk.internal.dkube_api.models.modelmonitor_status_def import (
    ModelmonitorStatusDef,
)

from .util import *


class DatasetClass(Enum):
    """
    This Enum class defines the dataset class that are suported for the Dkube modelmonitor.

    *Available in DKube Release: 3.0*

    """

    TrainData = "TrainData"
    PredictData = "PredictData"
    LabelledData = "LabelledData"

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class DatasetFormat(Enum):
    """
    This Enum class defines the dataset formats that are suported for the Dkube modelmonitor.

    *Available in DKube Release: 3.0*

    """

    csv = "csv"
    cloudevents = "cloudevents"
    sagemakerlogs = "sagemakerlogs"

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class ModelFrameworks(Enum):
    """
    This Enum class defines the frameworks that are suported for the Dkube modelmonitor.

    *Available in DKube Release: 3.0*

    """

    Tensorflow1x = "Tensorflow-1x"
    Tensorflow2x = "Tensorflow-2x"
    PyTorch = "PyTorch"
    SkLearn = "SkLearn"
    Other = "Other"

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class AlertClass(Enum):
    """
    This Enum class defines the alert class that are suported for the Dkube modelmonitor.

    *Available in DKube Release: 3.0*

    """

    FeatureDrift = "FeatureDrift"
    PerformanceDecay = "PerformanceDecay"
    PredictionDrift = "PredictionDrift"

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class ModelType(Enum):
    """
    This Enum class defines the model type that are suported for the Dkube modelmonitor.

    *Available in DKube Release: 3.0*

    """

    Regression = "Regression"
    Classification = "Classification"

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class ModelCategory(Enum):
    """
    This Enum class defines the category of the model that are suported for the Dkube modelmonitor.

    *Available in DKube Release: 3.0*

    """

    AutoEncoder = "AutoEncoder"
    TimeSeries = "TimeSeries"
    Other = "Other"

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class DriftAlgo(Enum):
    """
    This Enum class defines the drift detection algorithms that are suported for the Dkube modelmonitor.

    *Available in DKube Release: 3.0*

    """

    KS = "Kolmogorov-Smirnov"
    ChiSquared = "Chi Squared"
    KSChiSquared = "Kolmogorov-Smirnov & Chi Squared"
    Auto = "Auto"

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class DkubeModelmonitor(object):
    """
    This class defines the DKube Modelmonitor with helper functions to set properties of modelmonitor.::
        from dkube.sdk import *
        mm = DkubeModelmonitor(name="mm",model_name='insurancemodel:ocdkube')
        Where first argument is the name of the modelmonitor
        second argument is the name of the model that you want to monitor i.e. nameofmodel:user
        user should be a valid onboarded user in dkube.

    *Available in DKube Release: 3.0*

    """

    def __init__(self, name=generate("mm"), model_name="", description="", tags=None):

        self.schema = {}
        self.default_thresholds = []
        self.default_thresholds.append(
            ModelmonitorDefaultThresholdDef(
                id=None, type="performance_threshold", threshold=0, percent_threshold=0
            )
        )

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
            model_category=None,
            drift_detection_run_frequency_hrs=None,
            drift_detection_algorithm=None,
            performance_metrics_template=None,
            train_metrics=None,
            default_thresholds=self.default_thresholds,
            datasets=self.datasets,
            alerts=self.alerts,
        )

        self.update_basic(name, model_name, description, tags)

    def update_basic(self, name, model_name, description, tags):
        """
        Method to update the attributes specified at creation. Description and tags can be updated. tags is a list of string values.
        """
        tags = list_of_strs(tags)

        self.name = name
        self.modelmonitor.name = name
        self.modelmonitor.description = description
        self.modelmonitor.model = model_name
        self.modelmonitor.tags = tags

        return self

    def update_modelmonitor(
        self,
        model_type: ModelType = None,
        model_category: ModelCategory = None,
        model_framework: ModelFrameworks = None,
        version=None,
        run_freq=None,
        drift_algo: DriftAlgo = None,
        emails=None,
        train_metrics=None,
    ):
        """
        This function updates the DKube Modelmonitor configuration. The following updates are supported:
            model type,
            model category,
            model framework,
            drift detection algorithm,
            run frequency,
            train metrics,
            emails,
            model version.
        """
        if model_type == None:
            self.update_model_type("Regression")
        else:
            self.update_model_type(model_type)

        if model_category == None:
            self.update_model_category("TimeSeries")
        else:
            self.update_model_category(model_category)

        if model_framework == None:
            self.update_model_framework("Tensorflow-1x")
        else:
            self.update_model_framework(model_framework)

        if drift_algo == None:
            self.update_drift_detection_algorithm("Kolmogorov-Smirnov & Chi Squared")
        else:
            self.update_drift_detection_algorithm(drift_algo)

        if run_freq == None:
            self.update_run_frequency(1)
        else:
            self.update_run_frequency(run_freq)

        if train_metrics:
            self.update_train_metrics(train_metrics)

        if version:
            self.update_model_version(version)

        if emails:
            self.update_emails(emails)

    def update_model_type(self, model_type=None):
        """
        Method to update the type of the model, check the Enum Class ModelType for the posible values
        """
        self.modelmonitor.model_type = model_type

    def update_model_category(self, category=None):
        """
        Method to update the category of the model, check the Enum Class ModelCategory for the possible values
        """
        self.modelmonitor.model_category = category

    def update_model_framework(self, framework=None):
        """
        Method to update the framework, check the Enum Class ModelFramework for the possible values
        """
        self.modelmonitor.model_framework = framework

    def update_drift_detection_algorithm(self, algorithm=None):
        """
        Method to update the drift detection Algorithm, check the Enum Class DriftAlgo for the possible values
        """
        self.modelmonitor.drift_detection_algorithm = algorithm

    def update_run_frequency(self, frequency=None):
        """
        Method to update the frequency
        """
        self.modelmonitor.drift_detection_run_frequency_hrs = frequency

    def update_train_metrics(self, train_metrics=None):
        """
        Method to update the train metrics
        """
        self.modelmonitor.train_metrics = train_metrics

    def update_model_version(self, version=None):
        """
        Method to update the model version
        """
        self.modelmonitor.version = version

    def update_emails(self, emails=None):
        """
        Method to update the emails
        """
        self.modelmonitor.emails = emails

    def update_transformer_script(self, data_name, script):
        """
        Method to update the transformer script
        """
        for index, data in enumerate(self.modelmonitor.datasets):
            if data.name == data_name:
                self.modelmonitor.datasets[index].transformer_script = script
    
    def upsert_dataset(
        self,
        name,
        id=None,
        data_class: DatasetClass = None,
        data_format: DatasetFormat = "csv",
        version=None,
        s3_subpath=None,
        gt_col=None,
        predict_col=None,
        sql_query=None,
    ):
        """
        This function is for adding or updating the dataset in the model monitor.
            name : name of the dataset,
            data class : see the Enum DatasetClass,
            format of the dataset: see the Enum class DatasetFormat,
            version : version of the dataset,
            s3_subpath : s3_subpath of the dataset,
            gt_col: groundtruth column of Labelled Dataset,
            predict_col : predict column of Predict dataset,
            sql query in case of sql dataset.
        """
        mm_dataset = {}
        mm_dataset["name"]=name
        mm_dataset["id"]=id
        mm_dataset["_class"]=data_class
        mm_dataset["data_format"]=data_format
        mm_dataset["version"]=version
        mm_dataset["s3_subpath"]=s3_subpath
        mm_dataset["groundtruth_col"]=gt_col
        mm_dataset["predict_col"]=predict_col
        mm_dataset["sql_query"]=sql_query
        
        self.modelmonitor.datasets.append(mm_dataset)

class DkubeModelmonitordataset(object):
    """
    This class defines the DKube Modelmonitor dataset with helper functions to set properties of modelmonitor dataset.::
        from dkube.sdk import *
        mm = DkubeModelmonitordataset(name="mm-data:ocdkube")
        Where first argument is the name of the modelmonitor dataset.

    *Available in DKube Release: 3.0*
    
    """

    def __init__(self, name=generate("mm-data")):
        self._class = None
        self.transformer_script = None
        self.name = name
        self.sql_query = None
        self.s3_subpath = None
        self.version = None
        self.data_format = None
        self.groundtruth_col = None
        self.predict_col = None

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def update_dataset(
        self,
        data_name=None,
        data_class: DatasetClass = None,
        data_format: DatasetFormat = "csv",
        transformer_script=None,
        sql_query=None,
        groundtruth_col=None,
        predict_col=None,
        s3_subpath=None,
        version=None,
    ):

        """
        This function updates the DKube Modelmonitor dataset. The following updates are supported:
            data class,
            transformer script,
            sql query in case of sql dataset,
            groundtruth column of Labelled Dataset,
            predict column of Predict dataset,
            format of the dataset.

        """
        if data_name:
            self.update_data_name(data_name)

        if data_class:
            self.update_data_class(data_class)

        if transformer_script:
            self.update_transformer_script(transformer_script)

        if sql_query:
            self.update_sql_query(sql_query)

        if groundtruth_col:
            self.update_groundtruth_col(groundtruth_col)

        if predict_col:
            self.update_predict_col(predict_col)

        if data_format == None:
            self.update_data_format("csv")
        else:
            self.update_data_format(data_format)

        if s3_subpath:
            self.update_s3_subpath(s3_subpath)

        if version:
            self.update_dataset_version(version)

    def update_data_name(self, data_name=None):
        """
        Method to update the dataset name in the model monitor
        """
        self.name = data_name

    def update_data_class(self, data_class=None):
        """
        Method to update the class of the dataset
        """
        self._class = data_class

    def update_transformer_script(self, script=None):
        """
        Method to update transformer script
        """
        self.transformer_script = script

    def update_sql_query(self, sql_query=None):
        """
        Method to update sql query in case of sql dataset
        """
        self.sql_query = sql_query

    def update_groundtruth_col(self, groundtruth_col=None):
        """
        Method to update the groundtruth column for Labelled Dataset
        """
        self.groundtruth_col = groundtruth_col

    def update_predict_col(self, predict_col=None):
        """
        Method to update the predict column for the Predict Dataset
        """
        self.predict_col = predict_col

    def update_data_format(self, data_format=None):
        """
        Method to update the format of the dataset, check the Enum DatasetFormat class
        """
        self.data_format = data_format

    def update_s3_subpath(self, path=None):
        """
        Method to update s3 subpath of the dataset
        """
        self.s3_subpath = path

    def update_dataset_version(self, version=None):
        """
        Method to update the dataset version
        """
        self.version = version


class DkubeModelmonitoralert(object):
    """
    This class defines the DKube Modelmonitor alert with helper functions to set properties of modelmonitor alert.::
        from dkube.sdk import *
        mm = DkubeModelmonitoralert(name="mm-alert")
        Where first argument is the name of the alert in the modelmonitor .

    *Available in DKube Release: 3.0*

    """

    def __init__(self, name="mm-alert"):
        self.id = None
        self._class = None
        self.name = name
        self.email = None
        self.conditions = []

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def update_alert(
        self,
        email=None,
        alert_class: AlertClass = "FeatureDrift",
        feature=None,
        metric=None,
        threshold=None,
        percent_threshold=None,
    ):
        """
        This function updates the alert in the model monitor. The following updates are supported.
            email,
            alert_class,
            feature,
            metric,
            threshold,
            percent_threshold
        """

        self.id = None
        self.name = self.name
        self._class = alert_class
        self.email = email
        self.conditions.append(
            {
                "id": None,
                "feature": feature,
                "metric": metric,
                "op": ">",
                "threshold": threshold,
                "percent_threshold": percent_threshold,
            }
        )

