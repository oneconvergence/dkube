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


class ModelmonitorAlertDef(object):
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
        'id': 'str',
        '_class': 'str',
        'email': 'str',
        'name': 'str',
        'conditions': 'list[ModelmonitorAlertCondDef]',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        '_class': 'class',
        'email': 'email',
        'name': 'name',
        'conditions': 'conditions',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, _class='FeatureDrift', email=None, name=None, conditions=None, created_at=None, updated_at=None):  # noqa: E501
        """ModelmonitorAlertDef - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self.__class = None
        self._email = None
        self._name = None
        self._conditions = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self._class = _class
        if email is not None:
            self.email = email
        self.name = name
        self.conditions = conditions
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this ModelmonitorAlertDef.  # noqa: E501

        UUID4 id for the resource  # noqa: E501

        :return: The id of this ModelmonitorAlertDef.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelmonitorAlertDef.

        UUID4 id for the resource  # noqa: E501

        :param id: The id of this ModelmonitorAlertDef.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def _class(self):
        """Gets the _class of this ModelmonitorAlertDef.  # noqa: E501


        :return: The _class of this ModelmonitorAlertDef.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this ModelmonitorAlertDef.


        :param _class: The _class of this ModelmonitorAlertDef.  # noqa: E501
        :type: str
        """
        if _class is None:
            raise ValueError("Invalid value for `_class`, must not be `None`")  # noqa: E501
        allowed_values = ["FeatureDrift", "PerformanceDecay", "PredictionDrift"]  # noqa: E501
        if _class not in allowed_values:
            raise ValueError(
                "Invalid value for `_class` ({0}), must be one of {1}"  # noqa: E501
                .format(_class, allowed_values)
            )

        self.__class = _class

    @property
    def email(self):
        """Gets the email of this ModelmonitorAlertDef.  # noqa: E501

        One or more email addresses separated by comma  # noqa: E501

        :return: The email of this ModelmonitorAlertDef.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ModelmonitorAlertDef.

        One or more email addresses separated by comma  # noqa: E501

        :param email: The email of this ModelmonitorAlertDef.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def name(self):
        """Gets the name of this ModelmonitorAlertDef.  # noqa: E501


        :return: The name of this ModelmonitorAlertDef.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelmonitorAlertDef.


        :param name: The name of this ModelmonitorAlertDef.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def conditions(self):
        """Gets the conditions of this ModelmonitorAlertDef.  # noqa: E501

        All conditions need to satisfy for the alarm to fire  # noqa: E501

        :return: The conditions of this ModelmonitorAlertDef.  # noqa: E501
        :rtype: list[ModelmonitorAlertCondDef]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this ModelmonitorAlertDef.

        All conditions need to satisfy for the alarm to fire  # noqa: E501

        :param conditions: The conditions of this ModelmonitorAlertDef.  # noqa: E501
        :type: list[ModelmonitorAlertCondDef]
        """
        if conditions is None:
            raise ValueError("Invalid value for `conditions`, must not be `None`")  # noqa: E501

        self._conditions = conditions

    @property
    def created_at(self):
        """Gets the created_at of this ModelmonitorAlertDef.  # noqa: E501


        :return: The created_at of this ModelmonitorAlertDef.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ModelmonitorAlertDef.


        :param created_at: The created_at of this ModelmonitorAlertDef.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ModelmonitorAlertDef.  # noqa: E501


        :return: The updated_at of this ModelmonitorAlertDef.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ModelmonitorAlertDef.


        :param updated_at: The updated_at of this ModelmonitorAlertDef.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

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
        if issubclass(ModelmonitorAlertDef, dict):
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
        if not isinstance(other, ModelmonitorAlertDef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
