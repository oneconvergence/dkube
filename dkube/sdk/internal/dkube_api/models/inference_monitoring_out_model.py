# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0.0.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InferenceMonitoringOutModel(object):
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
        'job': 'JobModel',
        'prometheus_query': 'str',
        'deployments': 'list[str]'
    }

    attribute_map = {
        'job': 'job',
        'prometheus_query': 'prometheus_query',
        'deployments': 'deployments'
    }

    def __init__(self, job=None, prometheus_query=None, deployments=None):  # noqa: E501
        """InferenceMonitoringOutModel - a model defined in Swagger"""  # noqa: E501

        self._job = None
        self._prometheus_query = None
        self._deployments = None
        self.discriminator = None

        if job is not None:
            self.job = job
        if prometheus_query is not None:
            self.prometheus_query = prometheus_query
        if deployments is not None:
            self.deployments = deployments

    @property
    def job(self):
        """Gets the job of this InferenceMonitoringOutModel.  # noqa: E501


        :return: The job of this InferenceMonitoringOutModel.  # noqa: E501
        :rtype: JobModel
        """
        return self._job

    @job.setter
    def job(self, job):
        """Sets the job of this InferenceMonitoringOutModel.


        :param job: The job of this InferenceMonitoringOutModel.  # noqa: E501
        :type: JobModel
        """

        self._job = job

    @property
    def prometheus_query(self):
        """Gets the prometheus_query of this InferenceMonitoringOutModel.  # noqa: E501


        :return: The prometheus_query of this InferenceMonitoringOutModel.  # noqa: E501
        :rtype: str
        """
        return self._prometheus_query

    @prometheus_query.setter
    def prometheus_query(self, prometheus_query):
        """Sets the prometheus_query of this InferenceMonitoringOutModel.


        :param prometheus_query: The prometheus_query of this InferenceMonitoringOutModel.  # noqa: E501
        :type: str
        """

        self._prometheus_query = prometheus_query

    @property
    def deployments(self):
        """Gets the deployments of this InferenceMonitoringOutModel.  # noqa: E501


        :return: The deployments of this InferenceMonitoringOutModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._deployments

    @deployments.setter
    def deployments(self, deployments):
        """Sets the deployments of this InferenceMonitoringOutModel.


        :param deployments: The deployments of this InferenceMonitoringOutModel.  # noqa: E501
        :type: list[str]
        """

        self._deployments = deployments

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
        if issubclass(InferenceMonitoringOutModel, dict):
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
        if not isinstance(other, InferenceMonitoringOutModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
