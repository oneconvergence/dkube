# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.3.0.14
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ModelCatalogItemVersion(object):
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
        'version': 'str',
        'name': 'str',
        'publisher': 'str',
        'owner': 'str',
        'model': 'InlineResponse20024SearchDatasets',
        'serving': 'ModelServingInfo',
        'training': 'ModelTrainingInfo',
        'stage': 'str',
        'staged': 'bool',
        'description': 'str',
        'published_timestamp': 'TimeStamps'
    }

    attribute_map = {
        'version': 'version',
        'name': 'name',
        'publisher': 'publisher',
        'owner': 'owner',
        'model': 'model',
        'serving': 'serving',
        'training': 'training',
        'stage': 'stage',
        'staged': 'staged',
        'description': 'description',
        'published_timestamp': 'publishedTimestamp'
    }

    def __init__(self, version=None, name=None, publisher=None, owner=None, model=None, serving=None, training=None, stage=None, staged=None, description=None, published_timestamp=None):  # noqa: E501
        """ModelCatalogItemVersion - a model defined in Swagger"""  # noqa: E501

        self._version = None
        self._name = None
        self._publisher = None
        self._owner = None
        self._model = None
        self._serving = None
        self._training = None
        self._stage = None
        self._staged = None
        self._description = None
        self._published_timestamp = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if name is not None:
            self.name = name
        if publisher is not None:
            self.publisher = publisher
        if owner is not None:
            self.owner = owner
        if model is not None:
            self.model = model
        if serving is not None:
            self.serving = serving
        if training is not None:
            self.training = training
        if stage is not None:
            self.stage = stage
        if staged is not None:
            self.staged = staged
        if description is not None:
            self.description = description
        if published_timestamp is not None:
            self.published_timestamp = published_timestamp

    @property
    def version(self):
        """Gets the version of this ModelCatalogItemVersion.  # noqa: E501


        :return: The version of this ModelCatalogItemVersion.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ModelCatalogItemVersion.


        :param version: The version of this ModelCatalogItemVersion.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def name(self):
        """Gets the name of this ModelCatalogItemVersion.  # noqa: E501


        :return: The name of this ModelCatalogItemVersion.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelCatalogItemVersion.


        :param name: The name of this ModelCatalogItemVersion.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def publisher(self):
        """Gets the publisher of this ModelCatalogItemVersion.  # noqa: E501


        :return: The publisher of this ModelCatalogItemVersion.  # noqa: E501
        :rtype: str
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this ModelCatalogItemVersion.


        :param publisher: The publisher of this ModelCatalogItemVersion.  # noqa: E501
        :type: str
        """

        self._publisher = publisher

    @property
    def owner(self):
        """Gets the owner of this ModelCatalogItemVersion.  # noqa: E501


        :return: The owner of this ModelCatalogItemVersion.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ModelCatalogItemVersion.


        :param owner: The owner of this ModelCatalogItemVersion.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def model(self):
        """Gets the model of this ModelCatalogItemVersion.  # noqa: E501


        :return: The model of this ModelCatalogItemVersion.  # noqa: E501
        :rtype: InlineResponse20024SearchDatasets
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this ModelCatalogItemVersion.


        :param model: The model of this ModelCatalogItemVersion.  # noqa: E501
        :type: InlineResponse20024SearchDatasets
        """

        self._model = model

    @property
    def serving(self):
        """Gets the serving of this ModelCatalogItemVersion.  # noqa: E501


        :return: The serving of this ModelCatalogItemVersion.  # noqa: E501
        :rtype: ModelServingInfo
        """
        return self._serving

    @serving.setter
    def serving(self, serving):
        """Sets the serving of this ModelCatalogItemVersion.


        :param serving: The serving of this ModelCatalogItemVersion.  # noqa: E501
        :type: ModelServingInfo
        """

        self._serving = serving

    @property
    def training(self):
        """Gets the training of this ModelCatalogItemVersion.  # noqa: E501


        :return: The training of this ModelCatalogItemVersion.  # noqa: E501
        :rtype: ModelTrainingInfo
        """
        return self._training

    @training.setter
    def training(self, training):
        """Sets the training of this ModelCatalogItemVersion.


        :param training: The training of this ModelCatalogItemVersion.  # noqa: E501
        :type: ModelTrainingInfo
        """

        self._training = training

    @property
    def stage(self):
        """Gets the stage of this ModelCatalogItemVersion.  # noqa: E501


        :return: The stage of this ModelCatalogItemVersion.  # noqa: E501
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        """Sets the stage of this ModelCatalogItemVersion.


        :param stage: The stage of this ModelCatalogItemVersion.  # noqa: E501
        :type: str
        """

        self._stage = stage

    @property
    def staged(self):
        """Gets the staged of this ModelCatalogItemVersion.  # noqa: E501


        :return: The staged of this ModelCatalogItemVersion.  # noqa: E501
        :rtype: bool
        """
        return self._staged

    @staged.setter
    def staged(self, staged):
        """Sets the staged of this ModelCatalogItemVersion.


        :param staged: The staged of this ModelCatalogItemVersion.  # noqa: E501
        :type: bool
        """

        self._staged = staged

    @property
    def description(self):
        """Gets the description of this ModelCatalogItemVersion.  # noqa: E501


        :return: The description of this ModelCatalogItemVersion.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModelCatalogItemVersion.


        :param description: The description of this ModelCatalogItemVersion.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def published_timestamp(self):
        """Gets the published_timestamp of this ModelCatalogItemVersion.  # noqa: E501


        :return: The published_timestamp of this ModelCatalogItemVersion.  # noqa: E501
        :rtype: TimeStamps
        """
        return self._published_timestamp

    @published_timestamp.setter
    def published_timestamp(self, published_timestamp):
        """Sets the published_timestamp of this ModelCatalogItemVersion.


        :param published_timestamp: The published_timestamp of this ModelCatalogItemVersion.  # noqa: E501
        :type: TimeStamps
        """

        self._published_timestamp = published_timestamp

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
        if issubclass(ModelCatalogItemVersion, dict):
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
        if not isinstance(other, ModelCatalogItemVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
