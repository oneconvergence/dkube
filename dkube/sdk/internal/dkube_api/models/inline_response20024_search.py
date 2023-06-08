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


class InlineResponse20024Search(object):
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
        'datasets': 'list[InlineResponse20024SearchDatasets]'
    }

    attribute_map = {
        'datasets': 'datasets'
    }

    def __init__(self, datasets=None):  # noqa: E501
        """InlineResponse20024Search - a model defined in Swagger"""  # noqa: E501

        self._datasets = None
        self.discriminator = None

        if datasets is not None:
            self.datasets = datasets

    @property
    def datasets(self):
        """Gets the datasets of this InlineResponse20024Search.  # noqa: E501

        filled use.  # noqa: E501

        :return: The datasets of this InlineResponse20024Search.  # noqa: E501
        :rtype: list[InlineResponse20024SearchDatasets]
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets):
        """Sets the datasets of this InlineResponse20024Search.

        filled use.  # noqa: E501

        :param datasets: The datasets of this InlineResponse20024Search.  # noqa: E501
        :type: list[InlineResponse20024SearchDatasets]
        """

        self._datasets = datasets

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
        if issubclass(InlineResponse20024Search, dict):
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
        if not isinstance(other, InlineResponse20024Search):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
