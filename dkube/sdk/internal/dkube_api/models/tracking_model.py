# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.2.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TrackingModel(object):
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
        'run_id': 'str',
        'artifact_id': 'str',
        'version_id': 'str',
        'pipeline_id': 'str'
    }

    attribute_map = {
        'run_id': 'runId',
        'artifact_id': 'artifactId',
        'version_id': 'versionId',
        'pipeline_id': 'pipelineId'
    }

    def __init__(self, run_id=None, artifact_id=None, version_id=None, pipeline_id=None):  # noqa: E501
        """TrackingModel - a model defined in Swagger"""  # noqa: E501

        self._run_id = None
        self._artifact_id = None
        self._version_id = None
        self._pipeline_id = None
        self.discriminator = None

        if run_id is not None:
            self.run_id = run_id
        if artifact_id is not None:
            self.artifact_id = artifact_id
        if version_id is not None:
            self.version_id = version_id
        if pipeline_id is not None:
            self.pipeline_id = pipeline_id

    @property
    def run_id(self):
        """Gets the run_id of this TrackingModel.  # noqa: E501


        :return: The run_id of this TrackingModel.  # noqa: E501
        :rtype: str
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """Sets the run_id of this TrackingModel.


        :param run_id: The run_id of this TrackingModel.  # noqa: E501
        :type: str
        """

        self._run_id = run_id

    @property
    def artifact_id(self):
        """Gets the artifact_id of this TrackingModel.  # noqa: E501


        :return: The artifact_id of this TrackingModel.  # noqa: E501
        :rtype: str
        """
        return self._artifact_id

    @artifact_id.setter
    def artifact_id(self, artifact_id):
        """Sets the artifact_id of this TrackingModel.


        :param artifact_id: The artifact_id of this TrackingModel.  # noqa: E501
        :type: str
        """

        self._artifact_id = artifact_id

    @property
    def version_id(self):
        """Gets the version_id of this TrackingModel.  # noqa: E501


        :return: The version_id of this TrackingModel.  # noqa: E501
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this TrackingModel.


        :param version_id: The version_id of this TrackingModel.  # noqa: E501
        :type: str
        """

        self._version_id = version_id

    @property
    def pipeline_id(self):
        """Gets the pipeline_id of this TrackingModel.  # noqa: E501


        :return: The pipeline_id of this TrackingModel.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        """Sets the pipeline_id of this TrackingModel.


        :param pipeline_id: The pipeline_id of this TrackingModel.  # noqa: E501
        :type: str
        """

        self._pipeline_id = pipeline_id

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
        if issubclass(TrackingModel, dict):
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
        if not isinstance(other, TrackingModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
