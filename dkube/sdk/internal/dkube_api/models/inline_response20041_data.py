# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.3.0.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InlineResponse20041Data(object):
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
        '_class': 'str',
        'jobs': 'list[JobCollection]'
    }

    attribute_map = {
        '_class': 'class',
        'jobs': 'jobs'
    }

    def __init__(self, _class=None, jobs=None):  # noqa: E501
        """InlineResponse20041Data - a model defined in Swagger"""  # noqa: E501

        self.__class = None
        self._jobs = None
        self.discriminator = None

        if _class is not None:
            self._class = _class
        if jobs is not None:
            self.jobs = jobs

    @property
    def _class(self):
        """Gets the _class of this InlineResponse20041Data.  # noqa: E501


        :return: The _class of this InlineResponse20041Data.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this InlineResponse20041Data.


        :param _class: The _class of this InlineResponse20041Data.  # noqa: E501
        :type: str
        """

        self.__class = _class

    @property
    def jobs(self):
        """Gets the jobs of this InlineResponse20041Data.  # noqa: E501


        :return: The jobs of this InlineResponse20041Data.  # noqa: E501
        :rtype: list[JobCollection]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this InlineResponse20041Data.


        :param jobs: The jobs of this InlineResponse20041Data.  # noqa: E501
        :type: list[JobCollection]
        """

        self._jobs = jobs

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
        if issubclass(InlineResponse20041Data, dict):
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
        if not isinstance(other, InlineResponse20041Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
