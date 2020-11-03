# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.2.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AuthModelKeycloak(object):
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
        'client_id': 'str',
        'client_secret': 'str',
        'endpoint': 'str',
        'realm': 'str',
        'redirect_uri': 'str',
        'updated_at': 'str',
        'username': 'str'
    }

    attribute_map = {
        'client_id': 'clientId',
        'client_secret': 'clientSecret',
        'endpoint': 'endpoint',
        'realm': 'realm',
        'redirect_uri': 'redirectURI',
        'updated_at': 'updatedAt',
        'username': 'username'
    }

    def __init__(self, client_id=None, client_secret=None, endpoint=None, realm=None, redirect_uri=None, updated_at=None, username=None):  # noqa: E501
        """AuthModelKeycloak - a model defined in Swagger"""  # noqa: E501

        self._client_id = None
        self._client_secret = None
        self._endpoint = None
        self._realm = None
        self._redirect_uri = None
        self._updated_at = None
        self._username = None
        self.discriminator = None

        if client_id is not None:
            self.client_id = client_id
        if client_secret is not None:
            self.client_secret = client_secret
        if endpoint is not None:
            self.endpoint = endpoint
        if realm is not None:
            self.realm = realm
        if redirect_uri is not None:
            self.redirect_uri = redirect_uri
        if updated_at is not None:
            self.updated_at = updated_at
        if username is not None:
            self.username = username

    @property
    def client_id(self):
        """Gets the client_id of this AuthModelKeycloak.  # noqa: E501

        Keycloak App client id.  # noqa: E501

        :return: The client_id of this AuthModelKeycloak.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this AuthModelKeycloak.

        Keycloak App client id.  # noqa: E501

        :param client_id: The client_id of this AuthModelKeycloak.  # noqa: E501
        :type: str
        """
        if client_id is not None and len(client_id) > 255:
            raise ValueError("Invalid value for `client_id`, length must be less than or equal to `255`")  # noqa: E501
        if client_id is not None and len(client_id) < 1:
            raise ValueError("Invalid value for `client_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._client_id = client_id

    @property
    def client_secret(self):
        """Gets the client_secret of this AuthModelKeycloak.  # noqa: E501

        Keycloak App client secret.  # noqa: E501

        :return: The client_secret of this AuthModelKeycloak.  # noqa: E501
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this AuthModelKeycloak.

        Keycloak App client secret.  # noqa: E501

        :param client_secret: The client_secret of this AuthModelKeycloak.  # noqa: E501
        :type: str
        """
        if client_secret is not None and len(client_secret) > 255:
            raise ValueError("Invalid value for `client_secret`, length must be less than or equal to `255`")  # noqa: E501
        if client_secret is not None and len(client_secret) < 1:
            raise ValueError("Invalid value for `client_secret`, length must be greater than or equal to `1`")  # noqa: E501

        self._client_secret = client_secret

    @property
    def endpoint(self):
        """Gets the endpoint of this AuthModelKeycloak.  # noqa: E501

        Keycloak server's IP Address with scheme and port.  # noqa: E501

        :return: The endpoint of this AuthModelKeycloak.  # noqa: E501
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this AuthModelKeycloak.

        Keycloak server's IP Address with scheme and port.  # noqa: E501

        :param endpoint: The endpoint of this AuthModelKeycloak.  # noqa: E501
        :type: str
        """

        self._endpoint = endpoint

    @property
    def realm(self):
        """Gets the realm of this AuthModelKeycloak.  # noqa: E501


        :return: The realm of this AuthModelKeycloak.  # noqa: E501
        :rtype: str
        """
        return self._realm

    @realm.setter
    def realm(self, realm):
        """Sets the realm of this AuthModelKeycloak.


        :param realm: The realm of this AuthModelKeycloak.  # noqa: E501
        :type: str
        """
        if realm is not None and len(realm) > 255:
            raise ValueError("Invalid value for `realm`, length must be less than or equal to `255`")  # noqa: E501
        if realm is not None and len(realm) < 1:
            raise ValueError("Invalid value for `realm`, length must be greater than or equal to `1`")  # noqa: E501

        self._realm = realm

    @property
    def redirect_uri(self):
        """Gets the redirect_uri of this AuthModelKeycloak.  # noqa: E501

        redirect uri for keycloak server  # noqa: E501

        :return: The redirect_uri of this AuthModelKeycloak.  # noqa: E501
        :rtype: str
        """
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, redirect_uri):
        """Sets the redirect_uri of this AuthModelKeycloak.

        redirect uri for keycloak server  # noqa: E501

        :param redirect_uri: The redirect_uri of this AuthModelKeycloak.  # noqa: E501
        :type: str
        """

        self._redirect_uri = redirect_uri

    @property
    def updated_at(self):
        """Gets the updated_at of this AuthModelKeycloak.  # noqa: E501

        Time at which this provider was migrated to.  # noqa: E501

        :return: The updated_at of this AuthModelKeycloak.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this AuthModelKeycloak.

        Time at which this provider was migrated to.  # noqa: E501

        :param updated_at: The updated_at of this AuthModelKeycloak.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def username(self):
        """Gets the username of this AuthModelKeycloak.  # noqa: E501

        Name of the valid user. This user should be a keycloak user and must have admin priviliges.  # noqa: E501

        :return: The username of this AuthModelKeycloak.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AuthModelKeycloak.

        Name of the valid user. This user should be a keycloak user and must have admin priviliges.  # noqa: E501

        :param username: The username of this AuthModelKeycloak.  # noqa: E501
        :type: str
        """
        if username is not None and len(username) > 255:
            raise ValueError("Invalid value for `username`, length must be less than or equal to `255`")  # noqa: E501
        if username is not None and len(username) < 1:
            raise ValueError("Invalid value for `username`, length must be greater than or equal to `1`")  # noqa: E501

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
        if issubclass(AuthModelKeycloak, dict):
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
        if not isinstance(other, AuthModelKeycloak):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
