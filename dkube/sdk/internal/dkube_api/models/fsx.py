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


class Fsx(object):
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
        'dnsname': 'str',
        'volumehandle': 'str',
        'mountname': 'str'
    }

    attribute_map = {
        'dnsname': 'dnsname',
        'volumehandle': 'volumehandle',
        'mountname': 'mountname'
    }

    def __init__(self, dnsname=None, volumehandle=None, mountname=None):  # noqa: E501
        """Fsx - a model defined in Swagger"""  # noqa: E501

        self._dnsname = None
        self._volumehandle = None
        self._mountname = None
        self.discriminator = None

        if dnsname is not None:
            self.dnsname = dnsname
        if volumehandle is not None:
            self.volumehandle = volumehandle
        if mountname is not None:
            self.mountname = mountname

    @property
    def dnsname(self):
        """Gets the dnsname of this Fsx.  # noqa: E501


        :return: The dnsname of this Fsx.  # noqa: E501
        :rtype: str
        """
        return self._dnsname

    @dnsname.setter
    def dnsname(self, dnsname):
        """Sets the dnsname of this Fsx.


        :param dnsname: The dnsname of this Fsx.  # noqa: E501
        :type: str
        """

        self._dnsname = dnsname

    @property
    def volumehandle(self):
        """Gets the volumehandle of this Fsx.  # noqa: E501


        :return: The volumehandle of this Fsx.  # noqa: E501
        :rtype: str
        """
        return self._volumehandle

    @volumehandle.setter
    def volumehandle(self, volumehandle):
        """Sets the volumehandle of this Fsx.


        :param volumehandle: The volumehandle of this Fsx.  # noqa: E501
        :type: str
        """

        self._volumehandle = volumehandle

    @property
    def mountname(self):
        """Gets the mountname of this Fsx.  # noqa: E501


        :return: The mountname of this Fsx.  # noqa: E501
        :rtype: str
        """
        return self._mountname

    @mountname.setter
    def mountname(self, mountname):
        """Sets the mountname of this Fsx.


        :param mountname: The mountname of this Fsx.  # noqa: E501
        :type: str
        """

        self._mountname = mountname

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
        if issubclass(Fsx, dict):
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
        if not isinstance(other, Fsx):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
