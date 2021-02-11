# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.2.1.11
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PreprocessingJobModel(object):
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
        'kind': 'str',
        'executor': 'PreprocessingJobModelExecutor',
        'datums': 'JobDatumModel',
        'featuresets': 'JobFeaturesetModel',
        'tags': 'list[str]',
        'config': 'JobConfigModel',
        'cluster': 'JobClusterModel',
        'ngpus': 'int',
        'gpus_override': 'bool'
    }

    attribute_map = {
        'kind': 'kind',
        'executor': 'executor',
        'datums': 'datums',
        'featuresets': 'featuresets',
        'tags': 'tags',
        'config': 'config',
        'cluster': 'cluster',
        'ngpus': 'ngpus',
        'gpus_override': 'gpus_override'
    }

    def __init__(self, kind=None, executor=None, datums=None, featuresets=None, tags=None, config=None, cluster=None, ngpus=None, gpus_override=True):  # noqa: E501
        """PreprocessingJobModel - a model defined in Swagger"""  # noqa: E501

        self._kind = None
        self._executor = None
        self._datums = None
        self._featuresets = None
        self._tags = None
        self._config = None
        self._cluster = None
        self._ngpus = None
        self._gpus_override = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if executor is not None:
            self.executor = executor
        if datums is not None:
            self.datums = datums
        if featuresets is not None:
            self.featuresets = featuresets
        if tags is not None:
            self.tags = tags
        if config is not None:
            self.config = config
        if cluster is not None:
            self.cluster = cluster
        if ngpus is not None:
            self.ngpus = ngpus
        if gpus_override is not None:
            self.gpus_override = gpus_override

    @property
    def kind(self):
        """Gets the kind of this PreprocessingJobModel.  # noqa: E501


        :return: The kind of this PreprocessingJobModel.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this PreprocessingJobModel.


        :param kind: The kind of this PreprocessingJobModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["preprocessing", "ingestion"]  # noqa: E501
        if kind not in allowed_values:
            raise ValueError(
                "Invalid value for `kind` ({0}), must be one of {1}"  # noqa: E501
                .format(kind, allowed_values)
            )

        self._kind = kind

    @property
    def executor(self):
        """Gets the executor of this PreprocessingJobModel.  # noqa: E501


        :return: The executor of this PreprocessingJobModel.  # noqa: E501
        :rtype: PreprocessingJobModelExecutor
        """
        return self._executor

    @executor.setter
    def executor(self, executor):
        """Sets the executor of this PreprocessingJobModel.


        :param executor: The executor of this PreprocessingJobModel.  # noqa: E501
        :type: PreprocessingJobModelExecutor
        """

        self._executor = executor

    @property
    def datums(self):
        """Gets the datums of this PreprocessingJobModel.  # noqa: E501


        :return: The datums of this PreprocessingJobModel.  # noqa: E501
        :rtype: JobDatumModel
        """
        return self._datums

    @datums.setter
    def datums(self, datums):
        """Sets the datums of this PreprocessingJobModel.


        :param datums: The datums of this PreprocessingJobModel.  # noqa: E501
        :type: JobDatumModel
        """

        self._datums = datums

    @property
    def featuresets(self):
        """Gets the featuresets of this PreprocessingJobModel.  # noqa: E501


        :return: The featuresets of this PreprocessingJobModel.  # noqa: E501
        :rtype: JobFeaturesetModel
        """
        return self._featuresets

    @featuresets.setter
    def featuresets(self, featuresets):
        """Sets the featuresets of this PreprocessingJobModel.


        :param featuresets: The featuresets of this PreprocessingJobModel.  # noqa: E501
        :type: JobFeaturesetModel
        """

        self._featuresets = featuresets

    @property
    def tags(self):
        """Gets the tags of this PreprocessingJobModel.  # noqa: E501

        Custom tags set by user for the job.  # noqa: E501

        :return: The tags of this PreprocessingJobModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this PreprocessingJobModel.

        Custom tags set by user for the job.  # noqa: E501

        :param tags: The tags of this PreprocessingJobModel.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def config(self):
        """Gets the config of this PreprocessingJobModel.  # noqa: E501


        :return: The config of this PreprocessingJobModel.  # noqa: E501
        :rtype: JobConfigModel
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this PreprocessingJobModel.


        :param config: The config of this PreprocessingJobModel.  # noqa: E501
        :type: JobConfigModel
        """

        self._config = config

    @property
    def cluster(self):
        """Gets the cluster of this PreprocessingJobModel.  # noqa: E501


        :return: The cluster of this PreprocessingJobModel.  # noqa: E501
        :rtype: JobClusterModel
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this PreprocessingJobModel.


        :param cluster: The cluster of this PreprocessingJobModel.  # noqa: E501
        :type: JobClusterModel
        """

        self._cluster = cluster

    @property
    def ngpus(self):
        """Gets the ngpus of this PreprocessingJobModel.  # noqa: E501


        :return: The ngpus of this PreprocessingJobModel.  # noqa: E501
        :rtype: int
        """
        return self._ngpus

    @ngpus.setter
    def ngpus(self, ngpus):
        """Sets the ngpus of this PreprocessingJobModel.


        :param ngpus: The ngpus of this PreprocessingJobModel.  # noqa: E501
        :type: int
        """

        self._ngpus = ngpus

    @property
    def gpus_override(self):
        """Gets the gpus_override of this PreprocessingJobModel.  # noqa: E501


        :return: The gpus_override of this PreprocessingJobModel.  # noqa: E501
        :rtype: bool
        """
        return self._gpus_override

    @gpus_override.setter
    def gpus_override(self, gpus_override):
        """Sets the gpus_override of this PreprocessingJobModel.


        :param gpus_override: The gpus_override of this PreprocessingJobModel.  # noqa: E501
        :type: bool
        """

        self._gpus_override = gpus_override

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
        if issubclass(PreprocessingJobModel, dict):
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
        if not isinstance(other, PreprocessingJobModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
