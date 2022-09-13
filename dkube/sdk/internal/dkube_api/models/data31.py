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


class Data31(object):
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
        'metrics': 'object',
        'eval_run': 'str',
        'eval_run_name': 'str',
        'artifacts_url': 'str',
        'experiment_name': 'str',
        'pipeline_name': 'str'
    }

    attribute_map = {
        'metrics': 'metrics',
        'eval_run': 'eval_run',
        'eval_run_name': 'eval_run_name',
        'artifacts_url': 'artifacts_url',
        'experiment_name': 'experiment_name',
        'pipeline_name': 'pipeline_name'
    }

    def __init__(self, metrics=None, eval_run=None, eval_run_name=None, artifacts_url=None, experiment_name=None, pipeline_name=None):  # noqa: E501
        """Data31 - a model defined in Swagger"""  # noqa: E501

        self._metrics = None
        self._eval_run = None
        self._eval_run_name = None
        self._artifacts_url = None
        self._experiment_name = None
        self._pipeline_name = None
        self.discriminator = None

        if metrics is not None:
            self.metrics = metrics
        if eval_run is not None:
            self.eval_run = eval_run
        if eval_run_name is not None:
            self.eval_run_name = eval_run_name
        if artifacts_url is not None:
            self.artifacts_url = artifacts_url
        if experiment_name is not None:
            self.experiment_name = experiment_name
        if pipeline_name is not None:
            self.pipeline_name = pipeline_name

    @property
    def metrics(self):
        """Gets the metrics of this Data31.  # noqa: E501


        :return: The metrics of this Data31.  # noqa: E501
        :rtype: object
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this Data31.


        :param metrics: The metrics of this Data31.  # noqa: E501
        :type: object
        """

        self._metrics = metrics

    @property
    def eval_run(self):
        """Gets the eval_run of this Data31.  # noqa: E501


        :return: The eval_run of this Data31.  # noqa: E501
        :rtype: str
        """
        return self._eval_run

    @eval_run.setter
    def eval_run(self, eval_run):
        """Sets the eval_run of this Data31.


        :param eval_run: The eval_run of this Data31.  # noqa: E501
        :type: str
        """

        self._eval_run = eval_run

    @property
    def eval_run_name(self):
        """Gets the eval_run_name of this Data31.  # noqa: E501


        :return: The eval_run_name of this Data31.  # noqa: E501
        :rtype: str
        """
        return self._eval_run_name

    @eval_run_name.setter
    def eval_run_name(self, eval_run_name):
        """Sets the eval_run_name of this Data31.


        :param eval_run_name: The eval_run_name of this Data31.  # noqa: E501
        :type: str
        """

        self._eval_run_name = eval_run_name

    @property
    def artifacts_url(self):
        """Gets the artifacts_url of this Data31.  # noqa: E501


        :return: The artifacts_url of this Data31.  # noqa: E501
        :rtype: str
        """
        return self._artifacts_url

    @artifacts_url.setter
    def artifacts_url(self, artifacts_url):
        """Sets the artifacts_url of this Data31.


        :param artifacts_url: The artifacts_url of this Data31.  # noqa: E501
        :type: str
        """

        self._artifacts_url = artifacts_url

    @property
    def experiment_name(self):
        """Gets the experiment_name of this Data31.  # noqa: E501


        :return: The experiment_name of this Data31.  # noqa: E501
        :rtype: str
        """
        return self._experiment_name

    @experiment_name.setter
    def experiment_name(self, experiment_name):
        """Sets the experiment_name of this Data31.


        :param experiment_name: The experiment_name of this Data31.  # noqa: E501
        :type: str
        """

        self._experiment_name = experiment_name

    @property
    def pipeline_name(self):
        """Gets the pipeline_name of this Data31.  # noqa: E501


        :return: The pipeline_name of this Data31.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_name

    @pipeline_name.setter
    def pipeline_name(self, pipeline_name):
        """Sets the pipeline_name of this Data31.


        :param pipeline_name: The pipeline_name of this Data31.  # noqa: E501
        :type: str
        """

        self._pipeline_name = pipeline_name

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
        if issubclass(Data31, dict):
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
        if not isinstance(other, Data31):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
