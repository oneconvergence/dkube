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


class InlineResponse20079(object):
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
        'featureservices': 'list[FeatureServiceResponseDef]'
    }

    attribute_map = {
        'featureservices': 'featureservices'
    }

    def __init__(self, featureservices=None):  # noqa: E501
        """InlineResponse20079 - a model defined in Swagger"""  # noqa: E501

        self._featureservices = None
        self.discriminator = None

        if featureservices is not None:
            self.featureservices = featureservices

    @property
    def featureservices(self):
        """Gets the featureservices of this InlineResponse20079.  # noqa: E501


        :return: The featureservices of this InlineResponse20079.  # noqa: E501
        :rtype: list[FeatureServiceResponseDef]
        """
        return self._featureservices

    @featureservices.setter
    def featureservices(self, featureservices):
        """Sets the featureservices of this InlineResponse20079.


        :param featureservices: The featureservices of this InlineResponse20079.  # noqa: E501
        :type: list[FeatureServiceResponseDef]
        """

        self._featureservices = featureservices

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
        if issubclass(InlineResponse20079, dict):
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
        if not isinstance(other, InlineResponse20079):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
