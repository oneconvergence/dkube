# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.7.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Data31(object):
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
        'group': 'str',
        'description': 'str',
        'image': 'str',
        'leaderboard': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'group': 'group',
        'description': 'description',
        'image': 'image',
        'leaderboard': 'leaderboard'
    }

    def __init__(self, name=None, group=None, description=None, image=None, leaderboard=False):  # noqa: E501
        """Data31 - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._group = None
        self._description = None
        self._image = None
        self._leaderboard = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if group is not None:
            self.group = group
        if description is not None:
            self.description = description
        if image is not None:
            self.image = image
        if leaderboard is not None:
            self.leaderboard = leaderboard

    @property
    def name(self):
        """Gets the name of this Data31.  # noqa: E501


        :return: The name of this Data31.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Data31.


        :param name: The name of this Data31.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def group(self):
        """Gets the group of this Data31.  # noqa: E501


        :return: The group of this Data31.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this Data31.


        :param group: The group of this Data31.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def description(self):
        """Gets the description of this Data31.  # noqa: E501


        :return: The description of this Data31.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Data31.


        :param description: The description of this Data31.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def image(self):
        """Gets the image of this Data31.  # noqa: E501


        :return: The image of this Data31.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this Data31.


        :param image: The image of this Data31.  # noqa: E501
        :type: str
        """
        if image is not None and len(image) > 2083:
            raise ValueError("Invalid value for `image`, length must be less than or equal to `2083`")  # noqa: E501
        if image is not None and len(image) < 1:
            raise ValueError("Invalid value for `image`, length must be greater than or equal to `1`")  # noqa: E501

        self._image = image

    @property
    def leaderboard(self):
        """Gets the leaderboard of this Data31.  # noqa: E501


        :return: The leaderboard of this Data31.  # noqa: E501
        :rtype: bool
        """
        return self._leaderboard

    @leaderboard.setter
    def leaderboard(self, leaderboard):
        """Sets the leaderboard of this Data31.


        :param leaderboard: The leaderboard of this Data31.  # noqa: E501
        :type: bool
        """

        self._leaderboard = leaderboard

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
        if issubclass(Data31, dict):
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
        if not isinstance(other, Data31):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
