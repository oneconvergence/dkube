# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.2.1.13
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InlineResponse20017(object):
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
        'response': 'ApiResponse',
        'data': 'list[JobGroupModel]'
    }

    attribute_map = {
        'response': 'response',
        'data': 'data'
    }

    def __init__(self, response=None, data=None):  # noqa: E501
        """InlineResponse20017 - a model defined in Swagger"""  # noqa: E501

        self._response = None
        self._data = None
        self.discriminator = None

        if response is not None:
            self.response = response
        if data is not None:
            self.data = data

    @property
    def response(self):
        """Gets the response of this InlineResponse20017.  # noqa: E501


        :return: The response of this InlineResponse20017.  # noqa: E501
        :rtype: ApiResponse
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this InlineResponse20017.


        :param response: The response of this InlineResponse20017.  # noqa: E501
        :type: ApiResponse
        """

        self._response = response

    @property
    def data(self):
        """Gets the data of this InlineResponse20017.  # noqa: E501


        :return: The data of this InlineResponse20017.  # noqa: E501
        :rtype: list[JobGroupModel]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this InlineResponse20017.


        :param data: The data of this InlineResponse20017.  # noqa: E501
        :type: list[JobGroupModel]
        """

        self._data = data

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
        if issubclass(InlineResponse20017, dict):
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
        if not isinstance(other, InlineResponse20017):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
