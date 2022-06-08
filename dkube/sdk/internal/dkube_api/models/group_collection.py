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


class GroupCollection(object):
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
        'group': 'GroupModel',
        'users': 'list[GroupCollectionUsers]',
        'pools': 'list[PoolCollection]'
    }

    attribute_map = {
        'group': 'group',
        'users': 'users',
        'pools': 'pools'
    }

    def __init__(self, group=None, users=None, pools=None):  # noqa: E501
        """GroupCollection - a model defined in Swagger"""  # noqa: E501

        self._group = None
        self._users = None
        self._pools = None
        self.discriminator = None

        if group is not None:
            self.group = group
        if users is not None:
            self.users = users
        if pools is not None:
            self.pools = pools

    @property
    def group(self):
        """Gets the group of this GroupCollection.  # noqa: E501


        :return: The group of this GroupCollection.  # noqa: E501
        :rtype: GroupModel
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this GroupCollection.


        :param group: The group of this GroupCollection.  # noqa: E501
        :type: GroupModel
        """

        self._group = group

    @property
    def users(self):
        """Gets the users of this GroupCollection.  # noqa: E501


        :return: The users of this GroupCollection.  # noqa: E501
        :rtype: list[GroupCollectionUsers]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this GroupCollection.


        :param users: The users of this GroupCollection.  # noqa: E501
        :type: list[GroupCollectionUsers]
        """

        self._users = users

    @property
    def pools(self):
        """Gets the pools of this GroupCollection.  # noqa: E501


        :return: The pools of this GroupCollection.  # noqa: E501
        :rtype: list[PoolCollection]
        """
        return self._pools

    @pools.setter
    def pools(self, pools):
        """Sets the pools of this GroupCollection.


        :param pools: The pools of this GroupCollection.  # noqa: E501
        :type: list[PoolCollection]
        """

        self._pools = pools

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
        if issubclass(GroupCollection, dict):
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
        if not isinstance(other, GroupCollection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
