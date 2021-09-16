# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.3.0.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DSJobModelHyperparams(object):
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
        'epochs': 'int',
        'steps': 'int',
        'batchsize': 'int',
        'custom': 'list[str]',
        'customkv': 'CustomKVModel',
        'file': 'ConfigFileModel'
    }

    attribute_map = {
        'epochs': 'epochs',
        'steps': 'steps',
        'batchsize': 'batchsize',
        'custom': 'custom',
        'customkv': 'customkv',
        'file': 'file'
    }

    def __init__(self, epochs=None, steps=None, batchsize=None, custom=None, customkv=None, file=None):  # noqa: E501
        """DSJobModelHyperparams - a model defined in Swagger"""  # noqa: E501

        self._epochs = None
        self._steps = None
        self._batchsize = None
        self._custom = None
        self._customkv = None
        self._file = None
        self.discriminator = None

        if epochs is not None:
            self.epochs = epochs
        if steps is not None:
            self.steps = steps
        if batchsize is not None:
            self.batchsize = batchsize
        if custom is not None:
            self.custom = custom
        if customkv is not None:
            self.customkv = customkv
        if file is not None:
            self.file = file

    @property
    def epochs(self):
        """Gets the epochs of this DSJobModelHyperparams.  # noqa: E501


        :return: The epochs of this DSJobModelHyperparams.  # noqa: E501
        :rtype: int
        """
        return self._epochs

    @epochs.setter
    def epochs(self, epochs):
        """Sets the epochs of this DSJobModelHyperparams.


        :param epochs: The epochs of this DSJobModelHyperparams.  # noqa: E501
        :type: int
        """

        self._epochs = epochs

    @property
    def steps(self):
        """Gets the steps of this DSJobModelHyperparams.  # noqa: E501


        :return: The steps of this DSJobModelHyperparams.  # noqa: E501
        :rtype: int
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this DSJobModelHyperparams.


        :param steps: The steps of this DSJobModelHyperparams.  # noqa: E501
        :type: int
        """

        self._steps = steps

    @property
    def batchsize(self):
        """Gets the batchsize of this DSJobModelHyperparams.  # noqa: E501


        :return: The batchsize of this DSJobModelHyperparams.  # noqa: E501
        :rtype: int
        """
        return self._batchsize

    @batchsize.setter
    def batchsize(self, batchsize):
        """Sets the batchsize of this DSJobModelHyperparams.


        :param batchsize: The batchsize of this DSJobModelHyperparams.  # noqa: E501
        :type: int
        """

        self._batchsize = batchsize

    @property
    def custom(self):
        """Gets the custom of this DSJobModelHyperparams.  # noqa: E501

        Each entry should be JSON key:value pair  # noqa: E501

        :return: The custom of this DSJobModelHyperparams.  # noqa: E501
        :rtype: list[str]
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        """Sets the custom of this DSJobModelHyperparams.

        Each entry should be JSON key:value pair  # noqa: E501

        :param custom: The custom of this DSJobModelHyperparams.  # noqa: E501
        :type: list[str]
        """

        self._custom = custom

    @property
    def customkv(self):
        """Gets the customkv of this DSJobModelHyperparams.  # noqa: E501


        :return: The customkv of this DSJobModelHyperparams.  # noqa: E501
        :rtype: CustomKVModel
        """
        return self._customkv

    @customkv.setter
    def customkv(self, customkv):
        """Sets the customkv of this DSJobModelHyperparams.


        :param customkv: The customkv of this DSJobModelHyperparams.  # noqa: E501
        :type: CustomKVModel
        """

        self._customkv = customkv

    @property
    def file(self):
        """Gets the file of this DSJobModelHyperparams.  # noqa: E501


        :return: The file of this DSJobModelHyperparams.  # noqa: E501
        :rtype: ConfigFileModel
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this DSJobModelHyperparams.


        :param file: The file of this DSJobModelHyperparams.  # noqa: E501
        :type: ConfigFileModel
        """

        self._file = file

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
        if issubclass(DSJobModelHyperparams, dict):
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
        if not isinstance(other, DSJobModelHyperparams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
