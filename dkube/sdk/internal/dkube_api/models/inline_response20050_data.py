# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.3.0.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InlineResponse20050Data(object):
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
        'healthy': 'list[NodeCollection]',
        'unhealthy': 'list[NodeCollection]'
    }

    attribute_map = {
        'healthy': 'healthy',
        'unhealthy': 'unhealthy'
    }

    def __init__(self, healthy=None, unhealthy=None):  # noqa: E501
        """InlineResponse20050Data - a model defined in Swagger"""  # noqa: E501

        self._healthy = None
        self._unhealthy = None
        self.discriminator = None

        if healthy is not None:
            self.healthy = healthy
        if unhealthy is not None:
            self.unhealthy = unhealthy

    @property
    def healthy(self):
        """Gets the healthy of this InlineResponse20050Data.  # noqa: E501


        :return: The healthy of this InlineResponse20050Data.  # noqa: E501
        :rtype: list[NodeCollection]
        """
        return self._healthy

    @healthy.setter
    def healthy(self, healthy):
        """Sets the healthy of this InlineResponse20050Data.


        :param healthy: The healthy of this InlineResponse20050Data.  # noqa: E501
        :type: list[NodeCollection]
        """

        self._healthy = healthy

    @property
    def unhealthy(self):
        """Gets the unhealthy of this InlineResponse20050Data.  # noqa: E501


        :return: The unhealthy of this InlineResponse20050Data.  # noqa: E501
        :rtype: list[NodeCollection]
        """
        return self._unhealthy

    @unhealthy.setter
    def unhealthy(self, unhealthy):
        """Sets the unhealthy of this InlineResponse20050Data.


        :param unhealthy: The unhealthy of this InlineResponse20050Data.  # noqa: E501
        :type: list[NodeCollection]
        """

        self._unhealthy = unhealthy

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
        if issubclass(InlineResponse20050Data, dict):
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
        if not isinstance(other, InlineResponse20050Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
