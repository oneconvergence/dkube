# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.7.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Data47(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'input_data_type': 'str',
        'dashboard_plugin': 'object',
        'thresholds': 'object',
        'input_data_shape': 'ModelmonitorInputDataShapeDef',
        'pipeline_threshold': 'ModelmonitorThresholdDef',
        'data_timezone': 'str',
        'alerts': 'list[ModelmonitorAlertDef]',
        'schema': 'ModelmonitorFeaturesSpecDef',
        'model_type': 'str',
        'datasources': 'dict(str, ModelmonitorDataSourceDef)',
        'deployment_monitoring': 'DeploymentMonitoringDef',
        'drift_monitoring': 'DriftMonitoringDef',
        'performance_monitoring': 'PerformanceMonitoringDef',
        'cpu_limit': 'float',
        'memory_limit': 'float',
        'max_predict_image_samples': 'float'
    }

    attribute_map = {
        'input_data_type': 'input_data_type',
        'dashboard_plugin': 'dashboard_plugin',
        'thresholds': 'thresholds',
        'input_data_shape': 'input_data_shape',
        'pipeline_threshold': 'pipeline_threshold',
        'data_timezone': 'data_timezone',
        'alerts': 'alerts',
        'schema': 'schema',
        'model_type': 'model_type',
        'datasources': 'datasources',
        'deployment_monitoring': 'deployment_monitoring',
        'drift_monitoring': 'drift_monitoring',
        'performance_monitoring': 'performance_monitoring',
        'cpu_limit': 'cpu_limit',
        'memory_limit': 'memory_limit',
        'max_predict_image_samples': 'max_predict_image_samples'
    }

    def __init__(self, input_data_type=None, dashboard_plugin=None, thresholds=None, input_data_shape=None, pipeline_threshold=None, data_timezone=None, alerts=None, schema=None, model_type=None, datasources=None, deployment_monitoring=None, drift_monitoring=None, performance_monitoring=None, cpu_limit=None, memory_limit=None, max_predict_image_samples=None):  # noqa: E501
        """Data47 - a model defined in Swagger"""  # noqa: E501

        self._input_data_type = None
        self._dashboard_plugin = None
        self._thresholds = None
        self._input_data_shape = None
        self._pipeline_threshold = None
        self._data_timezone = None
        self._alerts = None
        self._schema = None
        self._model_type = None
        self._datasources = None
        self._deployment_monitoring = None
        self._drift_monitoring = None
        self._performance_monitoring = None
        self._cpu_limit = None
        self._memory_limit = None
        self._max_predict_image_samples = None
        self.discriminator = None

        if input_data_type is not None:
            self.input_data_type = input_data_type
        if dashboard_plugin is not None:
            self.dashboard_plugin = dashboard_plugin
        if thresholds is not None:
            self.thresholds = thresholds
        if input_data_shape is not None:
            self.input_data_shape = input_data_shape
        if pipeline_threshold is not None:
            self.pipeline_threshold = pipeline_threshold
        if data_timezone is not None:
            self.data_timezone = data_timezone
        if alerts is not None:
            self.alerts = alerts
        if schema is not None:
            self.schema = schema
        if model_type is not None:
            self.model_type = model_type
        if datasources is not None:
            self.datasources = datasources
        if deployment_monitoring is not None:
            self.deployment_monitoring = deployment_monitoring
        if drift_monitoring is not None:
            self.drift_monitoring = drift_monitoring
        if performance_monitoring is not None:
            self.performance_monitoring = performance_monitoring
        if cpu_limit is not None:
            self.cpu_limit = cpu_limit
        if memory_limit is not None:
            self.memory_limit = memory_limit
        if max_predict_image_samples is not None:
            self.max_predict_image_samples = max_predict_image_samples

    @property
    def input_data_type(self):
        """Gets the input_data_type of this Data47.  # noqa: E501

        training dataset type  # noqa: E501

        :return: The input_data_type of this Data47.  # noqa: E501
        :rtype: str
        """
        return self._input_data_type

    @input_data_type.setter
    def input_data_type(self, input_data_type):
        """Sets the input_data_type of this Data47.

        training dataset type  # noqa: E501

        :param input_data_type: The input_data_type of this Data47.  # noqa: E501
        :type: str
        """
        allowed_values = ["image", "tabular"]  # noqa: E501
        if input_data_type not in allowed_values:
            raise ValueError(
                "Invalid value for `input_data_type` ({0}), must be one of {1}"  # noqa: E501
                .format(input_data_type, allowed_values)
            )

        self._input_data_type = input_data_type

    @property
    def dashboard_plugin(self):
        """Gets the dashboard_plugin of this Data47.  # noqa: E501


        :return: The dashboard_plugin of this Data47.  # noqa: E501
        :rtype: object
        """
        return self._dashboard_plugin

    @dashboard_plugin.setter
    def dashboard_plugin(self, dashboard_plugin):
        """Sets the dashboard_plugin of this Data47.


        :param dashboard_plugin: The dashboard_plugin of this Data47.  # noqa: E501
        :type: object
        """

        self._dashboard_plugin = dashboard_plugin

    @property
    def thresholds(self):
        """Gets the thresholds of this Data47.  # noqa: E501


        :return: The thresholds of this Data47.  # noqa: E501
        :rtype: object
        """
        return self._thresholds

    @thresholds.setter
    def thresholds(self, thresholds):
        """Sets the thresholds of this Data47.


        :param thresholds: The thresholds of this Data47.  # noqa: E501
        :type: object
        """

        self._thresholds = thresholds

    @property
    def input_data_shape(self):
        """Gets the input_data_shape of this Data47.  # noqa: E501


        :return: The input_data_shape of this Data47.  # noqa: E501
        :rtype: ModelmonitorInputDataShapeDef
        """
        return self._input_data_shape

    @input_data_shape.setter
    def input_data_shape(self, input_data_shape):
        """Sets the input_data_shape of this Data47.


        :param input_data_shape: The input_data_shape of this Data47.  # noqa: E501
        :type: ModelmonitorInputDataShapeDef
        """

        self._input_data_shape = input_data_shape

    @property
    def pipeline_threshold(self):
        """Gets the pipeline_threshold of this Data47.  # noqa: E501


        :return: The pipeline_threshold of this Data47.  # noqa: E501
        :rtype: ModelmonitorThresholdDef
        """
        return self._pipeline_threshold

    @pipeline_threshold.setter
    def pipeline_threshold(self, pipeline_threshold):
        """Sets the pipeline_threshold of this Data47.


        :param pipeline_threshold: The pipeline_threshold of this Data47.  # noqa: E501
        :type: ModelmonitorThresholdDef
        """

        self._pipeline_threshold = pipeline_threshold

    @property
    def data_timezone(self):
        """Gets the data_timezone of this Data47.  # noqa: E501


        :return: The data_timezone of this Data47.  # noqa: E501
        :rtype: str
        """
        return self._data_timezone

    @data_timezone.setter
    def data_timezone(self, data_timezone):
        """Sets the data_timezone of this Data47.


        :param data_timezone: The data_timezone of this Data47.  # noqa: E501
        :type: str
        """

        self._data_timezone = data_timezone

    @property
    def alerts(self):
        """Gets the alerts of this Data47.  # noqa: E501

        model monitor alerts  # noqa: E501

        :return: The alerts of this Data47.  # noqa: E501
        :rtype: list[ModelmonitorAlertDef]
        """
        return self._alerts

    @alerts.setter
    def alerts(self, alerts):
        """Sets the alerts of this Data47.

        model monitor alerts  # noqa: E501

        :param alerts: The alerts of this Data47.  # noqa: E501
        :type: list[ModelmonitorAlertDef]
        """

        self._alerts = alerts

    @property
    def schema(self):
        """Gets the schema of this Data47.  # noqa: E501


        :return: The schema of this Data47.  # noqa: E501
        :rtype: ModelmonitorFeaturesSpecDef
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this Data47.


        :param schema: The schema of this Data47.  # noqa: E501
        :type: ModelmonitorFeaturesSpecDef
        """

        self._schema = schema

    @property
    def model_type(self):
        """Gets the model_type of this Data47.  # noqa: E501

        Model prediction type - regression or classification  # noqa: E501

        :return: The model_type of this Data47.  # noqa: E501
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this Data47.

        Model prediction type - regression or classification  # noqa: E501

        :param model_type: The model_type of this Data47.  # noqa: E501
        :type: str
        """
        allowed_values = ["regression", "classification"]  # noqa: E501
        if model_type not in allowed_values:
            raise ValueError(
                "Invalid value for `model_type` ({0}), must be one of {1}"  # noqa: E501
                .format(model_type, allowed_values)
            )

        self._model_type = model_type

    @property
    def datasources(self):
        """Gets the datasources of this Data47.  # noqa: E501

        model monitor datasources  # noqa: E501

        :return: The datasources of this Data47.  # noqa: E501
        :rtype: dict(str, ModelmonitorDataSourceDef)
        """
        return self._datasources

    @datasources.setter
    def datasources(self, datasources):
        """Sets the datasources of this Data47.

        model monitor datasources  # noqa: E501

        :param datasources: The datasources of this Data47.  # noqa: E501
        :type: dict(str, ModelmonitorDataSourceDef)
        """

        self._datasources = datasources

    @property
    def deployment_monitoring(self):
        """Gets the deployment_monitoring of this Data47.  # noqa: E501


        :return: The deployment_monitoring of this Data47.  # noqa: E501
        :rtype: DeploymentMonitoringDef
        """
        return self._deployment_monitoring

    @deployment_monitoring.setter
    def deployment_monitoring(self, deployment_monitoring):
        """Sets the deployment_monitoring of this Data47.


        :param deployment_monitoring: The deployment_monitoring of this Data47.  # noqa: E501
        :type: DeploymentMonitoringDef
        """

        self._deployment_monitoring = deployment_monitoring

    @property
    def drift_monitoring(self):
        """Gets the drift_monitoring of this Data47.  # noqa: E501


        :return: The drift_monitoring of this Data47.  # noqa: E501
        :rtype: DriftMonitoringDef
        """
        return self._drift_monitoring

    @drift_monitoring.setter
    def drift_monitoring(self, drift_monitoring):
        """Sets the drift_monitoring of this Data47.


        :param drift_monitoring: The drift_monitoring of this Data47.  # noqa: E501
        :type: DriftMonitoringDef
        """

        self._drift_monitoring = drift_monitoring

    @property
    def performance_monitoring(self):
        """Gets the performance_monitoring of this Data47.  # noqa: E501


        :return: The performance_monitoring of this Data47.  # noqa: E501
        :rtype: PerformanceMonitoringDef
        """
        return self._performance_monitoring

    @performance_monitoring.setter
    def performance_monitoring(self, performance_monitoring):
        """Sets the performance_monitoring of this Data47.


        :param performance_monitoring: The performance_monitoring of this Data47.  # noqa: E501
        :type: PerformanceMonitoringDef
        """

        self._performance_monitoring = performance_monitoring

    @property
    def cpu_limit(self):
        """Gets the cpu_limit of this Data47.  # noqa: E501

        CPU ceiling. 0 indicates no limit  # noqa: E501

        :return: The cpu_limit of this Data47.  # noqa: E501
        :rtype: float
        """
        return self._cpu_limit

    @cpu_limit.setter
    def cpu_limit(self, cpu_limit):
        """Sets the cpu_limit of this Data47.

        CPU ceiling. 0 indicates no limit  # noqa: E501

        :param cpu_limit: The cpu_limit of this Data47.  # noqa: E501
        :type: float
        """

        self._cpu_limit = cpu_limit

    @property
    def memory_limit(self):
        """Gets the memory_limit of this Data47.  # noqa: E501

        memory ceiling in Mi. 0 indicates no linit  # noqa: E501

        :return: The memory_limit of this Data47.  # noqa: E501
        :rtype: float
        """
        return self._memory_limit

    @memory_limit.setter
    def memory_limit(self, memory_limit):
        """Sets the memory_limit of this Data47.

        memory ceiling in Mi. 0 indicates no linit  # noqa: E501

        :param memory_limit: The memory_limit of this Data47.  # noqa: E501
        :type: float
        """

        self._memory_limit = memory_limit

    @property
    def max_predict_image_samples(self):
        """Gets the max_predict_image_samples of this Data47.  # noqa: E501

        Max samples to process if there are many. 0 indicates all samples  # noqa: E501

        :return: The max_predict_image_samples of this Data47.  # noqa: E501
        :rtype: float
        """
        return self._max_predict_image_samples

    @max_predict_image_samples.setter
    def max_predict_image_samples(self, max_predict_image_samples):
        """Sets the max_predict_image_samples of this Data47.

        Max samples to process if there are many. 0 indicates all samples  # noqa: E501

        :param max_predict_image_samples: The max_predict_image_samples of this Data47.  # noqa: E501
        :type: float
        """

        self._max_predict_image_samples = max_predict_image_samples

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Data47, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Data47):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
