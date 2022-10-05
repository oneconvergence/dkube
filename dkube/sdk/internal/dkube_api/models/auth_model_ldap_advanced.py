# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.3.0.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AuthModelLdapAdvanced(object):
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
        'data_profile': 'str',
        'superuser_profile': 'str'
    }

    attribute_map = {
        'name': 'name',
        'data_profile': 'dataProfile',
        'superuser_profile': 'superuserProfile'
    }

    def __init__(self, name=None, data_profile=None, superuser_profile=None):  # noqa: E501
        """AuthModelLdapAdvanced - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._data_profile = None
        self._superuser_profile = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if data_profile is not None:
            self.data_profile = data_profile
        if superuser_profile is not None:
            self.superuser_profile = superuser_profile

    @property
    def name(self):
        """Gets the name of this AuthModelLdapAdvanced.  # noqa: E501


        :return: The name of this AuthModelLdapAdvanced.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AuthModelLdapAdvanced.


        :param name: The name of this AuthModelLdapAdvanced.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def data_profile(self):
        """Gets the data_profile of this AuthModelLdapAdvanced.  # noqa: E501


        :return: The data_profile of this AuthModelLdapAdvanced.  # noqa: E501
        :rtype: str
        """
        return self._data_profile

    @data_profile.setter
    def data_profile(self, data_profile):
        """Sets the data_profile of this AuthModelLdapAdvanced.


        :param data_profile: The data_profile of this AuthModelLdapAdvanced.  # noqa: E501
        :type: str
        """

        self._data_profile = data_profile

    @property
    def superuser_profile(self):
        """Gets the superuser_profile of this AuthModelLdapAdvanced.  # noqa: E501


        :return: The superuser_profile of this AuthModelLdapAdvanced.  # noqa: E501
        :rtype: str
        """
        return self._superuser_profile

    @superuser_profile.setter
    def superuser_profile(self, superuser_profile):
        """Sets the superuser_profile of this AuthModelLdapAdvanced.


        :param superuser_profile: The superuser_profile of this AuthModelLdapAdvanced.  # noqa: E501
        :type: str
        """

        self._superuser_profile = superuser_profile

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
        if issubclass(AuthModelLdapAdvanced, dict):
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
        if not isinstance(other, AuthModelLdapAdvanced):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
