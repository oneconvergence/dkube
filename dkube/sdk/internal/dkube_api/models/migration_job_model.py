# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.3.0.10
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class MigrationJobModel(object):
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
        '_class': 'str',
        'uuid': 'str',
        'remote_uuid': 'str',
        'src_state': 'str',
        'dkube_job_uuids': 'MigrationObjUUID',
        'migration_uuid': 'str',
        'status': 'str',
        'progress': 'int',
        'datums': 'list[str]',
        'details': 'str'
    }

    attribute_map = {
        'name': 'name',
        '_class': 'class',
        'uuid': 'UUID',
        'remote_uuid': 'remote_UUID',
        'src_state': 'src_state',
        'dkube_job_uuids': 'dkubeJobUUIDS',
        'migration_uuid': 'migrationUUID',
        'status': 'status',
        'progress': 'progress',
        'datums': 'datums',
        'details': 'details'
    }

    def __init__(self, name=None, _class=None, uuid=None, remote_uuid=None, src_state=None, dkube_job_uuids=None, migration_uuid=None, status=None, progress=None, datums=None, details=None):  # noqa: E501
        """MigrationJobModel - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self.__class = None
        self._uuid = None
        self._remote_uuid = None
        self._src_state = None
        self._dkube_job_uuids = None
        self._migration_uuid = None
        self._status = None
        self._progress = None
        self._datums = None
        self._details = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if _class is not None:
            self._class = _class
        if uuid is not None:
            self.uuid = uuid
        if remote_uuid is not None:
            self.remote_uuid = remote_uuid
        if src_state is not None:
            self.src_state = src_state
        if dkube_job_uuids is not None:
            self.dkube_job_uuids = dkube_job_uuids
        if migration_uuid is not None:
            self.migration_uuid = migration_uuid
        if status is not None:
            self.status = status
        if progress is not None:
            self.progress = progress
        if datums is not None:
            self.datums = datums
        if details is not None:
            self.details = details

    @property
    def name(self):
        """Gets the name of this MigrationJobModel.  # noqa: E501


        :return: The name of this MigrationJobModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MigrationJobModel.


        :param name: The name of this MigrationJobModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def _class(self):
        """Gets the _class of this MigrationJobModel.  # noqa: E501


        :return: The _class of this MigrationJobModel.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this MigrationJobModel.


        :param _class: The _class of this MigrationJobModel.  # noqa: E501
        :type: str
        """

        self.__class = _class

    @property
    def uuid(self):
        """Gets the uuid of this MigrationJobModel.  # noqa: E501


        :return: The uuid of this MigrationJobModel.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this MigrationJobModel.


        :param uuid: The uuid of this MigrationJobModel.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def remote_uuid(self):
        """Gets the remote_uuid of this MigrationJobModel.  # noqa: E501


        :return: The remote_uuid of this MigrationJobModel.  # noqa: E501
        :rtype: str
        """
        return self._remote_uuid

    @remote_uuid.setter
    def remote_uuid(self, remote_uuid):
        """Sets the remote_uuid of this MigrationJobModel.


        :param remote_uuid: The remote_uuid of this MigrationJobModel.  # noqa: E501
        :type: str
        """

        self._remote_uuid = remote_uuid

    @property
    def src_state(self):
        """Gets the src_state of this MigrationJobModel.  # noqa: E501


        :return: The src_state of this MigrationJobModel.  # noqa: E501
        :rtype: str
        """
        return self._src_state

    @src_state.setter
    def src_state(self, src_state):
        """Sets the src_state of this MigrationJobModel.


        :param src_state: The src_state of this MigrationJobModel.  # noqa: E501
        :type: str
        """

        self._src_state = src_state

    @property
    def dkube_job_uuids(self):
        """Gets the dkube_job_uuids of this MigrationJobModel.  # noqa: E501


        :return: The dkube_job_uuids of this MigrationJobModel.  # noqa: E501
        :rtype: MigrationObjUUID
        """
        return self._dkube_job_uuids

    @dkube_job_uuids.setter
    def dkube_job_uuids(self, dkube_job_uuids):
        """Sets the dkube_job_uuids of this MigrationJobModel.


        :param dkube_job_uuids: The dkube_job_uuids of this MigrationJobModel.  # noqa: E501
        :type: MigrationObjUUID
        """

        self._dkube_job_uuids = dkube_job_uuids

    @property
    def migration_uuid(self):
        """Gets the migration_uuid of this MigrationJobModel.  # noqa: E501


        :return: The migration_uuid of this MigrationJobModel.  # noqa: E501
        :rtype: str
        """
        return self._migration_uuid

    @migration_uuid.setter
    def migration_uuid(self, migration_uuid):
        """Sets the migration_uuid of this MigrationJobModel.


        :param migration_uuid: The migration_uuid of this MigrationJobModel.  # noqa: E501
        :type: str
        """

        self._migration_uuid = migration_uuid

    @property
    def status(self):
        """Gets the status of this MigrationJobModel.  # noqa: E501


        :return: The status of this MigrationJobModel.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MigrationJobModel.


        :param status: The status of this MigrationJobModel.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def progress(self):
        """Gets the progress of this MigrationJobModel.  # noqa: E501


        :return: The progress of this MigrationJobModel.  # noqa: E501
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this MigrationJobModel.


        :param progress: The progress of this MigrationJobModel.  # noqa: E501
        :type: int
        """

        self._progress = progress

    @property
    def datums(self):
        """Gets the datums of this MigrationJobModel.  # noqa: E501


        :return: The datums of this MigrationJobModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._datums

    @datums.setter
    def datums(self, datums):
        """Sets the datums of this MigrationJobModel.


        :param datums: The datums of this MigrationJobModel.  # noqa: E501
        :type: list[str]
        """

        self._datums = datums

    @property
    def details(self):
        """Gets the details of this MigrationJobModel.  # noqa: E501


        :return: The details of this MigrationJobModel.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this MigrationJobModel.


        :param details: The details of this MigrationJobModel.  # noqa: E501
        :type: str
        """

        self._details = details

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
        if issubclass(MigrationJobModel, dict):
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
        if not isinstance(other, MigrationJobModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
