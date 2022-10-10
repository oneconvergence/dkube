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


class ModelCatalogItem(object):
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
        'description': 'str',
        'generated': 'ModelCatalogItemGenerated',
        'model': 'ModelCatalogItemModel',
        'update_timestamp': 'TimeStamps',
        'publisher': 'str',
        'versions': 'list[ModelCatalogItemVersion]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'generated': 'generated',
        'model': 'model',
        'update_timestamp': 'updateTimestamp',
        'publisher': 'publisher',
        'versions': 'versions'
    }

    def __init__(self, name=None, description=None, generated=None, model=None, update_timestamp=None, publisher=None, versions=None):  # noqa: E501
        """ModelCatalogItem - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._description = None
        self._generated = None
        self._model = None
        self._update_timestamp = None
        self._publisher = None
        self._versions = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if generated is not None:
            self.generated = generated
        if model is not None:
            self.model = model
        if update_timestamp is not None:
            self.update_timestamp = update_timestamp
        if publisher is not None:
            self.publisher = publisher
        if versions is not None:
            self.versions = versions

    @property
    def name(self):
        """Gets the name of this ModelCatalogItem.  # noqa: E501


        :return: The name of this ModelCatalogItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelCatalogItem.


        :param name: The name of this ModelCatalogItem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ModelCatalogItem.  # noqa: E501


        :return: The description of this ModelCatalogItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModelCatalogItem.


        :param description: The description of this ModelCatalogItem.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def generated(self):
        """Gets the generated of this ModelCatalogItem.  # noqa: E501


        :return: The generated of this ModelCatalogItem.  # noqa: E501
        :rtype: ModelCatalogItemGenerated
        """
        return self._generated

    @generated.setter
    def generated(self, generated):
        """Sets the generated of this ModelCatalogItem.


        :param generated: The generated of this ModelCatalogItem.  # noqa: E501
        :type: ModelCatalogItemGenerated
        """

        self._generated = generated

    @property
    def model(self):
        """Gets the model of this ModelCatalogItem.  # noqa: E501


        :return: The model of this ModelCatalogItem.  # noqa: E501
        :rtype: ModelCatalogItemModel
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this ModelCatalogItem.


        :param model: The model of this ModelCatalogItem.  # noqa: E501
        :type: ModelCatalogItemModel
        """

        self._model = model

    @property
    def update_timestamp(self):
        """Gets the update_timestamp of this ModelCatalogItem.  # noqa: E501


        :return: The update_timestamp of this ModelCatalogItem.  # noqa: E501
        :rtype: TimeStamps
        """
        return self._update_timestamp

    @update_timestamp.setter
    def update_timestamp(self, update_timestamp):
        """Sets the update_timestamp of this ModelCatalogItem.


        :param update_timestamp: The update_timestamp of this ModelCatalogItem.  # noqa: E501
        :type: TimeStamps
        """

        self._update_timestamp = update_timestamp

    @property
    def publisher(self):
        """Gets the publisher of this ModelCatalogItem.  # noqa: E501


        :return: The publisher of this ModelCatalogItem.  # noqa: E501
        :rtype: str
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this ModelCatalogItem.


        :param publisher: The publisher of this ModelCatalogItem.  # noqa: E501
        :type: str
        """

        self._publisher = publisher

    @property
    def versions(self):
        """Gets the versions of this ModelCatalogItem.  # noqa: E501


        :return: The versions of this ModelCatalogItem.  # noqa: E501
        :rtype: list[ModelCatalogItemVersion]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this ModelCatalogItem.


        :param versions: The versions of this ModelCatalogItem.  # noqa: E501
        :type: list[ModelCatalogItemVersion]
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
        if issubclass(ModelCatalogItem, dict):
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
        if not isinstance(other, ModelCatalogItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
