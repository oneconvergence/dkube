# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0.0.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DatumModelGeneratedDetails(object):
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
        'git': 'GitDetails',
        'model': 'ModelDetails',
        'tensorboard': 'TensorboardModel',
        'source': 'DatumSourceDetails'
    }

    attribute_map = {
        'git': 'git',
        'model': 'model',
        'tensorboard': 'tensorboard',
        'source': 'source'
    }

    def __init__(self, git=None, model=None, tensorboard=None, source=None):  # noqa: E501
        """DatumModelGeneratedDetails - a model defined in Swagger"""  # noqa: E501

        self._git = None
        self._model = None
        self._tensorboard = None
        self._source = None
        self.discriminator = None

        if git is not None:
            self.git = git
        if model is not None:
            self.model = model
        if tensorboard is not None:
            self.tensorboard = tensorboard
        if source is not None:
            self.source = source

    @property
    def git(self):
        """Gets the git of this DatumModelGeneratedDetails.  # noqa: E501


        :return: The git of this DatumModelGeneratedDetails.  # noqa: E501
        :rtype: GitDetails
        """
        return self._git

    @git.setter
    def git(self, git):
        """Sets the git of this DatumModelGeneratedDetails.


        :param git: The git of this DatumModelGeneratedDetails.  # noqa: E501
        :type: GitDetails
        """

        self._git = git

    @property
    def model(self):
        """Gets the model of this DatumModelGeneratedDetails.  # noqa: E501


        :return: The model of this DatumModelGeneratedDetails.  # noqa: E501
        :rtype: ModelDetails
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this DatumModelGeneratedDetails.


        :param model: The model of this DatumModelGeneratedDetails.  # noqa: E501
        :type: ModelDetails
        """

        self._model = model

    @property
    def tensorboard(self):
        """Gets the tensorboard of this DatumModelGeneratedDetails.  # noqa: E501


        :return: The tensorboard of this DatumModelGeneratedDetails.  # noqa: E501
        :rtype: TensorboardModel
        """
        return self._tensorboard

    @tensorboard.setter
    def tensorboard(self, tensorboard):
        """Sets the tensorboard of this DatumModelGeneratedDetails.


        :param tensorboard: The tensorboard of this DatumModelGeneratedDetails.  # noqa: E501
        :type: TensorboardModel
        """

        self._tensorboard = tensorboard

    @property
    def source(self):
        """Gets the source of this DatumModelGeneratedDetails.  # noqa: E501


        :return: The source of this DatumModelGeneratedDetails.  # noqa: E501
        :rtype: DatumSourceDetails
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this DatumModelGeneratedDetails.


        :param source: The source of this DatumModelGeneratedDetails.  # noqa: E501
        :type: DatumSourceDetails
        """

        self._source = source

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
        if issubclass(DatumModelGeneratedDetails, dict):
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
        if not isinstance(other, DatumModelGeneratedDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
