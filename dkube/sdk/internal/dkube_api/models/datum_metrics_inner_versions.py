# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.8.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DatumMetricsInnerVersions(object):
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
        'uuid': 'str',
        'inputs': 'DatumMetricsInnerInputs',
        'metrics': 'Metrics'
    }

    attribute_map = {
        'uuid': 'uuid',
        'inputs': 'inputs',
        'metrics': 'metrics'
    }

    def __init__(self, uuid=None, inputs=None, metrics=None):  # noqa: E501
        """DatumMetricsInnerVersions - a model defined in Swagger"""  # noqa: E501

        self._uuid = None
        self._inputs = None
        self._metrics = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if inputs is not None:
            self.inputs = inputs
        if metrics is not None:
            self.metrics = metrics

    @property
    def uuid(self):
        """Gets the uuid of this DatumMetricsInnerVersions.  # noqa: E501


        :return: The uuid of this DatumMetricsInnerVersions.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this DatumMetricsInnerVersions.


        :param uuid: The uuid of this DatumMetricsInnerVersions.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def inputs(self):
        """Gets the inputs of this DatumMetricsInnerVersions.  # noqa: E501


        :return: The inputs of this DatumMetricsInnerVersions.  # noqa: E501
        :rtype: DatumMetricsInnerInputs
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this DatumMetricsInnerVersions.


        :param inputs: The inputs of this DatumMetricsInnerVersions.  # noqa: E501
        :type: DatumMetricsInnerInputs
        """

        self._inputs = inputs

    @property
    def metrics(self):
        """Gets the metrics of this DatumMetricsInnerVersions.  # noqa: E501


        :return: The metrics of this DatumMetricsInnerVersions.  # noqa: E501
        :rtype: Metrics
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this DatumMetricsInnerVersions.


        :param metrics: The metrics of this DatumMetricsInnerVersions.  # noqa: E501
        :type: Metrics
        """

        self._metrics = metrics

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
        if issubclass(DatumMetricsInnerVersions, dict):
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
        if not isinstance(other, DatumMetricsInnerVersions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
