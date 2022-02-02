# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.1.0.3
    
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
        'enabled': 'bool',
        'name': 'str',
        'tags': 'list[str]',
        'conditions': 'list[ModelmonitorAlertCondDef]',
        'created_at': 'str',
        'updated_at': 'str',
        'status': 'ModelmonitorAlertStatusDef',
        'alert_action': 'ModelmonitorAlertActionDef'
    }

    attribute_map = {
        'id': 'id',
        '_class': 'class',
        'enabled': 'enabled',
        'name': 'name',
        'tags': 'tags',
        'conditions': 'conditions',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'status': 'status',
        'alert_action': 'alert_action'
    }

    def __init__(self, id=None, _class='feature_drift', enabled=None, name=None, tags=None, conditions=None, created_at=None, updated_at=None, status=None, alert_action=None):  # noqa: E501
        """ModelmonitorAlertDef - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self.__class = None
        self._enabled = None
        self._name = None
        self._tags = None
        self._conditions = None
        self._created_at = None
        self._updated_at = None
        self._status = None
        self._alert_action = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self._class = _class
        if enabled is not None:
            self.enabled = enabled
        self.name = name
        if tags is not None:
            self.tags = tags
        self.conditions = conditions
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if status is not None:
            self.status = status
        if alert_action is not None:
            self.alert_action = alert_action

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
        allowed_values = ["feature_drift", "performance_decay", "deployment_health"]  # noqa: E501
        if _class not in allowed_values:
            raise ValueError(
                "Invalid value for `_class` ({0}), must be one of {1}"  # noqa: E501
                .format(_class, allowed_values)
            )

        self.__class = _class

    @property
    def enabled(self):
        """Gets the enabled of this ModelmonitorAlertDef.  # noqa: E501

        To signify alert is enabled or disabled  # noqa: E501

        :return: The enabled of this ModelmonitorAlertDef.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ModelmonitorAlertDef.

        To signify alert is enabled or disabled  # noqa: E501

        :param enabled: The enabled of this ModelmonitorAlertDef.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

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
    def tags(self):
        """Gets the tags of this ModelmonitorAlertDef.  # noqa: E501


        :return: The tags of this ModelmonitorAlertDef.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ModelmonitorAlertDef.


        :param tags: The tags of this ModelmonitorAlertDef.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

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

    @property
    def status(self):
        """Gets the status of this ModelmonitorAlertDef.  # noqa: E501


        :return: The status of this ModelmonitorAlertDef.  # noqa: E501
        :rtype: ModelmonitorAlertStatusDef
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ModelmonitorAlertDef.


        :param status: The status of this ModelmonitorAlertDef.  # noqa: E501
        :type: ModelmonitorAlertStatusDef
        """

        self._status = status

    @property
    def alert_action(self):
        """Gets the alert_action of this ModelmonitorAlertDef.  # noqa: E501


        :return: The alert_action of this ModelmonitorAlertDef.  # noqa: E501
        :rtype: ModelmonitorAlertActionDef
        """
        return self._alert_action

    @alert_action.setter
    def alert_action(self, alert_action):
        """Sets the alert_action of this ModelmonitorAlertDef.


        :param alert_action: The alert_action of this ModelmonitorAlertDef.  # noqa: E501
        :type: ModelmonitorAlertActionDef
        """

        self._alert_action = alert_action

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
