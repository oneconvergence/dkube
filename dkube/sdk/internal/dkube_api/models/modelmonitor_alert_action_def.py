# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.4.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ModelmonitorAlertActionDef(object):
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
        'emails': 'str',
        'breach_threshold': 'int',
        'action_type': 'str',
        'additional_subject': 'object'
    }

    attribute_map = {
        'emails': 'emails',
        'breach_threshold': 'breach_threshold',
        'action_type': 'action_type',
        'additional_subject': 'additional_subject'
    }

    def __init__(self, emails=None, breach_threshold=None, action_type='email', additional_subject=None):  # noqa: E501
        """ModelmonitorAlertActionDef - a model defined in Swagger"""  # noqa: E501

        self._emails = None
        self._breach_threshold = None
        self._action_type = None
        self._additional_subject = None
        self.discriminator = None

        if emails is not None:
            self.emails = emails
        if breach_threshold is not None:
            self.breach_threshold = breach_threshold
        if action_type is not None:
            self.action_type = action_type
        if additional_subject is not None:
            self.additional_subject = additional_subject

    @property
    def emails(self):
        """Gets the emails of this ModelmonitorAlertActionDef.  # noqa: E501

        comma separated emails  # noqa: E501

        :return: The emails of this ModelmonitorAlertActionDef.  # noqa: E501
        :rtype: str
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this ModelmonitorAlertActionDef.

        comma separated emails  # noqa: E501

        :param emails: The emails of this ModelmonitorAlertActionDef.  # noqa: E501
        :type: str
        """

        self._emails = emails

    @property
    def breach_threshold(self):
        """Gets the breach_threshold of this ModelmonitorAlertActionDef.  # noqa: E501


        :return: The breach_threshold of this ModelmonitorAlertActionDef.  # noqa: E501
        :rtype: int
        """
        return self._breach_threshold

    @breach_threshold.setter
    def breach_threshold(self, breach_threshold):
        """Sets the breach_threshold of this ModelmonitorAlertActionDef.


        :param breach_threshold: The breach_threshold of this ModelmonitorAlertActionDef.  # noqa: E501
        :type: int
        """
        if breach_threshold is not None and breach_threshold > 7:  # noqa: E501
            raise ValueError("Invalid value for `breach_threshold`, must be a value less than or equal to `7`")  # noqa: E501

        self._breach_threshold = breach_threshold

    @property
    def action_type(self):
        """Gets the action_type of this ModelmonitorAlertActionDef.  # noqa: E501


        :return: The action_type of this ModelmonitorAlertActionDef.  # noqa: E501
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this ModelmonitorAlertActionDef.


        :param action_type: The action_type of this ModelmonitorAlertActionDef.  # noqa: E501
        :type: str
        """
        allowed_values = ["email"]  # noqa: E501
        if action_type not in allowed_values:
            raise ValueError(
                "Invalid value for `action_type` ({0}), must be one of {1}"  # noqa: E501
                .format(action_type, allowed_values)
            )

        self._action_type = action_type

    @property
    def additional_subject(self):
        """Gets the additional_subject of this ModelmonitorAlertActionDef.  # noqa: E501


        :return: The additional_subject of this ModelmonitorAlertActionDef.  # noqa: E501
        :rtype: object
        """
        return self._additional_subject

    @additional_subject.setter
    def additional_subject(self, additional_subject):
        """Sets the additional_subject of this ModelmonitorAlertActionDef.


        :param additional_subject: The additional_subject of this ModelmonitorAlertActionDef.  # noqa: E501
        :type: object
        """

        self._additional_subject = additional_subject

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
        if issubclass(ModelmonitorAlertActionDef, dict):
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
        if not isinstance(other, ModelmonitorAlertActionDef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
