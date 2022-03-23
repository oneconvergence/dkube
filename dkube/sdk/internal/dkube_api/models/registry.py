# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.2.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Registry(object):
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
        'name': 'str',
        'kind': 'str',
        'iam_role': 'str',
        'username': 'str',
        'password': 'str',
        'token': 'str'
    }

    attribute_map = {
        'name': 'name',
        'kind': 'kind',
        'iam_role': 'iam-role',
        'username': 'username',
        'password': 'password',
        'token': 'token'
    }

    def __init__(self, name=None, kind=None, iam_role=None, username=None, password=None, token=None):  # noqa: E501
        """Registry - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._kind = None
        self._iam_role = None
        self._username = None
        self._password = None
        self._token = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if kind is not None:
            self.kind = kind
        if iam_role is not None:
            self.iam_role = iam_role
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if token is not None:
            self.token = token

    @property
    def name(self):
        """Gets the name of this Registry.  # noqa: E501


        :return: The name of this Registry.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Registry.


        :param name: The name of this Registry.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def kind(self):
        """Gets the kind of this Registry.  # noqa: E501


        :return: The kind of this Registry.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this Registry.


        :param kind: The kind of this Registry.  # noqa: E501
        :type: str
        """
        allowed_values = ["docker", "ecr"]  # noqa: E501
        if kind not in allowed_values:
            raise ValueError(
                "Invalid value for `kind` ({0}), must be one of {1}"  # noqa: E501
                .format(kind, allowed_values)
            )

        self._kind = kind

    @property
    def iam_role(self):
        """Gets the iam_role of this Registry.  # noqa: E501


        :return: The iam_role of this Registry.  # noqa: E501
        :rtype: str
        """
        return self._iam_role

    @iam_role.setter
    def iam_role(self, iam_role):
        """Sets the iam_role of this Registry.


        :param iam_role: The iam_role of this Registry.  # noqa: E501
        :type: str
        """

        self._iam_role = iam_role

    @property
    def username(self):
        """Gets the username of this Registry.  # noqa: E501


        :return: The username of this Registry.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Registry.


        :param username: The username of this Registry.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this Registry.  # noqa: E501


        :return: The password of this Registry.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this Registry.


        :param password: The password of this Registry.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def token(self):
        """Gets the token of this Registry.  # noqa: E501


        :return: The token of this Registry.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this Registry.


        :param token: The token of this Registry.  # noqa: E501
        :type: str
        """

        self._token = token

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
        if issubclass(Registry, dict):
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
        if not isinstance(other, Registry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
