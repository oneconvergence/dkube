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


class Data6(object):
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
        'dvs': 'list[str]'
    }

    attribute_map = {
        'dvs': 'dvs'
    }

    def __init__(self, dvs=None):  # noqa: E501
        """Data6 - a model defined in Swagger"""  # noqa: E501

        self._dvs = None
        self.discriminator = None

        self.dvs = dvs

    @property
    def dvs(self):
        """Gets the dvs of this Data6.  # noqa: E501

        List of DVS config to delete  # noqa: E501

        :return: The dvs of this Data6.  # noqa: E501
        :rtype: list[str]
        """
        return self._dvs

    @dvs.setter
    def dvs(self, dvs):
        """Sets the dvs of this Data6.

        List of DVS config to delete  # noqa: E501

        :param dvs: The dvs of this Data6.  # noqa: E501
        :type: list[str]
        """
        if dvs is None:
            raise ValueError("Invalid value for `dvs`, must not be `None`")  # noqa: E501

        self._dvs = dvs

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
        if issubclass(Data6, dict):
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
        if not isinstance(other, Data6):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
