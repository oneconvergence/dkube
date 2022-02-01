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


class DkubeContainerModel(object):
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
        'framework': 'DkubeContainerModelFramework'
    }

    attribute_map = {
        'framework': 'framework'
    }

    def __init__(self, framework=None):  # noqa: E501
        """DkubeContainerModel - a model defined in Swagger"""  # noqa: E501

        self._framework = None
        self.discriminator = None

        if framework is not None:
            self.framework = framework

    @property
    def framework(self):
        """Gets the framework of this DkubeContainerModel.  # noqa: E501


        :return: The framework of this DkubeContainerModel.  # noqa: E501
        :rtype: DkubeContainerModelFramework
        """
        return self._framework

    @framework.setter
    def framework(self, framework):
        """Sets the framework of this DkubeContainerModel.


        :param framework: The framework of this DkubeContainerModel.  # noqa: E501
        :type: DkubeContainerModelFramework
        """

        self._framework = framework

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
        if issubclass(DkubeContainerModel, dict):
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
        if not isinstance(other, DkubeContainerModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
