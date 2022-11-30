# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.7.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class MigrationObjUUID(object):
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
        'src_uuid': 'str',
        'tgt_uuid': 'str',
        'src_name': 'str',
        'tgt_name': 'str'
    }

    attribute_map = {
        'src_uuid': 'src_UUID',
        'tgt_uuid': 'tgt_UUID',
        'src_name': 'src_name',
        'tgt_name': 'tgt_name'
    }

    def __init__(self, src_uuid=None, tgt_uuid=None, src_name=None, tgt_name=None):  # noqa: E501
        """MigrationObjUUID - a model defined in Swagger"""  # noqa: E501

        self._src_uuid = None
        self._tgt_uuid = None
        self._src_name = None
        self._tgt_name = None
        self.discriminator = None

        if src_uuid is not None:
            self.src_uuid = src_uuid
        if tgt_uuid is not None:
            self.tgt_uuid = tgt_uuid
        if src_name is not None:
            self.src_name = src_name
        if tgt_name is not None:
            self.tgt_name = tgt_name

    @property
    def src_uuid(self):
        """Gets the src_uuid of this MigrationObjUUID.  # noqa: E501


        :return: The src_uuid of this MigrationObjUUID.  # noqa: E501
        :rtype: str
        """
        return self._src_uuid

    @src_uuid.setter
    def src_uuid(self, src_uuid):
        """Sets the src_uuid of this MigrationObjUUID.


        :param src_uuid: The src_uuid of this MigrationObjUUID.  # noqa: E501
        :type: str
        """

        self._src_uuid = src_uuid

    @property
    def tgt_uuid(self):
        """Gets the tgt_uuid of this MigrationObjUUID.  # noqa: E501


        :return: The tgt_uuid of this MigrationObjUUID.  # noqa: E501
        :rtype: str
        """
        return self._tgt_uuid

    @tgt_uuid.setter
    def tgt_uuid(self, tgt_uuid):
        """Sets the tgt_uuid of this MigrationObjUUID.


        :param tgt_uuid: The tgt_uuid of this MigrationObjUUID.  # noqa: E501
        :type: str
        """

        self._tgt_uuid = tgt_uuid

    @property
    def src_name(self):
        """Gets the src_name of this MigrationObjUUID.  # noqa: E501


        :return: The src_name of this MigrationObjUUID.  # noqa: E501
        :rtype: str
        """
        return self._src_name

    @src_name.setter
    def src_name(self, src_name):
        """Sets the src_name of this MigrationObjUUID.


        :param src_name: The src_name of this MigrationObjUUID.  # noqa: E501
        :type: str
        """

        self._src_name = src_name

    @property
    def tgt_name(self):
        """Gets the tgt_name of this MigrationObjUUID.  # noqa: E501


        :return: The tgt_name of this MigrationObjUUID.  # noqa: E501
        :rtype: str
        """
        return self._tgt_name

    @tgt_name.setter
    def tgt_name(self, tgt_name):
        """Sets the tgt_name of this MigrationObjUUID.


        :param tgt_name: The tgt_name of this MigrationObjUUID.  # noqa: E501
        :type: str
        """

        self._tgt_name = tgt_name

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
        if issubclass(MigrationObjUUID, dict):
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
        if not isinstance(other, MigrationObjUUID):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
