# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.5.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ModelmonitorFeaturesSpecDef(object):
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
        'features': 'list[ModelmonitorSchemaFeature]',
        'invalid_alerts': 'dict(str, str)'
    }

    attribute_map = {
        'features': 'features',
        'invalid_alerts': 'invalid_alerts'
    }

    def __init__(self, features=None, invalid_alerts=None):  # noqa: E501
        """ModelmonitorFeaturesSpecDef - a model defined in Swagger"""  # noqa: E501

        self._features = None
        self._invalid_alerts = None
        self.discriminator = None

        if features is not None:
            self.features = features
        if invalid_alerts is not None:
            self.invalid_alerts = invalid_alerts

    @property
    def features(self):
        """Gets the features of this ModelmonitorFeaturesSpecDef.  # noqa: E501


        :return: The features of this ModelmonitorFeaturesSpecDef.  # noqa: E501
        :rtype: list[ModelmonitorSchemaFeature]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this ModelmonitorFeaturesSpecDef.


        :param features: The features of this ModelmonitorFeaturesSpecDef.  # noqa: E501
        :type: list[ModelmonitorSchemaFeature]
        """

        self._features = features

    @property
    def invalid_alerts(self):
        """Gets the invalid_alerts of this ModelmonitorFeaturesSpecDef.  # noqa: E501


        :return: The invalid_alerts of this ModelmonitorFeaturesSpecDef.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._invalid_alerts

    @invalid_alerts.setter
    def invalid_alerts(self, invalid_alerts):
        """Sets the invalid_alerts of this ModelmonitorFeaturesSpecDef.


        :param invalid_alerts: The invalid_alerts of this ModelmonitorFeaturesSpecDef.  # noqa: E501
        :type: dict(str, str)
        """

        self._invalid_alerts = invalid_alerts

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
        if issubclass(ModelmonitorFeaturesSpecDef, dict):
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
        if not isinstance(other, ModelmonitorFeaturesSpecDef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
