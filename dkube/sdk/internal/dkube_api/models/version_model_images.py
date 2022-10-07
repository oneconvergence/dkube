# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.5.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class VersionModelImages(object):
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
        'image_name': 'str',
        'build_name': 'str',
        'created_at': 'str'
    }

    attribute_map = {
        'image_name': 'image_name',
        'build_name': 'build_name',
        'created_at': 'created_at'
    }

    def __init__(self, image_name=None, build_name=None, created_at=None):  # noqa: E501
        """VersionModelImages - a model defined in Swagger"""  # noqa: E501

        self._image_name = None
        self._build_name = None
        self._created_at = None
        self.discriminator = None

        if image_name is not None:
            self.image_name = image_name
        if build_name is not None:
            self.build_name = build_name
        if created_at is not None:
            self.created_at = created_at

    @property
    def image_name(self):
        """Gets the image_name of this VersionModelImages.  # noqa: E501


        :return: The image_name of this VersionModelImages.  # noqa: E501
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this VersionModelImages.


        :param image_name: The image_name of this VersionModelImages.  # noqa: E501
        :type: str
        """

        self._image_name = image_name

    @property
    def build_name(self):
        """Gets the build_name of this VersionModelImages.  # noqa: E501


        :return: The build_name of this VersionModelImages.  # noqa: E501
        :rtype: str
        """
        return self._build_name

    @build_name.setter
    def build_name(self, build_name):
        """Sets the build_name of this VersionModelImages.


        :param build_name: The build_name of this VersionModelImages.  # noqa: E501
        :type: str
        """

        self._build_name = build_name

    @property
    def created_at(self):
        """Gets the created_at of this VersionModelImages.  # noqa: E501


        :return: The created_at of this VersionModelImages.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this VersionModelImages.


        :param created_at: The created_at of this VersionModelImages.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

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
        if issubclass(VersionModelImages, dict):
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
        if not isinstance(other, VersionModelImages):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
