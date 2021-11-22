# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0.0.4
    
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
        'options': 'list[UserProfileOptions]',
        'shareddir': 'str',
        'extra_mounts': 'list[str]',
        'limits': 'UserProfileLimits',
        'fsx_profile': 'list[FsxProfile]'
    }

    attribute_map = {
        'name': 'name',
        'uid': 'uid',
        'user': 'user',
        'homedir': 'homedir',
        'options': 'options',
        'shareddir': 'shareddir',
        'extra_mounts': 'extra_mounts',
        'limits': 'limits',
        'fsx_profile': 'fsx_profile'
    }

    def __init__(self, name=None, uid=None, user=None, homedir=None, options=None, shareddir=None, extra_mounts=None, limits=None, fsx_profile=None):  # noqa: E501
        """UserProfile - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._uid = None
        self._user = None
        self._homedir = None
        self._options = None
        self._shareddir = None
        self._extra_mounts = None
        self._limits = None
        self._fsx_profile = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if uid is not None:
            self.uid = uid
        if user is not None:
            self.user = user
        if homedir is not None:
            self.homedir = homedir
        if options is not None:
            self.options = options
        if shareddir is not None:
            self.shareddir = shareddir
        if extra_mounts is not None:
            self.extra_mounts = extra_mounts
        if limits is not None:
            self.limits = limits
        if fsx_profile is not None:
            self.fsx_profile = fsx_profile

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
    def options(self):
        """Gets the options of this UserProfile.  # noqa: E501


        :return: The options of this UserProfile.  # noqa: E501
        :rtype: list[UserProfileOptions]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this UserProfile.


        :param options: The options of this UserProfile.  # noqa: E501
        :type: list[UserProfileOptions]
        """

        self._options = options

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
    def extra_mounts(self):
        """Gets the extra_mounts of this UserProfile.  # noqa: E501


        :return: The extra_mounts of this UserProfile.  # noqa: E501
        :rtype: list[str]
        """
        return self._extra_mounts

    @extra_mounts.setter
    def extra_mounts(self, extra_mounts):
        """Sets the extra_mounts of this UserProfile.


        :param extra_mounts: The extra_mounts of this UserProfile.  # noqa: E501
        :type: list[str]
        """

        self._extra_mounts = extra_mounts

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

    @property
    def fsx_profile(self):
        """Gets the fsx_profile of this UserProfile.  # noqa: E501


        :return: The fsx_profile of this UserProfile.  # noqa: E501
        :rtype: list[FsxProfile]
        """
        return self._fsx_profile

    @fsx_profile.setter
    def fsx_profile(self, fsx_profile):
        """Sets the fsx_profile of this UserProfile.


        :param fsx_profile: The fsx_profile of this UserProfile.  # noqa: E501
        :type: list[FsxProfile]
        """

        self._fsx_profile = fsx_profile

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
