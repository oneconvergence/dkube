# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.3.0.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class MigrationStatus(object):
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
        'migration': 'MigrationModel',
        'jobs': 'list[MigrationJobStatus]'
    }

    attribute_map = {
        'migration': 'migration',
        'jobs': 'jobs'
    }

    def __init__(self, migration=None, jobs=None):  # noqa: E501
        """MigrationStatus - a model defined in Swagger"""  # noqa: E501

        self._migration = None
        self._jobs = None
        self.discriminator = None

        if migration is not None:
            self.migration = migration
        if jobs is not None:
            self.jobs = jobs

    @property
    def migration(self):
        """Gets the migration of this MigrationStatus.  # noqa: E501


        :return: The migration of this MigrationStatus.  # noqa: E501
        :rtype: MigrationModel
        """
        return self._migration

    @migration.setter
    def migration(self, migration):
        """Sets the migration of this MigrationStatus.


        :param migration: The migration of this MigrationStatus.  # noqa: E501
        :type: MigrationModel
        """

        self._migration = migration

    @property
    def jobs(self):
        """Gets the jobs of this MigrationStatus.  # noqa: E501


        :return: The jobs of this MigrationStatus.  # noqa: E501
        :rtype: list[MigrationJobStatus]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this MigrationStatus.


        :param jobs: The jobs of this MigrationStatus.  # noqa: E501
        :type: list[MigrationJobStatus]
        """

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
        if issubclass(MigrationStatus, dict):
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
        if not isinstance(other, MigrationStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
