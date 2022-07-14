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


class RunTemplateModelParameters(object):
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
        'gpu_allocation': 'GpuAllocation',
        'priority': 'RunTemplateModelParametersPriority',
        'training': 'DSJobModel',
        'preprocessing': 'PreprocessingJobModel'
    }

    attribute_map = {
        'gpu_allocation': 'gpu_allocation',
        'priority': 'priority',
        'training': 'training',
        'preprocessing': 'preprocessing'
    }

    def __init__(self, gpu_allocation=None, priority=None, training=None, preprocessing=None):  # noqa: E501
        """RunTemplateModelParameters - a model defined in Swagger"""  # noqa: E501

        self._gpu_allocation = None
        self._priority = None
        self._training = None
        self._preprocessing = None
        self.discriminator = None

        if gpu_allocation is not None:
            self.gpu_allocation = gpu_allocation
        if priority is not None:
            self.priority = priority
        if training is not None:
            self.training = training
        if preprocessing is not None:
            self.preprocessing = preprocessing

    @property
    def gpu_allocation(self):
        """Gets the gpu_allocation of this RunTemplateModelParameters.  # noqa: E501


        :return: The gpu_allocation of this RunTemplateModelParameters.  # noqa: E501
        :rtype: GpuAllocation
        """
        return self._gpu_allocation

    @gpu_allocation.setter
    def gpu_allocation(self, gpu_allocation):
        """Sets the gpu_allocation of this RunTemplateModelParameters.


        :param gpu_allocation: The gpu_allocation of this RunTemplateModelParameters.  # noqa: E501
        :type: GpuAllocation
        """

        self._gpu_allocation = gpu_allocation

    @property
    def priority(self):
        """Gets the priority of this RunTemplateModelParameters.  # noqa: E501


        :return: The priority of this RunTemplateModelParameters.  # noqa: E501
        :rtype: RunTemplateModelParametersPriority
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this RunTemplateModelParameters.


        :param priority: The priority of this RunTemplateModelParameters.  # noqa: E501
        :type: RunTemplateModelParametersPriority
        """

        self._priority = priority

    @property
    def training(self):
        """Gets the training of this RunTemplateModelParameters.  # noqa: E501

        Training job related inputs. Should be provided if choice is training job.  # noqa: E501

        :return: The training of this RunTemplateModelParameters.  # noqa: E501
        :rtype: DSJobModel
        """
        return self._training

    @training.setter
    def training(self, training):
        """Sets the training of this RunTemplateModelParameters.

        Training job related inputs. Should be provided if choice is training job.  # noqa: E501

        :param training: The training of this RunTemplateModelParameters.  # noqa: E501
        :type: DSJobModel
        """

        self._training = training

    @property
    def preprocessing(self):
        """Gets the preprocessing of this RunTemplateModelParameters.  # noqa: E501

        Data processing job related inputs.  # noqa: E501

        :return: The preprocessing of this RunTemplateModelParameters.  # noqa: E501
        :rtype: PreprocessingJobModel
        """
        return self._preprocessing

    @preprocessing.setter
    def preprocessing(self, preprocessing):
        """Sets the preprocessing of this RunTemplateModelParameters.

        Data processing job related inputs.  # noqa: E501

        :param preprocessing: The preprocessing of this RunTemplateModelParameters.  # noqa: E501
        :type: PreprocessingJobModel
        """

        self._preprocessing = preprocessing

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
        if issubclass(RunTemplateModelParameters, dict):
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
        if not isinstance(other, RunTemplateModelParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
