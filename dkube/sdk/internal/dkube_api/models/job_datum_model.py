# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.3.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class JobDatumModel(object):
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
        'workspace': 'JobDatumModelWorkspace',
        'models': 'list[JobInputDatumModel]',
        'datasets': 'list[JobInputDatumModel]',
        'outputs': 'list[JobInputDatumModel]'
    }

    attribute_map = {
        'workspace': 'workspace',
        'models': 'models',
        'datasets': 'datasets',
        'outputs': 'outputs'
    }

    def __init__(self, workspace=None, models=None, datasets=None, outputs=None):  # noqa: E501
        """JobDatumModel - a model defined in Swagger"""  # noqa: E501

        self._workspace = None
        self._models = None
        self._datasets = None
        self._outputs = None
        self.discriminator = None

        if workspace is not None:
            self.workspace = workspace
        if models is not None:
            self.models = models
        if datasets is not None:
            self.datasets = datasets
        if outputs is not None:
            self.outputs = outputs

    @property
    def workspace(self):
        """Gets the workspace of this JobDatumModel.  # noqa: E501


        :return: The workspace of this JobDatumModel.  # noqa: E501
        :rtype: JobDatumModelWorkspace
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this JobDatumModel.


        :param workspace: The workspace of this JobDatumModel.  # noqa: E501
        :type: JobDatumModelWorkspace
        """

        self._workspace = workspace

    @property
    def models(self):
        """Gets the models of this JobDatumModel.  # noqa: E501

        List of model names the job would use.  # noqa: E501

        :return: The models of this JobDatumModel.  # noqa: E501
        :rtype: list[JobInputDatumModel]
        """
        return self._models

    @models.setter
    def models(self, models):
        """Sets the models of this JobDatumModel.

        List of model names the job would use.  # noqa: E501

        :param models: The models of this JobDatumModel.  # noqa: E501
        :type: list[JobInputDatumModel]
        """

        self._models = models

    @property
    def datasets(self):
        """Gets the datasets of this JobDatumModel.  # noqa: E501

        List of dataset names the job would use.  # noqa: E501

        :return: The datasets of this JobDatumModel.  # noqa: E501
        :rtype: list[JobInputDatumModel]
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets):
        """Sets the datasets of this JobDatumModel.

        List of dataset names the job would use.  # noqa: E501

        :param datasets: The datasets of this JobDatumModel.  # noqa: E501
        :type: list[JobInputDatumModel]
        """

        self._datasets = datasets

    @property
    def outputs(self):
        """Gets the outputs of this JobDatumModel.  # noqa: E501

        List of datum names the job would generate.  # noqa: E501

        :return: The outputs of this JobDatumModel.  # noqa: E501
        :rtype: list[JobInputDatumModel]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this JobDatumModel.

        List of datum names the job would generate.  # noqa: E501

        :param outputs: The outputs of this JobDatumModel.  # noqa: E501
        :type: list[JobInputDatumModel]
        """

        self._outputs = outputs

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
        if issubclass(JobDatumModel, dict):
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
        if not isinstance(other, JobDatumModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
