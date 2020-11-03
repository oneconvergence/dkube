# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.2.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class WorkerModelContainers(object):
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
        'status': 'str',
        'uuid': 'str'
    }

    attribute_map = {
        'name': 'name',
        'reason': 'reason',
        'status': 'status',
        'uuid': 'uuid'
    }

    def __init__(self, name=None, reason=None, status=None, uuid=None):  # noqa: E501
        """WorkerModelContainers - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._reason = None
        self._status = None
        self._uuid = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if reason is not None:
            self.reason = reason
        if status is not None:
            self.status = status
        if uuid is not None:
            self.uuid = uuid

    @property
    def name(self):
        """Gets the name of this WorkerModelContainers.  # noqa: E501


        :return: The name of this WorkerModelContainers.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkerModelContainers.


        :param name: The name of this WorkerModelContainers.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def reason(self):
        """Gets the reason of this WorkerModelContainers.  # noqa: E501


        :return: The reason of this WorkerModelContainers.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this WorkerModelContainers.


        :param reason: The reason of this WorkerModelContainers.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def status(self):
        """Gets the status of this WorkerModelContainers.  # noqa: E501


        :return: The status of this WorkerModelContainers.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WorkerModelContainers.


        :param status: The status of this WorkerModelContainers.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def uuid(self):
        """Gets the uuid of this WorkerModelContainers.  # noqa: E501


        :return: The uuid of this WorkerModelContainers.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this WorkerModelContainers.


        :param uuid: The uuid of this WorkerModelContainers.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

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
        if issubclass(WorkerModelContainers, dict):
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
        if not isinstance(other, WorkerModelContainers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
