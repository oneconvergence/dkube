# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.5.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Cluster(object):
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
        'kind': 'str',
        '_class': 'str',
        'url': 'str',
        'ca': 'str',
        'version': 'str',
        'auth_type': 'str',
        'jwt_token_type': 'str',
        'headers': 'dict(str, str)',
        'jwt_token': 'str',
        'jwt_signing_key': 'str',
        'cluster_user': 'str',
        'access_keys': 'ClusterAccessKeysDef',
        'tags': 'list[str]',
        'description': 'str',
        'plugin': 'str'
    }

    attribute_map = {
        'name': 'name',
        'kind': 'kind',
        '_class': 'class',
        'url': 'url',
        'ca': 'ca',
        'version': 'version',
        'auth_type': 'auth_type',
        'jwt_token_type': 'jwt_token_type',
        'headers': 'headers',
        'jwt_token': 'jwt_token',
        'jwt_signing_key': 'jwt_signing_key',
        'cluster_user': 'cluster_user',
        'access_keys': 'access_keys',
        'tags': 'tags',
        'description': 'description',
        'plugin': 'plugin'
    }

    def __init__(self, name=None, kind=None, _class=None, url=None, ca=None, version=None, auth_type=None, jwt_token_type=None, headers=None, jwt_token=None, jwt_signing_key=None, cluster_user=None, access_keys=None, tags=None, description=None, plugin=None):  # noqa: E501
        """Cluster - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._kind = None
        self.__class = None
        self._url = None
        self._ca = None
        self._version = None
        self._auth_type = None
        self._jwt_token_type = None
        self._headers = None
        self._jwt_token = None
        self._jwt_signing_key = None
        self._cluster_user = None
        self._access_keys = None
        self._tags = None
        self._description = None
        self._plugin = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if kind is not None:
            self.kind = kind
        if _class is not None:
            self._class = _class
        if url is not None:
            self.url = url
        if ca is not None:
            self.ca = ca
        if version is not None:
            self.version = version
        self.auth_type = auth_type
        if jwt_token_type is not None:
            self.jwt_token_type = jwt_token_type
        if headers is not None:
            self.headers = headers
        if jwt_token is not None:
            self.jwt_token = jwt_token
        if jwt_signing_key is not None:
            self.jwt_signing_key = jwt_signing_key
        if cluster_user is not None:
            self.cluster_user = cluster_user
        if access_keys is not None:
            self.access_keys = access_keys
        if tags is not None:
            self.tags = tags
        if description is not None:
            self.description = description
        if plugin is not None:
            self.plugin = plugin

    @property
    def name(self):
        """Gets the name of this Cluster.  # noqa: E501


        :return: The name of this Cluster.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Cluster.


        :param name: The name of this Cluster.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def kind(self):
        """Gets the kind of this Cluster.  # noqa: E501


        :return: The kind of this Cluster.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this Cluster.


        :param kind: The kind of this Cluster.  # noqa: E501
        :type: str
        """
        allowed_values = ["kubernetes-local", "dkube-remote", "slurm-remote", "sagemaker", "kserve", "custom"]  # noqa: E501
        if kind not in allowed_values:
            raise ValueError(
                "Invalid value for `kind` ({0}), must be one of {1}"  # noqa: E501
                .format(kind, allowed_values)
            )

        self._kind = kind

    @property
    def _class(self):
        """Gets the _class of this Cluster.  # noqa: E501


        :return: The _class of this Cluster.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this Cluster.


        :param _class: The _class of this Cluster.  # noqa: E501
        :type: str
        """
        allowed_values = ["execution", "monitoring"]  # noqa: E501
        if _class not in allowed_values:
            raise ValueError(
                "Invalid value for `_class` ({0}), must be one of {1}"  # noqa: E501
                .format(_class, allowed_values)
            )

        self.__class = _class

    @property
    def url(self):
        """Gets the url of this Cluster.  # noqa: E501

        URL of cluster  # noqa: E501

        :return: The url of this Cluster.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Cluster.

        URL of cluster  # noqa: E501

        :param url: The url of this Cluster.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def ca(self):
        """Gets the ca of this Cluster.  # noqa: E501

        Certificate authority data  # noqa: E501

        :return: The ca of this Cluster.  # noqa: E501
        :rtype: str
        """
        return self._ca

    @ca.setter
    def ca(self, ca):
        """Sets the ca of this Cluster.

        Certificate authority data  # noqa: E501

        :param ca: The ca of this Cluster.  # noqa: E501
        :type: str
        """

        self._ca = ca

    @property
    def version(self):
        """Gets the version of this Cluster.  # noqa: E501

        version of cluster  # noqa: E501

        :return: The version of this Cluster.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Cluster.

        version of cluster  # noqa: E501

        :param version: The version of this Cluster.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def auth_type(self):
        """Gets the auth_type of this Cluster.  # noqa: E501


        :return: The auth_type of this Cluster.  # noqa: E501
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this Cluster.


        :param auth_type: The auth_type of this Cluster.  # noqa: E501
        :type: str
        """
        if auth_type is None:
            raise ValueError("Invalid value for `auth_type`, must not be `None`")  # noqa: E501
        allowed_values = ["jwt", "access_keys", "none"]  # noqa: E501
        if auth_type not in allowed_values:
            raise ValueError(
                "Invalid value for `auth_type` ({0}), must be one of {1}"  # noqa: E501
                .format(auth_type, allowed_values)
            )

        self._auth_type = auth_type

    @property
    def jwt_token_type(self):
        """Gets the jwt_token_type of this Cluster.  # noqa: E501


        :return: The jwt_token_type of this Cluster.  # noqa: E501
        :rtype: str
        """
        return self._jwt_token_type

    @jwt_token_type.setter
    def jwt_token_type(self, jwt_token_type):
        """Sets the jwt_token_type of this Cluster.


        :param jwt_token_type: The jwt_token_type of this Cluster.  # noqa: E501
        :type: str
        """
        allowed_values = ["sign-token", "use-token"]  # noqa: E501
        if jwt_token_type not in allowed_values:
            raise ValueError(
                "Invalid value for `jwt_token_type` ({0}), must be one of {1}"  # noqa: E501
                .format(jwt_token_type, allowed_values)
            )

        self._jwt_token_type = jwt_token_type

    @property
    def headers(self):
        """Gets the headers of this Cluster.  # noqa: E501


        :return: The headers of this Cluster.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this Cluster.


        :param headers: The headers of this Cluster.  # noqa: E501
        :type: dict(str, str)
        """

        self._headers = headers

    @property
    def jwt_token(self):
        """Gets the jwt_token of this Cluster.  # noqa: E501


        :return: The jwt_token of this Cluster.  # noqa: E501
        :rtype: str
        """
        return self._jwt_token

    @jwt_token.setter
    def jwt_token(self, jwt_token):
        """Sets the jwt_token of this Cluster.


        :param jwt_token: The jwt_token of this Cluster.  # noqa: E501
        :type: str
        """

        self._jwt_token = jwt_token

    @property
    def jwt_signing_key(self):
        """Gets the jwt_signing_key of this Cluster.  # noqa: E501


        :return: The jwt_signing_key of this Cluster.  # noqa: E501
        :rtype: str
        """
        return self._jwt_signing_key

    @jwt_signing_key.setter
    def jwt_signing_key(self, jwt_signing_key):
        """Sets the jwt_signing_key of this Cluster.


        :param jwt_signing_key: The jwt_signing_key of this Cluster.  # noqa: E501
        :type: str
        """

        self._jwt_signing_key = jwt_signing_key

    @property
    def cluster_user(self):
        """Gets the cluster_user of this Cluster.  # noqa: E501


        :return: The cluster_user of this Cluster.  # noqa: E501
        :rtype: str
        """
        return self._cluster_user

    @cluster_user.setter
    def cluster_user(self, cluster_user):
        """Sets the cluster_user of this Cluster.


        :param cluster_user: The cluster_user of this Cluster.  # noqa: E501
        :type: str
        """

        self._cluster_user = cluster_user

    @property
    def access_keys(self):
        """Gets the access_keys of this Cluster.  # noqa: E501


        :return: The access_keys of this Cluster.  # noqa: E501
        :rtype: ClusterAccessKeysDef
        """
        return self._access_keys

    @access_keys.setter
    def access_keys(self, access_keys):
        """Sets the access_keys of this Cluster.


        :param access_keys: The access_keys of this Cluster.  # noqa: E501
        :type: ClusterAccessKeysDef
        """

        self._access_keys = access_keys

    @property
    def tags(self):
        """Gets the tags of this Cluster.  # noqa: E501

        Unique tags provided by user  # noqa: E501

        :return: The tags of this Cluster.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Cluster.

        Unique tags provided by user  # noqa: E501

        :param tags: The tags of this Cluster.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def description(self):
        """Gets the description of this Cluster.  # noqa: E501

        User defined description for the cluster  # noqa: E501

        :return: The description of this Cluster.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Cluster.

        User defined description for the cluster  # noqa: E501

        :param description: The description of this Cluster.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def plugin(self):
        """Gets the plugin of this Cluster.  # noqa: E501


        :return: The plugin of this Cluster.  # noqa: E501
        :rtype: str
        """
        return self._plugin

    @plugin.setter
    def plugin(self, plugin):
        """Sets the plugin of this Cluster.


        :param plugin: The plugin of this Cluster.  # noqa: E501
        :type: str
        """

        self._plugin = plugin

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
        if issubclass(Cluster, dict):
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
        if not isinstance(other, Cluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
