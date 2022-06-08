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


class NodeModelCapacity(object):
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
        'cpus': 'CpuModel',
        'memory': 'str'
    }

    attribute_map = {
        'cpus': 'cpus',
        'memory': 'memory'
    }

    def __init__(self, cpus=None, memory=None):  # noqa: E501
        """NodeModelCapacity - a model defined in Swagger"""  # noqa: E501

        self._cpus = None
        self._memory = None
        self.discriminator = None

        if cpus is not None:
            self.cpus = cpus
        if memory is not None:
            self.memory = memory

    @property
    def cpus(self):
        """Gets the cpus of this NodeModelCapacity.  # noqa: E501


        :return: The cpus of this NodeModelCapacity.  # noqa: E501
        :rtype: CpuModel
        """
        return self._cpus

    @cpus.setter
    def cpus(self, cpus):
        """Sets the cpus of this NodeModelCapacity.


        :param cpus: The cpus of this NodeModelCapacity.  # noqa: E501
        :type: CpuModel
        """

        self._cpus = cpus

    @property
    def memory(self):
        """Gets the memory of this NodeModelCapacity.  # noqa: E501


        :return: The memory of this NodeModelCapacity.  # noqa: E501
        :rtype: str
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this NodeModelCapacity.


        :param memory: The memory of this NodeModelCapacity.  # noqa: E501
        :type: str
        """

        self._memory = memory

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
        if issubclass(NodeModelCapacity, dict):
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
        if not isinstance(other, NodeModelCapacity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
