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


class D3APIKeyModel(object):
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
        'apikey': 'str',
        'revoked': 'bool',
        'generated': 'ModelCatalogItemGenerated'
    }

    attribute_map = {
        'version': 'version',
        'apikey': 'apikey',
        'revoked': 'revoked',
        'generated': 'generated'
    }

    def __init__(self, version=None, apikey=None, revoked=False, generated=None):  # noqa: E501
        """D3APIKeyModel - a model defined in Swagger"""  # noqa: E501

        self._version = None
        self._apikey = None
        self._revoked = None
        self._generated = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if apikey is not None:
            self.apikey = apikey
        if revoked is not None:
            self.revoked = revoked
        if generated is not None:
            self.generated = generated

    @property
    def version(self):
        """Gets the version of this D3APIKeyModel.  # noqa: E501


        :return: The version of this D3APIKeyModel.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this D3APIKeyModel.


        :param version: The version of this D3APIKeyModel.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def apikey(self):
        """Gets the apikey of this D3APIKeyModel.  # noqa: E501


        :return: The apikey of this D3APIKeyModel.  # noqa: E501
        :rtype: str
        """
        return self._apikey

    @apikey.setter
    def apikey(self, apikey):
        """Sets the apikey of this D3APIKeyModel.


        :param apikey: The apikey of this D3APIKeyModel.  # noqa: E501
        :type: str
        """

        self._apikey = apikey

    @property
    def revoked(self):
        """Gets the revoked of this D3APIKeyModel.  # noqa: E501


        :return: The revoked of this D3APIKeyModel.  # noqa: E501
        :rtype: bool
        """
        return self._revoked

    @revoked.setter
    def revoked(self, revoked):
        """Sets the revoked of this D3APIKeyModel.


        :param revoked: The revoked of this D3APIKeyModel.  # noqa: E501
        :type: bool
        """

        self._revoked = revoked

    @property
    def generated(self):
        """Gets the generated of this D3APIKeyModel.  # noqa: E501


        :return: The generated of this D3APIKeyModel.  # noqa: E501
        :rtype: ModelCatalogItemGenerated
        """
        return self._generated

    @generated.setter
    def generated(self, generated):
        """Sets the generated of this D3APIKeyModel.


        :param generated: The generated of this D3APIKeyModel.  # noqa: E501
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
        if issubclass(D3APIKeyModel, dict):
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
        if not isinstance(other, D3APIKeyModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
