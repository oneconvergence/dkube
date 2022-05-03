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


class ModelmonitorMetricsTemplateDef(object):
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
        'id': 'str',
        'name': 'str',
        'category': 'str',
        'metrics': 'dict(str, ModelmonitorMetricDef)'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'category': 'category',
        'metrics': 'metrics'
    }

    def __init__(self, id=None, name=None, category=None, metrics=None):  # noqa: E501
        """ModelmonitorMetricsTemplateDef - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._category = None
        self._metrics = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if category is not None:
            self.category = category
        if metrics is not None:
            self.metrics = metrics

    @property
    def id(self):
        """Gets the id of this ModelmonitorMetricsTemplateDef.  # noqa: E501

        UUID4 id for the resource  # noqa: E501

        :return: The id of this ModelmonitorMetricsTemplateDef.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelmonitorMetricsTemplateDef.

        UUID4 id for the resource  # noqa: E501

        :param id: The id of this ModelmonitorMetricsTemplateDef.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ModelmonitorMetricsTemplateDef.  # noqa: E501

        Name of the template  # noqa: E501

        :return: The name of this ModelmonitorMetricsTemplateDef.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelmonitorMetricsTemplateDef.

        Name of the template  # noqa: E501

        :param name: The name of this ModelmonitorMetricsTemplateDef.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def category(self):
        """Gets the category of this ModelmonitorMetricsTemplateDef.  # noqa: E501

        Model category for which metrics are defined. One of regression, classification.  # noqa: E501

        :return: The category of this ModelmonitorMetricsTemplateDef.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ModelmonitorMetricsTemplateDef.

        Model category for which metrics are defined. One of regression, classification.  # noqa: E501

        :param category: The category of this ModelmonitorMetricsTemplateDef.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def metrics(self):
        """Gets the metrics of this ModelmonitorMetricsTemplateDef.  # noqa: E501


        :return: The metrics of this ModelmonitorMetricsTemplateDef.  # noqa: E501
        :rtype: dict(str, ModelmonitorMetricDef)
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this ModelmonitorMetricsTemplateDef.


        :param metrics: The metrics of this ModelmonitorMetricsTemplateDef.  # noqa: E501
        :type: dict(str, ModelmonitorMetricDef)
        """

        self._metrics = metrics

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
        if issubclass(ModelmonitorMetricsTemplateDef, dict):
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
        if not isinstance(other, ModelmonitorMetricsTemplateDef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
