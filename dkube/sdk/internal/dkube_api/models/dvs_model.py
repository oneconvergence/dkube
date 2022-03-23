# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.2.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DVSModel(object):
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
        'status': 'DVSModelStatus',
        'metadata': 'str',
        'store': 'str',
        'git': 'DVSModelGit',
        's3': 'DVSModelS3',
        'gcs': 'DVSModelGcs'
    }

    attribute_map = {
        'name': 'name',
        'uuid': 'uuid',
        'status': 'status',
        'metadata': 'metadata',
        'store': 'store',
        'git': 'git',
        's3': 's3',
        'gcs': 'gcs'
    }

    def __init__(self, name=None, uuid=None, status=None, metadata=None, store=None, git=None, s3=None, gcs=None):  # noqa: E501
        """DVSModel - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._uuid = None
        self._status = None
        self._metadata = None
        self._store = None
        self._git = None
        self._s3 = None
        self._gcs = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if uuid is not None:
            self.uuid = uuid
        if status is not None:
            self.status = status
        if metadata is not None:
            self.metadata = metadata
        if store is not None:
            self.store = store
        if git is not None:
            self.git = git
        if s3 is not None:
            self.s3 = s3
        if gcs is not None:
            self.gcs = gcs

    @property
    def name(self):
        """Gets the name of this DVSModel.  # noqa: E501


        :return: The name of this DVSModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DVSModel.


        :param name: The name of this DVSModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def uuid(self):
        """Gets the uuid of this DVSModel.  # noqa: E501


        :return: The uuid of this DVSModel.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this DVSModel.


        :param uuid: The uuid of this DVSModel.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def status(self):
        """Gets the status of this DVSModel.  # noqa: E501


        :return: The status of this DVSModel.  # noqa: E501
        :rtype: DVSModelStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DVSModel.


        :param status: The status of this DVSModel.  # noqa: E501
        :type: DVSModelStatus
        """

        self._status = status

    @property
    def metadata(self):
        """Gets the metadata of this DVSModel.  # noqa: E501


        :return: The metadata of this DVSModel.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this DVSModel.


        :param metadata: The metadata of this DVSModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["dkube", "git"]  # noqa: E501
        if metadata not in allowed_values:
            raise ValueError(
                "Invalid value for `metadata` ({0}), must be one of {1}"  # noqa: E501
                .format(metadata, allowed_values)
            )

        self._metadata = metadata

    @property
    def store(self):
        """Gets the store of this DVSModel.  # noqa: E501


        :return: The store of this DVSModel.  # noqa: E501
        :rtype: str
        """
        return self._store

    @store.setter
    def store(self, store):
        """Sets the store of this DVSModel.


        :param store: The store of this DVSModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["dkube", "s3", "gcs"]  # noqa: E501
        if store not in allowed_values:
            raise ValueError(
                "Invalid value for `store` ({0}), must be one of {1}"  # noqa: E501
                .format(store, allowed_values)
            )

        self._store = store

    @property
    def git(self):
        """Gets the git of this DVSModel.  # noqa: E501


        :return: The git of this DVSModel.  # noqa: E501
        :rtype: DVSModelGit
        """
        return self._git

    @git.setter
    def git(self, git):
        """Sets the git of this DVSModel.


        :param git: The git of this DVSModel.  # noqa: E501
        :type: DVSModelGit
        """

        self._git = git

    @property
    def s3(self):
        """Gets the s3 of this DVSModel.  # noqa: E501


        :return: The s3 of this DVSModel.  # noqa: E501
        :rtype: DVSModelS3
        """
        return self._s3

    @s3.setter
    def s3(self, s3):
        """Sets the s3 of this DVSModel.


        :param s3: The s3 of this DVSModel.  # noqa: E501
        :type: DVSModelS3
        """

        self._s3 = s3

    @property
    def gcs(self):
        """Gets the gcs of this DVSModel.  # noqa: E501


        :return: The gcs of this DVSModel.  # noqa: E501
        :rtype: DVSModelGcs
        """
        return self._gcs

    @gcs.setter
    def gcs(self, gcs):
        """Sets the gcs of this DVSModel.


        :param gcs: The gcs of this DVSModel.  # noqa: E501
        :type: DVSModelGcs
        """

        self._gcs = gcs

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
        if issubclass(DVSModel, dict):
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
        if not isinstance(other, DVSModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
