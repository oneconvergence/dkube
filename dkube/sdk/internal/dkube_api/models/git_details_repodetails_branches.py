# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.3.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GitDetailsRepodetailsBranches(object):
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
        'commits': 'list[GitCommitDetails]'
    }

    attribute_map = {
        'name': 'name',
        'commits': 'commits'
    }

    def __init__(self, name=None, commits=None):  # noqa: E501
        """GitDetailsRepodetailsBranches - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._commits = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if commits is not None:
            self.commits = commits

    @property
    def name(self):
        """Gets the name of this GitDetailsRepodetailsBranches.  # noqa: E501


        :return: The name of this GitDetailsRepodetailsBranches.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GitDetailsRepodetailsBranches.


        :param name: The name of this GitDetailsRepodetailsBranches.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def commits(self):
        """Gets the commits of this GitDetailsRepodetailsBranches.  # noqa: E501


        :return: The commits of this GitDetailsRepodetailsBranches.  # noqa: E501
        :rtype: list[GitCommitDetails]
        """
        return self._commits

    @commits.setter
    def commits(self, commits):
        """Sets the commits of this GitDetailsRepodetailsBranches.


        :param commits: The commits of this GitDetailsRepodetailsBranches.  # noqa: E501
        :type: list[GitCommitDetails]
        """

        self._commits = commits

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
        if issubclass(GitDetailsRepodetailsBranches, dict):
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
        if not isinstance(other, GitDetailsRepodetailsBranches):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
