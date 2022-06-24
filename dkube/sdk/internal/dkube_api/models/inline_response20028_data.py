# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.3.0.14
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InlineResponse20028Data(object):
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
        'owner': 'str',
        'datums': 'list[DatumModel]'
    }

    attribute_map = {
        'owner': 'owner',
        'datums': 'datums'
    }

    def __init__(self, owner=None, datums=None):  # noqa: E501
        """InlineResponse20028Data - a model defined in Swagger"""  # noqa: E501

        self._owner = None
        self._datums = None
        self.discriminator = None

        if owner is not None:
            self.owner = owner
        if datums is not None:
            self.datums = datums

    @property
    def owner(self):
        """Gets the owner of this InlineResponse20028Data.  # noqa: E501


        :return: The owner of this InlineResponse20028Data.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this InlineResponse20028Data.


        :param owner: The owner of this InlineResponse20028Data.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def datums(self):
        """Gets the datums of this InlineResponse20028Data.  # noqa: E501


        :return: The datums of this InlineResponse20028Data.  # noqa: E501
        :rtype: list[DatumModel]
        """
        return self._datums

    @datums.setter
    def datums(self, datums):
        """Sets the datums of this InlineResponse20028Data.


        :param datums: The datums of this InlineResponse20028Data.  # noqa: E501
        :type: list[DatumModel]
        """

        self._datums = datums

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
        if issubclass(InlineResponse20028Data, dict):
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
        if not isinstance(other, InlineResponse20028Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
