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


class JobStatusModel(object):
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
        'sub_state': 'str',
        'state': 'str',
        'reason': 'str'
    }

    attribute_map = {
        'sub_state': 'sub_state',
        'state': 'state',
        'reason': 'reason'
    }

    def __init__(self, sub_state=None, state=None, reason=None):  # noqa: E501
        """JobStatusModel - a model defined in Swagger"""  # noqa: E501

        self._sub_state = None
        self._state = None
        self._reason = None
        self.discriminator = None

        if sub_state is not None:
            self.sub_state = sub_state
        if state is not None:
            self.state = state
        if reason is not None:
            self.reason = reason

    @property
    def sub_state(self):
        """Gets the sub_state of this JobStatusModel.  # noqa: E501


        :return: The sub_state of this JobStatusModel.  # noqa: E501
        :rtype: str
        """
        return self._sub_state

    @sub_state.setter
    def sub_state(self, sub_state):
        """Sets the sub_state of this JobStatusModel.


        :param sub_state: The sub_state of this JobStatusModel.  # noqa: E501
        :type: str
        """

        self._sub_state = sub_state

    @property
    def state(self):
        """Gets the state of this JobStatusModel.  # noqa: E501


        :return: The state of this JobStatusModel.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this JobStatusModel.


        :param state: The state of this JobStatusModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["QUEUED", "STARTING", "TRAINING", "RUNNING", "COMPLETE", "STOPPED", "STOPPING", "DELETING", "DELETED", "ERROR", "IMAGEBUILDINPROGRESS", "UPDATING", "CREATED"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def reason(self):
        """Gets the reason of this JobStatusModel.  # noqa: E501


        :return: The reason of this JobStatusModel.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this JobStatusModel.


        :param reason: The reason of this JobStatusModel.  # noqa: E501
        :type: str
        """

        self._reason = reason

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
        if issubclass(JobStatusModel, dict):
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
        if not isinstance(other, JobStatusModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
