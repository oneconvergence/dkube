# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0.0.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InlineResponse20036Data(object):
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
        'owner': 'str',
        'name': 'str',
        'status': 'str',
        'endpoint': 'str',
        'stage': 'object',
        'time_stamps': 'TimeStamps'
    }

    attribute_map = {
        'owner': 'owner',
        'name': 'name',
        'status': 'status',
        'endpoint': 'endpoint',
        'stage': 'stage',
        'time_stamps': 'timeStamps'
    }

    def __init__(self, owner=None, name=None, status=None, endpoint=None, stage=None, time_stamps=None):  # noqa: E501
        """InlineResponse20036Data - a model defined in Swagger"""  # noqa: E501

        self._owner = None
        self._name = None
        self._status = None
        self._endpoint = None
        self._stage = None
        self._time_stamps = None
        self.discriminator = None

        if owner is not None:
            self.owner = owner
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if endpoint is not None:
            self.endpoint = endpoint
        if stage is not None:
            self.stage = stage
        if time_stamps is not None:
            self.time_stamps = time_stamps

    @property
    def owner(self):
        """Gets the owner of this InlineResponse20036Data.  # noqa: E501


        :return: The owner of this InlineResponse20036Data.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this InlineResponse20036Data.


        :param owner: The owner of this InlineResponse20036Data.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def name(self):
        """Gets the name of this InlineResponse20036Data.  # noqa: E501


        :return: The name of this InlineResponse20036Data.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20036Data.


        :param name: The name of this InlineResponse20036Data.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this InlineResponse20036Data.  # noqa: E501


        :return: The status of this InlineResponse20036Data.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse20036Data.


        :param status: The status of this InlineResponse20036Data.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def endpoint(self):
        """Gets the endpoint of this InlineResponse20036Data.  # noqa: E501


        :return: The endpoint of this InlineResponse20036Data.  # noqa: E501
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this InlineResponse20036Data.


        :param endpoint: The endpoint of this InlineResponse20036Data.  # noqa: E501
        :type: str
        """

        self._endpoint = endpoint

    @property
    def stage(self):
        """Gets the stage of this InlineResponse20036Data.  # noqa: E501


        :return: The stage of this InlineResponse20036Data.  # noqa: E501
        :rtype: object
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        """Sets the stage of this InlineResponse20036Data.


        :param stage: The stage of this InlineResponse20036Data.  # noqa: E501
        :type: object
        """

        self._stage = stage

    @property
    def time_stamps(self):
        """Gets the time_stamps of this InlineResponse20036Data.  # noqa: E501


        :return: The time_stamps of this InlineResponse20036Data.  # noqa: E501
        :rtype: TimeStamps
        """
        return self._time_stamps

    @time_stamps.setter
    def time_stamps(self, time_stamps):
        """Sets the time_stamps of this InlineResponse20036Data.


        :param time_stamps: The time_stamps of this InlineResponse20036Data.  # noqa: E501
        :type: TimeStamps
        """

        self._time_stamps = time_stamps

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
        if issubclass(InlineResponse20036Data, dict):
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
        if not isinstance(other, InlineResponse20036Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
