# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.2.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GroupModel(object):
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
        'providertype': 'str',
        'provider': 'str',
        'created_at': 'TimeStamps',
        'generated': 'ModelCatalogItemGenerated'
    }

    attribute_map = {
        'version': 'version',
        'name': 'name',
        'providertype': 'providertype',
        'provider': 'provider',
        'created_at': 'created_at',
        'generated': 'generated'
    }

    def __init__(self, version=None, name=None, providertype=None, provider=None, created_at=None, generated=None):  # noqa: E501
        """GroupModel - a model defined in Swagger"""  # noqa: E501

        self._version = None
        self._name = None
        self._providertype = None
        self._provider = None
        self._created_at = None
        self._generated = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if name is not None:
            self.name = name
        if providertype is not None:
            self.providertype = providertype
        if provider is not None:
            self.provider = provider
        if created_at is not None:
            self.created_at = created_at
        if generated is not None:
            self.generated = generated

    @property
    def version(self):
        """Gets the version of this GroupModel.  # noqa: E501


        :return: The version of this GroupModel.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this GroupModel.


        :param version: The version of this GroupModel.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def name(self):
        """Gets the name of this GroupModel.  # noqa: E501


        :return: The name of this GroupModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GroupModel.


        :param name: The name of this GroupModel.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def providertype(self):
        """Gets the providertype of this GroupModel.  # noqa: E501


        :return: The providertype of this GroupModel.  # noqa: E501
        :rtype: str
        """
        return self._providertype

    @providertype.setter
    def providertype(self, providertype):
        """Sets the providertype of this GroupModel.


        :param providertype: The providertype of this GroupModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["external"]  # noqa: E501
        if providertype not in allowed_values:
            raise ValueError(
                "Invalid value for `providertype` ({0}), must be one of {1}"  # noqa: E501
                .format(providertype, allowed_values)
            )

        self._providertype = providertype

    @property
    def provider(self):
        """Gets the provider of this GroupModel.  # noqa: E501


        :return: The provider of this GroupModel.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this GroupModel.


        :param provider: The provider of this GroupModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["github"]  # noqa: E501
        if provider not in allowed_values:
            raise ValueError(
                "Invalid value for `provider` ({0}), must be one of {1}"  # noqa: E501
                .format(provider, allowed_values)
            )

        self._provider = provider

    @property
    def created_at(self):
        """Gets the created_at of this GroupModel.  # noqa: E501


        :return: The created_at of this GroupModel.  # noqa: E501
        :rtype: TimeStamps
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GroupModel.


        :param created_at: The created_at of this GroupModel.  # noqa: E501
        :type: TimeStamps
        """

        self._created_at = created_at

    @property
    def generated(self):
        """Gets the generated of this GroupModel.  # noqa: E501


        :return: The generated of this GroupModel.  # noqa: E501
        :rtype: ModelCatalogItemGenerated
        """
        return self._generated

    @generated.setter
    def generated(self, generated):
        """Sets the generated of this GroupModel.


        :param generated: The generated of this GroupModel.  # noqa: E501
        :type: ModelCatalogItemGenerated
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
        if issubclass(GroupModel, dict):
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
        if not isinstance(other, GroupModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
