# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InlineResponse20064Data(object):
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
        'featureset': 'FeatureSetDef',
        'version': 'FeatureSetVersionDef',
        'run': 'JobModel',
        'run_inputs': 'list[FeaturesetLineageInOutModel]',
        'run_outputs': 'list[FeaturesetLineageInOutModel]'
    }

    attribute_map = {
        'featureset': 'featureset',
        'version': 'version',
        'run': 'run',
        'run_inputs': 'run_inputs',
        'run_outputs': 'run_outputs'
    }

    def __init__(self, featureset=None, version=None, run=None, run_inputs=None, run_outputs=None):  # noqa: E501
        """InlineResponse20064Data - a model defined in Swagger"""  # noqa: E501

        self._featureset = None
        self._version = None
        self._run = None
        self._run_inputs = None
        self._run_outputs = None
        self.discriminator = None

        if featureset is not None:
            self.featureset = featureset
        if version is not None:
            self.version = version
        if run is not None:
            self.run = run
        if run_inputs is not None:
            self.run_inputs = run_inputs
        if run_outputs is not None:
            self.run_outputs = run_outputs

    @property
    def featureset(self):
        """Gets the featureset of this InlineResponse20064Data.  # noqa: E501


        :return: The featureset of this InlineResponse20064Data.  # noqa: E501
        :rtype: FeatureSetDef
        """
        return self._featureset

    @featureset.setter
    def featureset(self, featureset):
        """Sets the featureset of this InlineResponse20064Data.


        :param featureset: The featureset of this InlineResponse20064Data.  # noqa: E501
        :type: FeatureSetDef
        """

        self._featureset = featureset

    @property
    def version(self):
        """Gets the version of this InlineResponse20064Data.  # noqa: E501


        :return: The version of this InlineResponse20064Data.  # noqa: E501
        :rtype: FeatureSetVersionDef
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this InlineResponse20064Data.


        :param version: The version of this InlineResponse20064Data.  # noqa: E501
        :type: FeatureSetVersionDef
        """

        self._version = version

    @property
    def run(self):
        """Gets the run of this InlineResponse20064Data.  # noqa: E501


        :return: The run of this InlineResponse20064Data.  # noqa: E501
        :rtype: JobModel
        """
        return self._run

    @run.setter
    def run(self, run):
        """Sets the run of this InlineResponse20064Data.


        :param run: The run of this InlineResponse20064Data.  # noqa: E501
        :type: JobModel
        """

        self._run = run

    @property
    def run_inputs(self):
        """Gets the run_inputs of this InlineResponse20064Data.  # noqa: E501


        :return: The run_inputs of this InlineResponse20064Data.  # noqa: E501
        :rtype: list[FeaturesetLineageInOutModel]
        """
        return self._run_inputs

    @run_inputs.setter
    def run_inputs(self, run_inputs):
        """Sets the run_inputs of this InlineResponse20064Data.


        :param run_inputs: The run_inputs of this InlineResponse20064Data.  # noqa: E501
        :type: list[FeaturesetLineageInOutModel]
        """

        self._run_inputs = run_inputs

    @property
    def run_outputs(self):
        """Gets the run_outputs of this InlineResponse20064Data.  # noqa: E501


        :return: The run_outputs of this InlineResponse20064Data.  # noqa: E501
        :rtype: list[FeaturesetLineageInOutModel]
        """
        return self._run_outputs

    @run_outputs.setter
    def run_outputs(self, run_outputs):
        """Sets the run_outputs of this InlineResponse20064Data.


        :param run_outputs: The run_outputs of this InlineResponse20064Data.  # noqa: E501
        :type: list[FeaturesetLineageInOutModel]
        """

        self._run_outputs = run_outputs

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
        if issubclass(InlineResponse20064Data, dict):
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
        if not isinstance(other, InlineResponse20064Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
