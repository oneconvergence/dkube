# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.2.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class UserProfileLimits(object):
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
        'cpus': 'str',
        'mem': 'str',
        'gpus': 'int'
    }

    attribute_map = {
        'cpus': 'cpus',
        'mem': 'mem',
        'gpus': 'gpus'
    }

    def __init__(self, cpus=None, mem=None, gpus=None):  # noqa: E501
        """UserProfileLimits - a model defined in Swagger"""  # noqa: E501

        self._cpus = None
        self._mem = None
        self._gpus = None
        self.discriminator = None

        if cpus is not None:
            self.cpus = cpus
        if mem is not None:
            self.mem = mem
        if gpus is not None:
            self.gpus = gpus

    @property
    def cpus(self):
        """Gets the cpus of this UserProfileLimits.  # noqa: E501


        :return: The cpus of this UserProfileLimits.  # noqa: E501
        :rtype: str
        """
        return self._cpus

    @cpus.setter
    def cpus(self, cpus):
        """Sets the cpus of this UserProfileLimits.


        :param cpus: The cpus of this UserProfileLimits.  # noqa: E501
        :type: str
        """

        self._cpus = cpus

    @property
    def mem(self):
        """Gets the mem of this UserProfileLimits.  # noqa: E501


        :return: The mem of this UserProfileLimits.  # noqa: E501
        :rtype: str
        """
        return self._mem

    @mem.setter
    def mem(self, mem):
        """Sets the mem of this UserProfileLimits.


        :param mem: The mem of this UserProfileLimits.  # noqa: E501
        :type: str
        """

        self._mem = mem

    @property
    def gpus(self):
        """Gets the gpus of this UserProfileLimits.  # noqa: E501


        :return: The gpus of this UserProfileLimits.  # noqa: E501
        :rtype: int
        """
        return self._gpus

    @gpus.setter
    def gpus(self, gpus):
        """Sets the gpus of this UserProfileLimits.


        :param gpus: The gpus of this UserProfileLimits.  # noqa: E501
        :type: int
        """

        self._gpus = gpus

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
        if issubclass(UserProfileLimits, dict):
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
        if not isinstance(other, UserProfileLimits):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
