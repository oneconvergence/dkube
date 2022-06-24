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


class DLFrameworkProject(object):
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
        'user': 'str',
        'name': 'str',
        'images': 'list[str]'
    }

    attribute_map = {
        'user': 'user',
        'name': 'name',
        'images': 'images'
    }

    def __init__(self, user=None, name=None, images=None):  # noqa: E501
        """DLFrameworkProject - a model defined in Swagger"""  # noqa: E501

        self._user = None
        self._name = None
        self._images = None
        self.discriminator = None

        if user is not None:
            self.user = user
        if name is not None:
            self.name = name
        if images is not None:
            self.images = images

    @property
    def user(self):
        """Gets the user of this DLFrameworkProject.  # noqa: E501


        :return: The user of this DLFrameworkProject.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this DLFrameworkProject.


        :param user: The user of this DLFrameworkProject.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def name(self):
        """Gets the name of this DLFrameworkProject.  # noqa: E501


        :return: The name of this DLFrameworkProject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DLFrameworkProject.


        :param name: The name of this DLFrameworkProject.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def images(self):
        """Gets the images of this DLFrameworkProject.  # noqa: E501


        :return: The images of this DLFrameworkProject.  # noqa: E501
        :rtype: list[str]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this DLFrameworkProject.


        :param images: The images of this DLFrameworkProject.  # noqa: E501
        :type: list[str]
        """

        self._images = images

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
        if issubclass(DLFrameworkProject, dict):
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
        if not isinstance(other, DLFrameworkProject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
