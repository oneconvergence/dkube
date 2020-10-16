# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.2.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class UserProfile(object):
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
        'uid': 'str',
        'user': 'str',
        'homedir': 'str',
        'shareddir': 'str',
        'limits': 'UserProfileLimits'
    }

    attribute_map = {
        'name': 'name',
        'uid': 'uid',
        'user': 'user',
        'homedir': 'homedir',
        'shareddir': 'shareddir',
        'limits': 'limits'
    }

    def __init__(self, name=None, uid=None, user=None, homedir=None, shareddir=None, limits=None):  # noqa: E501
        """UserProfile - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._uid = None
        self._user = None
        self._homedir = None
        self._shareddir = None
        self._limits = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if uid is not None:
            self.uid = uid
        if user is not None:
            self.user = user
        if homedir is not None:
            self.homedir = homedir
        if shareddir is not None:
            self.shareddir = shareddir
        if limits is not None:
            self.limits = limits

    @property
    def name(self):
        """Gets the name of this UserProfile.  # noqa: E501

        Unique name of the profile  # noqa: E501

        :return: The name of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserProfile.

        Unique name of the profile  # noqa: E501

        :param name: The name of this UserProfile.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def uid(self):
        """Gets the uid of this UserProfile.  # noqa: E501


        :return: The uid of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this UserProfile.


        :param uid: The uid of this UserProfile.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def user(self):
        """Gets the user of this UserProfile.  # noqa: E501


        :return: The user of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this UserProfile.


        :param user: The user of this UserProfile.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def homedir(self):
        """Gets the homedir of this UserProfile.  # noqa: E501


        :return: The homedir of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._homedir

    @homedir.setter
    def homedir(self, homedir):
        """Sets the homedir of this UserProfile.


        :param homedir: The homedir of this UserProfile.  # noqa: E501
        :type: str
        """

        self._homedir = homedir

    @property
    def shareddir(self):
        """Gets the shareddir of this UserProfile.  # noqa: E501


        :return: The shareddir of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._shareddir

    @shareddir.setter
    def shareddir(self, shareddir):
        """Sets the shareddir of this UserProfile.


        :param shareddir: The shareddir of this UserProfile.  # noqa: E501
        :type: str
        """

        self._shareddir = shareddir

    @property
    def limits(self):
        """Gets the limits of this UserProfile.  # noqa: E501


        :return: The limits of this UserProfile.  # noqa: E501
        :rtype: UserProfileLimits
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """Sets the limits of this UserProfile.


        :param limits: The limits of this UserProfile.  # noqa: E501
        :type: UserProfileLimits
        """

        self._limits = limits

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
        if issubclass(UserProfile, dict):
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
        if not isinstance(other, UserProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other