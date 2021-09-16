# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.3.0.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class FeatureSetCommitDef(object):
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
        'job_uuid': 'str',
        'description': 'str',
        'tags': 'list[str]',
        'featureset': 'str',
        'path': 'str',
        'job': 'FeatureSetCommitDefJob'
    }

    attribute_map = {
        'job_uuid': 'job_uuid',
        'description': 'description',
        'tags': 'tags',
        'featureset': 'featureset',
        'path': 'Path',
        'job': 'job'
    }

    def __init__(self, job_uuid=None, description=None, tags=None, featureset=None, path=None, job=None):  # noqa: E501
        """FeatureSetCommitDef - a model defined in Swagger"""  # noqa: E501

        self._job_uuid = None
        self._description = None
        self._tags = None
        self._featureset = None
        self._path = None
        self._job = None
        self.discriminator = None

        self.job_uuid = job_uuid
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if featureset is not None:
            self.featureset = featureset
        if path is not None:
            self.path = path
        if job is not None:
            self.job = job

    @property
    def job_uuid(self):
        """Gets the job_uuid of this FeatureSetCommitDef.  # noqa: E501

        job uuid. This is available as env parameter  # noqa: E501

        :return: The job_uuid of this FeatureSetCommitDef.  # noqa: E501
        :rtype: str
        """
        return self._job_uuid

    @job_uuid.setter
    def job_uuid(self, job_uuid):
        """Sets the job_uuid of this FeatureSetCommitDef.

        job uuid. This is available as env parameter  # noqa: E501

        :param job_uuid: The job_uuid of this FeatureSetCommitDef.  # noqa: E501
        :type: str
        """
        if job_uuid is None:
            raise ValueError("Invalid value for `job_uuid`, must not be `None`")  # noqa: E501

        self._job_uuid = job_uuid

    @property
    def description(self):
        """Gets the description of this FeatureSetCommitDef.  # noqa: E501

        description for the version created  # noqa: E501

        :return: The description of this FeatureSetCommitDef.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FeatureSetCommitDef.

        description for the version created  # noqa: E501

        :param description: The description of this FeatureSetCommitDef.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 255:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501
        if description is not None and len(description) < 1:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this FeatureSetCommitDef.  # noqa: E501

        User specified custom tags for the version  # noqa: E501

        :return: The tags of this FeatureSetCommitDef.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this FeatureSetCommitDef.

        User specified custom tags for the version  # noqa: E501

        :param tags: The tags of this FeatureSetCommitDef.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def featureset(self):
        """Gets the featureset of this FeatureSetCommitDef.  # noqa: E501

        Name of the featureset  # noqa: E501

        :return: The featureset of this FeatureSetCommitDef.  # noqa: E501
        :rtype: str
        """
        return self._featureset

    @featureset.setter
    def featureset(self, featureset):
        """Sets the featureset of this FeatureSetCommitDef.

        Name of the featureset  # noqa: E501

        :param featureset: The featureset of this FeatureSetCommitDef.  # noqa: E501
        :type: str
        """

        self._featureset = featureset

    @property
    def path(self):
        """Gets the path of this FeatureSetCommitDef.  # noqa: E501

        path where featureset is mounted.  # noqa: E501

        :return: The path of this FeatureSetCommitDef.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this FeatureSetCommitDef.

        path where featureset is mounted.  # noqa: E501

        :param path: The path of this FeatureSetCommitDef.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def job(self):
        """Gets the job of this FeatureSetCommitDef.  # noqa: E501


        :return: The job of this FeatureSetCommitDef.  # noqa: E501
        :rtype: FeatureSetCommitDefJob
        """
        return self._job

    @job.setter
    def job(self, job):
        """Sets the job of this FeatureSetCommitDef.


        :param job: The job of this FeatureSetCommitDef.  # noqa: E501
        :type: FeatureSetCommitDefJob
        """

        self._job = job

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
        if issubclass(FeatureSetCommitDef, dict):
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
        if not isinstance(other, FeatureSetCommitDef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
