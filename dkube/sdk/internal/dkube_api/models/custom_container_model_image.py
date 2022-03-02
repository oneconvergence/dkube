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


class CustomContainerModelImage(object):
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
        'path': 'str',
        'username': 'str',
        'password': 'str',
        'runas': 'str'
    }

    attribute_map = {
        'path': 'path',
        'username': 'username',
        'password': 'password',
        'runas': 'runas'
    }

    def __init__(self, path=None, username=None, password=None, runas=None):  # noqa: E501
        """CustomContainerModelImage - a model defined in Swagger"""  # noqa: E501

        self._path = None
        self._username = None
        self._password = None
        self._runas = None
        self.discriminator = None

        self.path = path
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if runas is not None:
            self.runas = runas

    @property
    def path(self):
        """Gets the path of this CustomContainerModelImage.  # noqa: E501


        :return: The path of this CustomContainerModelImage.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this CustomContainerModelImage.


        :param path: The path of this CustomContainerModelImage.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def username(self):
        """Gets the username of this CustomContainerModelImage.  # noqa: E501


        :return: The username of this CustomContainerModelImage.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this CustomContainerModelImage.


        :param username: The username of this CustomContainerModelImage.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this CustomContainerModelImage.  # noqa: E501


        :return: The password of this CustomContainerModelImage.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CustomContainerModelImage.


        :param password: The password of this CustomContainerModelImage.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def runas(self):
        """Gets the runas of this CustomContainerModelImage.  # noqa: E501


        :return: The runas of this CustomContainerModelImage.  # noqa: E501
        :rtype: str
        """
        return self._runas

    @runas.setter
    def runas(self, runas):
        """Sets the runas of this CustomContainerModelImage.


        :param runas: The runas of this CustomContainerModelImage.  # noqa: E501
        :type: str
        """

        self._runas = runas

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
        if issubclass(CustomContainerModelImage, dict):
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
        if not isinstance(other, CustomContainerModelImage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
