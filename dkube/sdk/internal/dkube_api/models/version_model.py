# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.3.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class VersionModel(object):
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
        'uuid': 'str',
        'tags': 'list[str]',
        'description': 'str',
        'index': 'int',
        'timestamps': 'TimeStamps',
        'sync_state': 'str',
        'storage_path': 'str',
        'user': 'str',
        'datum_name': 'str',
        'datum_uuid': 'str',
        'run_uuid': 'str',
        'tracking_uuid': 'str',
        'commit_id': 'str',
        'size': 'str',
        'datum_type': 'str',
        'model': 'VersionModelModel'
    }

    attribute_map = {
        'name': 'name',
        'uuid': 'uuid',
        'tags': 'tags',
        'description': 'description',
        'index': 'index',
        'timestamps': 'timestamps',
        'sync_state': 'syncState',
        'storage_path': 'storagePath',
        'user': 'user',
        'datum_name': 'datumName',
        'datum_uuid': 'datumUUID',
        'run_uuid': 'runUUID',
        'tracking_uuid': 'trackingUUID',
        'commit_id': 'commitID',
        'size': 'size',
        'datum_type': 'datumType',
        'model': 'model'
    }

    def __init__(self, name=None, uuid=None, tags=None, description=None, index=None, timestamps=None, sync_state=None, storage_path=None, user=None, datum_name=None, datum_uuid=None, run_uuid=None, tracking_uuid=None, commit_id=None, size=None, datum_type=None, model=None):  # noqa: E501
        """VersionModel - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._uuid = None
        self._tags = None
        self._description = None
        self._index = None
        self._timestamps = None
        self._sync_state = None
        self._storage_path = None
        self._user = None
        self._datum_name = None
        self._datum_uuid = None
        self._run_uuid = None
        self._tracking_uuid = None
        self._commit_id = None
        self._size = None
        self._datum_type = None
        self._model = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if uuid is not None:
            self.uuid = uuid
        if tags is not None:
            self.tags = tags
        if description is not None:
            self.description = description
        if index is not None:
            self.index = index
        if timestamps is not None:
            self.timestamps = timestamps
        if sync_state is not None:
            self.sync_state = sync_state
        if storage_path is not None:
            self.storage_path = storage_path
        if user is not None:
            self.user = user
        if datum_name is not None:
            self.datum_name = datum_name
        if datum_uuid is not None:
            self.datum_uuid = datum_uuid
        if run_uuid is not None:
            self.run_uuid = run_uuid
        if tracking_uuid is not None:
            self.tracking_uuid = tracking_uuid
        if commit_id is not None:
            self.commit_id = commit_id
        if size is not None:
            self.size = size
        if datum_type is not None:
            self.datum_type = datum_type
        if model is not None:
            self.model = model

    @property
    def name(self):
        """Gets the name of this VersionModel.  # noqa: E501

        Name of the version given by user  # noqa: E501

        :return: The name of this VersionModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VersionModel.

        Name of the version given by user  # noqa: E501

        :param name: The name of this VersionModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def uuid(self):
        """Gets the uuid of this VersionModel.  # noqa: E501

        Unique id generated by system (timestamp in milliseconds)  # noqa: E501

        :return: The uuid of this VersionModel.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this VersionModel.

        Unique id generated by system (timestamp in milliseconds)  # noqa: E501

        :param uuid: The uuid of this VersionModel.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def tags(self):
        """Gets the tags of this VersionModel.  # noqa: E501

        Unique tags provided by user  # noqa: E501

        :return: The tags of this VersionModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this VersionModel.

        Unique tags provided by user  # noqa: E501

        :param tags: The tags of this VersionModel.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def description(self):
        """Gets the description of this VersionModel.  # noqa: E501

        User defined description for the version  # noqa: E501

        :return: The description of this VersionModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VersionModel.

        User defined description for the version  # noqa: E501

        :param description: The description of this VersionModel.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def index(self):
        """Gets the index of this VersionModel.  # noqa: E501

        Incremental index to sort  # noqa: E501

        :return: The index of this VersionModel.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this VersionModel.

        Incremental index to sort  # noqa: E501

        :param index: The index of this VersionModel.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def timestamps(self):
        """Gets the timestamps of this VersionModel.  # noqa: E501


        :return: The timestamps of this VersionModel.  # noqa: E501
        :rtype: TimeStamps
        """
        return self._timestamps

    @timestamps.setter
    def timestamps(self, timestamps):
        """Sets the timestamps of this VersionModel.


        :param timestamps: The timestamps of this VersionModel.  # noqa: E501
        :type: TimeStamps
        """

        self._timestamps = timestamps

    @property
    def sync_state(self):
        """Gets the sync_state of this VersionModel.  # noqa: E501

        State of syncing data from cache to remote  # noqa: E501

        :return: The sync_state of this VersionModel.  # noqa: E501
        :rtype: str
        """
        return self._sync_state

    @sync_state.setter
    def sync_state(self, sync_state):
        """Sets the sync_state of this VersionModel.

        State of syncing data from cache to remote  # noqa: E501

        :param sync_state: The sync_state of this VersionModel.  # noqa: E501
        :type: str
        """

        self._sync_state = sync_state

    @property
    def storage_path(self):
        """Gets the storage_path of this VersionModel.  # noqa: E501

        Path at which the data of this version is  # noqa: E501

        :return: The storage_path of this VersionModel.  # noqa: E501
        :rtype: str
        """
        return self._storage_path

    @storage_path.setter
    def storage_path(self, storage_path):
        """Sets the storage_path of this VersionModel.

        Path at which the data of this version is  # noqa: E501

        :param storage_path: The storage_path of this VersionModel.  # noqa: E501
        :type: str
        """

        self._storage_path = storage_path

    @property
    def user(self):
        """Gets the user of this VersionModel.  # noqa: E501

        Name of the owner  # noqa: E501

        :return: The user of this VersionModel.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this VersionModel.

        Name of the owner  # noqa: E501

        :param user: The user of this VersionModel.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def datum_name(self):
        """Gets the datum_name of this VersionModel.  # noqa: E501

        Name of the datum  # noqa: E501

        :return: The datum_name of this VersionModel.  # noqa: E501
        :rtype: str
        """
        return self._datum_name

    @datum_name.setter
    def datum_name(self, datum_name):
        """Sets the datum_name of this VersionModel.

        Name of the datum  # noqa: E501

        :param datum_name: The datum_name of this VersionModel.  # noqa: E501
        :type: str
        """

        self._datum_name = datum_name

    @property
    def datum_uuid(self):
        """Gets the datum_uuid of this VersionModel.  # noqa: E501

        UUID of dataset/model.  # noqa: E501

        :return: The datum_uuid of this VersionModel.  # noqa: E501
        :rtype: str
        """
        return self._datum_uuid

    @datum_uuid.setter
    def datum_uuid(self, datum_uuid):
        """Sets the datum_uuid of this VersionModel.

        UUID of dataset/model.  # noqa: E501

        :param datum_uuid: The datum_uuid of this VersionModel.  # noqa: E501
        :type: str
        """

        self._datum_uuid = datum_uuid

    @property
    def run_uuid(self):
        """Gets the run_uuid of this VersionModel.  # noqa: E501

        UUID of run.  # noqa: E501

        :return: The run_uuid of this VersionModel.  # noqa: E501
        :rtype: str
        """
        return self._run_uuid

    @run_uuid.setter
    def run_uuid(self, run_uuid):
        """Sets the run_uuid of this VersionModel.

        UUID of run.  # noqa: E501

        :param run_uuid: The run_uuid of this VersionModel.  # noqa: E501
        :type: str
        """

        self._run_uuid = run_uuid

    @property
    def tracking_uuid(self):
        """Gets the tracking_uuid of this VersionModel.  # noqa: E501


        :return: The tracking_uuid of this VersionModel.  # noqa: E501
        :rtype: str
        """
        return self._tracking_uuid

    @tracking_uuid.setter
    def tracking_uuid(self, tracking_uuid):
        """Sets the tracking_uuid of this VersionModel.


        :param tracking_uuid: The tracking_uuid of this VersionModel.  # noqa: E501
        :type: str
        """

        self._tracking_uuid = tracking_uuid

    @property
    def commit_id(self):
        """Gets the commit_id of this VersionModel.  # noqa: E501


        :return: The commit_id of this VersionModel.  # noqa: E501
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        """Sets the commit_id of this VersionModel.


        :param commit_id: The commit_id of this VersionModel.  # noqa: E501
        :type: str
        """

        self._commit_id = commit_id

    @property
    def size(self):
        """Gets the size of this VersionModel.  # noqa: E501

        Size in bytes  # noqa: E501

        :return: The size of this VersionModel.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this VersionModel.

        Size in bytes  # noqa: E501

        :param size: The size of this VersionModel.  # noqa: E501
        :type: str
        """

        self._size = size

    @property
    def datum_type(self):
        """Gets the datum_type of this VersionModel.  # noqa: E501


        :return: The datum_type of this VersionModel.  # noqa: E501
        :rtype: str
        """
        return self._datum_type

    @datum_type.setter
    def datum_type(self, datum_type):
        """Sets the datum_type of this VersionModel.


        :param datum_type: The datum_type of this VersionModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["model", "dataset", "program"]  # noqa: E501
        if datum_type not in allowed_values:
            raise ValueError(
                "Invalid value for `datum_type` ({0}), must be one of {1}"  # noqa: E501
                .format(datum_type, allowed_values)
            )

        self._datum_type = datum_type

    @property
    def model(self):
        """Gets the model of this VersionModel.  # noqa: E501


        :return: The model of this VersionModel.  # noqa: E501
        :rtype: VersionModelModel
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this VersionModel.


        :param model: The model of this VersionModel.  # noqa: E501
        :type: VersionModelModel
        """

        self._model = model

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
        if issubclass(VersionModel, dict):
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
        if not isinstance(other, VersionModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
