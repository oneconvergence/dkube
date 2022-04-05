# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.3.0.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class UserModel(object):
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
        'version': 'str',
        'name': 'str',
        'role': 'str',
        'created_at': 'TimeStamps',
        'status': 'str',
        'default_group': 'str',
        'groups': 'list[str]',
        'generated': 'UserModelGenerated'
    }

    attribute_map = {
        'version': 'version',
        'name': 'name',
        'role': 'role',
        'created_at': 'created_at',
        'status': 'status',
        'default_group': 'default_group',
        'groups': 'groups',
        'generated': 'generated'
    }

    def __init__(self, version=None, name=None, role=None, created_at=None, status=None, default_group=None, groups=None, generated=None):  # noqa: E501
        """UserModel - a model defined in Swagger"""  # noqa: E501

        self._version = None
        self._name = None
        self._role = None
        self._created_at = None
        self._status = None
        self._default_group = None
        self._groups = None
        self._generated = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if name is not None:
            self.name = name
        if role is not None:
            self.role = role
        if created_at is not None:
            self.created_at = created_at
        if status is not None:
            self.status = status
        if default_group is not None:
            self.default_group = default_group
        if groups is not None:
            self.groups = groups
        if generated is not None:
            self.generated = generated

    @property
    def version(self):
        """Gets the version of this UserModel.  # noqa: E501


        :return: The version of this UserModel.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this UserModel.


        :param version: The version of this UserModel.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def name(self):
        """Gets the name of this UserModel.  # noqa: E501


        :return: The name of this UserModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserModel.


        :param name: The name of this UserModel.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def role(self):
        """Gets the role of this UserModel.  # noqa: E501


        :return: The role of this UserModel.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this UserModel.


        :param role: The role of this UserModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["operator", "datascientist"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"  # noqa: E501
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def created_at(self):
        """Gets the created_at of this UserModel.  # noqa: E501


        :return: The created_at of this UserModel.  # noqa: E501
        :rtype: TimeStamps
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UserModel.


        :param created_at: The created_at of this UserModel.  # noqa: E501
        :type: TimeStamps
        """

        self._created_at = created_at

    @property
    def status(self):
        """Gets the status of this UserModel.  # noqa: E501


        :return: The status of this UserModel.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UserModel.


        :param status: The status of this UserModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["onboarding", "onboarded"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def default_group(self):
        """Gets the default_group of this UserModel.  # noqa: E501


        :return: The default_group of this UserModel.  # noqa: E501
        :rtype: str
        """
        return self._default_group

    @default_group.setter
    def default_group(self, default_group):
        """Sets the default_group of this UserModel.


        :param default_group: The default_group of this UserModel.  # noqa: E501
        :type: str
        """

        self._default_group = default_group

    @property
    def groups(self):
        """Gets the groups of this UserModel.  # noqa: E501


        :return: The groups of this UserModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this UserModel.


        :param groups: The groups of this UserModel.  # noqa: E501
        :type: list[str]
        """

        self._groups = groups

    @property
    def generated(self):
        """Gets the generated of this UserModel.  # noqa: E501


        :return: The generated of this UserModel.  # noqa: E501
        :rtype: UserModelGenerated
        """
        return self._generated

    @generated.setter
    def generated(self, generated):
        """Sets the generated of this UserModel.


        :param generated: The generated of this UserModel.  # noqa: E501
        :type: UserModelGenerated
        """

        self._generated = generated

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
        if issubclass(UserModel, dict):
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
        if not isinstance(other, UserModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
