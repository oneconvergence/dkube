# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.5.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InlineResponse20024Datums(object):
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
        'datum': 'DatumModel',
        'versions': 'list[VersionModel]',
        'search': 'InlineResponse20024Search'
    }

    attribute_map = {
        'datum': 'datum',
        'versions': 'versions',
        'search': 'search'
    }

    def __init__(self, datum=None, versions=None, search=None):  # noqa: E501
        """InlineResponse20024Datums - a model defined in Swagger"""  # noqa: E501

        self._datum = None
        self._versions = None
        self._search = None
        self.discriminator = None

        if datum is not None:
            self.datum = datum
        if versions is not None:
            self.versions = versions
        if search is not None:
            self.search = search

    @property
    def datum(self):
        """Gets the datum of this InlineResponse20024Datums.  # noqa: E501


        :return: The datum of this InlineResponse20024Datums.  # noqa: E501
        :rtype: DatumModel
        """
        return self._datum

    @datum.setter
    def datum(self, datum):
        """Sets the datum of this InlineResponse20024Datums.


        :param datum: The datum of this InlineResponse20024Datums.  # noqa: E501
        :type: DatumModel
        """

        self._datum = datum

    @property
    def versions(self):
        """Gets the versions of this InlineResponse20024Datums.  # noqa: E501


        :return: The versions of this InlineResponse20024Datums.  # noqa: E501
        :rtype: list[VersionModel]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this InlineResponse20024Datums.


        :param versions: The versions of this InlineResponse20024Datums.  # noqa: E501
        :type: list[VersionModel]
        """

        self._versions = versions

    @property
    def search(self):
        """Gets the search of this InlineResponse20024Datums.  # noqa: E501


        :return: The search of this InlineResponse20024Datums.  # noqa: E501
        :rtype: InlineResponse20024Search
        """
        return self._search

    @search.setter
    def search(self, search):
        """Sets the search of this InlineResponse20024Datums.


        :param search: The search of this InlineResponse20024Datums.  # noqa: E501
        :type: InlineResponse20024Search
        """

        self._search = search

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
        if issubclass(InlineResponse20024Datums, dict):
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
        if not isinstance(other, InlineResponse20024Datums):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
