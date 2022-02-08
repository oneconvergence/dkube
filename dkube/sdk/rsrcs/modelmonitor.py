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
from dkube.sdk.internal.dkube_api.models.modelmonitor_data_source_def import (
    ModelmonitorDataSourceDef,
)
from dkube.sdk.internal.dkube_api.models.modelmonitor_def import ModelmonitorDef
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


class SchemaFeatureClass(Enum):
    """
    This Enum class defines the feature classes that are suported for the Dkube modelmonitor schema.

    *Available in DKube Release: 3.x*

    """

    Categorical = "categorical"
    Continuous = "continuous"

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class SchemaFeatureType(Enum):
    """
    This Enum class defines the feature type that are suported for the Dkube modelmonitor schema.

    *Available in DKube Release: 3.x*

    """

    InputFeature = "input_feature"
    PredictionOutput = "prediction_output"
    Timestamp = "timestamp"
    RowId = "row_id"
    Null = "null"

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class PipelineComponentType(Enum):
    """
    This Enum class defines the type that are suported for the Pipeline component of the Dkube modelmonitor.

    *Available in DKube Release: 3.x*

    """

    Baseline = "baseline"
    DataDrift = "data_drift"
    PerformanceDrift = "performance_drift"
    DeploymentHealth = "deployment_health"

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class Protocol(Enum):
    """
    This Enum class defines the protocols that are suported for the metrics in deployment of the Dkube modelmonitor.

    *Available in DKube Release: 3.x*

    """

    tcp = "tcp"
    http = "http"

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class DriftAlgo(Enum):
    """
    This Enum class defines the drift detection algorithms that are suported for the Dkube modelmonitor.

    *Available in DKube Release: 3.0*

    """

    KS = "kolmogorov-smirnov"
    ChiSquared = "chi Squared"
    KSChiSquared = "kolmogorov-smirnov & chi squared"
    Auto = "auto"

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class SourceTypePerformance(Enum):
    """
    This Enum class defines the source type for the performance monitoring.

    *Available in DKube Release: 3.0*

    """

    LabelledData = "labelled_data"
    Metrics = "metrics"
    Custom = "custom"

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class ModelType(Enum):
    """
    This Enum class defines the model type that are suported for the Dkube modelmonitor.

    *Available in DKube Release: 3.0*

    """

    Regression = "regression"
    Classification = "classification"

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class ModelCategory(Enum):
    """
    This Enum class defines the category of the model that are suported for the Dkube modelmonitor.

    *Available in DKube Release: 3.0*

    """

    TimeSeries = "time_series"
    Other = "other"

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class SourceTypeDeployment(Enum):
    """
    This Enum class defines the source type that are suported for the Dkube deployment monitoring.

    *Available in DKube Release: 3.0*

    """

    Metrics = "metrics"
    Custom = "custom"

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class DatasetClass(Enum):
    """
    This Enum class defines the dataset class that are suported for the Dkube modelmonitor.

    *Available in DKube Release: 3.x*

    """

    Train = "train"
    Predict = "predict"
    Labelled = "labelled"
    Metrics = "metrics"

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class DatasetFormat(Enum):
    """
    This Enum class defines the dataset formats that are suported for the Dkube modelmonitor.

    *Available in DKube Release: 3.0*

    """

    Tabular = "tabular"
    Cloudevents = "cloudevents"
    Sagemakerlogs = "sagemakerlogs"
    Image = "image"

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class AlertClass(Enum):
    """
    This Enum class defines the alert class that are suported for the Dkube modelmonitor.

    *Available in DKube Release: 3.x*

    """

    FeatureDrift = "feature_drift"
    PerformanceDecay = "performance_decay"
    DeploymentHealth = "deployment_health"

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class AlertState(Enum):
    """
    This Enum class defines the alert state that are suported for the Dkube modelmonitor.

    *Available in DKube Release: 3.0*

    """

    Enabled = "enabled"
    Disabled = "disabled"
    Invalid = "invalid"

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class AlertActionType(Enum):
    """
    This Enum class defines the alert action type that are suported for the Dkube modelmonitor.

    *Available in DKube Release: 3.0*

    """

    Email = "email"

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class DriftMonitor(object):
    """
    This class defines the DKube Drift Monitoring with helper functions to set properties
    *Available in DKube Release: 3.x
    """

    def __init__(
        self, enabled=None, frequency=None, algorithm=None, soft_threshold=None
    ):
        self.enabled = None
        self.frequency = None
        self.algorithm = None
        self.soft_threshold = None

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def update_drift_monitoring_details(
        self,
        enabled=None,
        frequency=None,
        algorithm: DriftAlgo = None,
        soft_threshold=None,
    ):
        """
        This function updates the DKube drift monitor details. The following updates are supported:
        enabled : boolean value,
        frequency : an integer, frequency for detecting concept drift
        algorithm : Drift Algorithm, see the DriftAlgo Enum class for the details,
        soft_threshold : float , threshold defined by user. if not defined the pipeline_soft_threshold will be utilised
        """
        if enabled:
            self.update_drift_enabled(enabled)
        if frequency:
            self.update_drift_frequency(frequency)
        if algorithm:
            self.update_drift_algorithm(algorithm)
        if soft_threshold:
            self.update_drift_soft_threshold(soft_threshold)

    def update_drift_enabled(self, enabled=None):
        """
        Method to update the enable option in drift monitoring
        """
        self.enabled = enabled

    def update_drift_frequency(self, frequency=None):
        """
        Method to update the drift frequency in the drift monitoring
        """
        self.frequency = frequency

    def update_drift_algorithm(self, algorithm: DriftAlgo = None):
        """
        Method to update the algorithm for evaluating the drift
        """
        self.algorithm = algorithm

    def update_drift_soft_threshold(self, soft_threshold=None):
        """
        Method to update the soft threshold in the drift monitoring
        """
        self.soft_threshold = soft_threshold


class PerformanceMonitor(object):
    """
    This class defines the DKube Performance Monitoring with helper functions to set properties
    *Available in DKube Release: 3.x
    """

    def __init__(
        self,
        enabled=None,
        frequency=None,
        source_type: SourceTypePerformance = None,
        docker_image=None,
        soft_thresholds=None,
    ):
        self.enabled = None
        self.frequency = None
        self.source_type = None
        self.docker_image = None
        self.soft_thresholds = None

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def update_performance_monitoring_details(
        self,
        enabled=None,
        frequency=None,
        source_type: SourceTypePerformance = None,
        docker_image=None,
        startup_script=None,
        soft_thresholds=None,
    ):
        """
        This function updates the DKube performance monitoring details. The following updates are supported:
        enabled : boolean value,
        frequency : an integer, frequency for performance monitoring
        source_type: SourceType see the SourceType Enum class for the details,
        startup_script: the startup script
        soft_thresholds : a dictionary containing baseline and soft thresholds, eg : { baseline:0.02, soft:0.01}
        """
        if enabled:
            self.update_performance_enabled(enabled)
        if frequency:
            self.update_performance_frequency(frequency)
        if source_type:
            self.update_performance_source_type(source_type)
        if docker_image:
            self.update_performance_docker_image(docker_image)
        if startup_script:
            self.update_performance_startup_script(startup_script)
        if soft_thresholds:
            self.update_performance_soft_thresholds(soft_thresholds)

    def update_performance_enabled(self, enabled=None):
        """
        Method to update the enable option in performance monitoring
        """
        self.enabled = enabled

    def update_performance_frequency(self, frequency=None):
        """
        Method to update the frequency in the perfromance monitoring
        """
        self.frequency = frequency

    def update_performance_source_type(self, source_type: SourceTypePerformance = None):
        """
        Method to update the source_type in performance monitoring
        """
        self.source_type = source_type

    def update_performance_docker_image(self, docker_image=None):
        """
        Method to update the docker image in the performance monitoring
        """
        self.docker_image = docker_image

    def update_performance_startup_script(self, startup_script=None):
        """
        Method to update the startup script in the performance montitoring
        """
        self.startup_script = startup_script

    def update_performance_soft_thresholds(self, soft_thresholds=None):
        """
        Method to update the soft thresholds in the performance monitoring
        """
        self.soft_thresholds = soft_thresholds


class DeploymentMonitor(object):
    def __init__(
        self,
        enabled=None,
        frequency=None,
        cluster=None,
        source_type: SourceTypeDeployment = None,
        metrics=None,
        collect_metrics=None,
        soft_thresholds=None,
    ):
        self.enabled = None
        self.frequency = None
        self.cluster = None
        self.source_type = None
        self.metrics = {}
        self.collect_metrics = None
        self.soft_thresholds = {}

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def update_deployment_monitoring_details(
        self,
        enabled=None,
        frequency=None,
        cluster=None,
        source_type: SourceTypeDeployment = None,
        metrics=None,
        collect_metrics=None,
        soft_thresholds=None,
    ):
        """
        This function updates the DKube deployment monitoring details. The following updates are supported:
        enabled : boolean value,
        frequency : an integer, frequency for deployment monitoring
        cluster: cluster
        source_type: SourceType see the DeploymentSourceType Enum class for the details,
        metrics:
        soft_thresholds : a dictionary containing baseline and soft thresholds, eg : { baseline:0.02, soft:0.01}
        """
        if enabled:
            self.update_deployment_enabled(enabled)
        if frequency:
            self.update_deployment_frequency(frequency)
        if cluster:
            self.update_deployment_cluster(cluster)
        if source_type:
            self.update_deployment_source_type(source_type)
        if collect_metrics:
            self.update_deployment_collect_metrics(collect_metrics)
        if soft_thresholds:
            self.update_deployment_soft_thresholds(soft_thresholds)

    def update_deployment_enabled(self, enabled=None):
        """
        Method to update the enable option in deployment monitoring
        """
        self.enabled = enabled

    def update_deployment_frequency(self, frequency=None):
        """
        Method to update the frequency in the deployment monitoring
        """
        self.frequency = frequency

    def update_deployment_cluster(self, cluster=None):
        """
        Method to update the cluster in the deployment monitoring
        """
        self.cluster = cluster

    def update_performance_source_type(self, source_type: SourceTypeDeployment = None):
        """
        Method to update the source_type in deployment monitoring
        """
        self.source_type = source_type

    def update_deployment_collect_metrics(self, collect_metrics=None):
        """
        Method to update whether to collect metrics in the performance monitoring or not
        """
        self.collect_metrics = collect_metrics

    def update_deployment_soft_thresholds(self, soft_thresholds=None):
        """
        Method to update deployment soft thresholds in performance monitoring
        """
        self.soft_thresholds = soft_thresholds

    def update_deployment_metrics(
        self,
        heartbeat=None,
        protocol: Protocol = None,
        payload=None,
        headers=None,
        response_status_code=None,
        response_body=None,
    ):
        """
        Method to update deployment metrics in performance monitoring
        """
        self.metrics = {
            "heartbeat": heartbeat,
            "protocol": protocol,
            "payload": payload,
            "headers": headers,
            "response_status_code": response_status_code,
            "response_body": response_body,
        }


class DkubeModelmonitoralert(object):
    """
    This class defines the DKube Modelmonitor alert with helper functions to set properties of modelmonitor alert.::
        from dkube.sdk import *
        mm = DkubeModelmonitoralert(name="mm-alert")
        Where first argument is the name of the alert in the modelmonitor .
    *Available in DKube Release: 3.x*
    """

    def __init__(self, name="mm-alert", tags=[]):
        self.id = None
        self._class = None
        self.enabled = None
        self.name = name
        self.tags = tags
        self.conditions = []
        self.alert_action = {}

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def update_alert(
        self,
        alert_class: AlertClass = "FeatureDrift",
        enabled=None,
        tags=None,
        feature=None,
        metric=None,
        threshold=None,
        percent_threshold=None,
        breach_threshold=None,
        action_type="email",
    ):
        """
        This function updates the alert in the model monitor. The following updates are supported.
            alert_class,
            enabled,
            tags,
            feature,
            metric,
            threshold,
            percent_threshold,
            breach_threshold,
            action_type
        """
        if tags:
            self.tags = tags
        self.name = self.name
        self._class = alert_class
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
        if breach_threshold:
            self.alert_action["breach_threshold"] = breach_threshold
        if action_type:
            self.alert_action["action_type"] = action_type


class DkubeModelmonitor(object):
    """
    This class defines the DKube Modelmonitor with helper functions to set properties of modelmonitor.::
        from dkube.sdk import *
        mm = DkubeModelmonitor(name="mm",model_name='insurancemodel:ocdkube')
        Where first argument is the name of the modelmonitor
        second argument is the name of the model that you want to monitor i.e. nameofmodel:user
        user should be a valid onboarded user in dkube.

    *Available in DKube Release: 3.x

    """

    def __init__(self, name=generate("mm"), model_name="", description="", tags=None):

        self.alerts = []
        self.datasources = {}
        self.features = []
        self.metrics = {}
        self.schema = {}
        self.deployment_monitoring = {}
        self.drift_monitoring = {}
        self.performance_monitoring = {}
        self.features.append(
            ModelmonitorSchemaFeature(selected=None, _class=None, label=None, type=None)
        )
        self.status = ModelmonitorStatusDef(
            state=None,
            sub_state=None,
            message=None,
            code=None,
            success=None,
            schema_updated=None,
            alerts_updated=None,
        )
        self.pipeline_component = ModelmonitorComponentDef(
            run_id=None, status_info=None, status=None, type=None
        )
        self.modelmonitor = ModelmonitorDef(
            id=None,
            status=self.status,
            schema=self.schema,
            pipeline_component=self.pipeline_component,
            deployment_monitoring=self.deployment_monitoring,
            drift_monitoring=self.drift_monitoring,
            performance_monitoring=self.performance_monitoring,
            owner=None,
            name=None,
            description=None,
            tags=None,
            model=None,
            version=None,
            endpoint_url=None,
            model_type=None,
            model_category=None,
            datasources=self.datasources,
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
        version=None,
    ):
        """
        This function updates the DKube Modelmonitor configuration. The following updates are supported:
            model type,
            model category,
            drift detection algorithm,
            model version.
        """
        if model_type == None:
            self.update_model_type("regression")
        else:
            self.update_model_type(model_type)

        if model_category == None:
            self.update_model_category("time_series")
        else:
            self.update_model_category(model_category)

        if version:
            self.update_model_version(version)

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

    def update_model_version(self, version=None):
        """
        Method to update the model version
        """
        self.modelmonitor.version = version

    def upsert_datasources(
        self,
        id=None,
        _class: DatasetClass = None,
        transfomer_script=None,
        name=None,
        sql_query=None,
        s3_subpath=None,
        version=None,
        data_format=str(DatasetFormat.Tabular),
        groundtruth_col=None,
        predict_col=None,
        date_suffix=None,
    ):
        """
        This function updates the DKube Modelmonitor datasources fields.
        """
        mm_dataset = {}
        if name:
            mm_dataset["name"] = name
        if id:
            mm_dataset["id"] = id
        if data_format:
            mm_dataset["data_format"] = data_format
        if version:
            mm_dataset["version"] = version
        if s3_subpath:
            mm_dataset["s3_subpath"] = s3_subpath
        if groundtruth_col:
            mm_dataset["groundtruth_col"] = groundtruth_col
        if predict_col:
            mm_dataset["predict_col"] = predict_col
        if sql_query:
            mm_dataset["sql_query"] = sql_query
        if _class not in self.modelmonitor.datasources:
            self.modelmonitor.datasources[_class] = mm_dataset
        else:
            for key in mm_dataset:
                self.modelmonitor.datasources[_class][key] = mm_dataset[key]

    def update_drift_monitoring(self, drift=None):
        """
        This function updates the DKube Modelmonitor drift monitoring field.
        """
        self.modelmonitor.drift_monitoring = json.loads(drift.to_JSON())

    def update_performance_monitoring(self, performance=None):
        """
        This function updates the DKube Modelmonitor performance monitoring field.
        """
        self.modelmonitor.performance_monitoring = json.loads(performance.to_JSON())

    def update_deployment_monitoring(self, deployment=None):
        """
        This function updates the DKube Modelmonitor deployment monitoring field.
        """
        self.modelmonitor.deployment_monitoring = json.loads(deployment.to_JSON())
