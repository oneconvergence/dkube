# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.3.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CapabilitiesModel(object):
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
        'resources': 'list[str]',
        'access': 'list[str]'
    }

    attribute_map = {
        'resources': 'resources',
        'access': 'access'
    }

    def __init__(self, resources=None, access=None):  # noqa: E501
        """CapabilitiesModel - a model defined in Swagger"""  # noqa: E501

        self._resources = None
        self._access = None
        self.discriminator = None

        if resources is not None:
            self.resources = resources
        if access is not None:
            self.access = access

    @property
    def resources(self):
        """Gets the resources of this CapabilitiesModel.  # noqa: E501


        :return: The resources of this CapabilitiesModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this CapabilitiesModel.


        :param resources: The resources of this CapabilitiesModel.  # noqa: E501
        :type: list[str]
        """

        self._resources = resources

    @property
    def access(self):
        """Gets the access of this CapabilitiesModel.  # noqa: E501


        :return: The access of this CapabilitiesModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._access

    @access.setter
    def access(self, access):
        """Sets the access of this CapabilitiesModel.


        :param access: The access of this CapabilitiesModel.  # noqa: E501
        :type: list[str]
        """

        self._access = access

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
        if issubclass(CapabilitiesModel, dict):
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
        if not isinstance(other, CapabilitiesModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
