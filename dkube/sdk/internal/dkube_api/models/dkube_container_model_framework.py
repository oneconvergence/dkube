# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.3.0.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DkubeContainerModelFramework(object):
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
        'choice': 'str',
        'details': 'DkubeContainerModelFrameworkDetails'
    }

    attribute_map = {
        'choice': 'choice',
        'details': 'details'
    }

    def __init__(self, choice=None, details=None):  # noqa: E501
        """DkubeContainerModelFramework - a model defined in Swagger"""  # noqa: E501

        self._choice = None
        self._details = None
        self.discriminator = None

        if choice is not None:
            self.choice = choice
        if details is not None:
            self.details = details

    @property
    def choice(self):
        """Gets the choice of this DkubeContainerModelFramework.  # noqa: E501


        :return: The choice of this DkubeContainerModelFramework.  # noqa: E501
        :rtype: str
        """
        return self._choice

    @choice.setter
    def choice(self, choice):
        """Sets the choice of this DkubeContainerModelFramework.


        :param choice: The choice of this DkubeContainerModelFramework.  # noqa: E501
        :type: str
        """

        self._choice = choice

    @property
    def details(self):
        """Gets the details of this DkubeContainerModelFramework.  # noqa: E501


        :return: The details of this DkubeContainerModelFramework.  # noqa: E501
        :rtype: DkubeContainerModelFrameworkDetails
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this DkubeContainerModelFramework.


        :param details: The details of this DkubeContainerModelFramework.  # noqa: E501
        :type: DkubeContainerModelFrameworkDetails
        """

        self._details = details

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
        if issubclass(DkubeContainerModelFramework, dict):
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
        if not isinstance(other, DkubeContainerModelFramework):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
