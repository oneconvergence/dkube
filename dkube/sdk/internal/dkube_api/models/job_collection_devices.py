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

class JobCollectionDevices(object):
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
        'device': 'DeviceModel',
        'node': 'NodeModel'
    }

    attribute_map = {
        'device': 'device',
        'node': 'node'
    }

    def __init__(self, device=None, node=None):  # noqa: E501
        """JobCollectionDevices - a model defined in Swagger"""  # noqa: E501
        self._device = None
        self._node = None
        self.discriminator = None
        if device is not None:
            self.device = device
        if node is not None:
            self.node = node

    @property
    def device(self):
        """Gets the device of this JobCollectionDevices.  # noqa: E501


        :return: The device of this JobCollectionDevices.  # noqa: E501
        :rtype: DeviceModel
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this JobCollectionDevices.


        :param device: The device of this JobCollectionDevices.  # noqa: E501
        :type: DeviceModel
        """

        self._device = device

    @property
    def node(self):
        """Gets the node of this JobCollectionDevices.  # noqa: E501


        :return: The node of this JobCollectionDevices.  # noqa: E501
        :rtype: NodeModel
        """
        return self._node

    @node.setter
    def node(self, node):
        """Sets the node of this JobCollectionDevices.


        :param node: The node of this JobCollectionDevices.  # noqa: E501
        :type: NodeModel
        """

        self._node = node

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
        if issubclass(JobCollectionDevices, dict):
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
        if not isinstance(other, JobCollectionDevices):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
