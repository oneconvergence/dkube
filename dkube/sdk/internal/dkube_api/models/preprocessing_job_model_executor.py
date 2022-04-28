# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.3.0.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PreprocessingJobModelExecutor(object):
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
        'buildfromproject': 'bool',
        'custom': 'CustomContainerModel'
    }

    attribute_map = {
        'choice': 'choice',
        'buildfromproject': 'buildfromproject',
        'custom': 'custom'
    }

    def __init__(self, choice=None, buildfromproject=False, custom=None):  # noqa: E501
        """PreprocessingJobModelExecutor - a model defined in Swagger"""  # noqa: E501

        self._choice = None
        self._buildfromproject = None
        self._custom = None
        self.discriminator = None

        if choice is not None:
            self.choice = choice
        if buildfromproject is not None:
            self.buildfromproject = buildfromproject
        if custom is not None:
            self.custom = custom

    @property
    def choice(self):
        """Gets the choice of this PreprocessingJobModelExecutor.  # noqa: E501


        :return: The choice of this PreprocessingJobModelExecutor.  # noqa: E501
        :rtype: str
        """
        return self._choice

    @choice.setter
    def choice(self, choice):
        """Sets the choice of this PreprocessingJobModelExecutor.


        :param choice: The choice of this PreprocessingJobModelExecutor.  # noqa: E501
        :type: str
        """
        allowed_values = ["custom", "spark"]  # noqa: E501
        if choice not in allowed_values:
            raise ValueError(
                "Invalid value for `choice` ({0}), must be one of {1}"  # noqa: E501
                .format(choice, allowed_values)
            )

        self._choice = choice

    @property
    def buildfromproject(self):
        """Gets the buildfromproject of this PreprocessingJobModelExecutor.  # noqa: E501


        :return: The buildfromproject of this PreprocessingJobModelExecutor.  # noqa: E501
        :rtype: bool
        """
        return self._buildfromproject

    @buildfromproject.setter
    def buildfromproject(self, buildfromproject):
        """Sets the buildfromproject of this PreprocessingJobModelExecutor.


        :param buildfromproject: The buildfromproject of this PreprocessingJobModelExecutor.  # noqa: E501
        :type: bool
        """

        self._buildfromproject = buildfromproject

    @property
    def custom(self):
        """Gets the custom of this PreprocessingJobModelExecutor.  # noqa: E501

        Executor object for custom class  # noqa: E501

        :return: The custom of this PreprocessingJobModelExecutor.  # noqa: E501
        :rtype: CustomContainerModel
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        """Sets the custom of this PreprocessingJobModelExecutor.

        Executor object for custom class  # noqa: E501

        :param custom: The custom of this PreprocessingJobModelExecutor.  # noqa: E501
        :type: CustomContainerModel
        """

        self._custom = custom

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
        if issubclass(PreprocessingJobModelExecutor, dict):
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
        if not isinstance(other, PreprocessingJobModelExecutor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
