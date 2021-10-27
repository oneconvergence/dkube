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


class Data1(object):
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
        'type': 'str',
        'operator': 'str',
        'event_data': 'ModeldeployEventData'
    }

    attribute_map = {
        'type': 'type',
        'operator': 'operator',
        'event_data': 'event_data'
    }

    def __init__(self, type=None, operator=None, event_data=None):  # noqa: E501
        """Data1 - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._operator = None
        self._event_data = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if operator is not None:
            self.operator = operator
        if event_data is not None:
            self.event_data = event_data

    @property
    def type(self):
        """Gets the type of this Data1.  # noqa: E501


        :return: The type of this Data1.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Data1.


        :param type: The type of this Data1.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def operator(self):
        """Gets the operator of this Data1.  # noqa: E501


        :return: The operator of this Data1.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this Data1.


        :param operator: The operator of this Data1.  # noqa: E501
        :type: str
        """

        self._operator = operator

    @property
    def event_data(self):
        """Gets the event_data of this Data1.  # noqa: E501


        :return: The event_data of this Data1.  # noqa: E501
        :rtype: ModeldeployEventData
        """
        return self._event_data

    @event_data.setter
    def event_data(self, event_data):
        """Sets the event_data of this Data1.


        :param event_data: The event_data of this Data1.  # noqa: E501
        :type: ModeldeployEventData
        """

        self._event_data = event_data

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
        if issubclass(Data1, dict):
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
        if not isinstance(other, Data1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
