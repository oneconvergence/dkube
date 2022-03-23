# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.2.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class FeatureViewResponse(object):
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
        'name': 'str',
        'entities': 'list[str]',
        'project': 'str',
        'userid': 'str'
    }

    attribute_map = {
        'name': 'name',
        'entities': 'entities',
        'project': 'project',
        'userid': 'userid'
    }

    def __init__(self, name=None, entities=None, project=None, userid=None):  # noqa: E501
        """FeatureViewResponse - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._entities = None
        self._project = None
        self._userid = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if entities is not None:
            self.entities = entities
        if project is not None:
            self.project = project
        if userid is not None:
            self.userid = userid

    @property
    def name(self):
        """Gets the name of this FeatureViewResponse.  # noqa: E501


        :return: The name of this FeatureViewResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FeatureViewResponse.


        :param name: The name of this FeatureViewResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def entities(self):
        """Gets the entities of this FeatureViewResponse.  # noqa: E501


        :return: The entities of this FeatureViewResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this FeatureViewResponse.


        :param entities: The entities of this FeatureViewResponse.  # noqa: E501
        :type: list[str]
        """

        self._entities = entities

    @property
    def project(self):
        """Gets the project of this FeatureViewResponse.  # noqa: E501


        :return: The project of this FeatureViewResponse.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this FeatureViewResponse.


        :param project: The project of this FeatureViewResponse.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def userid(self):
        """Gets the userid of this FeatureViewResponse.  # noqa: E501


        :return: The userid of this FeatureViewResponse.  # noqa: E501
        :rtype: str
        """
        return self._userid

    @userid.setter
    def userid(self, userid):
        """Sets the userid of this FeatureViewResponse.


        :param userid: The userid of this FeatureViewResponse.  # noqa: E501
        :type: str
        """

        self._userid = userid

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
        if issubclass(FeatureViewResponse, dict):
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
        if not isinstance(other, FeatureViewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
