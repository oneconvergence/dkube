# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.5.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SmtpArtifact(object):
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
        'full_name': 'str',
        'sender_email': 'str',
        'smtp_password': 'str',
        'smtp_port': 'str',
        'smtp_server': 'str',
        'smtp_tls_port': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'full_name': 'full_name',
        'sender_email': 'sender_email',
        'smtp_password': 'smtp_password',
        'smtp_port': 'smtp_port',
        'smtp_server': 'smtp_server',
        'smtp_tls_port': 'smtp_tls_port',
        'enabled': 'enabled'
    }

    def __init__(self, full_name=None, sender_email=None, smtp_password=None, smtp_port=None, smtp_server=None, smtp_tls_port=None, enabled=None):  # noqa: E501
        """SmtpArtifact - a model defined in Swagger"""  # noqa: E501

        self._full_name = None
        self._sender_email = None
        self._smtp_password = None
        self._smtp_port = None
        self._smtp_server = None
        self._smtp_tls_port = None
        self._enabled = None
        self.discriminator = None

        if full_name is not None:
            self.full_name = full_name
        if sender_email is not None:
            self.sender_email = sender_email
        if smtp_password is not None:
            self.smtp_password = smtp_password
        if smtp_port is not None:
            self.smtp_port = smtp_port
        if smtp_server is not None:
            self.smtp_server = smtp_server
        if smtp_tls_port is not None:
            self.smtp_tls_port = smtp_tls_port
        if enabled is not None:
            self.enabled = enabled

    @property
    def full_name(self):
        """Gets the full_name of this SmtpArtifact.  # noqa: E501


        :return: The full_name of this SmtpArtifact.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this SmtpArtifact.


        :param full_name: The full_name of this SmtpArtifact.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def sender_email(self):
        """Gets the sender_email of this SmtpArtifact.  # noqa: E501


        :return: The sender_email of this SmtpArtifact.  # noqa: E501
        :rtype: str
        """
        return self._sender_email

    @sender_email.setter
    def sender_email(self, sender_email):
        """Sets the sender_email of this SmtpArtifact.


        :param sender_email: The sender_email of this SmtpArtifact.  # noqa: E501
        :type: str
        """

        self._sender_email = sender_email

    @property
    def smtp_password(self):
        """Gets the smtp_password of this SmtpArtifact.  # noqa: E501


        :return: The smtp_password of this SmtpArtifact.  # noqa: E501
        :rtype: str
        """
        return self._smtp_password

    @smtp_password.setter
    def smtp_password(self, smtp_password):
        """Sets the smtp_password of this SmtpArtifact.


        :param smtp_password: The smtp_password of this SmtpArtifact.  # noqa: E501
        :type: str
        """

        self._smtp_password = smtp_password

    @property
    def smtp_port(self):
        """Gets the smtp_port of this SmtpArtifact.  # noqa: E501


        :return: The smtp_port of this SmtpArtifact.  # noqa: E501
        :rtype: str
        """
        return self._smtp_port

    @smtp_port.setter
    def smtp_port(self, smtp_port):
        """Sets the smtp_port of this SmtpArtifact.


        :param smtp_port: The smtp_port of this SmtpArtifact.  # noqa: E501
        :type: str
        """

        self._smtp_port = smtp_port

    @property
    def smtp_server(self):
        """Gets the smtp_server of this SmtpArtifact.  # noqa: E501


        :return: The smtp_server of this SmtpArtifact.  # noqa: E501
        :rtype: str
        """
        return self._smtp_server

    @smtp_server.setter
    def smtp_server(self, smtp_server):
        """Sets the smtp_server of this SmtpArtifact.


        :param smtp_server: The smtp_server of this SmtpArtifact.  # noqa: E501
        :type: str
        """

        self._smtp_server = smtp_server

    @property
    def smtp_tls_port(self):
        """Gets the smtp_tls_port of this SmtpArtifact.  # noqa: E501


        :return: The smtp_tls_port of this SmtpArtifact.  # noqa: E501
        :rtype: str
        """
        return self._smtp_tls_port

    @smtp_tls_port.setter
    def smtp_tls_port(self, smtp_tls_port):
        """Sets the smtp_tls_port of this SmtpArtifact.


        :param smtp_tls_port: The smtp_tls_port of this SmtpArtifact.  # noqa: E501
        :type: str
        """

        self._smtp_tls_port = smtp_tls_port

    @property
    def enabled(self):
        """Gets the enabled of this SmtpArtifact.  # noqa: E501


        :return: The enabled of this SmtpArtifact.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this SmtpArtifact.


        :param enabled: The enabled of this SmtpArtifact.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

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
        if issubclass(SmtpArtifact, dict):
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
        if not isinstance(other, SmtpArtifact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
