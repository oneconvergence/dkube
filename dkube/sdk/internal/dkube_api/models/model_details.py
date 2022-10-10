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


class ModelDetails(object):
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
        'kind': 'ModelDetailsKind',
        'format': 'str',
        'unsupported': 'ModelDetailsUnsupported',
        'tensorpb': 'ModelDetailsTensorpb'
    }

    attribute_map = {
        'kind': 'kind',
        'format': 'format',
        'unsupported': 'unsupported',
        'tensorpb': 'tensorpb'
    }

    def __init__(self, kind=None, format=None, unsupported=None, tensorpb=None):  # noqa: E501
        """ModelDetails - a model defined in Swagger"""  # noqa: E501

        self._kind = None
        self._format = None
        self._unsupported = None
        self._tensorpb = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if format is not None:
            self.format = format
        if unsupported is not None:
            self.unsupported = unsupported
        if tensorpb is not None:
            self.tensorpb = tensorpb

    @property
    def kind(self):
        """Gets the kind of this ModelDetails.  # noqa: E501


        :return: The kind of this ModelDetails.  # noqa: E501
        :rtype: ModelDetailsKind
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this ModelDetails.


        :param kind: The kind of this ModelDetails.  # noqa: E501
        :type: ModelDetailsKind
        """

        self._kind = kind

    @property
    def format(self):
        """Gets the format of this ModelDetails.  # noqa: E501


        :return: The format of this ModelDetails.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this ModelDetails.


        :param format: The format of this ModelDetails.  # noqa: E501
        :type: str
        """
        allowed_values = ["tensorpb", "unsupported"]  # noqa: E501
        if format not in allowed_values:
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"  # noqa: E501
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def unsupported(self):
        """Gets the unsupported of this ModelDetails.  # noqa: E501


        :return: The unsupported of this ModelDetails.  # noqa: E501
        :rtype: ModelDetailsUnsupported
        """
        return self._unsupported

    @unsupported.setter
    def unsupported(self, unsupported):
        """Sets the unsupported of this ModelDetails.


        :param unsupported: The unsupported of this ModelDetails.  # noqa: E501
        :type: ModelDetailsUnsupported
        """

        self._unsupported = unsupported

    @property
    def tensorpb(self):
        """Gets the tensorpb of this ModelDetails.  # noqa: E501


        :return: The tensorpb of this ModelDetails.  # noqa: E501
        :rtype: ModelDetailsTensorpb
        """
        return self._tensorpb

    @tensorpb.setter
    def tensorpb(self, tensorpb):
        """Sets the tensorpb of this ModelDetails.


        :param tensorpb: The tensorpb of this ModelDetails.  # noqa: E501
        :type: ModelDetailsTensorpb
        """

        self._tensorpb = tensorpb

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
        if issubclass(ModelDetails, dict):
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
        if not isinstance(other, ModelDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
