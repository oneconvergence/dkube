# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ModelmonitorMetricDef(object):
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
        'label': 'str',
        'value': 'str',
        'op_mode': 'str'
    }

    attribute_map = {
        'label': 'label',
        'value': 'value',
        'op_mode': 'op_mode'
    }

    def __init__(self, label=None, value=None, op_mode=None):  # noqa: E501
        """ModelmonitorMetricDef - a model defined in Swagger"""  # noqa: E501

        self._label = None
        self._value = None
        self._op_mode = None
        self.discriminator = None

        if label is not None:
            self.label = label
        if value is not None:
            self.value = value
        if op_mode is not None:
            self.op_mode = op_mode

    @property
    def label(self):
        """Gets the label of this ModelmonitorMetricDef.  # noqa: E501


        :return: The label of this ModelmonitorMetricDef.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ModelmonitorMetricDef.


        :param label: The label of this ModelmonitorMetricDef.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def value(self):
        """Gets the value of this ModelmonitorMetricDef.  # noqa: E501


        :return: The value of this ModelmonitorMetricDef.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ModelmonitorMetricDef.


        :param value: The value of this ModelmonitorMetricDef.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def op_mode(self):
        """Gets the op_mode of this ModelmonitorMetricDef.  # noqa: E501


        :return: The op_mode of this ModelmonitorMetricDef.  # noqa: E501
        :rtype: str
        """
        return self._op_mode

    @op_mode.setter
    def op_mode(self, op_mode):
        """Sets the op_mode of this ModelmonitorMetricDef.


        :param op_mode: The op_mode of this ModelmonitorMetricDef.  # noqa: E501
        :type: str
        """

        self._op_mode = op_mode

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
        if issubclass(ModelmonitorMetricDef, dict):
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
        if not isinstance(other, ModelmonitorMetricDef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
