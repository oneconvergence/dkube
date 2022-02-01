# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.1.0.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DSJobModel(object):
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
        'executor': 'DSJobModelExecutor',
        'datums': 'JobDatumModel',
        'featuresets': 'JobFeaturesetModel',
        'tags': 'list[str]',
        'hptuning': 'DSJobModelHptuning',
        'hyperparams': 'DSJobModelHyperparams',
        'nworkers': 'int',
        'ngpus': 'int',
        'rdma': 'bool',
        'gpus_override': 'bool',
        'view': 'DSJobModelView',
        'cluster': 'JobClusterModel'
    }

    attribute_map = {
        'executor': 'executor',
        'datums': 'datums',
        'featuresets': 'featuresets',
        'tags': 'tags',
        'hptuning': 'hptuning',
        'hyperparams': 'hyperparams',
        'nworkers': 'nworkers',
        'ngpus': 'ngpus',
        'rdma': 'rdma',
        'gpus_override': 'gpus_override',
        'view': 'view',
        'cluster': 'cluster'
    }

    def __init__(self, executor=None, datums=None, featuresets=None, tags=None, hptuning=None, hyperparams=None, nworkers=None, ngpus=None, rdma=True, gpus_override=True, view=None, cluster=None):  # noqa: E501
        """DSJobModel - a model defined in Swagger"""  # noqa: E501

        self._executor = None
        self._datums = None
        self._featuresets = None
        self._tags = None
        self._hptuning = None
        self._hyperparams = None
        self._nworkers = None
        self._ngpus = None
        self._rdma = None
        self._gpus_override = None
        self._view = None
        self._cluster = None
        self.discriminator = None

        if executor is not None:
            self.executor = executor
        if datums is not None:
            self.datums = datums
        if featuresets is not None:
            self.featuresets = featuresets
        if tags is not None:
            self.tags = tags
        if hptuning is not None:
            self.hptuning = hptuning
        if hyperparams is not None:
            self.hyperparams = hyperparams
        if nworkers is not None:
            self.nworkers = nworkers
        if ngpus is not None:
            self.ngpus = ngpus
        if rdma is not None:
            self.rdma = rdma
        if gpus_override is not None:
            self.gpus_override = gpus_override
        if view is not None:
            self.view = view
        if cluster is not None:
            self.cluster = cluster

    @property
    def executor(self):
        """Gets the executor of this DSJobModel.  # noqa: E501


        :return: The executor of this DSJobModel.  # noqa: E501
        :rtype: DSJobModelExecutor
        """
        return self._executor

    @executor.setter
    def executor(self, executor):
        """Sets the executor of this DSJobModel.


        :param executor: The executor of this DSJobModel.  # noqa: E501
        :type: DSJobModelExecutor
        """

        self._executor = executor

    @property
    def datums(self):
        """Gets the datums of this DSJobModel.  # noqa: E501


        :return: The datums of this DSJobModel.  # noqa: E501
        :rtype: JobDatumModel
        """
        return self._datums

    @datums.setter
    def datums(self, datums):
        """Sets the datums of this DSJobModel.


        :param datums: The datums of this DSJobModel.  # noqa: E501
        :type: JobDatumModel
        """

        self._datums = datums

    @property
    def featuresets(self):
        """Gets the featuresets of this DSJobModel.  # noqa: E501


        :return: The featuresets of this DSJobModel.  # noqa: E501
        :rtype: JobFeaturesetModel
        """
        return self._featuresets

    @featuresets.setter
    def featuresets(self, featuresets):
        """Sets the featuresets of this DSJobModel.


        :param featuresets: The featuresets of this DSJobModel.  # noqa: E501
        :type: JobFeaturesetModel
        """

        self._featuresets = featuresets

    @property
    def tags(self):
        """Gets the tags of this DSJobModel.  # noqa: E501

        Custom tags set by user for the job.  # noqa: E501

        :return: The tags of this DSJobModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DSJobModel.

        Custom tags set by user for the job.  # noqa: E501

        :param tags: The tags of this DSJobModel.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def hptuning(self):
        """Gets the hptuning of this DSJobModel.  # noqa: E501


        :return: The hptuning of this DSJobModel.  # noqa: E501
        :rtype: DSJobModelHptuning
        """
        return self._hptuning

    @hptuning.setter
    def hptuning(self, hptuning):
        """Sets the hptuning of this DSJobModel.


        :param hptuning: The hptuning of this DSJobModel.  # noqa: E501
        :type: DSJobModelHptuning
        """

        self._hptuning = hptuning

    @property
    def hyperparams(self):
        """Gets the hyperparams of this DSJobModel.  # noqa: E501


        :return: The hyperparams of this DSJobModel.  # noqa: E501
        :rtype: DSJobModelHyperparams
        """
        return self._hyperparams

    @hyperparams.setter
    def hyperparams(self, hyperparams):
        """Sets the hyperparams of this DSJobModel.


        :param hyperparams: The hyperparams of this DSJobModel.  # noqa: E501
        :type: DSJobModelHyperparams
        """

        self._hyperparams = hyperparams

    @property
    def nworkers(self):
        """Gets the nworkers of this DSJobModel.  # noqa: E501


        :return: The nworkers of this DSJobModel.  # noqa: E501
        :rtype: int
        """
        return self._nworkers

    @nworkers.setter
    def nworkers(self, nworkers):
        """Sets the nworkers of this DSJobModel.


        :param nworkers: The nworkers of this DSJobModel.  # noqa: E501
        :type: int
        """

        self._nworkers = nworkers

    @property
    def ngpus(self):
        """Gets the ngpus of this DSJobModel.  # noqa: E501


        :return: The ngpus of this DSJobModel.  # noqa: E501
        :rtype: int
        """
        return self._ngpus

    @ngpus.setter
    def ngpus(self, ngpus):
        """Sets the ngpus of this DSJobModel.


        :param ngpus: The ngpus of this DSJobModel.  # noqa: E501
        :type: int
        """

        self._ngpus = ngpus

    @property
    def rdma(self):
        """Gets the rdma of this DSJobModel.  # noqa: E501


        :return: The rdma of this DSJobModel.  # noqa: E501
        :rtype: bool
        """
        return self._rdma

    @rdma.setter
    def rdma(self, rdma):
        """Sets the rdma of this DSJobModel.


        :param rdma: The rdma of this DSJobModel.  # noqa: E501
        :type: bool
        """

        self._rdma = rdma

    @property
    def gpus_override(self):
        """Gets the gpus_override of this DSJobModel.  # noqa: E501


        :return: The gpus_override of this DSJobModel.  # noqa: E501
        :rtype: bool
        """
        return self._gpus_override

    @gpus_override.setter
    def gpus_override(self, gpus_override):
        """Sets the gpus_override of this DSJobModel.


        :param gpus_override: The gpus_override of this DSJobModel.  # noqa: E501
        :type: bool
        """

        self._gpus_override = gpus_override

    @property
    def view(self):
        """Gets the view of this DSJobModel.  # noqa: E501


        :return: The view of this DSJobModel.  # noqa: E501
        :rtype: DSJobModelView
        """
        return self._view

    @view.setter
    def view(self, view):
        """Sets the view of this DSJobModel.


        :param view: The view of this DSJobModel.  # noqa: E501
        :type: DSJobModelView
        """

        self._view = view

    @property
    def cluster(self):
        """Gets the cluster of this DSJobModel.  # noqa: E501


        :return: The cluster of this DSJobModel.  # noqa: E501
        :rtype: JobClusterModel
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this DSJobModel.


        :param cluster: The cluster of this DSJobModel.  # noqa: E501
        :type: JobClusterModel
        """

        self._cluster = cluster

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
        if issubclass(DSJobModel, dict):
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
        if not isinstance(other, DSJobModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
