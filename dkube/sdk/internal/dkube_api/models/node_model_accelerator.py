# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.3.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class NodeModelAccelerator(object):
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
        'healthy': 'bool',
        '_class': 'str',
        'name': 'str'
    }

    attribute_map = {
        'healthy': 'healthy',
        '_class': 'class',
        'name': 'name'
    }

    def __init__(self, healthy=True, _class='gpu', name=None):  # noqa: E501
        """NodeModelAccelerator - a model defined in Swagger"""  # noqa: E501

        self._healthy = None
        self.__class = None
        self._name = None
        self.discriminator = None

        if healthy is not None:
            self.healthy = healthy
        if _class is not None:
            self._class = _class
        if name is not None:
            self.name = name

    @property
    def healthy(self):
        """Gets the healthy of this NodeModelAccelerator.  # noqa: E501


        :return: The healthy of this NodeModelAccelerator.  # noqa: E501
        :rtype: bool
        """
        return self._healthy

    @healthy.setter
    def healthy(self, healthy):
        """Sets the healthy of this NodeModelAccelerator.


        :param healthy: The healthy of this NodeModelAccelerator.  # noqa: E501
        :type: bool
        """

        self._healthy = healthy

    @property
    def _class(self):
        """Gets the _class of this NodeModelAccelerator.  # noqa: E501


        :return: The _class of this NodeModelAccelerator.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this NodeModelAccelerator.


        :param _class: The _class of this NodeModelAccelerator.  # noqa: E501
        :type: str
        """
        allowed_values = ["gpu"]  # noqa: E501
        if _class not in allowed_values:
            raise ValueError(
                "Invalid value for `_class` ({0}), must be one of {1}"  # noqa: E501
                .format(_class, allowed_values)
            )

        self.__class = _class

    @property
    def name(self):
        """Gets the name of this NodeModelAccelerator.  # noqa: E501


        :return: The name of this NodeModelAccelerator.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NodeModelAccelerator.


        :param name: The name of this NodeModelAccelerator.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(NodeModelAccelerator, dict):
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
        if not isinstance(other, NodeModelAccelerator):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
