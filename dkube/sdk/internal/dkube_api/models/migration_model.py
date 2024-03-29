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


class MigrationModel(object):
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
        'version': 'str',
        'name': 'str',
        'uuid': 'str',
        'remote_uuid': 'str',
        'user': 'str',
        'triggering_point': 'str',
        'location': 'str',
        'remote': 'MigrationModelRemote',
        'progress': 'int',
        'status': 'MigrationStatusModel',
        'time_stamp': 'str',
        'jobs': 'list[MigrationJobEntry]',
        'job_refs': 'list[str]'
    }

    attribute_map = {
        'version': 'version',
        'name': 'name',
        'uuid': 'UUID',
        'remote_uuid': 'remote_UUID',
        'user': 'User',
        'triggering_point': 'triggering_point',
        'location': 'location',
        'remote': 'remote',
        'progress': 'progress',
        'status': 'status',
        'time_stamp': 'time_stamp',
        'jobs': 'jobs',
        'job_refs': 'job_refs'
    }

    def __init__(self, version=None, name=None, uuid=None, remote_uuid=None, user=None, triggering_point=None, location=None, remote=None, progress=None, status=None, time_stamp=None, jobs=None, job_refs=None):  # noqa: E501
        """MigrationModel - a model defined in Swagger"""  # noqa: E501

        self._version = None
        self._name = None
        self._uuid = None
        self._remote_uuid = None
        self._user = None
        self._triggering_point = None
        self._location = None
        self._remote = None
        self._progress = None
        self._status = None
        self._time_stamp = None
        self._jobs = None
        self._job_refs = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if name is not None:
            self.name = name
        if uuid is not None:
            self.uuid = uuid
        if remote_uuid is not None:
            self.remote_uuid = remote_uuid
        if user is not None:
            self.user = user
        if triggering_point is not None:
            self.triggering_point = triggering_point
        if location is not None:
            self.location = location
        if remote is not None:
            self.remote = remote
        if progress is not None:
            self.progress = progress
        if status is not None:
            self.status = status
        if time_stamp is not None:
            self.time_stamp = time_stamp
        if jobs is not None:
            self.jobs = jobs
        if job_refs is not None:
            self.job_refs = job_refs

    @property
    def version(self):
        """Gets the version of this MigrationModel.  # noqa: E501


        :return: The version of this MigrationModel.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this MigrationModel.


        :param version: The version of this MigrationModel.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def name(self):
        """Gets the name of this MigrationModel.  # noqa: E501


        :return: The name of this MigrationModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MigrationModel.


        :param name: The name of this MigrationModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def uuid(self):
        """Gets the uuid of this MigrationModel.  # noqa: E501


        :return: The uuid of this MigrationModel.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this MigrationModel.


        :param uuid: The uuid of this MigrationModel.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def remote_uuid(self):
        """Gets the remote_uuid of this MigrationModel.  # noqa: E501


        :return: The remote_uuid of this MigrationModel.  # noqa: E501
        :rtype: str
        """
        return self._remote_uuid

    @remote_uuid.setter
    def remote_uuid(self, remote_uuid):
        """Sets the remote_uuid of this MigrationModel.


        :param remote_uuid: The remote_uuid of this MigrationModel.  # noqa: E501
        :type: str
        """

        self._remote_uuid = remote_uuid

    @property
    def user(self):
        """Gets the user of this MigrationModel.  # noqa: E501


        :return: The user of this MigrationModel.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this MigrationModel.


        :param user: The user of this MigrationModel.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def triggering_point(self):
        """Gets the triggering_point of this MigrationModel.  # noqa: E501


        :return: The triggering_point of this MigrationModel.  # noqa: E501
        :rtype: str
        """
        return self._triggering_point

    @triggering_point.setter
    def triggering_point(self, triggering_point):
        """Sets the triggering_point of this MigrationModel.


        :param triggering_point: The triggering_point of this MigrationModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["source", "target"]  # noqa: E501
        if triggering_point not in allowed_values:
            raise ValueError(
                "Invalid value for `triggering_point` ({0}), must be one of {1}"  # noqa: E501
                .format(triggering_point, allowed_values)
            )

        self._triggering_point = triggering_point

    @property
    def location(self):
        """Gets the location of this MigrationModel.  # noqa: E501


        :return: The location of this MigrationModel.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this MigrationModel.


        :param location: The location of this MigrationModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["source", "target"]  # noqa: E501
        if location not in allowed_values:
            raise ValueError(
                "Invalid value for `location` ({0}), must be one of {1}"  # noqa: E501
                .format(location, allowed_values)
            )

        self._location = location

    @property
    def remote(self):
        """Gets the remote of this MigrationModel.  # noqa: E501


        :return: The remote of this MigrationModel.  # noqa: E501
        :rtype: MigrationModelRemote
        """
        return self._remote

    @remote.setter
    def remote(self, remote):
        """Sets the remote of this MigrationModel.


        :param remote: The remote of this MigrationModel.  # noqa: E501
        :type: MigrationModelRemote
        """

        self._remote = remote

    @property
    def progress(self):
        """Gets the progress of this MigrationModel.  # noqa: E501


        :return: The progress of this MigrationModel.  # noqa: E501
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this MigrationModel.


        :param progress: The progress of this MigrationModel.  # noqa: E501
        :type: int
        """

        self._progress = progress

    @property
    def status(self):
        """Gets the status of this MigrationModel.  # noqa: E501


        :return: The status of this MigrationModel.  # noqa: E501
        :rtype: MigrationStatusModel
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MigrationModel.


        :param status: The status of this MigrationModel.  # noqa: E501
        :type: MigrationStatusModel
        """

        self._status = status

    @property
    def time_stamp(self):
        """Gets the time_stamp of this MigrationModel.  # noqa: E501


        :return: The time_stamp of this MigrationModel.  # noqa: E501
        :rtype: str
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """Sets the time_stamp of this MigrationModel.


        :param time_stamp: The time_stamp of this MigrationModel.  # noqa: E501
        :type: str
        """

        self._time_stamp = time_stamp

    @property
    def jobs(self):
        """Gets the jobs of this MigrationModel.  # noqa: E501


        :return: The jobs of this MigrationModel.  # noqa: E501
        :rtype: list[MigrationJobEntry]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this MigrationModel.


        :param jobs: The jobs of this MigrationModel.  # noqa: E501
        :type: list[MigrationJobEntry]
        """

        self._jobs = jobs

    @property
    def job_refs(self):
        """Gets the job_refs of this MigrationModel.  # noqa: E501


        :return: The job_refs of this MigrationModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._job_refs

    @job_refs.setter
    def job_refs(self, job_refs):
        """Sets the job_refs of this MigrationModel.


        :param job_refs: The job_refs of this MigrationModel.  # noqa: E501
        :type: list[str]
        """

        self._job_refs = job_refs

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
        if issubclass(MigrationModel, dict):
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
        if not isinstance(other, MigrationModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
