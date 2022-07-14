# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Data4(object):
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
        'users': 'list[str]',
        'role': 'str',
        'default_group': 'str',
        'groups': 'list[str]'
    }

    attribute_map = {
        'users': 'users',
        'role': 'role',
        'default_group': 'default_group',
        'groups': 'groups'
    }

    def __init__(self, users=None, role=None, default_group=None, groups=None):  # noqa: E501
        """Data4 - a model defined in Swagger"""  # noqa: E501

        self._users = None
        self._role = None
        self._default_group = None
        self._groups = None
        self.discriminator = None

        self.users = users
        if role is not None:
            self.role = role
        if default_group is not None:
            self.default_group = default_group
        if groups is not None:
            self.groups = groups

    @property
    def users(self):
        """Gets the users of this Data4.  # noqa: E501

        Name of the valid users. Each  user should be a valid github user.  # noqa: E501

        :return: The users of this Data4.  # noqa: E501
        :rtype: list[str]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this Data4.

        Name of the valid users. Each  user should be a valid github user.  # noqa: E501

        :param users: The users of this Data4.  # noqa: E501
        :type: list[str]
        """
        if users is None:
            raise ValueError("Invalid value for `users`, must not be `None`")  # noqa: E501

        self._users = users

    @property
    def role(self):
        """Gets the role of this Data4.  # noqa: E501


        :return: The role of this Data4.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this Data4.


        :param role: The role of this Data4.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def default_group(self):
        """Gets the default_group of this Data4.  # noqa: E501


        :return: The default_group of this Data4.  # noqa: E501
        :rtype: str
        """
        return self._default_group

    @default_group.setter
    def default_group(self, default_group):
        """Sets the default_group of this Data4.


        :param default_group: The default_group of this Data4.  # noqa: E501
        :type: str
        """

        self._default_group = default_group

    @property
    def groups(self):
        """Gets the groups of this Data4.  # noqa: E501

        Name of the valid group. This should be a valid group existing in dkube.  # noqa: E501

        :return: The groups of this Data4.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this Data4.

        Name of the valid group. This should be a valid group existing in dkube.  # noqa: E501

        :param groups: The groups of this Data4.  # noqa: E501
        :type: list[str]
        """

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
        if issubclass(Data4, dict):
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
        if not isinstance(other, Data4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
