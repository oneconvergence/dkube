# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.4.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GitAccessInfo(object):
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
        'path': 'str',
        'url': 'str',
        'branch': 'str',
        'credentials': 'GitAccessCredentials'
    }

    attribute_map = {
        'path': 'path',
        'url': 'url',
        'branch': 'branch',
        'credentials': 'credentials'
    }

    def __init__(self, path=None, url=None, branch=None, credentials=None):  # noqa: E501
        """GitAccessInfo - a model defined in Swagger"""  # noqa: E501

        self._path = None
        self._url = None
        self._branch = None
        self._credentials = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if url is not None:
            self.url = url
        if branch is not None:
            self.branch = branch
        if credentials is not None:
            self.credentials = credentials

    @property
    def path(self):
        """Gets the path of this GitAccessInfo.  # noqa: E501


        :return: The path of this GitAccessInfo.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this GitAccessInfo.


        :param path: The path of this GitAccessInfo.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def url(self):
        """Gets the url of this GitAccessInfo.  # noqa: E501


        :return: The url of this GitAccessInfo.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this GitAccessInfo.


        :param url: The url of this GitAccessInfo.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def branch(self):
        """Gets the branch of this GitAccessInfo.  # noqa: E501


        :return: The branch of this GitAccessInfo.  # noqa: E501
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this GitAccessInfo.


        :param branch: The branch of this GitAccessInfo.  # noqa: E501
        :type: str
        """

        self._branch = branch

    @property
    def credentials(self):
        """Gets the credentials of this GitAccessInfo.  # noqa: E501


        :return: The credentials of this GitAccessInfo.  # noqa: E501
        :rtype: GitAccessCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this GitAccessInfo.


        :param credentials: The credentials of this GitAccessInfo.  # noqa: E501
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
        if issubclass(GitAccessInfo, dict):
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
        if not isinstance(other, GitAccessInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
