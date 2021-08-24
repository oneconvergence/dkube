# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.3.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GpuAllocation(object):
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
        'manual': 'bool',
        'auto': 'bool'
    }

    attribute_map = {
        'manual': 'manual',
        'auto': 'auto'
    }

    def __init__(self, manual=None, auto=None):  # noqa: E501
        """GpuAllocation - a model defined in Swagger"""  # noqa: E501

        self._manual = None
        self._auto = None
        self.discriminator = None

        if manual is not None:
            self.manual = manual
        if auto is not None:
            self.auto = auto

    @property
    def manual(self):
        """Gets the manual of this GpuAllocation.  # noqa: E501


        :return: The manual of this GpuAllocation.  # noqa: E501
        :rtype: bool
        """
        return self._manual

    @manual.setter
    def manual(self, manual):
        """Sets the manual of this GpuAllocation.


        :param manual: The manual of this GpuAllocation.  # noqa: E501
        :type: bool
        """

        self._manual = manual

    @property
    def auto(self):
        """Gets the auto of this GpuAllocation.  # noqa: E501


        :return: The auto of this GpuAllocation.  # noqa: E501
        :rtype: bool
        """
        return self._auto

    @auto.setter
    def auto(self, auto):
        """Sets the auto of this GpuAllocation.


        :param auto: The auto of this GpuAllocation.  # noqa: E501
        :type: bool
        """

        self._auto = auto

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
        if issubclass(GpuAllocation, dict):
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
        if not isinstance(other, GpuAllocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
