# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.5.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Data27(object):
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
        'upsert': 'bool',
        'poolname': 'str',
        'pooltype': 'str',
        'ndevices': 'int'
    }

    attribute_map = {
        'upsert': 'upsert',
        'poolname': 'poolname',
        'pooltype': 'pooltype',
        'ndevices': 'ndevices'
    }

    def __init__(self, upsert=True, poolname=None, pooltype=None, ndevices=None):  # noqa: E501
        """Data27 - a model defined in Swagger"""  # noqa: E501

        self._upsert = None
        self._poolname = None
        self._pooltype = None
        self._ndevices = None
        self.discriminator = None

        if upsert is not None:
            self.upsert = upsert
        self.poolname = poolname
        self.pooltype = pooltype
        self.ndevices = ndevices

    @property
    def upsert(self):
        """Gets the upsert of this Data27.  # noqa: E501


        :return: The upsert of this Data27.  # noqa: E501
        :rtype: bool
        """
        return self._upsert

    @upsert.setter
    def upsert(self, upsert):
        """Sets the upsert of this Data27.


        :param upsert: The upsert of this Data27.  # noqa: E501
        :type: bool
        """

        self._upsert = upsert

    @property
    def poolname(self):
        """Gets the poolname of this Data27.  # noqa: E501


        :return: The poolname of this Data27.  # noqa: E501
        :rtype: str
        """
        return self._poolname

    @poolname.setter
    def poolname(self, poolname):
        """Sets the poolname of this Data27.


        :param poolname: The poolname of this Data27.  # noqa: E501
        :type: str
        """
        if poolname is None:
            raise ValueError("Invalid value for `poolname`, must not be `None`")  # noqa: E501
        if poolname is not None and len(poolname) > 255:
            raise ValueError("Invalid value for `poolname`, length must be less than or equal to `255`")  # noqa: E501
        if poolname is not None and len(poolname) < 1:
            raise ValueError("Invalid value for `poolname`, length must be greater than or equal to `1`")  # noqa: E501

        self._poolname = poolname

    @property
    def pooltype(self):
        """Gets the pooltype of this Data27.  # noqa: E501


        :return: The pooltype of this Data27.  # noqa: E501
        :rtype: str
        """
        return self._pooltype

    @pooltype.setter
    def pooltype(self, pooltype):
        """Sets the pooltype of this Data27.


        :param pooltype: The pooltype of this Data27.  # noqa: E501
        :type: str
        """
        if pooltype is None:
            raise ValueError("Invalid value for `pooltype`, must not be `None`")  # noqa: E501
        if pooltype is not None and len(pooltype) > 255:
            raise ValueError("Invalid value for `pooltype`, length must be less than or equal to `255`")  # noqa: E501
        if pooltype is not None and len(pooltype) < 1:
            raise ValueError("Invalid value for `pooltype`, length must be greater than or equal to `1`")  # noqa: E501

        self._pooltype = pooltype

    @property
    def ndevices(self):
        """Gets the ndevices of this Data27.  # noqa: E501


        :return: The ndevices of this Data27.  # noqa: E501
        :rtype: int
        """
        return self._ndevices

    @ndevices.setter
    def ndevices(self, ndevices):
        """Sets the ndevices of this Data27.


        :param ndevices: The ndevices of this Data27.  # noqa: E501
        :type: int
        """
        if ndevices is None:
            raise ValueError("Invalid value for `ndevices`, must not be `None`")  # noqa: E501

        self._ndevices = ndevices

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
        if issubclass(Data27, dict):
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
        if not isinstance(other, Data27):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
