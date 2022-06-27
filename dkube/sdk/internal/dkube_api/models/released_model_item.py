# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.3.0.14
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ReleasedModelItem(object):
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
        'reason': 'str',
        'version': 'str',
        'user': 'str',
        'stage': 'str',
        'tracking_url': 'str',
        'uuid': 'str',
        'description': 'str',
        'released_timestamp': 'TimeStamps'
    }

    attribute_map = {
        'name': 'name',
        'reason': 'reason',
        'version': 'version',
        'user': 'user',
        'stage': 'stage',
        'tracking_url': 'trackingURL',
        'uuid': 'UUID',
        'description': 'description',
        'released_timestamp': 'releasedTimestamp'
    }

    def __init__(self, name=None, reason=None, version=None, user=None, stage=None, tracking_url=None, uuid=None, description=None, released_timestamp=None):  # noqa: E501
        """ReleasedModelItem - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._reason = None
        self._version = None
        self._user = None
        self._stage = None
        self._tracking_url = None
        self._uuid = None
        self._description = None
        self._released_timestamp = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if reason is not None:
            self.reason = reason
        if version is not None:
            self.version = version
        if user is not None:
            self.user = user
        if stage is not None:
            self.stage = stage
        if tracking_url is not None:
            self.tracking_url = tracking_url
        if uuid is not None:
            self.uuid = uuid
        if description is not None:
            self.description = description
        if released_timestamp is not None:
            self.released_timestamp = released_timestamp

    @property
    def name(self):
        """Gets the name of this ReleasedModelItem.  # noqa: E501


        :return: The name of this ReleasedModelItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReleasedModelItem.


        :param name: The name of this ReleasedModelItem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def reason(self):
        """Gets the reason of this ReleasedModelItem.  # noqa: E501


        :return: The reason of this ReleasedModelItem.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this ReleasedModelItem.


        :param reason: The reason of this ReleasedModelItem.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def version(self):
        """Gets the version of this ReleasedModelItem.  # noqa: E501


        :return: The version of this ReleasedModelItem.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ReleasedModelItem.


        :param version: The version of this ReleasedModelItem.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def user(self):
        """Gets the user of this ReleasedModelItem.  # noqa: E501


        :return: The user of this ReleasedModelItem.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ReleasedModelItem.


        :param user: The user of this ReleasedModelItem.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def stage(self):
        """Gets the stage of this ReleasedModelItem.  # noqa: E501


        :return: The stage of this ReleasedModelItem.  # noqa: E501
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        """Sets the stage of this ReleasedModelItem.


        :param stage: The stage of this ReleasedModelItem.  # noqa: E501
        :type: str
        """

        self._stage = stage

    @property
    def tracking_url(self):
        """Gets the tracking_url of this ReleasedModelItem.  # noqa: E501


        :return: The tracking_url of this ReleasedModelItem.  # noqa: E501
        :rtype: str
        """
        return self._tracking_url

    @tracking_url.setter
    def tracking_url(self, tracking_url):
        """Sets the tracking_url of this ReleasedModelItem.


        :param tracking_url: The tracking_url of this ReleasedModelItem.  # noqa: E501
        :type: str
        """

        self._tracking_url = tracking_url

    @property
    def uuid(self):
        """Gets the uuid of this ReleasedModelItem.  # noqa: E501


        :return: The uuid of this ReleasedModelItem.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this ReleasedModelItem.


        :param uuid: The uuid of this ReleasedModelItem.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def description(self):
        """Gets the description of this ReleasedModelItem.  # noqa: E501


        :return: The description of this ReleasedModelItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ReleasedModelItem.


        :param description: The description of this ReleasedModelItem.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def released_timestamp(self):
        """Gets the released_timestamp of this ReleasedModelItem.  # noqa: E501


        :return: The released_timestamp of this ReleasedModelItem.  # noqa: E501
        :rtype: TimeStamps
        """
        return self._released_timestamp

    @released_timestamp.setter
    def released_timestamp(self, released_timestamp):
        """Sets the released_timestamp of this ReleasedModelItem.


        :param released_timestamp: The released_timestamp of this ReleasedModelItem.  # noqa: E501
        :type: TimeStamps
        """

        self._released_timestamp = released_timestamp

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
        if issubclass(ReleasedModelItem, dict):
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
        if not isinstance(other, ReleasedModelItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
