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


class PluginModelGenerated(object):
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
        'user': 'str',
        'status': 'PluginStatusModel',
        'timestamps': 'TimeStamps',
        'service_name': 'str',
        'service_port': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'user': 'user',
        'status': 'status',
        'timestamps': 'timestamps',
        'service_name': 'service_name',
        'service_port': 'service_port'
    }

    def __init__(self, uuid=None, user=None, status=None, timestamps=None, service_name=None, service_port=None):  # noqa: E501
        """PluginModelGenerated - a model defined in Swagger"""  # noqa: E501

        self._uuid = None
        self._user = None
        self._status = None
        self._timestamps = None
        self._service_name = None
        self._service_port = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if user is not None:
            self.user = user
        if status is not None:
            self.status = status
        if timestamps is not None:
            self.timestamps = timestamps
        if service_name is not None:
            self.service_name = service_name
        if service_port is not None:
            self.service_port = service_port

    @property
    def uuid(self):
        """Gets the uuid of this PluginModelGenerated.  # noqa: E501


        :return: The uuid of this PluginModelGenerated.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this PluginModelGenerated.


        :param uuid: The uuid of this PluginModelGenerated.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def user(self):
        """Gets the user of this PluginModelGenerated.  # noqa: E501


        :return: The user of this PluginModelGenerated.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this PluginModelGenerated.


        :param user: The user of this PluginModelGenerated.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def status(self):
        """Gets the status of this PluginModelGenerated.  # noqa: E501


        :return: The status of this PluginModelGenerated.  # noqa: E501
        :rtype: PluginStatusModel
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PluginModelGenerated.


        :param status: The status of this PluginModelGenerated.  # noqa: E501
        :type: PluginStatusModel
        """

        self._status = status

    @property
    def timestamps(self):
        """Gets the timestamps of this PluginModelGenerated.  # noqa: E501


        :return: The timestamps of this PluginModelGenerated.  # noqa: E501
        :rtype: TimeStamps
        """
        return self._timestamps

    @timestamps.setter
    def timestamps(self, timestamps):
        """Sets the timestamps of this PluginModelGenerated.


        :param timestamps: The timestamps of this PluginModelGenerated.  # noqa: E501
        :type: TimeStamps
        """

        self._timestamps = timestamps

    @property
    def service_name(self):
        """Gets the service_name of this PluginModelGenerated.  # noqa: E501


        :return: The service_name of this PluginModelGenerated.  # noqa: E501
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this PluginModelGenerated.


        :param service_name: The service_name of this PluginModelGenerated.  # noqa: E501
        :type: str
        """

        self._service_name = service_name

    @property
    def service_port(self):
        """Gets the service_port of this PluginModelGenerated.  # noqa: E501


        :return: The service_port of this PluginModelGenerated.  # noqa: E501
        :rtype: str
        """
        return self._service_port

    @service_port.setter
    def service_port(self, service_port):
        """Sets the service_port of this PluginModelGenerated.


        :param service_port: The service_port of this PluginModelGenerated.  # noqa: E501
        :type: str
        """

        self._service_port = service_port

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
        if issubclass(PluginModelGenerated, dict):
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
        if not isinstance(other, PluginModelGenerated):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
