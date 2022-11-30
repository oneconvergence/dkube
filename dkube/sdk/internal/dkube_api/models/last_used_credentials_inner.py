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


class LastUsedCredentialsInner(object):
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
        'host': 'str',
        'credentials': 'GitAccessCredentials'
    }

    attribute_map = {
        'host': 'host',
        'credentials': 'credentials'
    }

    def __init__(self, host=None, credentials=None):  # noqa: E501
        """LastUsedCredentialsInner - a model defined in Swagger"""  # noqa: E501

        self._host = None
        self._credentials = None
        self.discriminator = None

        if host is not None:
            self.host = host
        if credentials is not None:
            self.credentials = credentials

    @property
    def host(self):
        """Gets the host of this LastUsedCredentialsInner.  # noqa: E501


        :return: The host of this LastUsedCredentialsInner.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this LastUsedCredentialsInner.


        :param host: The host of this LastUsedCredentialsInner.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def credentials(self):
        """Gets the credentials of this LastUsedCredentialsInner.  # noqa: E501


        :return: The credentials of this LastUsedCredentialsInner.  # noqa: E501
        :rtype: GitAccessCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this LastUsedCredentialsInner.


        :param credentials: The credentials of this LastUsedCredentialsInner.  # noqa: E501
        :type: GitAccessCredentials
        """

        self._credentials = credentials

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
        if issubclass(LastUsedCredentialsInner, dict):
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
        if not isinstance(other, LastUsedCredentialsInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
