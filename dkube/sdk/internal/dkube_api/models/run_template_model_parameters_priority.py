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


class RunTemplateModelParametersPriority(object):
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
        'donot_queue': 'str'
    }

    attribute_map = {
        'donot_queue': 'donot_queue'
    }

    def __init__(self, donot_queue=None):  # noqa: E501
        """RunTemplateModelParametersPriority - a model defined in Swagger"""  # noqa: E501

        self._donot_queue = None
        self.discriminator = None

        if donot_queue is not None:
            self.donot_queue = donot_queue

    @property
    def donot_queue(self):
        """Gets the donot_queue of this RunTemplateModelParametersPriority.  # noqa: E501


        :return: The donot_queue of this RunTemplateModelParametersPriority.  # noqa: E501
        :rtype: str
        """
        return self._donot_queue

    @donot_queue.setter
    def donot_queue(self, donot_queue):
        """Sets the donot_queue of this RunTemplateModelParametersPriority.


        :param donot_queue: The donot_queue of this RunTemplateModelParametersPriority.  # noqa: E501
        :type: str
        """

        self._donot_queue = donot_queue

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
        if issubclass(RunTemplateModelParametersPriority, dict):
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
        if not isinstance(other, RunTemplateModelParametersPriority):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
