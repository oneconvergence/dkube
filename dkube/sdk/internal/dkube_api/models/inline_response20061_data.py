# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.3.0.10
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InlineResponse20061Data(object):
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
        'featureset': 'FeatureSetDef',
        'featurespec': 'list[FeatureSpecDef]',
        'versions': 'list[InlineResponse20061DataVersions]'
    }

    attribute_map = {
        'featureset': 'featureset',
        'featurespec': 'featurespec',
        'versions': 'versions'
    }

    def __init__(self, featureset=None, featurespec=None, versions=None):  # noqa: E501
        """InlineResponse20061Data - a model defined in Swagger"""  # noqa: E501

        self._featureset = None
        self._featurespec = None
        self._versions = None
        self.discriminator = None

        if featureset is not None:
            self.featureset = featureset
        if featurespec is not None:
            self.featurespec = featurespec
        if versions is not None:
            self.versions = versions

    @property
    def featureset(self):
        """Gets the featureset of this InlineResponse20061Data.  # noqa: E501


        :return: The featureset of this InlineResponse20061Data.  # noqa: E501
        :rtype: FeatureSetDef
        """
        return self._featureset

    @featureset.setter
    def featureset(self, featureset):
        """Sets the featureset of this InlineResponse20061Data.


        :param featureset: The featureset of this InlineResponse20061Data.  # noqa: E501
        :type: FeatureSetDef
        """

        self._featureset = featureset

    @property
    def featurespec(self):
        """Gets the featurespec of this InlineResponse20061Data.  # noqa: E501


        :return: The featurespec of this InlineResponse20061Data.  # noqa: E501
        :rtype: list[FeatureSpecDef]
        """
        return self._featurespec

    @featurespec.setter
    def featurespec(self, featurespec):
        """Sets the featurespec of this InlineResponse20061Data.


        :param featurespec: The featurespec of this InlineResponse20061Data.  # noqa: E501
        :type: list[FeatureSpecDef]
        """

        self._featurespec = featurespec

    @property
    def versions(self):
        """Gets the versions of this InlineResponse20061Data.  # noqa: E501


        :return: The versions of this InlineResponse20061Data.  # noqa: E501
        :rtype: list[InlineResponse20061DataVersions]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this InlineResponse20061Data.


        :param versions: The versions of this InlineResponse20061Data.  # noqa: E501
        :type: list[InlineResponse20061DataVersions]
        """

        self._versions = versions

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
        if issubclass(InlineResponse20061Data, dict):
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
        if not isinstance(other, InlineResponse20061Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
