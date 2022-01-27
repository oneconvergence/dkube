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


class AuthModelLdap(object):
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
        'basedn': 'str',
        'cacert': 'CertFileModel',
        'scope': 'str',
        'user_attr': 'str',
        'group_attr': 'str',
        'group_filter': 'str',
        'user_filter': 'str',
        'binddn': 'str',
        'endpoint': 'str',
        'advanced': 'AuthModelLdapAdvanced',
        'updated_at': 'str'
    }

    attribute_map = {
        'username': 'username',
        'password': 'password',
        'basedn': 'basedn',
        'cacert': 'cacert',
        'scope': 'scope',
        'user_attr': 'userAttr',
        'group_attr': 'groupAttr',
        'group_filter': 'groupFilter',
        'user_filter': 'userFilter',
        'binddn': 'binddn',
        'endpoint': 'endpoint',
        'advanced': 'advanced',
        'updated_at': 'updatedAt'
    }

    def __init__(self, username=None, password=None, basedn=None, cacert=None, scope=None, user_attr=None, group_attr=None, group_filter=None, user_filter=None, binddn=None, endpoint=None, advanced=None, updated_at=None):  # noqa: E501
        """AuthModelLdap - a model defined in Swagger"""  # noqa: E501

        self._username = None
        self._password = None
        self._basedn = None
        self._cacert = None
        self._scope = None
        self._user_attr = None
        self._group_attr = None
        self._group_filter = None
        self._user_filter = None
        self._binddn = None
        self._endpoint = None
        self._advanced = None
        self._updated_at = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if basedn is not None:
            self.basedn = basedn
        if cacert is not None:
            self.cacert = cacert
        if scope is not None:
            self.scope = scope
        if user_attr is not None:
            self.user_attr = user_attr
        if group_attr is not None:
            self.group_attr = group_attr
        if group_filter is not None:
            self.group_filter = group_filter
        if user_filter is not None:
            self.user_filter = user_filter
        if binddn is not None:
            self.binddn = binddn
        if endpoint is not None:
            self.endpoint = endpoint
        if advanced is not None:
            self.advanced = advanced
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def username(self):
        """Gets the username of this AuthModelLdap.  # noqa: E501

        Name of the valid user. This user must be present in LDAP server.  # noqa: E501

        :return: The username of this AuthModelLdap.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AuthModelLdap.

        Name of the valid user. This user must be present in LDAP server.  # noqa: E501

        :param username: The username of this AuthModelLdap.  # noqa: E501
        :type: str
        """
        if username is not None and len(username) > 255:
            raise ValueError("Invalid value for `username`, length must be less than or equal to `255`")  # noqa: E501
        if username is not None and len(username) < 1:
            raise ValueError("Invalid value for `username`, length must be greater than or equal to `1`")  # noqa: E501

        self._username = username

    @property
    def password(self):
        """Gets the password of this AuthModelLdap.  # noqa: E501

        Password of the user.  # noqa: E501

        :return: The password of this AuthModelLdap.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this AuthModelLdap.

        Password of the user.  # noqa: E501

        :param password: The password of this AuthModelLdap.  # noqa: E501
        :type: str
        """
        if password is not None and len(password) > 255:
            raise ValueError("Invalid value for `password`, length must be less than or equal to `255`")  # noqa: E501
        if password is not None and len(password) < 1:
            raise ValueError("Invalid value for `password`, length must be greater than or equal to `1`")  # noqa: E501

        self._password = password

    @property
    def basedn(self):
        """Gets the basedn of this AuthModelLdap.  # noqa: E501

        LDAP BaseDN.  # noqa: E501

        :return: The basedn of this AuthModelLdap.  # noqa: E501
        :rtype: str
        """
        return self._basedn

    @basedn.setter
    def basedn(self, basedn):
        """Sets the basedn of this AuthModelLdap.

        LDAP BaseDN.  # noqa: E501

        :param basedn: The basedn of this AuthModelLdap.  # noqa: E501
        :type: str
        """

        self._basedn = basedn

    @property
    def cacert(self):
        """Gets the cacert of this AuthModelLdap.  # noqa: E501


        :return: The cacert of this AuthModelLdap.  # noqa: E501
        :rtype: CertFileModel
        """
        return self._cacert

    @cacert.setter
    def cacert(self, cacert):
        """Sets the cacert of this AuthModelLdap.


        :param cacert: The cacert of this AuthModelLdap.  # noqa: E501
        :type: CertFileModel
        """

        self._cacert = cacert

    @property
    def scope(self):
        """Gets the scope of this AuthModelLdap.  # noqa: E501

        Search scope  # noqa: E501

        :return: The scope of this AuthModelLdap.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this AuthModelLdap.

        Search scope  # noqa: E501

        :param scope: The scope of this AuthModelLdap.  # noqa: E501
        :type: str
        """
        allowed_values = ["base", "singlelevel", "wholesubtree"]  # noqa: E501
        if scope not in allowed_values:
            raise ValueError(
                "Invalid value for `scope` ({0}), must be one of {1}"  # noqa: E501
                .format(scope, allowed_values)
            )

        self._scope = scope

    @property
    def user_attr(self):
        """Gets the user_attr of this AuthModelLdap.  # noqa: E501

        Search scope  # noqa: E501

        :return: The user_attr of this AuthModelLdap.  # noqa: E501
        :rtype: str
        """
        return self._user_attr

    @user_attr.setter
    def user_attr(self, user_attr):
        """Sets the user_attr of this AuthModelLdap.

        Search scope  # noqa: E501

        :param user_attr: The user_attr of this AuthModelLdap.  # noqa: E501
        :type: str
        """

        self._user_attr = user_attr

    @property
    def group_attr(self):
        """Gets the group_attr of this AuthModelLdap.  # noqa: E501

        Search scope  # noqa: E501

        :return: The group_attr of this AuthModelLdap.  # noqa: E501
        :rtype: str
        """
        return self._group_attr

    @group_attr.setter
    def group_attr(self, group_attr):
        """Sets the group_attr of this AuthModelLdap.

        Search scope  # noqa: E501

        :param group_attr: The group_attr of this AuthModelLdap.  # noqa: E501
        :type: str
        """

        self._group_attr = group_attr

    @property
    def group_filter(self):
        """Gets the group_filter of this AuthModelLdap.  # noqa: E501

        Optional LDAP group search filter  # noqa: E501

        :return: The group_filter of this AuthModelLdap.  # noqa: E501
        :rtype: str
        """
        return self._group_filter

    @group_filter.setter
    def group_filter(self, group_filter):
        """Sets the group_filter of this AuthModelLdap.

        Optional LDAP group search filter  # noqa: E501

        :param group_filter: The group_filter of this AuthModelLdap.  # noqa: E501
        :type: str
        """

        self._group_filter = group_filter

    @property
    def user_filter(self):
        """Gets the user_filter of this AuthModelLdap.  # noqa: E501

        Optional LDAP user search filter  # noqa: E501

        :return: The user_filter of this AuthModelLdap.  # noqa: E501
        :rtype: str
        """
        return self._user_filter

    @user_filter.setter
    def user_filter(self, user_filter):
        """Sets the user_filter of this AuthModelLdap.

        Optional LDAP user search filter  # noqa: E501

        :param user_filter: The user_filter of this AuthModelLdap.  # noqa: E501
        :type: str
        """

        self._user_filter = user_filter

    @property
    def binddn(self):
        """Gets the binddn of this AuthModelLdap.  # noqa: E501

        LDAP BindDN.  # noqa: E501

        :return: The binddn of this AuthModelLdap.  # noqa: E501
        :rtype: str
        """
        return self._binddn

    @binddn.setter
    def binddn(self, binddn):
        """Sets the binddn of this AuthModelLdap.

        LDAP BindDN.  # noqa: E501

        :param binddn: The binddn of this AuthModelLdap.  # noqa: E501
        :type: str
        """

        self._binddn = binddn

    @property
    def endpoint(self):
        """Gets the endpoint of this AuthModelLdap.  # noqa: E501

        AD IP Address without protocol and port.  # noqa: E501

        :return: The endpoint of this AuthModelLdap.  # noqa: E501
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this AuthModelLdap.

        AD IP Address without protocol and port.  # noqa: E501

        :param endpoint: The endpoint of this AuthModelLdap.  # noqa: E501
        :type: str
        """

        self._endpoint = endpoint

    @property
    def advanced(self):
        """Gets the advanced of this AuthModelLdap.  # noqa: E501


        :return: The advanced of this AuthModelLdap.  # noqa: E501
        :rtype: AuthModelLdapAdvanced
        """
        return self._advanced

    @advanced.setter
    def advanced(self, advanced):
        """Sets the advanced of this AuthModelLdap.


        :param advanced: The advanced of this AuthModelLdap.  # noqa: E501
        :type: AuthModelLdapAdvanced
        """

        self._advanced = advanced

    @property
    def updated_at(self):
        """Gets the updated_at of this AuthModelLdap.  # noqa: E501

        Time at which this provider was migrated to.  # noqa: E501

        :return: The updated_at of this AuthModelLdap.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this AuthModelLdap.

        Time at which this provider was migrated to.  # noqa: E501

        :param updated_at: The updated_at of this AuthModelLdap.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

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
        if issubclass(AuthModelLdap, dict):
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
        if not isinstance(other, AuthModelLdap):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
