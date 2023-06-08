# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.8.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Data25(object):
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
        'groupname': 'str',
        'users': 'list[str]',
        'pools': 'list[str]'
    }

    attribute_map = {
        'upsert': 'upsert',
        'groupname': 'groupname',
        'users': 'users',
        'pools': 'pools'
    }

    def __init__(self, upsert=True, groupname=None, users=None, pools=None):  # noqa: E501
        """Data25 - a model defined in Swagger"""  # noqa: E501

        self._upsert = None
        self._groupname = None
        self._users = None
        self._pools = None
        self.discriminator = None

        if upsert is not None:
            self.upsert = upsert
        self.groupname = groupname
        self.users = users
        self.pools = pools

    @property
    def upsert(self):
        """Gets the upsert of this Data25.  # noqa: E501


        :return: The upsert of this Data25.  # noqa: E501
        :rtype: bool
        """
        return self._upsert

    @upsert.setter
    def upsert(self, upsert):
        """Sets the upsert of this Data25.


        :param upsert: The upsert of this Data25.  # noqa: E501
        :type: bool
        """

        self._upsert = upsert

    @property
    def groupname(self):
        """Gets the groupname of this Data25.  # noqa: E501


        :return: The groupname of this Data25.  # noqa: E501
        :rtype: str
        """
        return self._groupname

    @groupname.setter
    def groupname(self, groupname):
        """Sets the groupname of this Data25.


        :param groupname: The groupname of this Data25.  # noqa: E501
        :type: str
        """
        if groupname is None:
            raise ValueError("Invalid value for `groupname`, must not be `None`")  # noqa: E501
        if groupname is not None and len(groupname) > 255:
            raise ValueError("Invalid value for `groupname`, length must be less than or equal to `255`")  # noqa: E501
        if groupname is not None and len(groupname) < 1:
            raise ValueError("Invalid value for `groupname`, length must be greater than or equal to `1`")  # noqa: E501

        self._groupname = groupname

    @property
    def users(self):
        """Gets the users of this Data25.  # noqa: E501

        List of users by names to be added into this group.  # noqa: E501

        :return: The users of this Data25.  # noqa: E501
        :rtype: list[str]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this Data25.

        List of users by names to be added into this group.  # noqa: E501

        :param users: The users of this Data25.  # noqa: E501
        :type: list[str]
        """
        if users is None:
            raise ValueError("Invalid value for `users`, must not be `None`")  # noqa: E501

        self._users = users

    @property
    def pools(self):
        """Gets the pools of this Data25.  # noqa: E501

        List of pools by names to be added into this group.  # noqa: E501

        :return: The pools of this Data25.  # noqa: E501
        :rtype: list[str]
        """
        return self._pools

    @pools.setter
    def pools(self, pools):
        """Sets the pools of this Data25.

        List of pools by names to be added into this group.  # noqa: E501

        :param pools: The pools of this Data25.  # noqa: E501
        :type: list[str]
        """
        if pools is None:
            raise ValueError("Invalid value for `pools`, must not be `None`")  # noqa: E501

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
        if issubclass(Data25, dict):
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
        if not isinstance(other, Data25):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
