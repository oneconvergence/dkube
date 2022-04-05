# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.3.0.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ModelDetailsTensorpbDevices(object):
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
        'cpu': 'bool',
        'gpu': 'bool'
    }

    attribute_map = {
        'cpu': 'cpu',
        'gpu': 'gpu'
    }

    def __init__(self, cpu=False, gpu=False):  # noqa: E501
        """ModelDetailsTensorpbDevices - a model defined in Swagger"""  # noqa: E501

        self._cpu = None
        self._gpu = None
        self.discriminator = None

        if cpu is not None:
            self.cpu = cpu
        if gpu is not None:
            self.gpu = gpu

    @property
    def cpu(self):
        """Gets the cpu of this ModelDetailsTensorpbDevices.  # noqa: E501


        :return: The cpu of this ModelDetailsTensorpbDevices.  # noqa: E501
        :rtype: bool
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this ModelDetailsTensorpbDevices.


        :param cpu: The cpu of this ModelDetailsTensorpbDevices.  # noqa: E501
        :type: bool
        """

        self._cpu = cpu

    @property
    def gpu(self):
        """Gets the gpu of this ModelDetailsTensorpbDevices.  # noqa: E501


        :return: The gpu of this ModelDetailsTensorpbDevices.  # noqa: E501
        :rtype: bool
        """
        return self._gpu

    @gpu.setter
    def gpu(self, gpu):
        """Sets the gpu of this ModelDetailsTensorpbDevices.


        :param gpu: The gpu of this ModelDetailsTensorpbDevices.  # noqa: E501
        :type: bool
        """

        self._gpu = gpu

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
        if issubclass(ModelDetailsTensorpbDevices, dict):
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
        if not isinstance(other, ModelDetailsTensorpbDevices):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
