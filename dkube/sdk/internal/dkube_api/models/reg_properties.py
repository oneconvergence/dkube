# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.3.0.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class RegProperties(object):
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
        'entities': 'EntitySchema',
        'feature_views': 'FeatureViewSchema',
        'odfvs': 'OdfvSchema',
        'sfvs': 'SfvSchema',
        'feature_services': 'FeatureServiceSchema',
        'datasources': 'DatasourceSchema'
    }

    attribute_map = {
        'entities': 'entities',
        'feature_views': 'feature_views',
        'odfvs': 'odfvs',
        'sfvs': 'sfvs',
        'feature_services': 'feature_services',
        'datasources': 'datasources'
    }

    def __init__(self, entities=None, feature_views=None, odfvs=None, sfvs=None, feature_services=None, datasources=None):  # noqa: E501
        """RegProperties - a model defined in Swagger"""  # noqa: E501

        self._entities = None
        self._feature_views = None
        self._odfvs = None
        self._sfvs = None
        self._feature_services = None
        self._datasources = None
        self.discriminator = None

        if entities is not None:
            self.entities = entities
        if feature_views is not None:
            self.feature_views = feature_views
        if odfvs is not None:
            self.odfvs = odfvs
        if sfvs is not None:
            self.sfvs = sfvs
        if feature_services is not None:
            self.feature_services = feature_services
        if datasources is not None:
            self.datasources = datasources

    @property
    def entities(self):
        """Gets the entities of this RegProperties.  # noqa: E501


        :return: The entities of this RegProperties.  # noqa: E501
        :rtype: EntitySchema
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this RegProperties.


        :param entities: The entities of this RegProperties.  # noqa: E501
        :type: EntitySchema
        """

        self._entities = entities

    @property
    def feature_views(self):
        """Gets the feature_views of this RegProperties.  # noqa: E501


        :return: The feature_views of this RegProperties.  # noqa: E501
        :rtype: FeatureViewSchema
        """
        return self._feature_views

    @feature_views.setter
    def feature_views(self, feature_views):
        """Sets the feature_views of this RegProperties.


        :param feature_views: The feature_views of this RegProperties.  # noqa: E501
        :type: FeatureViewSchema
        """

        self._feature_views = feature_views

    @property
    def odfvs(self):
        """Gets the odfvs of this RegProperties.  # noqa: E501


        :return: The odfvs of this RegProperties.  # noqa: E501
        :rtype: OdfvSchema
        """
        return self._odfvs

    @odfvs.setter
    def odfvs(self, odfvs):
        """Sets the odfvs of this RegProperties.


        :param odfvs: The odfvs of this RegProperties.  # noqa: E501
        :type: OdfvSchema
        """

        self._odfvs = odfvs

    @property
    def sfvs(self):
        """Gets the sfvs of this RegProperties.  # noqa: E501


        :return: The sfvs of this RegProperties.  # noqa: E501
        :rtype: SfvSchema
        """
        return self._sfvs

    @sfvs.setter
    def sfvs(self, sfvs):
        """Sets the sfvs of this RegProperties.


        :param sfvs: The sfvs of this RegProperties.  # noqa: E501
        :type: SfvSchema
        """

        self._sfvs = sfvs

    @property
    def feature_services(self):
        """Gets the feature_services of this RegProperties.  # noqa: E501


        :return: The feature_services of this RegProperties.  # noqa: E501
        :rtype: FeatureServiceSchema
        """
        return self._feature_services

    @feature_services.setter
    def feature_services(self, feature_services):
        """Sets the feature_services of this RegProperties.


        :param feature_services: The feature_services of this RegProperties.  # noqa: E501
        :type: FeatureServiceSchema
        """

        self._feature_services = feature_services

    @property
    def datasources(self):
        """Gets the datasources of this RegProperties.  # noqa: E501


        :return: The datasources of this RegProperties.  # noqa: E501
        :rtype: DatasourceSchema
        """
        return self._datasources

    @datasources.setter
    def datasources(self, datasources):
        """Sets the datasources of this RegProperties.


        :param datasources: The datasources of this RegProperties.  # noqa: E501
        :type: DatasourceSchema
        """

        self._datasources = datasources

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
        if issubclass(RegProperties, dict):
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
        if not isinstance(other, RegProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
