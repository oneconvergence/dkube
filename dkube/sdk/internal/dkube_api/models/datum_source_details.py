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


class DatumSourceDetails(object):
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
        'kind': 'str',
        'job': 'DatumSourceDetailsJob'
    }

    attribute_map = {
        'kind': 'kind',
        'job': 'job'
    }

    def __init__(self, kind=None, job=None):  # noqa: E501
        """DatumSourceDetails - a model defined in Swagger"""  # noqa: E501

        self._kind = None
        self._job = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if job is not None:
            self.job = job

    @property
    def kind(self):
        """Gets the kind of this DatumSourceDetails.  # noqa: E501


        :return: The kind of this DatumSourceDetails.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this DatumSourceDetails.


        :param kind: The kind of this DatumSourceDetails.  # noqa: E501
        :type: str
        """
        allowed_values = ["dkube_generated", "dkube_referenced"]  # noqa: E501
        if kind not in allowed_values:
            raise ValueError(
                "Invalid value for `kind` ({0}), must be one of {1}"  # noqa: E501
                .format(kind, allowed_values)
            )

        self._kind = kind

    @property
    def job(self):
        """Gets the job of this DatumSourceDetails.  # noqa: E501


        :return: The job of this DatumSourceDetails.  # noqa: E501
        :rtype: DatumSourceDetailsJob
        """
        return self._job

    @job.setter
    def job(self, job):
        """Sets the job of this DatumSourceDetails.


        :param job: The job of this DatumSourceDetails.  # noqa: E501
        :type: DatumSourceDetailsJob
        """

        self._job = job

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
        if issubclass(DatumSourceDetails, dict):
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
        if not isinstance(other, DatumSourceDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
