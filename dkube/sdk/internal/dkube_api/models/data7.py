# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.3.0.10
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Data7(object):
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
        'user': 'str',
        'default_group': 'str',
        'groups': 'list[str]'
    }

    attribute_map = {
        'user': 'user',
        'default_group': 'default_group',
        'groups': 'groups'
    }

    def __init__(self, user=None, default_group=None, groups=None):  # noqa: E501
        """Data7 - a model defined in Swagger"""  # noqa: E501

        self._user = None
        self._default_group = None
        self._groups = None
        self.discriminator = None

        self.user = user
        if default_group is not None:
            self.default_group = default_group
        self.groups = groups

    @property
    def user(self):
        """Gets the user of this Data7.  # noqa: E501


        :return: The user of this Data7.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Data7.


        :param user: The user of this Data7.  # noqa: E501
        :type: str
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def default_group(self):
        """Gets the default_group of this Data7.  # noqa: E501


        :return: The default_group of this Data7.  # noqa: E501
        :rtype: str
        """
        return self._default_group

    @default_group.setter
    def default_group(self, default_group):
        """Sets the default_group of this Data7.


        :param default_group: The default_group of this Data7.  # noqa: E501
        :type: str
        """

        self._default_group = default_group

    @property
    def groups(self):
        """Gets the groups of this Data7.  # noqa: E501


        :return: The groups of this Data7.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this Data7.


        :param groups: The groups of this Data7.  # noqa: E501
        :type: list[str]
        """
        if groups is None:
            raise ValueError("Invalid value for `groups`, must not be `None`")  # noqa: E501

        self._groups = groups

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
        if issubclass(Data7, dict):
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
        if not isinstance(other, Data7):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
