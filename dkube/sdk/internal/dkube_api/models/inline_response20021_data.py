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


class InlineResponse20021Data(object):
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
        'total_gpus': 'int',
        'used_gpus': 'int'
    }

    attribute_map = {
        'total_gpus': 'total_gpus',
        'used_gpus': 'used_gpus'
    }

    def __init__(self, total_gpus=None, used_gpus=None):  # noqa: E501
        """InlineResponse20021Data - a model defined in Swagger"""  # noqa: E501

        self._total_gpus = None
        self._used_gpus = None
        self.discriminator = None

        self.total_gpus = total_gpus
        self.used_gpus = used_gpus

    @property
    def total_gpus(self):
        """Gets the total_gpus of this InlineResponse20021Data.  # noqa: E501


        :return: The total_gpus of this InlineResponse20021Data.  # noqa: E501
        :rtype: int
        """
        return self._total_gpus

    @total_gpus.setter
    def total_gpus(self, total_gpus):
        """Sets the total_gpus of this InlineResponse20021Data.


        :param total_gpus: The total_gpus of this InlineResponse20021Data.  # noqa: E501
        :type: int
        """
        if total_gpus is None:
            raise ValueError("Invalid value for `total_gpus`, must not be `None`")  # noqa: E501

        self._total_gpus = total_gpus

    @property
    def used_gpus(self):
        """Gets the used_gpus of this InlineResponse20021Data.  # noqa: E501


        :return: The used_gpus of this InlineResponse20021Data.  # noqa: E501
        :rtype: int
        """
        return self._used_gpus

    @used_gpus.setter
    def used_gpus(self, used_gpus):
        """Sets the used_gpus of this InlineResponse20021Data.


        :param used_gpus: The used_gpus of this InlineResponse20021Data.  # noqa: E501
        :type: int
        """
        if used_gpus is None:
            raise ValueError("Invalid value for `used_gpus`, must not be `None`")  # noqa: E501

        self._used_gpus = used_gpus

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
        if issubclass(InlineResponse20021Data, dict):
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
        if not isinstance(other, InlineResponse20021Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
