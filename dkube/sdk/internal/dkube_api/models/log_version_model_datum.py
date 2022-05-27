# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.2.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class LogVersionModelDatum(object):
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
        '_class': 'str',
        'user': 'str',
        'category': 'str'
    }

    attribute_map = {
        'name': 'name',
        '_class': 'class',
        'user': 'user',
        'category': 'category'
    }

    def __init__(self, name=None, _class=None, user=None, category=None):  # noqa: E501
        """LogVersionModelDatum - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self.__class = None
        self._user = None
        self._category = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if _class is not None:
            self._class = _class
        if user is not None:
            self.user = user
        if category is not None:
            self.category = category

    @property
    def name(self):
        """Gets the name of this LogVersionModelDatum.  # noqa: E501


        :return: The name of this LogVersionModelDatum.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LogVersionModelDatum.


        :param name: The name of this LogVersionModelDatum.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def _class(self):
        """Gets the _class of this LogVersionModelDatum.  # noqa: E501


        :return: The _class of this LogVersionModelDatum.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this LogVersionModelDatum.


        :param _class: The _class of this LogVersionModelDatum.  # noqa: E501
        :type: str
        """

        self.__class = _class

    @property
    def user(self):
        """Gets the user of this LogVersionModelDatum.  # noqa: E501


        :return: The user of this LogVersionModelDatum.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this LogVersionModelDatum.


        :param user: The user of this LogVersionModelDatum.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def category(self):
        """Gets the category of this LogVersionModelDatum.  # noqa: E501


        :return: The category of this LogVersionModelDatum.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this LogVersionModelDatum.


        :param category: The category of this LogVersionModelDatum.  # noqa: E501
        :type: str
        """
        allowed_values = ["input", "output"]  # noqa: E501
        if category not in allowed_values:
            raise ValueError(
                "Invalid value for `category` ({0}), must be one of {1}"  # noqa: E501
                .format(category, allowed_values)
            )

        self._category = category

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
        if issubclass(LogVersionModelDatum, dict):
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
        if not isinstance(other, LogVersionModelDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other