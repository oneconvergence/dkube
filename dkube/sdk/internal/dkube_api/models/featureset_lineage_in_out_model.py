# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0.0.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class FeaturesetLineageInOutModel(object):
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
        'version_name': 'str',
        'version_uuid': 'str',
        'type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'uuid': 'uuid',
        'version_name': 'version_name',
        'version_uuid': 'version_uuid',
        'type': 'type'
    }

    def __init__(self, name=None, uuid=None, version_name=None, version_uuid=None, type=None):  # noqa: E501
        """FeaturesetLineageInOutModel - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._uuid = None
        self._version_name = None
        self._version_uuid = None
        self._type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if uuid is not None:
            self.uuid = uuid
        if version_name is not None:
            self.version_name = version_name
        if version_uuid is not None:
            self.version_uuid = version_uuid
        if type is not None:
            self.type = type

    @property
    def name(self):
        """Gets the name of this FeaturesetLineageInOutModel.  # noqa: E501


        :return: The name of this FeaturesetLineageInOutModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FeaturesetLineageInOutModel.


        :param name: The name of this FeaturesetLineageInOutModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def uuid(self):
        """Gets the uuid of this FeaturesetLineageInOutModel.  # noqa: E501


        :return: The uuid of this FeaturesetLineageInOutModel.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this FeaturesetLineageInOutModel.


        :param uuid: The uuid of this FeaturesetLineageInOutModel.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def version_name(self):
        """Gets the version_name of this FeaturesetLineageInOutModel.  # noqa: E501


        :return: The version_name of this FeaturesetLineageInOutModel.  # noqa: E501
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        """Sets the version_name of this FeaturesetLineageInOutModel.


        :param version_name: The version_name of this FeaturesetLineageInOutModel.  # noqa: E501
        :type: str
        """

        self._version_name = version_name

    @property
    def version_uuid(self):
        """Gets the version_uuid of this FeaturesetLineageInOutModel.  # noqa: E501


        :return: The version_uuid of this FeaturesetLineageInOutModel.  # noqa: E501
        :rtype: str
        """
        return self._version_uuid

    @version_uuid.setter
    def version_uuid(self, version_uuid):
        """Sets the version_uuid of this FeaturesetLineageInOutModel.


        :param version_uuid: The version_uuid of this FeaturesetLineageInOutModel.  # noqa: E501
        :type: str
        """

        self._version_uuid = version_uuid

    @property
    def type(self):
        """Gets the type of this FeaturesetLineageInOutModel.  # noqa: E501


        :return: The type of this FeaturesetLineageInOutModel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FeaturesetLineageInOutModel.


        :param type: The type of this FeaturesetLineageInOutModel.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(FeaturesetLineageInOutModel, dict):
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
        if not isinstance(other, FeaturesetLineageInOutModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
