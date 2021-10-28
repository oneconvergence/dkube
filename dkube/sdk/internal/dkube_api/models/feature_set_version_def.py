# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.3.0.11
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class FeatureSetVersionDef(object):
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
        'created_ts': 'str',
        'updated_ts': 'str',
        'state': 'str',
        'user': 'str',
        'featureset_name': 'str',
        'featureset_uuid': 'str',
        'job': 'FeatureSetVersionDefJob',
        'tracking_uuid': 'str',
        'commit_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'uuid': 'uuid',
        'tags': 'tags',
        'description': 'description',
        'index': 'index',
        'created_ts': 'created_ts',
        'updated_ts': 'updated_ts',
        'state': 'state',
        'user': 'user',
        'featureset_name': 'featuresetName',
        'featureset_uuid': 'featuresetUUID',
        'job': 'job',
        'tracking_uuid': 'trackingUUID',
        'commit_id': 'commitID'
    }

    def __init__(self, name=None, uuid=None, tags=None, description=None, index=None, created_ts=None, updated_ts=None, state=None, user=None, featureset_name=None, featureset_uuid=None, job=None, tracking_uuid=None, commit_id=None):  # noqa: E501
        """FeatureSetVersionDef - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._uuid = None
        self._tags = None
        self._description = None
        self._index = None
        self._created_ts = None
        self._updated_ts = None
        self._state = None
        self._user = None
        self._featureset_name = None
        self._featureset_uuid = None
        self._job = None
        self._tracking_uuid = None
        self._commit_id = None
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
        if created_ts is not None:
            self.created_ts = created_ts
        if updated_ts is not None:
            self.updated_ts = updated_ts
        if state is not None:
            self.state = state
        if user is not None:
            self.user = user
        if featureset_name is not None:
            self.featureset_name = featureset_name
        if featureset_uuid is not None:
            self.featureset_uuid = featureset_uuid
        if job is not None:
            self.job = job
        if tracking_uuid is not None:
            self.tracking_uuid = tracking_uuid
        if commit_id is not None:
            self.commit_id = commit_id

    @property
    def name(self):
        """Gets the name of this FeatureSetVersionDef.  # noqa: E501

        Name of the version given by user  # noqa: E501

        :return: The name of this FeatureSetVersionDef.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FeatureSetVersionDef.

        Name of the version given by user  # noqa: E501

        :param name: The name of this FeatureSetVersionDef.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def uuid(self):
        """Gets the uuid of this FeatureSetVersionDef.  # noqa: E501

        Unique id generated by system (timestamp in milliseconds)  # noqa: E501

        :return: The uuid of this FeatureSetVersionDef.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this FeatureSetVersionDef.

        Unique id generated by system (timestamp in milliseconds)  # noqa: E501

        :param uuid: The uuid of this FeatureSetVersionDef.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def tags(self):
        """Gets the tags of this FeatureSetVersionDef.  # noqa: E501

        Unique tags provided by user  # noqa: E501

        :return: The tags of this FeatureSetVersionDef.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this FeatureSetVersionDef.

        Unique tags provided by user  # noqa: E501

        :param tags: The tags of this FeatureSetVersionDef.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def description(self):
        """Gets the description of this FeatureSetVersionDef.  # noqa: E501

        User defined description for the version  # noqa: E501

        :return: The description of this FeatureSetVersionDef.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FeatureSetVersionDef.

        User defined description for the version  # noqa: E501

        :param description: The description of this FeatureSetVersionDef.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def index(self):
        """Gets the index of this FeatureSetVersionDef.  # noqa: E501

        Incremental index to sort  # noqa: E501

        :return: The index of this FeatureSetVersionDef.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this FeatureSetVersionDef.

        Incremental index to sort  # noqa: E501

        :param index: The index of this FeatureSetVersionDef.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def created_ts(self):
        """Gets the created_ts of this FeatureSetVersionDef.  # noqa: E501


        :return: The created_ts of this FeatureSetVersionDef.  # noqa: E501
        :rtype: str
        """
        return self._created_ts

    @created_ts.setter
    def created_ts(self, created_ts):
        """Sets the created_ts of this FeatureSetVersionDef.


        :param created_ts: The created_ts of this FeatureSetVersionDef.  # noqa: E501
        :type: str
        """

        self._created_ts = created_ts

    @property
    def updated_ts(self):
        """Gets the updated_ts of this FeatureSetVersionDef.  # noqa: E501


        :return: The updated_ts of this FeatureSetVersionDef.  # noqa: E501
        :rtype: str
        """
        return self._updated_ts

    @updated_ts.setter
    def updated_ts(self, updated_ts):
        """Sets the updated_ts of this FeatureSetVersionDef.


        :param updated_ts: The updated_ts of this FeatureSetVersionDef.  # noqa: E501
        :type: str
        """

        self._updated_ts = updated_ts

    @property
    def state(self):
        """Gets the state of this FeatureSetVersionDef.  # noqa: E501

        State of syncing data from cache to remote or remote to cache  # noqa: E501

        :return: The state of this FeatureSetVersionDef.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this FeatureSetVersionDef.

        State of syncing data from cache to remote or remote to cache  # noqa: E501

        :param state: The state of this FeatureSetVersionDef.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def user(self):
        """Gets the user of this FeatureSetVersionDef.  # noqa: E501

        Name of the owner  # noqa: E501

        :return: The user of this FeatureSetVersionDef.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this FeatureSetVersionDef.

        Name of the owner  # noqa: E501

        :param user: The user of this FeatureSetVersionDef.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def featureset_name(self):
        """Gets the featureset_name of this FeatureSetVersionDef.  # noqa: E501

        Name of the featureset  # noqa: E501

        :return: The featureset_name of this FeatureSetVersionDef.  # noqa: E501
        :rtype: str
        """
        return self._featureset_name

    @featureset_name.setter
    def featureset_name(self, featureset_name):
        """Sets the featureset_name of this FeatureSetVersionDef.

        Name of the featureset  # noqa: E501

        :param featureset_name: The featureset_name of this FeatureSetVersionDef.  # noqa: E501
        :type: str
        """

        self._featureset_name = featureset_name

    @property
    def featureset_uuid(self):
        """Gets the featureset_uuid of this FeatureSetVersionDef.  # noqa: E501

        UUID of featureset.  # noqa: E501

        :return: The featureset_uuid of this FeatureSetVersionDef.  # noqa: E501
        :rtype: str
        """
        return self._featureset_uuid

    @featureset_uuid.setter
    def featureset_uuid(self, featureset_uuid):
        """Sets the featureset_uuid of this FeatureSetVersionDef.

        UUID of featureset.  # noqa: E501

        :param featureset_uuid: The featureset_uuid of this FeatureSetVersionDef.  # noqa: E501
        :type: str
        """

        self._featureset_uuid = featureset_uuid

    @property
    def job(self):
        """Gets the job of this FeatureSetVersionDef.  # noqa: E501


        :return: The job of this FeatureSetVersionDef.  # noqa: E501
        :rtype: FeatureSetVersionDefJob
        """
        return self._job

    @job.setter
    def job(self, job):
        """Sets the job of this FeatureSetVersionDef.


        :param job: The job of this FeatureSetVersionDef.  # noqa: E501
        :type: FeatureSetVersionDefJob
        """

        self._job = job

    @property
    def tracking_uuid(self):
        """Gets the tracking_uuid of this FeatureSetVersionDef.  # noqa: E501


        :return: The tracking_uuid of this FeatureSetVersionDef.  # noqa: E501
        :rtype: str
        """
        return self._tracking_uuid

    @tracking_uuid.setter
    def tracking_uuid(self, tracking_uuid):
        """Sets the tracking_uuid of this FeatureSetVersionDef.


        :param tracking_uuid: The tracking_uuid of this FeatureSetVersionDef.  # noqa: E501
        :type: str
        """

        self._tracking_uuid = tracking_uuid

    @property
    def commit_id(self):
        """Gets the commit_id of this FeatureSetVersionDef.  # noqa: E501


        :return: The commit_id of this FeatureSetVersionDef.  # noqa: E501
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        """Sets the commit_id of this FeatureSetVersionDef.


        :param commit_id: The commit_id of this FeatureSetVersionDef.  # noqa: E501
        :type: str
        """

        self._commit_id = commit_id

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
        if issubclass(FeatureSetVersionDef, dict):
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
        if not isinstance(other, FeatureSetVersionDef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
