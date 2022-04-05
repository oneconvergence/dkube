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


class ClusterRoleDelegationDef(object):
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
        'account_id': 'str',
        'external_id': 'str',
        'role_name': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'external_id': 'external_id',
        'role_name': 'role_name'
    }

    def __init__(self, account_id=None, external_id=None, role_name=None):  # noqa: E501
        """ClusterRoleDelegationDef - a model defined in Swagger"""  # noqa: E501

        self._account_id = None
        self._external_id = None
        self._role_name = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if external_id is not None:
            self.external_id = external_id
        if role_name is not None:
            self.role_name = role_name

    @property
    def account_id(self):
        """Gets the account_id of this ClusterRoleDelegationDef.  # noqa: E501


        :return: The account_id of this ClusterRoleDelegationDef.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ClusterRoleDelegationDef.


        :param account_id: The account_id of this ClusterRoleDelegationDef.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def external_id(self):
        """Gets the external_id of this ClusterRoleDelegationDef.  # noqa: E501


        :return: The external_id of this ClusterRoleDelegationDef.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this ClusterRoleDelegationDef.


        :param external_id: The external_id of this ClusterRoleDelegationDef.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def role_name(self):
        """Gets the role_name of this ClusterRoleDelegationDef.  # noqa: E501


        :return: The role_name of this ClusterRoleDelegationDef.  # noqa: E501
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """Sets the role_name of this ClusterRoleDelegationDef.


        :param role_name: The role_name of this ClusterRoleDelegationDef.  # noqa: E501
        :type: str
        """

        self._role_name = role_name

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
        if issubclass(ClusterRoleDelegationDef, dict):
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
        if not isinstance(other, ClusterRoleDelegationDef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
