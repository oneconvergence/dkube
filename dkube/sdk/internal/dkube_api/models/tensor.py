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


class Tensor(object):
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
        'dtype': 'str',
        'name': 'str',
        'tensor_shape': 'str',
        'key': 'str'
    }

    attribute_map = {
        'dtype': 'dtype',
        'name': 'name',
        'tensor_shape': 'tensor_shape',
        'key': 'key'
    }

    def __init__(self, dtype=None, name=None, tensor_shape=None, key=None):  # noqa: E501
        """Tensor - a model defined in Swagger"""  # noqa: E501

        self._dtype = None
        self._name = None
        self._tensor_shape = None
        self._key = None
        self.discriminator = None

        if dtype is not None:
            self.dtype = dtype
        if name is not None:
            self.name = name
        if tensor_shape is not None:
            self.tensor_shape = tensor_shape
        if key is not None:
            self.key = key

    @property
    def dtype(self):
        """Gets the dtype of this Tensor.  # noqa: E501


        :return: The dtype of this Tensor.  # noqa: E501
        :rtype: str
        """
        return self._dtype

    @dtype.setter
    def dtype(self, dtype):
        """Sets the dtype of this Tensor.


        :param dtype: The dtype of this Tensor.  # noqa: E501
        :type: str
        """

        self._dtype = dtype

    @property
    def name(self):
        """Gets the name of this Tensor.  # noqa: E501


        :return: The name of this Tensor.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Tensor.


        :param name: The name of this Tensor.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def tensor_shape(self):
        """Gets the tensor_shape of this Tensor.  # noqa: E501


        :return: The tensor_shape of this Tensor.  # noqa: E501
        :rtype: str
        """
        return self._tensor_shape

    @tensor_shape.setter
    def tensor_shape(self, tensor_shape):
        """Sets the tensor_shape of this Tensor.


        :param tensor_shape: The tensor_shape of this Tensor.  # noqa: E501
        :type: str
        """

        self._tensor_shape = tensor_shape

    @property
    def key(self):
        """Gets the key of this Tensor.  # noqa: E501


        :return: The key of this Tensor.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Tensor.


        :param key: The key of this Tensor.  # noqa: E501
        :type: str
        """

        self._key = key

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
        if issubclass(Tensor, dict):
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
        if not isinstance(other, Tensor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
