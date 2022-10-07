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


class InlineResponse20020Data(object):
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
        'dnsname': 'str',
        'volumehandle': 'str',
        'mountname': 'str'
    }

    attribute_map = {
        'name': 'name',
        'dnsname': 'dnsname',
        'volumehandle': 'volumehandle',
        'mountname': 'mountname'
    }

    def __init__(self, name=None, dnsname=None, volumehandle=None, mountname=None):  # noqa: E501
        """InlineResponse20020Data - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._dnsname = None
        self._volumehandle = None
        self._mountname = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if dnsname is not None:
            self.dnsname = dnsname
        if volumehandle is not None:
            self.volumehandle = volumehandle
        if mountname is not None:
            self.mountname = mountname

    @property
    def name(self):
        """Gets the name of this InlineResponse20020Data.  # noqa: E501


        :return: The name of this InlineResponse20020Data.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20020Data.


        :param name: The name of this InlineResponse20020Data.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def dnsname(self):
        """Gets the dnsname of this InlineResponse20020Data.  # noqa: E501


        :return: The dnsname of this InlineResponse20020Data.  # noqa: E501
        :rtype: str
        """
        return self._dnsname

    @dnsname.setter
    def dnsname(self, dnsname):
        """Sets the dnsname of this InlineResponse20020Data.


        :param dnsname: The dnsname of this InlineResponse20020Data.  # noqa: E501
        :type: str
        """

        self._dnsname = dnsname

    @property
    def volumehandle(self):
        """Gets the volumehandle of this InlineResponse20020Data.  # noqa: E501


        :return: The volumehandle of this InlineResponse20020Data.  # noqa: E501
        :rtype: str
        """
        return self._volumehandle

    @volumehandle.setter
    def volumehandle(self, volumehandle):
        """Sets the volumehandle of this InlineResponse20020Data.


        :param volumehandle: The volumehandle of this InlineResponse20020Data.  # noqa: E501
        :type: str
        """

        self._volumehandle = volumehandle

    @property
    def mountname(self):
        """Gets the mountname of this InlineResponse20020Data.  # noqa: E501


        :return: The mountname of this InlineResponse20020Data.  # noqa: E501
        :rtype: str
        """
        return self._mountname

    @mountname.setter
    def mountname(self, mountname):
        """Sets the mountname of this InlineResponse20020Data.


        :param mountname: The mountname of this InlineResponse20020Data.  # noqa: E501
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
        if issubclass(InlineResponse20020Data, dict):
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
        if not isinstance(other, InlineResponse20020Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
