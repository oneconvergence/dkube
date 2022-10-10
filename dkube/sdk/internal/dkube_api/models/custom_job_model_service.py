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


class CustomJobModelService(object):
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
        'targetport': 'int',
        'exposeas': 'str'
    }

    attribute_map = {
        'targetport': 'targetport',
        'exposeas': 'exposeas'
    }

    def __init__(self, targetport=None, exposeas=None):  # noqa: E501
        """CustomJobModelService - a model defined in Swagger"""  # noqa: E501

        self._targetport = None
        self._exposeas = None
        self.discriminator = None

        if targetport is not None:
            self.targetport = targetport
        if exposeas is not None:
            self.exposeas = exposeas

    @property
    def targetport(self):
        """Gets the targetport of this CustomJobModelService.  # noqa: E501


        :return: The targetport of this CustomJobModelService.  # noqa: E501
        :rtype: int
        """
        return self._targetport

    @targetport.setter
    def targetport(self, targetport):
        """Sets the targetport of this CustomJobModelService.


        :param targetport: The targetport of this CustomJobModelService.  # noqa: E501
        :type: int
        """

        self._targetport = targetport

    @property
    def exposeas(self):
        """Gets the exposeas of this CustomJobModelService.  # noqa: E501


        :return: The exposeas of this CustomJobModelService.  # noqa: E501
        :rtype: str
        """
        return self._exposeas

    @exposeas.setter
    def exposeas(self, exposeas):
        """Sets the exposeas of this CustomJobModelService.


        :param exposeas: The exposeas of this CustomJobModelService.  # noqa: E501
        :type: str
        """
        allowed_values = ["nodeport", "dkubeproxy", "clusterip"]  # noqa: E501
        if exposeas not in allowed_values:
            raise ValueError(
                "Invalid value for `exposeas` ({0}), must be one of {1}"  # noqa: E501
                .format(exposeas, allowed_values)
            )

        self._exposeas = exposeas

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
        if issubclass(CustomJobModelService, dict):
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
        if not isinstance(other, CustomJobModelService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
