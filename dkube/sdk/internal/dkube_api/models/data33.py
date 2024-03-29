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


class Data33(object):
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
        'image': 'str',
        'private': 'bool',
        'username': 'str',
        'password': 'str',
        'project': 'str',
        'description': 'str',
        'tags': 'list[str]',
        'registry': 'str',
        'digest': 'str',
        'repo': 'str'
    }

    attribute_map = {
        'name': 'name',
        'image': 'image',
        'private': 'private',
        'username': 'username',
        'password': 'password',
        'project': 'project',
        'description': 'description',
        'tags': 'tags',
        'registry': 'registry',
        'digest': 'digest',
        'repo': 'repo'
    }

    def __init__(self, name=None, image=None, private=False, username=None, password=None, project=None, description=None, tags=None, registry=None, digest=None, repo=None):  # noqa: E501
        """Data33 - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._image = None
        self._private = None
        self._username = None
        self._password = None
        self._project = None
        self._description = None
        self._tags = None
        self._registry = None
        self._digest = None
        self._repo = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if image is not None:
            self.image = image
        if private is not None:
            self.private = private
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if project is not None:
            self.project = project
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if registry is not None:
            self.registry = registry
        if digest is not None:
            self.digest = digest
        if repo is not None:
            self.repo = repo

    @property
    def name(self):
        """Gets the name of this Data33.  # noqa: E501


        :return: The name of this Data33.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Data33.


        :param name: The name of this Data33.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def image(self):
        """Gets the image of this Data33.  # noqa: E501


        :return: The image of this Data33.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this Data33.


        :param image: The image of this Data33.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def private(self):
        """Gets the private of this Data33.  # noqa: E501


        :return: The private of this Data33.  # noqa: E501
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this Data33.


        :param private: The private of this Data33.  # noqa: E501
        :type: bool
        """

        self._private = private

    @property
    def username(self):
        """Gets the username of this Data33.  # noqa: E501


        :return: The username of this Data33.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Data33.


        :param username: The username of this Data33.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this Data33.  # noqa: E501


        :return: The password of this Data33.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this Data33.


        :param password: The password of this Data33.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def project(self):
        """Gets the project of this Data33.  # noqa: E501


        :return: The project of this Data33.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this Data33.


        :param project: The project of this Data33.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def description(self):
        """Gets the description of this Data33.  # noqa: E501


        :return: The description of this Data33.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Data33.


        :param description: The description of this Data33.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this Data33.  # noqa: E501


        :return: The tags of this Data33.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Data33.


        :param tags: The tags of this Data33.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def registry(self):
        """Gets the registry of this Data33.  # noqa: E501


        :return: The registry of this Data33.  # noqa: E501
        :rtype: str
        """
        return self._registry

    @registry.setter
    def registry(self, registry):
        """Sets the registry of this Data33.


        :param registry: The registry of this Data33.  # noqa: E501
        :type: str
        """

        self._registry = registry

    @property
    def digest(self):
        """Gets the digest of this Data33.  # noqa: E501


        :return: The digest of this Data33.  # noqa: E501
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        """Sets the digest of this Data33.


        :param digest: The digest of this Data33.  # noqa: E501
        :type: str
        """

        self._digest = digest

    @property
    def repo(self):
        """Gets the repo of this Data33.  # noqa: E501


        :return: The repo of this Data33.  # noqa: E501
        :rtype: str
        """
        return self._repo

    @repo.setter
    def repo(self, repo):
        """Sets the repo of this Data33.


        :param repo: The repo of this Data33.  # noqa: E501
        :type: str
        """

        self._repo = repo

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
        if issubclass(Data33, dict):
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
        if not isinstance(other, Data33):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
