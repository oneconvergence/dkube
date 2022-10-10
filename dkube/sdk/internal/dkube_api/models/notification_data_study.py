# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.5.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class NotificationDataStudy(object):
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
        'study_id': 'str',
        'best_trial_id': 'str',
        'best_objective_value': 'float'
    }

    attribute_map = {
        'study_id': 'StudyID',
        'best_trial_id': 'BestTrialID',
        'best_objective_value': 'BestObjectiveValue'
    }

    def __init__(self, study_id=None, best_trial_id=None, best_objective_value=None):  # noqa: E501
        """NotificationDataStudy - a model defined in Swagger"""  # noqa: E501

        self._study_id = None
        self._best_trial_id = None
        self._best_objective_value = None
        self.discriminator = None

        if study_id is not None:
            self.study_id = study_id
        if best_trial_id is not None:
            self.best_trial_id = best_trial_id
        if best_objective_value is not None:
            self.best_objective_value = best_objective_value

    @property
    def study_id(self):
        """Gets the study_id of this NotificationDataStudy.  # noqa: E501


        :return: The study_id of this NotificationDataStudy.  # noqa: E501
        :rtype: str
        """
        return self._study_id

    @study_id.setter
    def study_id(self, study_id):
        """Sets the study_id of this NotificationDataStudy.


        :param study_id: The study_id of this NotificationDataStudy.  # noqa: E501
        :type: str
        """

        self._study_id = study_id

    @property
    def best_trial_id(self):
        """Gets the best_trial_id of this NotificationDataStudy.  # noqa: E501


        :return: The best_trial_id of this NotificationDataStudy.  # noqa: E501
        :rtype: str
        """
        return self._best_trial_id

    @best_trial_id.setter
    def best_trial_id(self, best_trial_id):
        """Sets the best_trial_id of this NotificationDataStudy.


        :param best_trial_id: The best_trial_id of this NotificationDataStudy.  # noqa: E501
        :type: str
        """

        self._best_trial_id = best_trial_id

    @property
    def best_objective_value(self):
        """Gets the best_objective_value of this NotificationDataStudy.  # noqa: E501


        :return: The best_objective_value of this NotificationDataStudy.  # noqa: E501
        :rtype: float
        """
        return self._best_objective_value

    @best_objective_value.setter
    def best_objective_value(self, best_objective_value):
        """Sets the best_objective_value of this NotificationDataStudy.


        :param best_objective_value: The best_objective_value of this NotificationDataStudy.  # noqa: E501
        :type: float
        """

        self._best_objective_value = best_objective_value

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
        if issubclass(NotificationDataStudy, dict):
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
        if not isinstance(other, NotificationDataStudy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
