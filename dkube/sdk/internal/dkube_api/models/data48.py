# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.3.0.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Data48(object):
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
        'alert_action': 'ModelmonitorAlertActionDef',
        '_class': 'str',
        'conditions': 'list[ModelmonitorAlertCondDef]',
        'enabled': 'bool'
    }

    attribute_map = {
        'alert_action': 'alert_action',
        '_class': 'class',
        'conditions': 'conditions',
        'enabled': 'enabled'
    }

    def __init__(self, alert_action=None, _class=None, conditions=None, enabled=None):  # noqa: E501
        """Data48 - a model defined in Swagger"""  # noqa: E501

        self._alert_action = None
        self.__class = None
        self._conditions = None
        self._enabled = None
        self.discriminator = None

        if alert_action is not None:
            self.alert_action = alert_action
        if _class is not None:
            self._class = _class
        if conditions is not None:
            self.conditions = conditions
        if enabled is not None:
            self.enabled = enabled

    @property
    def alert_action(self):
        """Gets the alert_action of this Data48.  # noqa: E501


        :return: The alert_action of this Data48.  # noqa: E501
        :rtype: ModelmonitorAlertActionDef
        """
        return self._alert_action

    @alert_action.setter
    def alert_action(self, alert_action):
        """Sets the alert_action of this Data48.


        :param alert_action: The alert_action of this Data48.  # noqa: E501
        :type: ModelmonitorAlertActionDef
        """

        self._alert_action = alert_action

    @property
    def _class(self):
        """Gets the _class of this Data48.  # noqa: E501


        :return: The _class of this Data48.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this Data48.


        :param _class: The _class of this Data48.  # noqa: E501
        :type: str
        """

        self.__class = _class

    @property
    def conditions(self):
        """Gets the conditions of this Data48.  # noqa: E501


        :return: The conditions of this Data48.  # noqa: E501
        :rtype: list[ModelmonitorAlertCondDef]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this Data48.


        :param conditions: The conditions of this Data48.  # noqa: E501
        :type: list[ModelmonitorAlertCondDef]
        """

        self._conditions = conditions

    @property
    def enabled(self):
        """Gets the enabled of this Data48.  # noqa: E501


        :return: The enabled of this Data48.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Data48.


        :param enabled: The enabled of this Data48.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

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
        if issubclass(Data48, dict):
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
        if not isinstance(other, Data48):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
