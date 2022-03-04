# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.3.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ModelmonitorDef(object):
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
        'id': 'str',
        'data_timezone': 'str',
        'dashboard_plugin': 'object',
        'status': 'ModelmonitorStatusDef',
        'schema': 'ModelmonitorFeaturesSpecDef',
        'pipeline_component': 'ModelmonitorComponentDef',
        'deployment_monitoring': 'DeploymentMonitoringDef',
        'drift_monitoring': 'DriftMonitoringDef',
        'performance_monitoring': 'PerformanceMonitoringDef',
        'thresholds': 'object',
        'owner': 'str',
        'name': 'str',
        'model_type': 'str',
        'input_data_type': 'str',
        'input_data_shape': 'ModelmonitorInputDataShapeDef',
        'datasources': 'dict(str, ModelmonitorDataSourceDef)',
        'created_at': 'str',
        'updated_at': 'str',
        'alerts': 'list[ModelmonitorAlertDef]'
    }

    attribute_map = {
        'id': 'id',
        'data_timezone': 'data_timezone',
        'dashboard_plugin': 'dashboard_plugin',
        'status': 'status',
        'schema': 'schema',
        'pipeline_component': 'pipeline_component',
        'deployment_monitoring': 'deployment_monitoring',
        'drift_monitoring': 'drift_monitoring',
        'performance_monitoring': 'performance_monitoring',
        'thresholds': 'thresholds',
        'owner': 'owner',
        'name': 'name',
        'model_type': 'model_type',
        'input_data_type': 'input_data_type',
        'input_data_shape': 'input_data_shape',
        'datasources': 'datasources',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'alerts': 'alerts'
    }

    def __init__(self, id=None, data_timezone=None, dashboard_plugin=None, status=None, schema=None, pipeline_component=None, deployment_monitoring=None, drift_monitoring=None, performance_monitoring=None, thresholds=None, owner=None, name=None, model_type=None, input_data_type=None, input_data_shape=None, datasources=None, created_at=None, updated_at=None, alerts=None):  # noqa: E501
        """ModelmonitorDef - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._data_timezone = None
        self._dashboard_plugin = None
        self._status = None
        self._schema = None
        self._pipeline_component = None
        self._deployment_monitoring = None
        self._drift_monitoring = None
        self._performance_monitoring = None
        self._thresholds = None
        self._owner = None
        self._name = None
        self._model_type = None
        self._input_data_type = None
        self._input_data_shape = None
        self._datasources = None
        self._created_at = None
        self._updated_at = None
        self._alerts = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if data_timezone is not None:
            self.data_timezone = data_timezone
        if dashboard_plugin is not None:
            self.dashboard_plugin = dashboard_plugin
        if status is not None:
            self.status = status
        if schema is not None:
            self.schema = schema
        if pipeline_component is not None:
            self.pipeline_component = pipeline_component
        if deployment_monitoring is not None:
            self.deployment_monitoring = deployment_monitoring
        if drift_monitoring is not None:
            self.drift_monitoring = drift_monitoring
        if performance_monitoring is not None:
            self.performance_monitoring = performance_monitoring
        if thresholds is not None:
            self.thresholds = thresholds
        if owner is not None:
            self.owner = owner
        if name is not None:
            self.name = name
        if model_type is not None:
            self.model_type = model_type
        if input_data_type is not None:
            self.input_data_type = input_data_type
        if input_data_shape is not None:
            self.input_data_shape = input_data_shape
        if datasources is not None:
            self.datasources = datasources
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if alerts is not None:
            self.alerts = alerts

    @property
    def id(self):
        """Gets the id of this ModelmonitorDef.  # noqa: E501

        UUID4 id for the resource  # noqa: E501

        :return: The id of this ModelmonitorDef.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelmonitorDef.

        UUID4 id for the resource  # noqa: E501

        :param id: The id of this ModelmonitorDef.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def data_timezone(self):
        """Gets the data_timezone of this ModelmonitorDef.  # noqa: E501


        :return: The data_timezone of this ModelmonitorDef.  # noqa: E501
        :rtype: str
        """
        return self._data_timezone

    @data_timezone.setter
    def data_timezone(self, data_timezone):
        """Sets the data_timezone of this ModelmonitorDef.


        :param data_timezone: The data_timezone of this ModelmonitorDef.  # noqa: E501
        :type: str
        """

        self._data_timezone = data_timezone

    @property
    def dashboard_plugin(self):
        """Gets the dashboard_plugin of this ModelmonitorDef.  # noqa: E501


        :return: The dashboard_plugin of this ModelmonitorDef.  # noqa: E501
        :rtype: object
        """
        return self._dashboard_plugin

    @dashboard_plugin.setter
    def dashboard_plugin(self, dashboard_plugin):
        """Sets the dashboard_plugin of this ModelmonitorDef.


        :param dashboard_plugin: The dashboard_plugin of this ModelmonitorDef.  # noqa: E501
        :type: object
        """

        self._dashboard_plugin = dashboard_plugin

    @property
    def status(self):
        """Gets the status of this ModelmonitorDef.  # noqa: E501


        :return: The status of this ModelmonitorDef.  # noqa: E501
        :rtype: ModelmonitorStatusDef
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ModelmonitorDef.


        :param status: The status of this ModelmonitorDef.  # noqa: E501
        :type: ModelmonitorStatusDef
        """

        self._status = status

    @property
    def schema(self):
        """Gets the schema of this ModelmonitorDef.  # noqa: E501


        :return: The schema of this ModelmonitorDef.  # noqa: E501
        :rtype: ModelmonitorFeaturesSpecDef
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this ModelmonitorDef.


        :param schema: The schema of this ModelmonitorDef.  # noqa: E501
        :type: ModelmonitorFeaturesSpecDef
        """

        self._schema = schema

    @property
    def pipeline_component(self):
        """Gets the pipeline_component of this ModelmonitorDef.  # noqa: E501


        :return: The pipeline_component of this ModelmonitorDef.  # noqa: E501
        :rtype: ModelmonitorComponentDef
        """
        return self._pipeline_component

    @pipeline_component.setter
    def pipeline_component(self, pipeline_component):
        """Sets the pipeline_component of this ModelmonitorDef.


        :param pipeline_component: The pipeline_component of this ModelmonitorDef.  # noqa: E501
        :type: ModelmonitorComponentDef
        """

        self._pipeline_component = pipeline_component

    @property
    def deployment_monitoring(self):
        """Gets the deployment_monitoring of this ModelmonitorDef.  # noqa: E501


        :return: The deployment_monitoring of this ModelmonitorDef.  # noqa: E501
        :rtype: DeploymentMonitoringDef
        """
        return self._deployment_monitoring

    @deployment_monitoring.setter
    def deployment_monitoring(self, deployment_monitoring):
        """Sets the deployment_monitoring of this ModelmonitorDef.


        :param deployment_monitoring: The deployment_monitoring of this ModelmonitorDef.  # noqa: E501
        :type: DeploymentMonitoringDef
        """

        self._deployment_monitoring = deployment_monitoring

    @property
    def drift_monitoring(self):
        """Gets the drift_monitoring of this ModelmonitorDef.  # noqa: E501


        :return: The drift_monitoring of this ModelmonitorDef.  # noqa: E501
        :rtype: DriftMonitoringDef
        """
        return self._drift_monitoring

    @drift_monitoring.setter
    def drift_monitoring(self, drift_monitoring):
        """Sets the drift_monitoring of this ModelmonitorDef.


        :param drift_monitoring: The drift_monitoring of this ModelmonitorDef.  # noqa: E501
        :type: DriftMonitoringDef
        """

        self._drift_monitoring = drift_monitoring

    @property
    def performance_monitoring(self):
        """Gets the performance_monitoring of this ModelmonitorDef.  # noqa: E501


        :return: The performance_monitoring of this ModelmonitorDef.  # noqa: E501
        :rtype: PerformanceMonitoringDef
        """
        return self._performance_monitoring

    @performance_monitoring.setter
    def performance_monitoring(self, performance_monitoring):
        """Sets the performance_monitoring of this ModelmonitorDef.


        :param performance_monitoring: The performance_monitoring of this ModelmonitorDef.  # noqa: E501
        :type: PerformanceMonitoringDef
        """

        self._performance_monitoring = performance_monitoring

    @property
    def thresholds(self):
        """Gets the thresholds of this ModelmonitorDef.  # noqa: E501


        :return: The thresholds of this ModelmonitorDef.  # noqa: E501
        :rtype: object
        """
        return self._thresholds

    @thresholds.setter
    def thresholds(self, thresholds):
        """Sets the thresholds of this ModelmonitorDef.


        :param thresholds: The thresholds of this ModelmonitorDef.  # noqa: E501
        :type: object
        """

        self._thresholds = thresholds

    @property
    def owner(self):
        """Gets the owner of this ModelmonitorDef.  # noqa: E501

        owner name of modelmonitor  # noqa: E501

        :return: The owner of this ModelmonitorDef.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ModelmonitorDef.

        owner name of modelmonitor  # noqa: E501

        :param owner: The owner of this ModelmonitorDef.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def name(self):
        """Gets the name of this ModelmonitorDef.  # noqa: E501


        :return: The name of this ModelmonitorDef.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelmonitorDef.


        :param name: The name of this ModelmonitorDef.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def model_type(self):
        """Gets the model_type of this ModelmonitorDef.  # noqa: E501

        Model prediction type - regression or classification  # noqa: E501

        :return: The model_type of this ModelmonitorDef.  # noqa: E501
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this ModelmonitorDef.

        Model prediction type - regression or classification  # noqa: E501

        :param model_type: The model_type of this ModelmonitorDef.  # noqa: E501
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
    def input_data_type(self):
        """Gets the input_data_type of this ModelmonitorDef.  # noqa: E501

        training dataset type  # noqa: E501

        :return: The input_data_type of this ModelmonitorDef.  # noqa: E501
        :rtype: str
        """
        return self._input_data_type

    @input_data_type.setter
    def input_data_type(self, input_data_type):
        """Sets the input_data_type of this ModelmonitorDef.

        training dataset type  # noqa: E501

        :param input_data_type: The input_data_type of this ModelmonitorDef.  # noqa: E501
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
    def input_data_shape(self):
        """Gets the input_data_shape of this ModelmonitorDef.  # noqa: E501


        :return: The input_data_shape of this ModelmonitorDef.  # noqa: E501
        :rtype: ModelmonitorInputDataShapeDef
        """
        return self._input_data_shape

    @input_data_shape.setter
    def input_data_shape(self, input_data_shape):
        """Sets the input_data_shape of this ModelmonitorDef.


        :param input_data_shape: The input_data_shape of this ModelmonitorDef.  # noqa: E501
        :type: ModelmonitorInputDataShapeDef
        """

        self._input_data_shape = input_data_shape

    @property
    def datasources(self):
        """Gets the datasources of this ModelmonitorDef.  # noqa: E501

        model monitor datasources  # noqa: E501

        :return: The datasources of this ModelmonitorDef.  # noqa: E501
        :rtype: dict(str, ModelmonitorDataSourceDef)
        """
        return self._datasources

    @datasources.setter
    def datasources(self, datasources):
        """Sets the datasources of this ModelmonitorDef.

        model monitor datasources  # noqa: E501

        :param datasources: The datasources of this ModelmonitorDef.  # noqa: E501
        :type: dict(str, ModelmonitorDataSourceDef)
        """

        self._datasources = datasources

    @property
    def created_at(self):
        """Gets the created_at of this ModelmonitorDef.  # noqa: E501


        :return: The created_at of this ModelmonitorDef.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ModelmonitorDef.


        :param created_at: The created_at of this ModelmonitorDef.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ModelmonitorDef.  # noqa: E501


        :return: The updated_at of this ModelmonitorDef.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ModelmonitorDef.


        :param updated_at: The updated_at of this ModelmonitorDef.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def alerts(self):
        """Gets the alerts of this ModelmonitorDef.  # noqa: E501

        model monitor alerts  # noqa: E501

        :return: The alerts of this ModelmonitorDef.  # noqa: E501
        :rtype: list[ModelmonitorAlertDef]
        """
        return self._alerts

    @alerts.setter
    def alerts(self, alerts):
        """Sets the alerts of this ModelmonitorDef.

        model monitor alerts  # noqa: E501

        :param alerts: The alerts of this ModelmonitorDef.  # noqa: E501
        :type: list[ModelmonitorAlertDef]
        """

        self._alerts = alerts

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
        if issubclass(ModelmonitorDef, dict):
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
        if not isinstance(other, ModelmonitorDef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
