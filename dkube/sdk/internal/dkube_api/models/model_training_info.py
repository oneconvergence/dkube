# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.3.0.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ModelTrainingInfo(object):
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
        'images': 'ModelTrainingInfoImages',
        'training_code': 'ModelTrainingInfoTrainingCode',
        'datasets': 'ModelTrainingInfoDatasets',
        'featuresets': 'list[InlineResponse20024SearchDatasets]'
    }

    attribute_map = {
        'images': 'images',
        'training_code': 'training_code',
        'datasets': 'datasets',
        'featuresets': 'featuresets'
    }

    def __init__(self, images=None, training_code=None, datasets=None, featuresets=None):  # noqa: E501
        """ModelTrainingInfo - a model defined in Swagger"""  # noqa: E501

        self._images = None
        self._training_code = None
        self._datasets = None
        self._featuresets = None
        self.discriminator = None

        if images is not None:
            self.images = images
        if training_code is not None:
            self.training_code = training_code
        if datasets is not None:
            self.datasets = datasets
        if featuresets is not None:
            self.featuresets = featuresets

    @property
    def images(self):
        """Gets the images of this ModelTrainingInfo.  # noqa: E501


        :return: The images of this ModelTrainingInfo.  # noqa: E501
        :rtype: ModelTrainingInfoImages
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this ModelTrainingInfo.


        :param images: The images of this ModelTrainingInfo.  # noqa: E501
        :type: ModelTrainingInfoImages
        """

        self._images = images

    @property
    def training_code(self):
        """Gets the training_code of this ModelTrainingInfo.  # noqa: E501


        :return: The training_code of this ModelTrainingInfo.  # noqa: E501
        :rtype: ModelTrainingInfoTrainingCode
        """
        return self._training_code

    @training_code.setter
    def training_code(self, training_code):
        """Sets the training_code of this ModelTrainingInfo.


        :param training_code: The training_code of this ModelTrainingInfo.  # noqa: E501
        :type: ModelTrainingInfoTrainingCode
        """

        self._training_code = training_code

    @property
    def datasets(self):
        """Gets the datasets of this ModelTrainingInfo.  # noqa: E501


        :return: The datasets of this ModelTrainingInfo.  # noqa: E501
        :rtype: ModelTrainingInfoDatasets
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets):
        """Sets the datasets of this ModelTrainingInfo.


        :param datasets: The datasets of this ModelTrainingInfo.  # noqa: E501
        :type: ModelTrainingInfoDatasets
        """

        self._datasets = datasets

    @property
    def featuresets(self):
        """Gets the featuresets of this ModelTrainingInfo.  # noqa: E501


        :return: The featuresets of this ModelTrainingInfo.  # noqa: E501
        :rtype: list[InlineResponse20024SearchDatasets]
        """
        return self._featuresets

    @featuresets.setter
    def featuresets(self, featuresets):
        """Sets the featuresets of this ModelTrainingInfo.


        :param featuresets: The featuresets of this ModelTrainingInfo.  # noqa: E501
        :type: list[InlineResponse20024SearchDatasets]
        """

        self._featuresets = featuresets

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
        if issubclass(ModelTrainingInfo, dict):
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
        if not isinstance(other, ModelTrainingInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
