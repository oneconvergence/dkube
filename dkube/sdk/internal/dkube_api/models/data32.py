# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.3.0.14
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Data32(object):
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
        'source_url': 'str',
        'source_jwt': 'str',
        'target_url': 'str',
        'target_jwt': 'str',
        'jobs': 'list[MigrationJobEntry]'
    }

    attribute_map = {
        'name': 'name',
        'source_url': 'source_url',
        'source_jwt': 'source_JWT',
        'target_url': 'target_url',
        'target_jwt': 'target_JWT',
        'jobs': 'jobs'
    }

    def __init__(self, name=None, source_url=None, source_jwt=None, target_url=None, target_jwt=None, jobs=None):  # noqa: E501
        """Data32 - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._source_url = None
        self._source_jwt = None
        self._target_url = None
        self._target_jwt = None
        self._jobs = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if source_url is not None:
            self.source_url = source_url
        if source_jwt is not None:
            self.source_jwt = source_jwt
        if target_url is not None:
            self.target_url = target_url
        if target_jwt is not None:
            self.target_jwt = target_jwt
        self.jobs = jobs

    @property
    def name(self):
        """Gets the name of this Data32.  # noqa: E501


        :return: The name of this Data32.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Data32.


        :param name: The name of this Data32.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def source_url(self):
        """Gets the source_url of this Data32.  # noqa: E501


        :return: The source_url of this Data32.  # noqa: E501
        :rtype: str
        """
        return self._source_url

    @source_url.setter
    def source_url(self, source_url):
        """Sets the source_url of this Data32.


        :param source_url: The source_url of this Data32.  # noqa: E501
        :type: str
        """

        self._source_url = source_url

    @property
    def source_jwt(self):
        """Gets the source_jwt of this Data32.  # noqa: E501


        :return: The source_jwt of this Data32.  # noqa: E501
        :rtype: str
        """
        return self._source_jwt

    @source_jwt.setter
    def source_jwt(self, source_jwt):
        """Sets the source_jwt of this Data32.


        :param source_jwt: The source_jwt of this Data32.  # noqa: E501
        :type: str
        """

        self._source_jwt = source_jwt

    @property
    def target_url(self):
        """Gets the target_url of this Data32.  # noqa: E501


        :return: The target_url of this Data32.  # noqa: E501
        :rtype: str
        """
        return self._target_url

    @target_url.setter
    def target_url(self, target_url):
        """Sets the target_url of this Data32.


        :param target_url: The target_url of this Data32.  # noqa: E501
        :type: str
        """

        self._target_url = target_url

    @property
    def target_jwt(self):
        """Gets the target_jwt of this Data32.  # noqa: E501


        :return: The target_jwt of this Data32.  # noqa: E501
        :rtype: str
        """
        return self._target_jwt

    @target_jwt.setter
    def target_jwt(self, target_jwt):
        """Sets the target_jwt of this Data32.


        :param target_jwt: The target_jwt of this Data32.  # noqa: E501
        :type: str
        """

        self._target_jwt = target_jwt

    @property
    def jobs(self):
        """Gets the jobs of this Data32.  # noqa: E501


        :return: The jobs of this Data32.  # noqa: E501
        :rtype: list[MigrationJobEntry]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this Data32.


        :param jobs: The jobs of this Data32.  # noqa: E501
        :type: list[MigrationJobEntry]
        """
        if jobs is None:
            raise ValueError("Invalid value for `jobs`, must not be `None`")  # noqa: E501

        self._jobs = jobs

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
        if issubclass(Data32, dict):
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
        if not isinstance(other, Data32):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
