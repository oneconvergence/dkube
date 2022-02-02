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


class VersionModelModel(object):
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
        'released_timestamp': 'TimeStamps',
        'published_timestamp': 'TimeStamps',
        'published_name': 'str',
        'published_description': 'str',
        'reason': 'str',
        'stage': 'str'
    }

    attribute_map = {
        'released_timestamp': 'releasedTimestamp',
        'published_timestamp': 'publishedTimestamp',
        'published_name': 'publishedName',
        'published_description': 'publishedDescription',
        'reason': 'reason',
        'stage': 'stage'
    }

    def __init__(self, released_timestamp=None, published_timestamp=None, published_name=None, published_description=None, reason=None, stage=None):  # noqa: E501
        """VersionModelModel - a model defined in Swagger"""  # noqa: E501

        self._released_timestamp = None
        self._published_timestamp = None
        self._published_name = None
        self._published_description = None
        self._reason = None
        self._stage = None
        self.discriminator = None

        if released_timestamp is not None:
            self.released_timestamp = released_timestamp
        if published_timestamp is not None:
            self.published_timestamp = published_timestamp
        if published_name is not None:
            self.published_name = published_name
        if published_description is not None:
            self.published_description = published_description
        if reason is not None:
            self.reason = reason
        if stage is not None:
            self.stage = stage

    @property
    def released_timestamp(self):
        """Gets the released_timestamp of this VersionModelModel.  # noqa: E501


        :return: The released_timestamp of this VersionModelModel.  # noqa: E501
        :rtype: TimeStamps
        """
        return self._released_timestamp

    @released_timestamp.setter
    def released_timestamp(self, released_timestamp):
        """Sets the released_timestamp of this VersionModelModel.


        :param released_timestamp: The released_timestamp of this VersionModelModel.  # noqa: E501
        :type: TimeStamps
        """

        self._released_timestamp = released_timestamp

    @property
    def published_timestamp(self):
        """Gets the published_timestamp of this VersionModelModel.  # noqa: E501


        :return: The published_timestamp of this VersionModelModel.  # noqa: E501
        :rtype: TimeStamps
        """
        return self._published_timestamp

    @published_timestamp.setter
    def published_timestamp(self, published_timestamp):
        """Sets the published_timestamp of this VersionModelModel.


        :param published_timestamp: The published_timestamp of this VersionModelModel.  # noqa: E501
        :type: TimeStamps
        """

        self._published_timestamp = published_timestamp

    @property
    def published_name(self):
        """Gets the published_name of this VersionModelModel.  # noqa: E501


        :return: The published_name of this VersionModelModel.  # noqa: E501
        :rtype: str
        """
        return self._published_name

    @published_name.setter
    def published_name(self, published_name):
        """Sets the published_name of this VersionModelModel.


        :param published_name: The published_name of this VersionModelModel.  # noqa: E501
        :type: str
        """

        self._published_name = published_name

    @property
    def published_description(self):
        """Gets the published_description of this VersionModelModel.  # noqa: E501


        :return: The published_description of this VersionModelModel.  # noqa: E501
        :rtype: str
        """
        return self._published_description

    @published_description.setter
    def published_description(self, published_description):
        """Sets the published_description of this VersionModelModel.


        :param published_description: The published_description of this VersionModelModel.  # noqa: E501
        :type: str
        """

        self._published_description = published_description

    @property
    def reason(self):
        """Gets the reason of this VersionModelModel.  # noqa: E501


        :return: The reason of this VersionModelModel.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this VersionModelModel.


        :param reason: The reason of this VersionModelModel.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def stage(self):
        """Gets the stage of this VersionModelModel.  # noqa: E501


        :return: The stage of this VersionModelModel.  # noqa: E501
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        """Sets the stage of this VersionModelModel.


        :param stage: The stage of this VersionModelModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["DEFAULT", "RELEASED", "PUBLISHING", "PUBLISHED", "DEPLOYED", "STAGED"]  # noqa: E501
        if stage not in allowed_values:
            raise ValueError(
                "Invalid value for `stage` ({0}), must be one of {1}"  # noqa: E501
                .format(stage, allowed_values)
            )

        self._stage = stage

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
        if issubclass(VersionModelModel, dict):
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
        if not isinstance(other, VersionModelModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
