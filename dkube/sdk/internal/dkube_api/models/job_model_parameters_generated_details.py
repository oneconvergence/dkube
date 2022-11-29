# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.7.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class JobModelParametersGeneratedDetails(object):
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
        'tensorboard': 'TensorboardModel',
        'notebook': 'NotebookResultModel',
        'training': 'TrainingResultModel',
        'serving': 'ServingResultModel',
        'custom': 'CustomJobResultModel',
        'accesstoken': 'str',
        'ssh': 'SSHModel'
    }

    attribute_map = {
        'tensorboard': 'tensorboard',
        'notebook': 'notebook',
        'training': 'training',
        'serving': 'serving',
        'custom': 'custom',
        'accesstoken': 'accesstoken',
        'ssh': 'ssh'
    }

    def __init__(self, tensorboard=None, notebook=None, training=None, serving=None, custom=None, accesstoken=None, ssh=None):  # noqa: E501
        """JobModelParametersGeneratedDetails - a model defined in Swagger"""  # noqa: E501

        self._tensorboard = None
        self._notebook = None
        self._training = None
        self._serving = None
        self._custom = None
        self._accesstoken = None
        self._ssh = None
        self.discriminator = None

        if tensorboard is not None:
            self.tensorboard = tensorboard
        if notebook is not None:
            self.notebook = notebook
        if training is not None:
            self.training = training
        if serving is not None:
            self.serving = serving
        if custom is not None:
            self.custom = custom
        if accesstoken is not None:
            self.accesstoken = accesstoken
        if ssh is not None:
            self.ssh = ssh

    @property
    def tensorboard(self):
        """Gets the tensorboard of this JobModelParametersGeneratedDetails.  # noqa: E501


        :return: The tensorboard of this JobModelParametersGeneratedDetails.  # noqa: E501
        :rtype: TensorboardModel
        """
        return self._tensorboard

    @tensorboard.setter
    def tensorboard(self, tensorboard):
        """Sets the tensorboard of this JobModelParametersGeneratedDetails.


        :param tensorboard: The tensorboard of this JobModelParametersGeneratedDetails.  # noqa: E501
        :type: TensorboardModel
        """

        self._tensorboard = tensorboard

    @property
    def notebook(self):
        """Gets the notebook of this JobModelParametersGeneratedDetails.  # noqa: E501

        Will be set if the choice was notebook  # noqa: E501

        :return: The notebook of this JobModelParametersGeneratedDetails.  # noqa: E501
        :rtype: NotebookResultModel
        """
        return self._notebook

    @notebook.setter
    def notebook(self, notebook):
        """Sets the notebook of this JobModelParametersGeneratedDetails.

        Will be set if the choice was notebook  # noqa: E501

        :param notebook: The notebook of this JobModelParametersGeneratedDetails.  # noqa: E501
        :type: NotebookResultModel
        """

        self._notebook = notebook

    @property
    def training(self):
        """Gets the training of this JobModelParametersGeneratedDetails.  # noqa: E501

        Will be set if the choice was training  # noqa: E501

        :return: The training of this JobModelParametersGeneratedDetails.  # noqa: E501
        :rtype: TrainingResultModel
        """
        return self._training

    @training.setter
    def training(self, training):
        """Sets the training of this JobModelParametersGeneratedDetails.

        Will be set if the choice was training  # noqa: E501

        :param training: The training of this JobModelParametersGeneratedDetails.  # noqa: E501
        :type: TrainingResultModel
        """

        self._training = training

    @property
    def serving(self):
        """Gets the serving of this JobModelParametersGeneratedDetails.  # noqa: E501

        Will be generated and set if the choice was serving  # noqa: E501

        :return: The serving of this JobModelParametersGeneratedDetails.  # noqa: E501
        :rtype: ServingResultModel
        """
        return self._serving

    @serving.setter
    def serving(self, serving):
        """Sets the serving of this JobModelParametersGeneratedDetails.

        Will be generated and set if the choice was serving  # noqa: E501

        :param serving: The serving of this JobModelParametersGeneratedDetails.  # noqa: E501
        :type: ServingResultModel
        """

        self._serving = serving

    @property
    def custom(self):
        """Gets the custom of this JobModelParametersGeneratedDetails.  # noqa: E501


        :return: The custom of this JobModelParametersGeneratedDetails.  # noqa: E501
        :rtype: CustomJobResultModel
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        """Sets the custom of this JobModelParametersGeneratedDetails.


        :param custom: The custom of this JobModelParametersGeneratedDetails.  # noqa: E501
        :type: CustomJobResultModel
        """

        self._custom = custom

    @property
    def accesstoken(self):
        """Gets the accesstoken of this JobModelParametersGeneratedDetails.  # noqa: E501


        :return: The accesstoken of this JobModelParametersGeneratedDetails.  # noqa: E501
        :rtype: str
        """
        return self._accesstoken

    @accesstoken.setter
    def accesstoken(self, accesstoken):
        """Sets the accesstoken of this JobModelParametersGeneratedDetails.


        :param accesstoken: The accesstoken of this JobModelParametersGeneratedDetails.  # noqa: E501
        :type: str
        """

        self._accesstoken = accesstoken

    @property
    def ssh(self):
        """Gets the ssh of this JobModelParametersGeneratedDetails.  # noqa: E501


        :return: The ssh of this JobModelParametersGeneratedDetails.  # noqa: E501
        :rtype: SSHModel
        """
        return self._ssh

    @ssh.setter
    def ssh(self, ssh):
        """Sets the ssh of this JobModelParametersGeneratedDetails.


        :param ssh: The ssh of this JobModelParametersGeneratedDetails.  # noqa: E501
        :type: SSHModel
        """

        self._ssh = ssh

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
        if issubclass(JobModelParametersGeneratedDetails, dict):
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
        if not isinstance(other, JobModelParametersGeneratedDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
