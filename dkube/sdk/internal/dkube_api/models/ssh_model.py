# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.7.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SSHModel(object):
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
        'port': 'int',
        'private_key': 'str',
        'ssh_cmd': 'str'
    }

    attribute_map = {
        'port': 'port',
        'private_key': 'private_key',
        'ssh_cmd': 'ssh_cmd'
    }

    def __init__(self, port=None, private_key=None, ssh_cmd=None):  # noqa: E501
        """SSHModel - a model defined in Swagger"""  # noqa: E501

        self._port = None
        self._private_key = None
        self._ssh_cmd = None
        self.discriminator = None

        if port is not None:
            self.port = port
        if private_key is not None:
            self.private_key = private_key
        if ssh_cmd is not None:
            self.ssh_cmd = ssh_cmd

    @property
    def port(self):
        """Gets the port of this SSHModel.  # noqa: E501


        :return: The port of this SSHModel.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this SSHModel.


        :param port: The port of this SSHModel.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def private_key(self):
        """Gets the private_key of this SSHModel.  # noqa: E501


        :return: The private_key of this SSHModel.  # noqa: E501
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this SSHModel.


        :param private_key: The private_key of this SSHModel.  # noqa: E501
        :type: str
        """

        self._private_key = private_key

    @property
    def ssh_cmd(self):
        """Gets the ssh_cmd of this SSHModel.  # noqa: E501


        :return: The ssh_cmd of this SSHModel.  # noqa: E501
        :rtype: str
        """
        return self._ssh_cmd

    @ssh_cmd.setter
    def ssh_cmd(self, ssh_cmd):
        """Sets the ssh_cmd of this SSHModel.


        :param ssh_cmd: The ssh_cmd of this SSHModel.  # noqa: E501
        :type: str
        """

        self._ssh_cmd = ssh_cmd

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
        if issubclass(SSHModel, dict):
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
        if not isinstance(other, SSHModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
