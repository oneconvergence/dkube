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


class MigrationDatumModel(object):
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
        'uuid': 'str',
        'remote_uuid': 'str',
        'dkube_datum_uui_ds': 'MigrationObjUUID',
        'migration_uuid': 'str',
        'migration_job_uuid': 'str',
        'duplicate': 'bool',
        'duplicate_ref': 'str',
        'datum_type': 'str',
        'bucket': 'str',
        'status': 'str',
        'progress': 'int',
        'details': 'str'
    }

    attribute_map = {
        'uuid': 'UUID',
        'remote_uuid': 'remote_UUID',
        'dkube_datum_uui_ds': 'dkubeDatumUUIDs',
        'migration_uuid': 'migrationUUID',
        'migration_job_uuid': 'migrationJobUUID',
        'duplicate': 'duplicate',
        'duplicate_ref': 'duplicate_ref',
        'datum_type': 'datum_type',
        'bucket': 'bucket',
        'status': 'status',
        'progress': 'progress',
        'details': 'details'
    }

    def __init__(self, uuid=None, remote_uuid=None, dkube_datum_uui_ds=None, migration_uuid=None, migration_job_uuid=None, duplicate=None, duplicate_ref=None, datum_type=None, bucket=None, status=None, progress=None, details=None):  # noqa: E501
        """MigrationDatumModel - a model defined in Swagger"""  # noqa: E501

        self._uuid = None
        self._remote_uuid = None
        self._dkube_datum_uui_ds = None
        self._migration_uuid = None
        self._migration_job_uuid = None
        self._duplicate = None
        self._duplicate_ref = None
        self._datum_type = None
        self._bucket = None
        self._status = None
        self._progress = None
        self._details = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if remote_uuid is not None:
            self.remote_uuid = remote_uuid
        if dkube_datum_uui_ds is not None:
            self.dkube_datum_uui_ds = dkube_datum_uui_ds
        if migration_uuid is not None:
            self.migration_uuid = migration_uuid
        if migration_job_uuid is not None:
            self.migration_job_uuid = migration_job_uuid
        if duplicate is not None:
            self.duplicate = duplicate
        if duplicate_ref is not None:
            self.duplicate_ref = duplicate_ref
        if datum_type is not None:
            self.datum_type = datum_type
        if bucket is not None:
            self.bucket = bucket
        if status is not None:
            self.status = status
        if progress is not None:
            self.progress = progress
        if details is not None:
            self.details = details

    @property
    def uuid(self):
        """Gets the uuid of this MigrationDatumModel.  # noqa: E501


        :return: The uuid of this MigrationDatumModel.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this MigrationDatumModel.


        :param uuid: The uuid of this MigrationDatumModel.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def remote_uuid(self):
        """Gets the remote_uuid of this MigrationDatumModel.  # noqa: E501


        :return: The remote_uuid of this MigrationDatumModel.  # noqa: E501
        :rtype: str
        """
        return self._remote_uuid

    @remote_uuid.setter
    def remote_uuid(self, remote_uuid):
        """Sets the remote_uuid of this MigrationDatumModel.


        :param remote_uuid: The remote_uuid of this MigrationDatumModel.  # noqa: E501
        :type: str
        """

        self._remote_uuid = remote_uuid

    @property
    def dkube_datum_uui_ds(self):
        """Gets the dkube_datum_uui_ds of this MigrationDatumModel.  # noqa: E501


        :return: The dkube_datum_uui_ds of this MigrationDatumModel.  # noqa: E501
        :rtype: MigrationObjUUID
        """
        return self._dkube_datum_uui_ds

    @dkube_datum_uui_ds.setter
    def dkube_datum_uui_ds(self, dkube_datum_uui_ds):
        """Sets the dkube_datum_uui_ds of this MigrationDatumModel.


        :param dkube_datum_uui_ds: The dkube_datum_uui_ds of this MigrationDatumModel.  # noqa: E501
        :type: MigrationObjUUID
        """

        self._dkube_datum_uui_ds = dkube_datum_uui_ds

    @property
    def migration_uuid(self):
        """Gets the migration_uuid of this MigrationDatumModel.  # noqa: E501


        :return: The migration_uuid of this MigrationDatumModel.  # noqa: E501
        :rtype: str
        """
        return self._migration_uuid

    @migration_uuid.setter
    def migration_uuid(self, migration_uuid):
        """Sets the migration_uuid of this MigrationDatumModel.


        :param migration_uuid: The migration_uuid of this MigrationDatumModel.  # noqa: E501
        :type: str
        """

        self._migration_uuid = migration_uuid

    @property
    def migration_job_uuid(self):
        """Gets the migration_job_uuid of this MigrationDatumModel.  # noqa: E501


        :return: The migration_job_uuid of this MigrationDatumModel.  # noqa: E501
        :rtype: str
        """
        return self._migration_job_uuid

    @migration_job_uuid.setter
    def migration_job_uuid(self, migration_job_uuid):
        """Sets the migration_job_uuid of this MigrationDatumModel.


        :param migration_job_uuid: The migration_job_uuid of this MigrationDatumModel.  # noqa: E501
        :type: str
        """

        self._migration_job_uuid = migration_job_uuid

    @property
    def duplicate(self):
        """Gets the duplicate of this MigrationDatumModel.  # noqa: E501


        :return: The duplicate of this MigrationDatumModel.  # noqa: E501
        :rtype: bool
        """
        return self._duplicate

    @duplicate.setter
    def duplicate(self, duplicate):
        """Sets the duplicate of this MigrationDatumModel.


        :param duplicate: The duplicate of this MigrationDatumModel.  # noqa: E501
        :type: bool
        """

        self._duplicate = duplicate

    @property
    def duplicate_ref(self):
        """Gets the duplicate_ref of this MigrationDatumModel.  # noqa: E501


        :return: The duplicate_ref of this MigrationDatumModel.  # noqa: E501
        :rtype: str
        """
        return self._duplicate_ref

    @duplicate_ref.setter
    def duplicate_ref(self, duplicate_ref):
        """Sets the duplicate_ref of this MigrationDatumModel.


        :param duplicate_ref: The duplicate_ref of this MigrationDatumModel.  # noqa: E501
        :type: str
        """

        self._duplicate_ref = duplicate_ref

    @property
    def datum_type(self):
        """Gets the datum_type of this MigrationDatumModel.  # noqa: E501


        :return: The datum_type of this MigrationDatumModel.  # noqa: E501
        :rtype: str
        """
        return self._datum_type

    @datum_type.setter
    def datum_type(self, datum_type):
        """Sets the datum_type of this MigrationDatumModel.


        :param datum_type: The datum_type of this MigrationDatumModel.  # noqa: E501
        :type: str
        """

        self._datum_type = datum_type

    @property
    def bucket(self):
        """Gets the bucket of this MigrationDatumModel.  # noqa: E501


        :return: The bucket of this MigrationDatumModel.  # noqa: E501
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this MigrationDatumModel.


        :param bucket: The bucket of this MigrationDatumModel.  # noqa: E501
        :type: str
        """

        self._bucket = bucket

    @property
    def status(self):
        """Gets the status of this MigrationDatumModel.  # noqa: E501


        :return: The status of this MigrationDatumModel.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MigrationDatumModel.


        :param status: The status of this MigrationDatumModel.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def progress(self):
        """Gets the progress of this MigrationDatumModel.  # noqa: E501


        :return: The progress of this MigrationDatumModel.  # noqa: E501
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this MigrationDatumModel.


        :param progress: The progress of this MigrationDatumModel.  # noqa: E501
        :type: int
        """

        self._progress = progress

    @property
    def details(self):
        """Gets the details of this MigrationDatumModel.  # noqa: E501


        :return: The details of this MigrationDatumModel.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this MigrationDatumModel.


        :param details: The details of this MigrationDatumModel.  # noqa: E501
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
        if issubclass(MigrationDatumModel, dict):
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
        if not isinstance(other, MigrationDatumModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
