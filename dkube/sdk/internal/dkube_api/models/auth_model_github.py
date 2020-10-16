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


class AuthModelGithub(object):
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
        'organization': 'str',
        'token': 'str',
        'code': 'str',
        'client_id': 'str',
        'client_secret': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'username': 'username',
        'organization': 'organization',
        'token': 'token',
        'code': 'code',
        'client_id': 'clientId',
        'client_secret': 'clientSecret',
        'updated_at': 'updatedAt'
    }

    def __init__(self, username=None, organization=None, token=None, code=None, client_id=None, client_secret=None, updated_at=None):  # noqa: E501
        """AuthModelGithub - a model defined in Swagger"""  # noqa: E501

        self._username = None
        self._organization = None
        self._token = None
        self._code = None
        self._client_id = None
        self._client_secret = None
        self._updated_at = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if organization is not None:
            self.organization = organization
        if token is not None:
            self.token = token
        if code is not None:
            self.code = code
        if client_id is not None:
            self.client_id = client_id
        if client_secret is not None:
            self.client_secret = client_secret
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def username(self):
        """Gets the username of this AuthModelGithub.  # noqa: E501

        Name of the valid user. This user should be a github user and must have admin priviliges.  # noqa: E501

        :return: The username of this AuthModelGithub.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AuthModelGithub.

        Name of the valid user. This user should be a github user and must have admin priviliges.  # noqa: E501

        :param username: The username of this AuthModelGithub.  # noqa: E501
        :type: str
        """
        if username is not None and len(username) > 255:
            raise ValueError("Invalid value for `username`, length must be less than or equal to `255`")  # noqa: E501
        if username is not None and len(username) < 1:
            raise ValueError("Invalid value for `username`, length must be greater than or equal to `1`")  # noqa: E501

        self._username = username

    @property
    def organization(self):
        """Gets the organization of this AuthModelGithub.  # noqa: E501

        Git organization of which this user is admin. All the members of organization will auto imported as part of init. They will just be created and not onboarded. Such users still do not have access to Dkube APIs. This user with operator role would need to onboard the user explicitly.  # noqa: E501

        :return: The organization of this AuthModelGithub.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this AuthModelGithub.

        Git organization of which this user is admin. All the members of organization will auto imported as part of init. They will just be created and not onboarded. Such users still do not have access to Dkube APIs. This user with operator role would need to onboard the user explicitly.  # noqa: E501

        :param organization: The organization of this AuthModelGithub.  # noqa: E501
        :type: str
        """
        if organization is not None and len(organization) > 255:
            raise ValueError("Invalid value for `organization`, length must be less than or equal to `255`")  # noqa: E501
        if organization is not None and len(organization) < 1:
            raise ValueError("Invalid value for `organization`, length must be greater than or equal to `1`")  # noqa: E501

        self._organization = organization

    @property
    def token(self):
        """Gets the token of this AuthModelGithub.  # noqa: E501

        Github token with admin priviliges.  # noqa: E501

        :return: The token of this AuthModelGithub.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this AuthModelGithub.

        Github token with admin priviliges.  # noqa: E501

        :param token: The token of this AuthModelGithub.  # noqa: E501
        :type: str
        """
        if token is not None and len(token) < 1:
            raise ValueError("Invalid value for `token`, length must be greater than or equal to `1`")  # noqa: E501

        self._token = token

    @property
    def code(self):
        """Gets the code of this AuthModelGithub.  # noqa: E501

        Github session code for generating access_token.  # noqa: E501

        :return: The code of this AuthModelGithub.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this AuthModelGithub.

        Github session code for generating access_token.  # noqa: E501

        :param code: The code of this AuthModelGithub.  # noqa: E501
        :type: str
        """
        if code is not None and len(code) > 255:
            raise ValueError("Invalid value for `code`, length must be less than or equal to `255`")  # noqa: E501
        if code is not None and len(code) < 1:
            raise ValueError("Invalid value for `code`, length must be greater than or equal to `1`")  # noqa: E501

        self._code = code

    @property
    def client_id(self):
        """Gets the client_id of this AuthModelGithub.  # noqa: E501

        Github App client id.  # noqa: E501

        :return: The client_id of this AuthModelGithub.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this AuthModelGithub.

        Github App client id.  # noqa: E501

        :param client_id: The client_id of this AuthModelGithub.  # noqa: E501
        :type: str
        """
        if client_id is not None and len(client_id) > 255:
            raise ValueError("Invalid value for `client_id`, length must be less than or equal to `255`")  # noqa: E501
        if client_id is not None and len(client_id) < 1:
            raise ValueError("Invalid value for `client_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._client_id = client_id

    @property
    def client_secret(self):
        """Gets the client_secret of this AuthModelGithub.  # noqa: E501

        Github App client secret.  # noqa: E501

        :return: The client_secret of this AuthModelGithub.  # noqa: E501
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this AuthModelGithub.

        Github App client secret.  # noqa: E501

        :param client_secret: The client_secret of this AuthModelGithub.  # noqa: E501
        :type: str
        """
        if client_secret is not None and len(client_secret) > 255:
            raise ValueError("Invalid value for `client_secret`, length must be less than or equal to `255`")  # noqa: E501
        if client_secret is not None and len(client_secret) < 1:
            raise ValueError("Invalid value for `client_secret`, length must be greater than or equal to `1`")  # noqa: E501

        self._client_secret = client_secret

    @property
    def updated_at(self):
        """Gets the updated_at of this AuthModelGithub.  # noqa: E501

        Time at which this provider was migrated to.  # noqa: E501

        :return: The updated_at of this AuthModelGithub.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this AuthModelGithub.

        Time at which this provider was migrated to.  # noqa: E501

        :param updated_at: The updated_at of this AuthModelGithub.  # noqa: E501
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
        if issubclass(AuthModelGithub, dict):
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
        if not isinstance(other, AuthModelGithub):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other