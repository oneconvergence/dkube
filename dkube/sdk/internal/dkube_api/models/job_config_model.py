# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0.0.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class JobConfigModel(object):
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
        'envs': 'CustomKVModel',
        'file': 'ConfigFileModel'
    }

    attribute_map = {
        'envs': 'envs',
        'file': 'file'
    }

    def __init__(self, envs=None, file=None):  # noqa: E501
        """JobConfigModel - a model defined in Swagger"""  # noqa: E501

        self._envs = None
        self._file = None
        self.discriminator = None

        if envs is not None:
            self.envs = envs
        if file is not None:
            self.file = file

    @property
    def envs(self):
        """Gets the envs of this JobConfigModel.  # noqa: E501


        :return: The envs of this JobConfigModel.  # noqa: E501
        :rtype: CustomKVModel
        """
        return self._envs

    @envs.setter
    def envs(self, envs):
        """Sets the envs of this JobConfigModel.


        :param envs: The envs of this JobConfigModel.  # noqa: E501
        :type: CustomKVModel
        """

        self._envs = envs

    @property
    def file(self):
        """Gets the file of this JobConfigModel.  # noqa: E501


        :return: The file of this JobConfigModel.  # noqa: E501
        :rtype: ConfigFileModel
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this JobConfigModel.


        :param file: The file of this JobConfigModel.  # noqa: E501
        :type: ConfigFileModel
        """

        self._file = file

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
        if issubclass(JobConfigModel, dict):
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
        if not isinstance(other, JobConfigModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
