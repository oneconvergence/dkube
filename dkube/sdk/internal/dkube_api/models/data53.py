# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Data53(object):
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
        'deployment_ids': 'list[str]'
    }

    attribute_map = {
        'deployment_ids': 'deployment_ids'
    }

    def __init__(self, deployment_ids=None):  # noqa: E501
        """Data53 - a model defined in Swagger"""  # noqa: E501

        self._deployment_ids = None
        self.discriminator = None

        if deployment_ids is not None:
            self.deployment_ids = deployment_ids

    @property
    def deployment_ids(self):
        """Gets the deployment_ids of this Data53.  # noqa: E501

        IDs of deployments  # noqa: E501

        :return: The deployment_ids of this Data53.  # noqa: E501
        :rtype: list[str]
        """
        return self._deployment_ids

    @deployment_ids.setter
    def deployment_ids(self, deployment_ids):
        """Sets the deployment_ids of this Data53.

        IDs of deployments  # noqa: E501

        :param deployment_ids: The deployment_ids of this Data53.  # noqa: E501
        :type: list[str]
        """

        self._deployment_ids = deployment_ids

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
        if issubclass(Data53, dict):
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
        if not isinstance(other, Data53):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
