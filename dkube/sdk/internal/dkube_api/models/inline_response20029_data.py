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


class InlineResponse20029Data(object):
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
        'published_name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'published_name': 'publishedName',
        'description': 'description'
    }

    def __init__(self, published_name=None, description=None):  # noqa: E501
        """InlineResponse20029Data - a model defined in Swagger"""  # noqa: E501

        self._published_name = None
        self._description = None
        self.discriminator = None

        if published_name is not None:
            self.published_name = published_name
        if description is not None:
            self.description = description

    @property
    def published_name(self):
        """Gets the published_name of this InlineResponse20029Data.  # noqa: E501


        :return: The published_name of this InlineResponse20029Data.  # noqa: E501
        :rtype: str
        """
        return self._published_name

    @published_name.setter
    def published_name(self, published_name):
        """Sets the published_name of this InlineResponse20029Data.


        :param published_name: The published_name of this InlineResponse20029Data.  # noqa: E501
        :type: str
        """

        self._published_name = published_name

    @property
    def description(self):
        """Gets the description of this InlineResponse20029Data.  # noqa: E501


        :return: The description of this InlineResponse20029Data.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineResponse20029Data.


        :param description: The description of this InlineResponse20029Data.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(InlineResponse20029Data, dict):
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
        if not isinstance(other, InlineResponse20029Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
