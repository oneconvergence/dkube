# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.3.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ModelmonitorInputDataShapeDef(object):
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
        'height': 'float',
        'width': 'float',
        'channel': 'float',
        'channel_order': 'str'
    }

    attribute_map = {
        'height': 'height',
        'width': 'width',
        'channel': 'channel',
        'channel_order': 'channel_order'
    }

    def __init__(self, height=None, width=None, channel=None, channel_order=None):  # noqa: E501
        """ModelmonitorInputDataShapeDef - a model defined in Swagger"""  # noqa: E501

        self._height = None
        self._width = None
        self._channel = None
        self._channel_order = None
        self.discriminator = None

        if height is not None:
            self.height = height
        if width is not None:
            self.width = width
        if channel is not None:
            self.channel = channel
        if channel_order is not None:
            self.channel_order = channel_order

    @property
    def height(self):
        """Gets the height of this ModelmonitorInputDataShapeDef.  # noqa: E501


        :return: The height of this ModelmonitorInputDataShapeDef.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this ModelmonitorInputDataShapeDef.


        :param height: The height of this ModelmonitorInputDataShapeDef.  # noqa: E501
        :type: float
        """

        self._height = height

    @property
    def width(self):
        """Gets the width of this ModelmonitorInputDataShapeDef.  # noqa: E501


        :return: The width of this ModelmonitorInputDataShapeDef.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this ModelmonitorInputDataShapeDef.


        :param width: The width of this ModelmonitorInputDataShapeDef.  # noqa: E501
        :type: float
        """

        self._width = width

    @property
    def channel(self):
        """Gets the channel of this ModelmonitorInputDataShapeDef.  # noqa: E501

        The colour spaces used by the image dataset. - 0 for no channel - 1 for 1 channel (grayscale) - 3 for 3 channel (for eg rgb, hsv etc) - 4 for 4 channel (for eg cmyk etc)  # noqa: E501

        :return: The channel of this ModelmonitorInputDataShapeDef.  # noqa: E501
        :rtype: float
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this ModelmonitorInputDataShapeDef.

        The colour spaces used by the image dataset. - 0 for no channel - 1 for 1 channel (grayscale) - 3 for 3 channel (for eg rgb, hsv etc) - 4 for 4 channel (for eg cmyk etc)  # noqa: E501

        :param channel: The channel of this ModelmonitorInputDataShapeDef.  # noqa: E501
        :type: float
        """

        self._channel = channel

    @property
    def channel_order(self):
        """Gets the channel_order of this ModelmonitorInputDataShapeDef.  # noqa: E501


        :return: The channel_order of this ModelmonitorInputDataShapeDef.  # noqa: E501
        :rtype: str
        """
        return self._channel_order

    @channel_order.setter
    def channel_order(self, channel_order):
        """Sets the channel_order of this ModelmonitorInputDataShapeDef.


        :param channel_order: The channel_order of this ModelmonitorInputDataShapeDef.  # noqa: E501
        :type: str
        """
        allowed_values = ["last", "first"]  # noqa: E501
        if channel_order not in allowed_values:
            raise ValueError(
                "Invalid value for `channel_order` ({0}), must be one of {1}"  # noqa: E501
                .format(channel_order, allowed_values)
            )

        self._channel_order = channel_order

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
        if issubclass(ModelmonitorInputDataShapeDef, dict):
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
        if not isinstance(other, ModelmonitorInputDataShapeDef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
