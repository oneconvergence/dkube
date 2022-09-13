# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AuthModelPingfederate(object):
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
        'endpoint': 'str',
        'redirect_uri': 'str',
        'client_id': 'str',
        'client_secret': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'username': 'username',
        'endpoint': 'endpoint',
        'redirect_uri': 'redirectURI',
        'client_id': 'clientId',
        'client_secret': 'clientSecret',
        'updated_at': 'updatedAt'
    }

    def __init__(self, username=None, endpoint=None, redirect_uri=None, client_id=None, client_secret=None, updated_at=None):  # noqa: E501
        """AuthModelPingfederate - a model defined in Swagger"""  # noqa: E501

        self._username = None
        self._endpoint = None
        self._redirect_uri = None
        self._client_id = None
        self._client_secret = None
        self._updated_at = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if endpoint is not None:
            self.endpoint = endpoint
        if redirect_uri is not None:
            self.redirect_uri = redirect_uri
        if client_id is not None:
            self.client_id = client_id
        if client_secret is not None:
            self.client_secret = client_secret
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def username(self):
        """Gets the username of this AuthModelPingfederate.  # noqa: E501

        Name of the valid user. This user should be a pingfederate user and must have admin priviliges.  # noqa: E501

        :return: The username of this AuthModelPingfederate.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AuthModelPingfederate.

        Name of the valid user. This user should be a pingfederate user and must have admin priviliges.  # noqa: E501

        :param username: The username of this AuthModelPingfederate.  # noqa: E501
        :type: str
        """
        if username is not None and len(username) > 255:
            raise ValueError("Invalid value for `username`, length must be less than or equal to `255`")  # noqa: E501
        if username is not None and len(username) < 1:
            raise ValueError("Invalid value for `username`, length must be greater than or equal to `1`")  # noqa: E501

        self._username = username

    @property
    def endpoint(self):
        """Gets the endpoint of this AuthModelPingfederate.  # noqa: E501

        pingfederate server's IP Address with scheme and port.  # noqa: E501

        :return: The endpoint of this AuthModelPingfederate.  # noqa: E501
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this AuthModelPingfederate.

        pingfederate server's IP Address with scheme and port.  # noqa: E501

        :param endpoint: The endpoint of this AuthModelPingfederate.  # noqa: E501
        :type: str
        """

        self._endpoint = endpoint

    @property
    def redirect_uri(self):
        """Gets the redirect_uri of this AuthModelPingfederate.  # noqa: E501

        redirect uri for pingfederate server  # noqa: E501

        :return: The redirect_uri of this AuthModelPingfederate.  # noqa: E501
        :rtype: str
        """
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, redirect_uri):
        """Sets the redirect_uri of this AuthModelPingfederate.

        redirect uri for pingfederate server  # noqa: E501

        :param redirect_uri: The redirect_uri of this AuthModelPingfederate.  # noqa: E501
        :type: str
        """

        self._redirect_uri = redirect_uri

    @property
    def client_id(self):
        """Gets the client_id of this AuthModelPingfederate.  # noqa: E501

        pingfederate App client id.  # noqa: E501

        :return: The client_id of this AuthModelPingfederate.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this AuthModelPingfederate.

        pingfederate App client id.  # noqa: E501

        :param client_id: The client_id of this AuthModelPingfederate.  # noqa: E501
        :type: str
        """
        if client_id is not None and len(client_id) > 255:
            raise ValueError("Invalid value for `client_id`, length must be less than or equal to `255`")  # noqa: E501
        if client_id is not None and len(client_id) < 1:
            raise ValueError("Invalid value for `client_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._client_id = client_id

    @property
    def client_secret(self):
        """Gets the client_secret of this AuthModelPingfederate.  # noqa: E501

        pingfederate App client secret.  # noqa: E501

        :return: The client_secret of this AuthModelPingfederate.  # noqa: E501
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this AuthModelPingfederate.

        pingfederate App client secret.  # noqa: E501

        :param client_secret: The client_secret of this AuthModelPingfederate.  # noqa: E501
        :type: str
        """
        if client_secret is not None and len(client_secret) > 255:
            raise ValueError("Invalid value for `client_secret`, length must be less than or equal to `255`")  # noqa: E501
        if client_secret is not None and len(client_secret) < 1:
            raise ValueError("Invalid value for `client_secret`, length must be greater than or equal to `1`")  # noqa: E501

        self._client_secret = client_secret

    @property
    def updated_at(self):
        """Gets the updated_at of this AuthModelPingfederate.  # noqa: E501

        Time at which this provider was migrated to.  # noqa: E501

        :return: The updated_at of this AuthModelPingfederate.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this AuthModelPingfederate.

        Time at which this provider was migrated to.  # noqa: E501

        :param updated_at: The updated_at of this AuthModelPingfederate.  # noqa: E501
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
        if issubclass(AuthModelPingfederate, dict):
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
        if not isinstance(other, AuthModelPingfederate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
