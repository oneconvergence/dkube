# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.3.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DkubeInfoRelease(object):
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
        'previous': 'str',
        'current': 'str'
    }

    attribute_map = {
        'previous': 'previous',
        'current': 'current'
    }

    def __init__(self, previous=None, current=None):  # noqa: E501
        """DkubeInfoRelease - a model defined in Swagger"""  # noqa: E501

        self._previous = None
        self._current = None
        self.discriminator = None

        self.previous = previous
        self.current = current

    @property
    def previous(self):
        """Gets the previous of this DkubeInfoRelease.  # noqa: E501

        The previous Dkube version if it has been migrated.  # noqa: E501

        :return: The previous of this DkubeInfoRelease.  # noqa: E501
        :rtype: str
        """
        return self._previous

    @previous.setter
    def previous(self, previous):
        """Sets the previous of this DkubeInfoRelease.

        The previous Dkube version if it has been migrated.  # noqa: E501

        :param previous: The previous of this DkubeInfoRelease.  # noqa: E501
        :type: str
        """
        if previous is None:
            raise ValueError("Invalid value for `previous`, must not be `None`")  # noqa: E501

        self._previous = previous

    @property
    def current(self):
        """Gets the current of this DkubeInfoRelease.  # noqa: E501

        The current Dkube version.  # noqa: E501

        :return: The current of this DkubeInfoRelease.  # noqa: E501
        :rtype: str
        """
        return self._current

    @current.setter
    def current(self, current):
        """Sets the current of this DkubeInfoRelease.

        The current Dkube version.  # noqa: E501

        :param current: The current of this DkubeInfoRelease.  # noqa: E501
        :type: str
        """
        if current is None:
            raise ValueError("Invalid value for `current`, must not be `None`")  # noqa: E501

        self._current = current

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
        if issubclass(DkubeInfoRelease, dict):
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
        if not isinstance(other, DkubeInfoRelease):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
