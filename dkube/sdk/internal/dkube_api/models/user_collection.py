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


class UserCollection(object):
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
        'counters': 'UserCollectionCounters',
        'datasets': 'list[DatumModel]',
        'jobs': 'UserCollectionJobs',
        'models': 'list[DatumModel]',
        'programs': 'list[DatumModel]',
        'user': 'UserModel'
    }

    attribute_map = {
        'counters': 'counters',
        'datasets': 'datasets',
        'jobs': 'jobs',
        'models': 'models',
        'programs': 'programs',
        'user': 'user'
    }

    def __init__(self, counters=None, datasets=None, jobs=None, models=None, programs=None, user=None):  # noqa: E501
        """UserCollection - a model defined in Swagger"""  # noqa: E501

        self._counters = None
        self._datasets = None
        self._jobs = None
        self._models = None
        self._programs = None
        self._user = None
        self.discriminator = None

        if counters is not None:
            self.counters = counters
        if datasets is not None:
            self.datasets = datasets
        if jobs is not None:
            self.jobs = jobs
        if models is not None:
            self.models = models
        if programs is not None:
            self.programs = programs
        if user is not None:
            self.user = user

    @property
    def counters(self):
        """Gets the counters of this UserCollection.  # noqa: E501


        :return: The counters of this UserCollection.  # noqa: E501
        :rtype: UserCollectionCounters
        """
        return self._counters

    @counters.setter
    def counters(self, counters):
        """Sets the counters of this UserCollection.


        :param counters: The counters of this UserCollection.  # noqa: E501
        :type: UserCollectionCounters
        """

        self._counters = counters

    @property
    def datasets(self):
        """Gets the datasets of this UserCollection.  # noqa: E501


        :return: The datasets of this UserCollection.  # noqa: E501
        :rtype: list[DatumModel]
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets):
        """Sets the datasets of this UserCollection.


        :param datasets: The datasets of this UserCollection.  # noqa: E501
        :type: list[DatumModel]
        """

        self._datasets = datasets

    @property
    def jobs(self):
        """Gets the jobs of this UserCollection.  # noqa: E501


        :return: The jobs of this UserCollection.  # noqa: E501
        :rtype: UserCollectionJobs
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this UserCollection.


        :param jobs: The jobs of this UserCollection.  # noqa: E501
        :type: UserCollectionJobs
        """

        self._jobs = jobs

    @property
    def models(self):
        """Gets the models of this UserCollection.  # noqa: E501


        :return: The models of this UserCollection.  # noqa: E501
        :rtype: list[DatumModel]
        """
        return self._models

    @models.setter
    def models(self, models):
        """Sets the models of this UserCollection.


        :param models: The models of this UserCollection.  # noqa: E501
        :type: list[DatumModel]
        """

        self._models = models

    @property
    def programs(self):
        """Gets the programs of this UserCollection.  # noqa: E501


        :return: The programs of this UserCollection.  # noqa: E501
        :rtype: list[DatumModel]
        """
        return self._programs

    @programs.setter
    def programs(self, programs):
        """Sets the programs of this UserCollection.


        :param programs: The programs of this UserCollection.  # noqa: E501
        :type: list[DatumModel]
        """

        self._programs = programs

    @property
    def user(self):
        """Gets the user of this UserCollection.  # noqa: E501


        :return: The user of this UserCollection.  # noqa: E501
        :rtype: UserModel
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this UserCollection.


        :param user: The user of this UserCollection.  # noqa: E501
        :type: UserModel
        """

        self._user = user

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
        if issubclass(UserCollection, dict):
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
        if not isinstance(other, UserCollection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
