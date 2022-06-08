# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.4.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DeploymentMonitoringDef(object):
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
        'enabled': 'bool',
        'frequency': 'int',
        'metrics': 'ModelmonitorHeartbeatDef',
        'collect_metrics': 'bool'
    }

    attribute_map = {
        'enabled': 'enabled',
        'frequency': 'frequency',
        'metrics': 'metrics',
        'collect_metrics': 'collect_metrics'
    }

    def __init__(self, enabled=None, frequency=None, metrics=None, collect_metrics=None):  # noqa: E501
        """DeploymentMonitoringDef - a model defined in Swagger"""  # noqa: E501

        self._enabled = None
        self._frequency = None
        self._metrics = None
        self._collect_metrics = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if frequency is not None:
            self.frequency = frequency
        if metrics is not None:
            self.metrics = metrics
        if collect_metrics is not None:
            self.collect_metrics = collect_metrics

    @property
    def enabled(self):
        """Gets the enabled of this DeploymentMonitoringDef.  # noqa: E501


        :return: The enabled of this DeploymentMonitoringDef.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this DeploymentMonitoringDef.


        :param enabled: The enabled of this DeploymentMonitoringDef.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def frequency(self):
        """Gets the frequency of this DeploymentMonitoringDef.  # noqa: E501

        frequency in minutes, minimum 5 minutes  # noqa: E501

        :return: The frequency of this DeploymentMonitoringDef.  # noqa: E501
        :rtype: int
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this DeploymentMonitoringDef.

        frequency in minutes, minimum 5 minutes  # noqa: E501

        :param frequency: The frequency of this DeploymentMonitoringDef.  # noqa: E501
        :type: int
        """

        self._frequency = frequency

    @property
    def metrics(self):
        """Gets the metrics of this DeploymentMonitoringDef.  # noqa: E501


        :return: The metrics of this DeploymentMonitoringDef.  # noqa: E501
        :rtype: ModelmonitorHeartbeatDef
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this DeploymentMonitoringDef.


        :param metrics: The metrics of this DeploymentMonitoringDef.  # noqa: E501
        :type: ModelmonitorHeartbeatDef
        """

        self._metrics = metrics

    @property
    def collect_metrics(self):
        """Gets the collect_metrics of this DeploymentMonitoringDef.  # noqa: E501


        :return: The collect_metrics of this DeploymentMonitoringDef.  # noqa: E501
        :rtype: bool
        """
        return self._collect_metrics

    @collect_metrics.setter
    def collect_metrics(self, collect_metrics):
        """Sets the collect_metrics of this DeploymentMonitoringDef.


        :param collect_metrics: The collect_metrics of this DeploymentMonitoringDef.  # noqa: E501
        :type: bool
        """

        self._collect_metrics = collect_metrics

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
        if issubclass(DeploymentMonitoringDef, dict):
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
        if not isinstance(other, DeploymentMonitoringDef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
