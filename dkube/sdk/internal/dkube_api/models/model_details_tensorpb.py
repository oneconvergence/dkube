# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0.0.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ModelDetailsTensorpb(object):
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
        'signatures': 'ModelDetailsTensorpbSignatures',
        'devicenodes': 'list[str]',
        'devices': 'ModelDetailsTensorpbDevices',
        'parameters': 'int',
        'weights': 'int',
        'layers': 'int',
        'servable': 'bool'
    }

    attribute_map = {
        'signatures': 'signatures',
        'devicenodes': 'devicenodes',
        'devices': 'devices',
        'parameters': 'parameters',
        'weights': 'weights',
        'layers': 'layers',
        'servable': 'servable'
    }

    def __init__(self, signatures=None, devicenodes=None, devices=None, parameters=None, weights=None, layers=None, servable=None):  # noqa: E501
        """ModelDetailsTensorpb - a model defined in Swagger"""  # noqa: E501

        self._signatures = None
        self._devicenodes = None
        self._devices = None
        self._parameters = None
        self._weights = None
        self._layers = None
        self._servable = None
        self.discriminator = None

        if signatures is not None:
            self.signatures = signatures
        if devicenodes is not None:
            self.devicenodes = devicenodes
        if devices is not None:
            self.devices = devices
        if parameters is not None:
            self.parameters = parameters
        if weights is not None:
            self.weights = weights
        if layers is not None:
            self.layers = layers
        if servable is not None:
            self.servable = servable

    @property
    def signatures(self):
        """Gets the signatures of this ModelDetailsTensorpb.  # noqa: E501


        :return: The signatures of this ModelDetailsTensorpb.  # noqa: E501
        :rtype: ModelDetailsTensorpbSignatures
        """
        return self._signatures

    @signatures.setter
    def signatures(self, signatures):
        """Sets the signatures of this ModelDetailsTensorpb.


        :param signatures: The signatures of this ModelDetailsTensorpb.  # noqa: E501
        :type: ModelDetailsTensorpbSignatures
        """

        self._signatures = signatures

    @property
    def devicenodes(self):
        """Gets the devicenodes of this ModelDetailsTensorpb.  # noqa: E501


        :return: The devicenodes of this ModelDetailsTensorpb.  # noqa: E501
        :rtype: list[str]
        """
        return self._devicenodes

    @devicenodes.setter
    def devicenodes(self, devicenodes):
        """Sets the devicenodes of this ModelDetailsTensorpb.


        :param devicenodes: The devicenodes of this ModelDetailsTensorpb.  # noqa: E501
        :type: list[str]
        """

        self._devicenodes = devicenodes

    @property
    def devices(self):
        """Gets the devices of this ModelDetailsTensorpb.  # noqa: E501


        :return: The devices of this ModelDetailsTensorpb.  # noqa: E501
        :rtype: ModelDetailsTensorpbDevices
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this ModelDetailsTensorpb.


        :param devices: The devices of this ModelDetailsTensorpb.  # noqa: E501
        :type: ModelDetailsTensorpbDevices
        """

        self._devices = devices

    @property
    def parameters(self):
        """Gets the parameters of this ModelDetailsTensorpb.  # noqa: E501


        :return: The parameters of this ModelDetailsTensorpb.  # noqa: E501
        :rtype: int
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this ModelDetailsTensorpb.


        :param parameters: The parameters of this ModelDetailsTensorpb.  # noqa: E501
        :type: int
        """

        self._parameters = parameters

    @property
    def weights(self):
        """Gets the weights of this ModelDetailsTensorpb.  # noqa: E501


        :return: The weights of this ModelDetailsTensorpb.  # noqa: E501
        :rtype: int
        """
        return self._weights

    @weights.setter
    def weights(self, weights):
        """Sets the weights of this ModelDetailsTensorpb.


        :param weights: The weights of this ModelDetailsTensorpb.  # noqa: E501
        :type: int
        """

        self._weights = weights

    @property
    def layers(self):
        """Gets the layers of this ModelDetailsTensorpb.  # noqa: E501


        :return: The layers of this ModelDetailsTensorpb.  # noqa: E501
        :rtype: int
        """
        return self._layers

    @layers.setter
    def layers(self, layers):
        """Sets the layers of this ModelDetailsTensorpb.


        :param layers: The layers of this ModelDetailsTensorpb.  # noqa: E501
        :type: int
        """

        self._layers = layers

    @property
    def servable(self):
        """Gets the servable of this ModelDetailsTensorpb.  # noqa: E501


        :return: The servable of this ModelDetailsTensorpb.  # noqa: E501
        :rtype: bool
        """
        return self._servable

    @servable.setter
    def servable(self, servable):
        """Sets the servable of this ModelDetailsTensorpb.


        :param servable: The servable of this ModelDetailsTensorpb.  # noqa: E501
        :type: bool
        """

        self._servable = servable

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
        if issubclass(ModelDetailsTensorpb, dict):
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
        if not isinstance(other, ModelDetailsTensorpb):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
