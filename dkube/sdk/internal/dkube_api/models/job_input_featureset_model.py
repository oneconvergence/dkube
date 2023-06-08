# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.8.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class JobInputFeaturesetModel(object):
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
        'version': 'str',
        'owner': 'str',
        'mountpath': 'str',
        'version_name': 'str',
        'job_added': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'version': 'version',
        'owner': 'owner',
        'mountpath': 'mountpath',
        'version_name': 'version_name',
        'job_added': 'job_added'
    }

    def __init__(self, name=None, version=None, owner=None, mountpath=None, version_name=None, job_added=False):  # noqa: E501
        """JobInputFeaturesetModel - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._version = None
        self._owner = None
        self._mountpath = None
        self._version_name = None
        self._job_added = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if owner is not None:
            self.owner = owner
        if mountpath is not None:
            self.mountpath = mountpath
        if version_name is not None:
            self.version_name = version_name
        if job_added is not None:
            self.job_added = job_added

    @property
    def name(self):
        """Gets the name of this JobInputFeaturesetModel.  # noqa: E501


        :return: The name of this JobInputFeaturesetModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobInputFeaturesetModel.


        :param name: The name of this JobInputFeaturesetModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def version(self):
        """Gets the version of this JobInputFeaturesetModel.  # noqa: E501


        :return: The version of this JobInputFeaturesetModel.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this JobInputFeaturesetModel.


        :param version: The version of this JobInputFeaturesetModel.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def owner(self):
        """Gets the owner of this JobInputFeaturesetModel.  # noqa: E501


        :return: The owner of this JobInputFeaturesetModel.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this JobInputFeaturesetModel.


        :param owner: The owner of this JobInputFeaturesetModel.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def mountpath(self):
        """Gets the mountpath of this JobInputFeaturesetModel.  # noqa: E501


        :return: The mountpath of this JobInputFeaturesetModel.  # noqa: E501
        :rtype: str
        """
        return self._mountpath

    @mountpath.setter
    def mountpath(self, mountpath):
        """Sets the mountpath of this JobInputFeaturesetModel.


        :param mountpath: The mountpath of this JobInputFeaturesetModel.  # noqa: E501
        :type: str
        """

        self._mountpath = mountpath

    @property
    def version_name(self):
        """Gets the version_name of this JobInputFeaturesetModel.  # noqa: E501


        :return: The version_name of this JobInputFeaturesetModel.  # noqa: E501
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        """Sets the version_name of this JobInputFeaturesetModel.


        :param version_name: The version_name of this JobInputFeaturesetModel.  # noqa: E501
        :type: str
        """

        self._version_name = version_name

    @property
    def job_added(self):
        """Gets the job_added of this JobInputFeaturesetModel.  # noqa: E501


        :return: The job_added of this JobInputFeaturesetModel.  # noqa: E501
        :rtype: bool
        """
        return self._job_added

    @job_added.setter
    def job_added(self, job_added):
        """Sets the job_added of this JobInputFeaturesetModel.


        :param job_added: The job_added of this JobInputFeaturesetModel.  # noqa: E501
        :type: bool
        """

        self._job_added = job_added

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
        if issubclass(JobInputFeaturesetModel, dict):
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
        if not isinstance(other, JobInputFeaturesetModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
