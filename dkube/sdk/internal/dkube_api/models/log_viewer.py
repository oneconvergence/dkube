# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0.0.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class LogViewer(object):
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
        'username': 'str',
        'password': 'str',
        'svr_address': 'str',
        'protocol': 'str',
        'port': 'str'
    }

    attribute_map = {
        'username': 'Username',
        'password': 'Password',
        'svr_address': 'SvrAddress',
        'protocol': 'Protocol',
        'port': 'Port'
    }

    def __init__(self, username=None, password=None, svr_address=None, protocol=None, port=None):  # noqa: E501
        """LogViewer - a model defined in Swagger"""  # noqa: E501

        self._username = None
        self._password = None
        self._svr_address = None
        self._protocol = None
        self._port = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if svr_address is not None:
            self.svr_address = svr_address
        if protocol is not None:
            self.protocol = protocol
        if port is not None:
            self.port = port

    @property
    def username(self):
        """Gets the username of this LogViewer.  # noqa: E501


        :return: The username of this LogViewer.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this LogViewer.


        :param username: The username of this LogViewer.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this LogViewer.  # noqa: E501


        :return: The password of this LogViewer.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this LogViewer.


        :param password: The password of this LogViewer.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def svr_address(self):
        """Gets the svr_address of this LogViewer.  # noqa: E501


        :return: The svr_address of this LogViewer.  # noqa: E501
        :rtype: str
        """
        return self._svr_address

    @svr_address.setter
    def svr_address(self, svr_address):
        """Sets the svr_address of this LogViewer.


        :param svr_address: The svr_address of this LogViewer.  # noqa: E501
        :type: str
        """

        self._svr_address = svr_address

    @property
    def protocol(self):
        """Gets the protocol of this LogViewer.  # noqa: E501


        :return: The protocol of this LogViewer.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this LogViewer.


        :param protocol: The protocol of this LogViewer.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def port(self):
        """Gets the port of this LogViewer.  # noqa: E501


        :return: The port of this LogViewer.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this LogViewer.


        :param port: The port of this LogViewer.  # noqa: E501
        :type: str
        """

        self._port = port

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
        if issubclass(LogViewer, dict):
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
        if not isinstance(other, LogViewer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
