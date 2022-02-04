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


class InlineResponse2009Data(object):
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
        'jwt': 'str',
        'role': 'str',
        'group': 'str',
        'username': 'str'
    }

    attribute_map = {
        'jwt': 'jwt',
        'role': 'role',
        'group': 'group',
        'username': 'username'
    }

    def __init__(self, jwt=None, role=None, group=None, username=None):  # noqa: E501
        """InlineResponse2009Data - a model defined in Swagger"""  # noqa: E501

        self._jwt = None
        self._role = None
        self._group = None
        self._username = None
        self.discriminator = None

        if jwt is not None:
            self.jwt = jwt
        if role is not None:
            self.role = role
        if group is not None:
            self.group = group
        if username is not None:
            self.username = username

    @property
    def jwt(self):
        """Gets the jwt of this InlineResponse2009Data.  # noqa: E501


        :return: The jwt of this InlineResponse2009Data.  # noqa: E501
        :rtype: str
        """
        return self._jwt

    @jwt.setter
    def jwt(self, jwt):
        """Sets the jwt of this InlineResponse2009Data.


        :param jwt: The jwt of this InlineResponse2009Data.  # noqa: E501
        :type: str
        """

        self._jwt = jwt

    @property
    def role(self):
        """Gets the role of this InlineResponse2009Data.  # noqa: E501


        :return: The role of this InlineResponse2009Data.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this InlineResponse2009Data.


        :param role: The role of this InlineResponse2009Data.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def group(self):
        """Gets the group of this InlineResponse2009Data.  # noqa: E501


        :return: The group of this InlineResponse2009Data.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this InlineResponse2009Data.


        :param group: The group of this InlineResponse2009Data.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def username(self):
        """Gets the username of this InlineResponse2009Data.  # noqa: E501


        :return: The username of this InlineResponse2009Data.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this InlineResponse2009Data.


        :param username: The username of this InlineResponse2009Data.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if issubclass(InlineResponse2009Data, dict):
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
        if not isinstance(other, InlineResponse2009Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
