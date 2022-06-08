# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.4.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DkubeInfoLicenseQuotas(object):
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
        'count': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'name': 'name',
        'count': 'count',
        'limit': 'limit'
    }

    def __init__(self, name=None, count=None, limit=None):  # noqa: E501
        """DkubeInfoLicenseQuotas - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._count = None
        self._limit = None
        self.discriminator = None

        self.name = name
        self.count = count
        self.limit = limit

    @property
    def name(self):
        """Gets the name of this DkubeInfoLicenseQuotas.  # noqa: E501


        :return: The name of this DkubeInfoLicenseQuotas.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DkubeInfoLicenseQuotas.


        :param name: The name of this DkubeInfoLicenseQuotas.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def count(self):
        """Gets the count of this DkubeInfoLicenseQuotas.  # noqa: E501


        :return: The count of this DkubeInfoLicenseQuotas.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this DkubeInfoLicenseQuotas.


        :param count: The count of this DkubeInfoLicenseQuotas.  # noqa: E501
        :type: int
        """
        if count is None:
            raise ValueError("Invalid value for `count`, must not be `None`")  # noqa: E501

        self._count = count

    @property
    def limit(self):
        """Gets the limit of this DkubeInfoLicenseQuotas.  # noqa: E501


        :return: The limit of this DkubeInfoLicenseQuotas.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this DkubeInfoLicenseQuotas.


        :param limit: The limit of this DkubeInfoLicenseQuotas.  # noqa: E501
        :type: int
        """
        if limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

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
        if issubclass(DkubeInfoLicenseQuotas, dict):
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
        if not isinstance(other, DkubeInfoLicenseQuotas):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other