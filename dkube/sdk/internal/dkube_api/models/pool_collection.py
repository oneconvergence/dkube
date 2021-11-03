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


class PoolCollection(object):
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
        'pool': 'DevicePoolModel',
        'devices': 'PoolCollectionDevices'
    }

    attribute_map = {
        'pool': 'pool',
        'devices': 'devices'
    }

    def __init__(self, pool=None, devices=None):  # noqa: E501
        """PoolCollection - a model defined in Swagger"""  # noqa: E501

        self._pool = None
        self._devices = None
        self.discriminator = None

        if pool is not None:
            self.pool = pool
        if devices is not None:
            self.devices = devices

    @property
    def pool(self):
        """Gets the pool of this PoolCollection.  # noqa: E501


        :return: The pool of this PoolCollection.  # noqa: E501
        :rtype: DevicePoolModel
        """
        return self._pool

    @pool.setter
    def pool(self, pool):
        """Sets the pool of this PoolCollection.


        :param pool: The pool of this PoolCollection.  # noqa: E501
        :type: DevicePoolModel
        """

        self._pool = pool

    @property
    def devices(self):
        """Gets the devices of this PoolCollection.  # noqa: E501


        :return: The devices of this PoolCollection.  # noqa: E501
        :rtype: PoolCollectionDevices
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this PoolCollection.


        :param devices: The devices of this PoolCollection.  # noqa: E501
        :type: PoolCollectionDevices
        """

        self._devices = devices

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
        if issubclass(PoolCollection, dict):
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
        if not isinstance(other, PoolCollection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
