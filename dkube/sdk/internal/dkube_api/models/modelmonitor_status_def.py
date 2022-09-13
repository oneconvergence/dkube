# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ModelmonitorStatusDef(object):
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
        'state': 'str',
        'sub_state': 'str',
        'message': 'str',
        'code': 'str',
        'success': 'bool',
        'schema_updated': 'bool',
        'alerts_updated': 'bool',
        'deploy_logs_status': 'bool'
    }

    attribute_map = {
        'state': 'state',
        'sub_state': 'sub_state',
        'message': 'message',
        'code': 'code',
        'success': 'success',
        'schema_updated': 'schema_updated',
        'alerts_updated': 'alerts_updated',
        'deploy_logs_status': 'deploy_logs_status'
    }

    def __init__(self, state=None, sub_state=None, message=None, code=None, success=None, schema_updated=None, alerts_updated=None, deploy_logs_status=None):  # noqa: E501
        """ModelmonitorStatusDef - a model defined in Swagger"""  # noqa: E501

        self._state = None
        self._sub_state = None
        self._message = None
        self._code = None
        self._success = None
        self._schema_updated = None
        self._alerts_updated = None
        self._deploy_logs_status = None
        self.discriminator = None

        if state is not None:
            self.state = state
        if sub_state is not None:
            self.sub_state = sub_state
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code
        if success is not None:
            self.success = success
        if schema_updated is not None:
            self.schema_updated = schema_updated
        if alerts_updated is not None:
            self.alerts_updated = alerts_updated
        if deploy_logs_status is not None:
            self.deploy_logs_status = deploy_logs_status

    @property
    def state(self):
        """Gets the state of this ModelmonitorStatusDef.  # noqa: E501


        :return: The state of this ModelmonitorStatusDef.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ModelmonitorStatusDef.


        :param state: The state of this ModelmonitorStatusDef.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def sub_state(self):
        """Gets the sub_state of this ModelmonitorStatusDef.  # noqa: E501

        Sub state of resource  # noqa: E501

        :return: The sub_state of this ModelmonitorStatusDef.  # noqa: E501
        :rtype: str
        """
        return self._sub_state

    @sub_state.setter
    def sub_state(self, sub_state):
        """Sets the sub_state of this ModelmonitorStatusDef.

        Sub state of resource  # noqa: E501

        :param sub_state: The sub_state of this ModelmonitorStatusDef.  # noqa: E501
        :type: str
        """
        if sub_state is not None and len(sub_state) > 255:
            raise ValueError("Invalid value for `sub_state`, length must be less than or equal to `255`")  # noqa: E501
        if sub_state is not None and len(sub_state) < 1:
            raise ValueError("Invalid value for `sub_state`, length must be greater than or equal to `1`")  # noqa: E501

        self._sub_state = sub_state

    @property
    def message(self):
        """Gets the message of this ModelmonitorStatusDef.  # noqa: E501


        :return: The message of this ModelmonitorStatusDef.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ModelmonitorStatusDef.


        :param message: The message of this ModelmonitorStatusDef.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def code(self):
        """Gets the code of this ModelmonitorStatusDef.  # noqa: E501


        :return: The code of this ModelmonitorStatusDef.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ModelmonitorStatusDef.


        :param code: The code of this ModelmonitorStatusDef.  # noqa: E501
        :type: str
        """
        if code is not None and len(code) > 255:
            raise ValueError("Invalid value for `code`, length must be less than or equal to `255`")  # noqa: E501
        if code is not None and len(code) < 1:
            raise ValueError("Invalid value for `code`, length must be greater than or equal to `1`")  # noqa: E501

        self._code = code

    @property
    def success(self):
        """Gets the success of this ModelmonitorStatusDef.  # noqa: E501


        :return: The success of this ModelmonitorStatusDef.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this ModelmonitorStatusDef.


        :param success: The success of this ModelmonitorStatusDef.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def schema_updated(self):
        """Gets the schema_updated of this ModelmonitorStatusDef.  # noqa: E501


        :return: The schema_updated of this ModelmonitorStatusDef.  # noqa: E501
        :rtype: bool
        """
        return self._schema_updated

    @schema_updated.setter
    def schema_updated(self, schema_updated):
        """Sets the schema_updated of this ModelmonitorStatusDef.


        :param schema_updated: The schema_updated of this ModelmonitorStatusDef.  # noqa: E501
        :type: bool
        """

        self._schema_updated = schema_updated

    @property
    def alerts_updated(self):
        """Gets the alerts_updated of this ModelmonitorStatusDef.  # noqa: E501


        :return: The alerts_updated of this ModelmonitorStatusDef.  # noqa: E501
        :rtype: bool
        """
        return self._alerts_updated

    @alerts_updated.setter
    def alerts_updated(self, alerts_updated):
        """Sets the alerts_updated of this ModelmonitorStatusDef.


        :param alerts_updated: The alerts_updated of this ModelmonitorStatusDef.  # noqa: E501
        :type: bool
        """

        self._alerts_updated = alerts_updated

    @property
    def deploy_logs_status(self):
        """Gets the deploy_logs_status of this ModelmonitorStatusDef.  # noqa: E501


        :return: The deploy_logs_status of this ModelmonitorStatusDef.  # noqa: E501
        :rtype: bool
        """
        return self._deploy_logs_status

    @deploy_logs_status.setter
    def deploy_logs_status(self, deploy_logs_status):
        """Sets the deploy_logs_status of this ModelmonitorStatusDef.


        :param deploy_logs_status: The deploy_logs_status of this ModelmonitorStatusDef.  # noqa: E501
        :type: bool
        """

        self._deploy_logs_status = deploy_logs_status

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
        if issubclass(ModelmonitorStatusDef, dict):
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
        if not isinstance(other, ModelmonitorStatusDef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
