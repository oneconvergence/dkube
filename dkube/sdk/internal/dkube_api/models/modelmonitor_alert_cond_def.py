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


class ModelmonitorAlertCondDef(object):
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
        'feature': 'str',
        'metric': 'str',
        'op': 'str',
        'threshold': 'float',
        'state': 'str'
    }

    attribute_map = {
        'feature': 'feature',
        'metric': 'metric',
        'op': 'op',
        'threshold': 'threshold',
        'state': 'state'
    }

    def __init__(self, feature=None, metric=None, op='>', threshold=None, state=None):  # noqa: E501
        """ModelmonitorAlertCondDef - a model defined in Swagger"""  # noqa: E501

        self._feature = None
        self._metric = None
        self._op = None
        self._threshold = None
        self._state = None
        self.discriminator = None

        if feature is not None:
            self.feature = feature
        if metric is not None:
            self.metric = metric
        if op is not None:
            self.op = op
        if threshold is not None:
            self.threshold = threshold
        if state is not None:
            self.state = state

    @property
    def feature(self):
        """Gets the feature of this ModelmonitorAlertCondDef.  # noqa: E501


        :return: The feature of this ModelmonitorAlertCondDef.  # noqa: E501
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """Sets the feature of this ModelmonitorAlertCondDef.


        :param feature: The feature of this ModelmonitorAlertCondDef.  # noqa: E501
        :type: str
        """

        self._feature = feature

    @property
    def metric(self):
        """Gets the metric of this ModelmonitorAlertCondDef.  # noqa: E501


        :return: The metric of this ModelmonitorAlertCondDef.  # noqa: E501
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this ModelmonitorAlertCondDef.


        :param metric: The metric of this ModelmonitorAlertCondDef.  # noqa: E501
        :type: str
        """

        self._metric = metric

    @property
    def op(self):
        """Gets the op of this ModelmonitorAlertCondDef.  # noqa: E501


        :return: The op of this ModelmonitorAlertCondDef.  # noqa: E501
        :rtype: str
        """
        return self._op

    @op.setter
    def op(self, op):
        """Sets the op of this ModelmonitorAlertCondDef.


        :param op: The op of this ModelmonitorAlertCondDef.  # noqa: E501
        :type: str
        """

        self._op = op

    @property
    def threshold(self):
        """Gets the threshold of this ModelmonitorAlertCondDef.  # noqa: E501


        :return: The threshold of this ModelmonitorAlertCondDef.  # noqa: E501
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this ModelmonitorAlertCondDef.


        :param threshold: The threshold of this ModelmonitorAlertCondDef.  # noqa: E501
        :type: float
        """

        self._threshold = threshold

    @property
    def state(self):
        """Gets the state of this ModelmonitorAlertCondDef.  # noqa: E501


        :return: The state of this ModelmonitorAlertCondDef.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ModelmonitorAlertCondDef.


        :param state: The state of this ModelmonitorAlertCondDef.  # noqa: E501
        :type: str
        """
        allowed_values = ["warning", "critical"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

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
        if issubclass(ModelmonitorAlertCondDef, dict):
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
        if not isinstance(other, ModelmonitorAlertCondDef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
