# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.1.0.3
    
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
        'cluster': 'str',
        'source_type': 'str',
        'metrics': 'ModelmonitorMetricSourceDef',
        'soft_thresholds': 'object'
    }

    attribute_map = {
        'enabled': 'enabled',
        'frequency': 'frequency',
        'cluster': 'cluster',
        'source_type': 'source_type',
        'metrics': 'metrics',
        'soft_thresholds': 'soft_thresholds'
    }

    def __init__(self, enabled=None, frequency=None, cluster=None, source_type=None, metrics=None, soft_thresholds=None):  # noqa: E501
        """DeploymentMonitoringDef - a model defined in Swagger"""  # noqa: E501

        self._enabled = None
        self._frequency = None
        self._cluster = None
        self._source_type = None
        self._metrics = None
        self._soft_thresholds = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if frequency is not None:
            self.frequency = frequency
        if cluster is not None:
            self.cluster = cluster
        if source_type is not None:
            self.source_type = source_type
        if metrics is not None:
            self.metrics = metrics
        if soft_thresholds is not None:
            self.soft_thresholds = soft_thresholds

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

        frequency in minutes  # noqa: E501

        :return: The frequency of this DeploymentMonitoringDef.  # noqa: E501
        :rtype: int
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this DeploymentMonitoringDef.

        frequency in minutes  # noqa: E501

        :param frequency: The frequency of this DeploymentMonitoringDef.  # noqa: E501
        :type: int
        """

        self._frequency = frequency

    @property
    def cluster(self):
        """Gets the cluster of this DeploymentMonitoringDef.  # noqa: E501

        name of the cluster  # noqa: E501

        :return: The cluster of this DeploymentMonitoringDef.  # noqa: E501
        :rtype: str
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this DeploymentMonitoringDef.

        name of the cluster  # noqa: E501

        :param cluster: The cluster of this DeploymentMonitoringDef.  # noqa: E501
        :type: str
        """

        self._cluster = cluster

    @property
    def source_type(self):
        """Gets the source_type of this DeploymentMonitoringDef.  # noqa: E501


        :return: The source_type of this DeploymentMonitoringDef.  # noqa: E501
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this DeploymentMonitoringDef.


        :param source_type: The source_type of this DeploymentMonitoringDef.  # noqa: E501
        :type: str
        """
        allowed_values = ["metrics", "custom"]  # noqa: E501
        if source_type not in allowed_values:
            raise ValueError(
                "Invalid value for `source_type` ({0}), must be one of {1}"  # noqa: E501
                .format(source_type, allowed_values)
            )

        self._source_type = source_type

    @property
    def metrics(self):
        """Gets the metrics of this DeploymentMonitoringDef.  # noqa: E501


        :return: The metrics of this DeploymentMonitoringDef.  # noqa: E501
        :rtype: ModelmonitorMetricSourceDef
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this DeploymentMonitoringDef.


        :param metrics: The metrics of this DeploymentMonitoringDef.  # noqa: E501
        :type: ModelmonitorMetricSourceDef
        """

        self._metrics = metrics

    @property
    def soft_thresholds(self):
        """Gets the soft_thresholds of this DeploymentMonitoringDef.  # noqa: E501


        :return: The soft_thresholds of this DeploymentMonitoringDef.  # noqa: E501
        :rtype: object
        """
        return self._soft_thresholds

    @soft_thresholds.setter
    def soft_thresholds(self, soft_thresholds):
        """Sets the soft_thresholds of this DeploymentMonitoringDef.


        :param soft_thresholds: The soft_thresholds of this DeploymentMonitoringDef.  # noqa: E501
        :type: object
        """

        self._soft_thresholds = soft_thresholds

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
