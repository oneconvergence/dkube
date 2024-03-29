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


class AuthModel(object):
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
        'mode': 'str',
        'code': 'str',
        'providers': 'list[str]',
        'ldap': 'AuthModelLdap',
        'github': 'AuthModelGithub',
        'keycloak': 'AuthModelKeycloak',
        'local': 'AuthModelLocal'
    }

    attribute_map = {
        'mode': 'mode',
        'code': 'code',
        'providers': 'providers',
        'ldap': 'ldap',
        'github': 'github',
        'keycloak': 'keycloak',
        'local': 'local'
    }

    def __init__(self, mode=None, code=None, providers=None, ldap=None, github=None, keycloak=None, local=None):  # noqa: E501
        """AuthModel - a model defined in Swagger"""  # noqa: E501

        self._mode = None
        self._code = None
        self._providers = None
        self._ldap = None
        self._github = None
        self._keycloak = None
        self._local = None
        self.discriminator = None

        self.mode = mode
        if code is not None:
            self.code = code
        if providers is not None:
            self.providers = providers
        if ldap is not None:
            self.ldap = ldap
        if github is not None:
            self.github = github
        if keycloak is not None:
            self.keycloak = keycloak
        if local is not None:
            self.local = local

    @property
    def mode(self):
        """Gets the mode of this AuthModel.  # noqa: E501

        The authorization mode to switch to.  # noqa: E501

        :return: The mode of this AuthModel.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this AuthModel.

        The authorization mode to switch to.  # noqa: E501

        :param mode: The mode of this AuthModel.  # noqa: E501
        :type: str
        """
        if mode is None:
            raise ValueError("Invalid value for `mode`, must not be `None`")  # noqa: E501
        allowed_values = ["github", "local", "ldap", "keycloak"]  # noqa: E501
        if mode not in allowed_values:
            raise ValueError(
                "Invalid value for `mode` ({0}), must be one of {1}"  # noqa: E501
                .format(mode, allowed_values)
            )

        self._mode = mode

    @property
    def code(self):
        """Gets the code of this AuthModel.  # noqa: E501

        Code provided by Dex that can be exchanged with it to receive JWT token.  # noqa: E501

        :return: The code of this AuthModel.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this AuthModel.

        Code provided by Dex that can be exchanged with it to receive JWT token.  # noqa: E501

        :param code: The code of this AuthModel.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def providers(self):
        """Gets the providers of this AuthModel.  # noqa: E501

        The modes of authorization that supports changing to from operator dashboard.  # noqa: E501

        :return: The providers of this AuthModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._providers

    @providers.setter
    def providers(self, providers):
        """Sets the providers of this AuthModel.

        The modes of authorization that supports changing to from operator dashboard.  # noqa: E501

        :param providers: The providers of this AuthModel.  # noqa: E501
        :type: list[str]
        """

        self._providers = providers

    @property
    def ldap(self):
        """Gets the ldap of this AuthModel.  # noqa: E501


        :return: The ldap of this AuthModel.  # noqa: E501
        :rtype: AuthModelLdap
        """
        return self._ldap

    @ldap.setter
    def ldap(self, ldap):
        """Sets the ldap of this AuthModel.


        :param ldap: The ldap of this AuthModel.  # noqa: E501
        :type: AuthModelLdap
        """

        self._ldap = ldap

    @property
    def github(self):
        """Gets the github of this AuthModel.  # noqa: E501


        :return: The github of this AuthModel.  # noqa: E501
        :rtype: AuthModelGithub
        """
        return self._github

    @github.setter
    def github(self, github):
        """Sets the github of this AuthModel.


        :param github: The github of this AuthModel.  # noqa: E501
        :type: AuthModelGithub
        """

        self._github = github

    @property
    def keycloak(self):
        """Gets the keycloak of this AuthModel.  # noqa: E501


        :return: The keycloak of this AuthModel.  # noqa: E501
        :rtype: AuthModelKeycloak
        """
        return self._keycloak

    @keycloak.setter
    def keycloak(self, keycloak):
        """Sets the keycloak of this AuthModel.


        :param keycloak: The keycloak of this AuthModel.  # noqa: E501
        :type: AuthModelKeycloak
        """

        self._keycloak = keycloak

    @property
    def local(self):
        """Gets the local of this AuthModel.  # noqa: E501


        :return: The local of this AuthModel.  # noqa: E501
        :rtype: AuthModelLocal
        """
        return self._local

    @local.setter
    def local(self, local):
        """Sets the local of this AuthModel.


        :param local: The local of this AuthModel.  # noqa: E501
        :type: AuthModelLocal
        """

        self._local = local

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
        if issubclass(AuthModel, dict):
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
        if not isinstance(other, AuthModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
