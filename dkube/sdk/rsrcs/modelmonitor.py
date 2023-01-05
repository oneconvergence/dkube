from __future__ import print_function

import json
import operator
import sys
import time
from enum import Enum

from dkube.sdk.internal import dkube_api
from dkube.sdk.internal.dkube_api.models import conditions
from dkube.sdk.internal.dkube_api.models.modelmonitor_alert_cond_def import \
    ModelmonitorAlertCondDef
from dkube.sdk.internal.dkube_api.models.modelmonitor_alert_def import \
    ModelmonitorAlertDef
from dkube.sdk.internal.dkube_api.models.modelmonitor_component_def import \
    ModelmonitorComponentDef
from dkube.sdk.internal.dkube_api.models.modelmonitor_data_source_def import \
    ModelmonitorDataSourceDef
from dkube.sdk.internal.dkube_api.models.modelmonitor_def import \
    ModelmonitorDef
from dkube.sdk.internal.dkube_api.models.modelmonitor_features_spec_def import \
    ModelmonitorFeaturesSpecDef
from dkube.sdk.internal.dkube_api.models.modelmonitor_input_data_shape_def import \
    ModelmonitorInputDataShapeDef
from dkube.sdk.internal.dkube_api.models.modelmonitor_schema_feature import \
    ModelmonitorSchemaFeature
from dkube.sdk.internal.dkube_api.models.modelmonitor_status_def import \
    ModelmonitorStatusDef

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


class DataType(Enum):
    """
    This Enum class defines the input data type for the Dkube modelmonitor.

    *Available in DKube Release: 3.3*

    """

    Tabular = "tabular"
    Image = "image"

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class TimeZone(Enum):
    """
    This Enum class defines the timezone for the Dkube modelmonitor.

    *Available in DKube Release: 3.3*

    """

    UTC = "utc"
    DKube = "dkube"

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class ChannelOrder(Enum):
    """
    This Enum class defines the channel order for image data.

    *Available in DKube Release: 3.3*

    """

    ChannelsLast = "last"
    ChannelsFirst = "first"

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class ImageDataSavedFileFormat(Enum):
    """
    This Enum class defines the possible data arrangements for image data.

    *Available in DKube Release: 3.3*

    """

    BinNumpyArray = "bin_numpy_array"
    ImgFilesLabelsCSV = "img_files_labels_csv"
    ImagesInLabelledFolder = "images_in_labelled_folder"

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


class ModelMonitorState(Enum):
    """
    This Enum class defines the states that the Dkube modelmonitor can belong to.

    *Available in DKube Release: 3.x*

    """

    WarningState = "warning"
    CriticalState = "critical"

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

    *Available in DKube Release: 3.x

    """

    def __init__(self, deployemnt_id):
        self.alerts = []
        self.datasources = {}
        self.features = []
        self.metrics = {}
        self.schema = {}
        self.deployment_monitoring = {}
        self.drift_monitoring = {}
        self.performance_monitoring = {}
        self.input_data_shape = {}
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
            id=deployemnt_id,
            status=self.status,
            schema=self.schema,
            pipeline_component=self.pipeline_component,
            deployment_monitoring=self.deployment_monitoring,
            drift_monitoring=self.drift_monitoring,
            performance_monitoring=self.performance_monitoring,
            owner=None,
            name=None,
            thresholds=None,
            model_type=None,
            input_data_shape=self.input_data_shape,
            datasources=self.datasources,
            alerts=self.alerts,
        )

    def update_modelmonitor_basics(
        self, 
        model_type: ModelType,  
        input_data_type: DataType,
        data_timezone: TimeZone = "utc",
    ):
        """
        Method to update the basic attributes specified at creation.
        """
        if data_timezone:
            self.modelmonitor.data_timezone = data_timezone
        if model_type in ["regression", "classification"]:
            self.modelmonitor.model_type = model_type
        else:
            raise ValueError(
                "Please define the supported model types, regression or classification"
            )
        if input_data_type:
            self.modelmonitor.input_data_type = input_data_type
        else:
            raise ValueError("Input data type is required")

    def add_thresholds(
        self,
        thresholds
    ):
        """
        Method to update the thresholds.
        """
        if thresholds:
            self.modelmonitor.thresholds = thresholds

    def add_datasources(
        self,
        dataset_id=None,
        data_class: DatasetClass = None,
        transformer_script=None,
        name=None,
        sql_query=None,
        s3_subpath=None,
        version=None,
        data_format: DatasetFormat = None,
        groundtruth_col=None,
        predict_col=None,
        date_suffix=None,
        timestamp_col=None,
    ):
        """
        This function adds the datasource in dkube Model monitor.
        """
        if data_class is None:
            raise ValueError("Please provide a class for which dataset needs to be added")

        else:
            mm_dataset = {}
            if name:
                mm_dataset["name"] = name
            if dataset_id:
                mm_dataset["id"] = dataset_id
            if transformer_script:
                mm_dataset["transformer_script"] = transformer_script
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
            if data_class:
                mm_dataset["class"] = data_class
            if date_suffix:
                mm_dataset["date_suffix"] = date_suffix
            if data_class == "labelled" and timestamp_col:
                mm_dataset["timestamp_col"] = timestamp_col

            if data_class not in self.modelmonitor.datasources:
                self.modelmonitor.datasources[data_class] = mm_dataset

    def update_image_data_shape(
        self,
        height,
        width,
        channel=0,
        channel_order=str(ChannelOrder.ChannelsLast)
    ):
        """
        This function updates the DKube Modelmonitor image data shape.
        """
        self.input_data_shape["height"] = height
        self.input_data_shape["width"] = width
        self.input_data_shape["channel"] = channel
        self.input_data_shape["channel_order"] = channel_order

    def update_datasources(
        self,
        dataset_id=None,
        data_class: DatasetClass = None,
        transformer_script=None,
        name=None,
        sql_query=None,
        s3_subpath=None,
        version=None,
        data_format=str(DatasetFormat.Tabular),
        groundtruth_col=None,
        predict_col=None,
        date_suffix=None,
        timestamp_col=None,
    ):
        """
        This function updates the DKube Modelmonitor datasource.
        """
        if data_class is None:
            raise ValueError("Please provide a class for which dataset needs to be updated")
        else:

            mm_dataset = {}
            if name:
                mm_dataset["name"] = name
            if dataset_id:
                mm_dataset["id"] = dataset_id
            if transformer_script:
                mm_dataset["transformer_script"] = transformer_script
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
            if data_class:
                mm_dataset["class"] = data_class
            if date_suffix:
                mm_dataset["date_suffix"] = date_suffix
            if data_class == "labelled" and timestamp_col:
                mm_dataset["timestamp_col"] = timestamp_col

            for key in mm_dataset:
                self.modelmonitor.datasources[data_class][key] = mm_dataset[key]

    def update_drift_monitoring_details(
        self,
        enabled=None,
        frequency=5,
        algorithm: DriftAlgo = "auto",
        image_train_data_savedfile_format: ImageDataSavedFileFormat = None,
        image_predict_data_savedfile_format: ImageDataSavedFileFormat = None,
        image_path=None,
        run_as_script=None,
    ):
        """
        This function updates the DKube drift monitor details. The following updates are supported:
        enabled : boolean value,
        frequency : an integer, frequency for detecting concept drift
        algorithm : Drift Algorithm, see the DriftAlgo Enum class for the details,
        """
        if enabled:
            self.modelmonitor.drift_monitoring["enabled"] = enabled
        if frequency:
            self.modelmonitor.drift_monitoring["frequency"] = frequency
        if algorithm:
            self.modelmonitor.drift_monitoring["algorithm"] = algorithm
        if str(self.modelmonitor.input_data_type) == "image":
            if (image_train_data_savedfile_format is None
                and
                    image_predict_data_savedfile_format is None):
                raise ValueError("Please provide image saved file format for train and predict data")
            else:
                self.modelmonitor.drift_monitoring["image_train_data_savedfile_format"] = image_train_data_savedfile_format
                self.modelmonitor.drift_monitoring["image_predict_data_savedfile_format"] = image_predict_data_savedfile_format
            self.schema = None
        if algorithm == "custom":
            self.modelmonitor.drift_monitoring["custom"] = {"image":dict()}
            if image_path:
                self.modelmonitor.drift_monitoring["custom"]["path"] = image_path
            else:
                raise ValueError("image_path not passed for custom data drift")
            if run_as_script:
                self.modelmonitor.drift_monitoring["custom"]["runas"] = run_as_script
            else:
                raise ValueError("run_as_script not passed for custom data drift")
     
    def update_performance_monitoring_details(
        self,
        enabled=None,
        frequency=5,
        source_type: SourceTypePerformance = None,
        image_path=None,
        run_as_script=None,
    ):
        """
        This function updates the DKube performance monitoring details. The following updates are supported:
        enabled : boolean value,
        frequency : an integer, frequency for performance monitoring
        source_type: SourceType see the SourceType Enum class for the details,
        startup_script: the startup script
        """
        if enabled:
            self.modelmonitor.performance_monitoring["enabled"] = enabled
        if frequency:
            self.modelmonitor.performance_monitoring["frequency"] = frequency
        if source_type:
            self.modelmonitor.performance_monitoring["source_type"] = source_type
        if source_type == SourceTypePerformance.Custom.value:
            self.modelmonitor.performance_monitoring["custom"] = {"image":dict()}
            if image_path:
                self.modelmonitor.performance_monitoring["custom"]["path"] = image_path
            else:
                raise ValueError("Image not passed for custom performacne drift")
            if run_as_script:
                self.modelmonitor.performance_monitoring["custom"]["runas"] = run_as_script
            else:
                raise ValueError("Run as script not passed for custom performacne drift")
        
    def update_deployment_monitoring_details(
        self,
        enabled,
        frequency=1,
    ):
        """
        This function updates the DKube deployment monitoring details. The following updates are supported:
        enabled : boolean value,
        frequency : an integer, frequency for deployment monitoring
        """
        if enabled:
            self.modelmonitor.deployment_monitoring["enabled"] = enabled
        if frequency:
            self.modelmonitor.deployment_monitoring["frequency"] = frequency
        self.modelmonitor.deployment_monitoring["collect_metrics"] = True


class DkubeModelmonitorAlert(object):
    """
    This class defines the DKube Modelmonitor alert with helper functions to set properties of modelmonitor alert.::
        from dkube.sdk import *
        mm = DkubeModelmonitoralert(name="mm-alert")
        Where the arguments are .
        alert_class, enabled, tags, emails
    *Available in DKube Release: 3.x*
    """

    def __init__(self, name,
                 alert_class: AlertClass = "feature_drift",
                 enabled=None,
                 emails=None,
                 action_type="email",
                 tags=[]
                 ):
        self.id = None
        self._class = alert_class
        self.enabled = enabled
        self.name = name
        self.tags = tags
        self.conditions = []
        self.alert_action = {}
        self.alert_action["action_type"] = action_type
        self.alert_action["emails"] = emails
        self.alert_loaded = False

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def load_modelmonitor_alert(self, alert_obj):
        self.id = alert_obj["id"]
        self._class = alert_obj["_class"]
        self.enabled = alert_obj["enabled"]
        self.name = alert_obj["name"]
        self.tags = alert_obj["tags"]
        self.conditions = alert_obj["conditions"]
        self.alert_action = alert_obj["alert_action"]
        self.alert_loaded = True
        
    def add_alert_condition(
        self,
        feature=None,
        metric=None,
        threshold=None,
        state: ModelMonitorState = None,
        op=None,
    ):
        """
        This function add the alert condition in the model monitor alert. The following updates are supported.
            feature,
            metric,
            threshold,
            op,
            state
        """
        ops = {operator.gt: ">", operator.lt: '<', operator.ge: '>=', operator.le: '<=', None: None}
        try:
            alert_op = ops[op]
        except Exception:
            raise ValueError(f"{op} not supported, only operator.gt, operator.lt, operator.ge and operator.le are allowed")
        if (feature is None) and (metric is None):
            raise ValueError("Both feature and metric can not be none, one is required")
        if (feature is not None) and (metric is not None):
            raise ValueError("Both feature and metric can not passed, only one can be passed")
        # Adding the check otherwise the condition is getting appended
        if (threshold is None) and (state is None):
            raise ValueError("Both threshold and state can not be None, only one can be passed")
        if (threshold is not None) and (state is not None):
            raise ValueError("Both threshold and state can not passed, only one can be passed")
        if (op is None) and (threshold is not None):
            raise ValueError("Operator is not passed")

        alert_key = "feature" if self._class == "feature_drift" else "metric"
        cond = dict()
        cond["state"] = state
        cond["op"] = alert_op
        cond["threshold"] = threshold
        cond[alert_key] = feature if feature is not None else metric
        cond["action"] = "add"
        self.conditions.append(cond)


    def update_alert_condition(
        self,
        feature=None,
        metric=None,
        threshold=None,
        state: ModelMonitorState = None,
        op=None,
    ):
        """
        This function update the alert condition in the model monitor alert. The following updates are supported.
            feature,
            metric,
            threshold,
            op,
            state
        """
        ops = {operator.gt: ">", operator.lt: '<', operator.ge: '>=', operator.le: '<=', None: None}
        try:
            alert_op = ops[op]
        except Exception:
            raise ValueError(f"{op} not supported, only operator.gt, operator.lt, operator.ge and operator.le are allowed")
        if (feature is None) and (metric is None):
            raise ValueError("Both feature and metric can not be none, one is required")
        if (feature is not None) and (metric is not None):
            raise ValueError("Both feature and metric can not passed, only one can be passed")
        if (threshold is None) and (op is None) and (state is None):
            raise ValueError("All threshold, state, and op is none, nothing to update")

        alert_key = "feature" if self._class == "feature_drift" else "metric"
        alert_key_name = feature if feature is not None else metric
        
        if len(self.conditions) == 0:
            raise ValueError("existing conditions are empty, use load_modelmonitor_alert first before updating an alert")

        for cond in self.conditions:
            if cond[alert_key] == alert_key_name:
                if alert_op:
                    cond["op"] = alert_op
                if threshold:
                    cond["threshold"] = threshold
                if state:
                    cond["state"] = state
                return
        
        raise ValueError(f"update key not found {alert_key_name}")

    def delete_alert_condition(
        self,
        feature=None,
        metric=None,
    ):
        """
        This function deletes the alert condition in the model monitor alert. The following updates are supported.
            feature,
            metric,
        """
        if (feature is None) and (metric is None):
            raise ValueError("Both feature and metric can not be none, one is required")
        if (feature is not None) and (metric is not None):
            raise ValueError("Both feature and metric can not passed, only one can be passed")
        
        alert_key = "feature" if self._class == "feature_drift" else "metric"
        alert_key_name = feature if feature is not None else metric
        
        if len(self.conditions) == 0:
            raise ValueError("existing conditions are empty, use load_modelmonitor_alert first before deleting an alert")
        for each_condition in self.conditions:
            if each_condition[alert_key] == alert_key_name:
                self.conditions.remove(each_condition)
                return
        raise ValueError(f"{alert_key_name} not found in existing conditions")

    update_alert = add_alert_condition

    def update_breach_incidents(
        self,
        breach_incidents
    ):
        """
        This function update breach incidents of the model monitor alert. Input,
            breach_incidents
        """
        self.alert_action["breach_threshold"] = breach_incidents

    def update_emails(
        self,
        emails
    ):
        """
        This function update emails of the model monitor alert. Input,
            emails
        """
        self.alert_action["emails"] = emails

    def validate_alert(self):
        
        alert_key = "feature" if self._class == "feature_drift" else "metric"
        alert_keys_used = list()
        for each_condition in self.conditions:
            if each_condition["state"] is None:
                if each_condition["op"] is None:
                    raise ValueError(f"operator is none for condition {each_condition}")
                if (each_condition["threshold"] is None) and (each_condition["state"] is None):
                    raise ValueError(f"Both threshold and state can not be none, one is required, condition {each_condition}")
            elif each_condition["state"] != "critical" or each_condition["state"] != "warning":
                raise ValueError(f"Invalid value for state {each_condition}")
            # Keeping it here also as user can set state while updating, whereas threshold is already present.
            if (each_condition["threshold"] is not None) and (each_condition["state"] is not None):
                raise ValueError(f"Both threshold and state can not be passed, only one can be passed, condition {each_condition}")
            if each_condition[alert_key] in alert_keys_used:
                raise ValueError(f"Multiple alert conditions defined on the same {alert_key}: {each_condition[alert_key]}")
            else:
                alert_keys_used.append(each_condition[alert_key])
