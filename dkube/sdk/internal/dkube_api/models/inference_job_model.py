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


class InferenceJobModel(object):
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
        'model': 'str',
        'version': 'str',
        'owner': 'str',
        'device': 'str',
        'deploy': 'bool',
        'mcname': 'str',
        'serving_image': 'CustomContainerModel',
        'transformer': 'bool',
        'transformer_image': 'CustomContainerModel',
        'transformer_project': 'str',
        'transformer_commit_id': 'str',
        'transformer_code': 'str',
        'min_replicas': 'int',
        'max_concurrent_requests': 'int',
        'envs': 'CustomKVModel',
        'resource_requirements': 'ResourceRequirements',
        'enable_logs': 'bool'
    }

    attribute_map = {
        'model': 'model',
        'version': 'version',
        'owner': 'owner',
        'device': 'device',
        'deploy': 'deploy',
        'mcname': 'mcname',
        'serving_image': 'serving_image',
        'transformer': 'transformer',
        'transformer_image': 'transformer_image',
        'transformer_project': 'transformer_project',
        'transformer_commit_id': 'transformer-commitID',
        'transformer_code': 'transformer_code',
        'min_replicas': 'minReplicas',
        'max_concurrent_requests': 'maxConcurrentRequests',
        'envs': 'envs',
        'resource_requirements': 'resourceRequirements',
        'enable_logs': 'enable_logs'
    }

    def __init__(self, model=None, version=None, owner=None, device=None, deploy=False, mcname=None, serving_image=None, transformer=False, transformer_image=None, transformer_project=None, transformer_commit_id=None, transformer_code=None, min_replicas=None, max_concurrent_requests=None, envs=None, resource_requirements=None, enable_logs=None):  # noqa: E501
        """InferenceJobModel - a model defined in Swagger"""  # noqa: E501

        self._model = None
        self._version = None
        self._owner = None
        self._device = None
        self._deploy = None
        self._mcname = None
        self._serving_image = None
        self._transformer = None
        self._transformer_image = None
        self._transformer_project = None
        self._transformer_commit_id = None
        self._transformer_code = None
        self._min_replicas = None
        self._max_concurrent_requests = None
        self._envs = None
        self._resource_requirements = None
        self._enable_logs = None
        self.discriminator = None

        if model is not None:
            self.model = model
        if version is not None:
            self.version = version
        if owner is not None:
            self.owner = owner
        if device is not None:
            self.device = device
        if deploy is not None:
            self.deploy = deploy
        if mcname is not None:
            self.mcname = mcname
        if serving_image is not None:
            self.serving_image = serving_image
        if transformer is not None:
            self.transformer = transformer
        if transformer_image is not None:
            self.transformer_image = transformer_image
        if transformer_project is not None:
            self.transformer_project = transformer_project
        if transformer_commit_id is not None:
            self.transformer_commit_id = transformer_commit_id
        if transformer_code is not None:
            self.transformer_code = transformer_code
        if min_replicas is not None:
            self.min_replicas = min_replicas
        if max_concurrent_requests is not None:
            self.max_concurrent_requests = max_concurrent_requests
        if envs is not None:
            self.envs = envs
        if resource_requirements is not None:
            self.resource_requirements = resource_requirements
        if enable_logs is not None:
            self.enable_logs = enable_logs

    @property
    def model(self):
        """Gets the model of this InferenceJobModel.  # noqa: E501

        Name of the model to be deployed  # noqa: E501

        :return: The model of this InferenceJobModel.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this InferenceJobModel.

        Name of the model to be deployed  # noqa: E501

        :param model: The model of this InferenceJobModel.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def version(self):
        """Gets the version of this InferenceJobModel.  # noqa: E501

        Version of the model to be deployed  # noqa: E501

        :return: The version of this InferenceJobModel.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this InferenceJobModel.

        Version of the model to be deployed  # noqa: E501

        :param version: The version of this InferenceJobModel.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def owner(self):
        """Gets the owner of this InferenceJobModel.  # noqa: E501

        Name of the user who owns the model  # noqa: E501

        :return: The owner of this InferenceJobModel.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this InferenceJobModel.

        Name of the user who owns the model  # noqa: E501

        :param owner: The owner of this InferenceJobModel.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def device(self):
        """Gets the device of this InferenceJobModel.  # noqa: E501

        Type of device to serve model on  # noqa: E501

        :return: The device of this InferenceJobModel.  # noqa: E501
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this InferenceJobModel.

        Type of device to serve model on  # noqa: E501

        :param device: The device of this InferenceJobModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["cpu", "gpu"]  # noqa: E501
        if device not in allowed_values:
            raise ValueError(
                "Invalid value for `device` ({0}), must be one of {1}"  # noqa: E501
                .format(device, allowed_values)
            )

        self._device = device

    @property
    def deploy(self):
        """Gets the deploy of this InferenceJobModel.  # noqa: E501


        :return: The deploy of this InferenceJobModel.  # noqa: E501
        :rtype: bool
        """
        return self._deploy

    @deploy.setter
    def deploy(self, deploy):
        """Sets the deploy of this InferenceJobModel.


        :param deploy: The deploy of this InferenceJobModel.  # noqa: E501
        :type: bool
        """

        self._deploy = deploy

    @property
    def mcname(self):
        """Gets the mcname of this InferenceJobModel.  # noqa: E501

        Model catalog item name  # noqa: E501

        :return: The mcname of this InferenceJobModel.  # noqa: E501
        :rtype: str
        """
        return self._mcname

    @mcname.setter
    def mcname(self, mcname):
        """Sets the mcname of this InferenceJobModel.

        Model catalog item name  # noqa: E501

        :param mcname: The mcname of this InferenceJobModel.  # noqa: E501
        :type: str
        """

        self._mcname = mcname

    @property
    def serving_image(self):
        """Gets the serving_image of this InferenceJobModel.  # noqa: E501


        :return: The serving_image of this InferenceJobModel.  # noqa: E501
        :rtype: CustomContainerModel
        """
        return self._serving_image

    @serving_image.setter
    def serving_image(self, serving_image):
        """Sets the serving_image of this InferenceJobModel.


        :param serving_image: The serving_image of this InferenceJobModel.  # noqa: E501
        :type: CustomContainerModel
        """

        self._serving_image = serving_image

    @property
    def transformer(self):
        """Gets the transformer of this InferenceJobModel.  # noqa: E501


        :return: The transformer of this InferenceJobModel.  # noqa: E501
        :rtype: bool
        """
        return self._transformer

    @transformer.setter
    def transformer(self, transformer):
        """Sets the transformer of this InferenceJobModel.


        :param transformer: The transformer of this InferenceJobModel.  # noqa: E501
        :type: bool
        """

        self._transformer = transformer

    @property
    def transformer_image(self):
        """Gets the transformer_image of this InferenceJobModel.  # noqa: E501


        :return: The transformer_image of this InferenceJobModel.  # noqa: E501
        :rtype: CustomContainerModel
        """
        return self._transformer_image

    @transformer_image.setter
    def transformer_image(self, transformer_image):
        """Sets the transformer_image of this InferenceJobModel.


        :param transformer_image: The transformer_image of this InferenceJobModel.  # noqa: E501
        :type: CustomContainerModel
        """

        self._transformer_image = transformer_image

    @property
    def transformer_project(self):
        """Gets the transformer_project of this InferenceJobModel.  # noqa: E501


        :return: The transformer_project of this InferenceJobModel.  # noqa: E501
        :rtype: str
        """
        return self._transformer_project

    @transformer_project.setter
    def transformer_project(self, transformer_project):
        """Sets the transformer_project of this InferenceJobModel.


        :param transformer_project: The transformer_project of this InferenceJobModel.  # noqa: E501
        :type: str
        """

        self._transformer_project = transformer_project

    @property
    def transformer_commit_id(self):
        """Gets the transformer_commit_id of this InferenceJobModel.  # noqa: E501


        :return: The transformer_commit_id of this InferenceJobModel.  # noqa: E501
        :rtype: str
        """
        return self._transformer_commit_id

    @transformer_commit_id.setter
    def transformer_commit_id(self, transformer_commit_id):
        """Sets the transformer_commit_id of this InferenceJobModel.


        :param transformer_commit_id: The transformer_commit_id of this InferenceJobModel.  # noqa: E501
        :type: str
        """

        self._transformer_commit_id = transformer_commit_id

    @property
    def transformer_code(self):
        """Gets the transformer_code of this InferenceJobModel.  # noqa: E501

        path to transformer code in the project selected  # noqa: E501

        :return: The transformer_code of this InferenceJobModel.  # noqa: E501
        :rtype: str
        """
        return self._transformer_code

    @transformer_code.setter
    def transformer_code(self, transformer_code):
        """Sets the transformer_code of this InferenceJobModel.

        path to transformer code in the project selected  # noqa: E501

        :param transformer_code: The transformer_code of this InferenceJobModel.  # noqa: E501
        :type: str
        """

        self._transformer_code = transformer_code

    @property
    def min_replicas(self):
        """Gets the min_replicas of this InferenceJobModel.  # noqa: E501


        :return: The min_replicas of this InferenceJobModel.  # noqa: E501
        :rtype: int
        """
        return self._min_replicas

    @min_replicas.setter
    def min_replicas(self, min_replicas):
        """Sets the min_replicas of this InferenceJobModel.


        :param min_replicas: The min_replicas of this InferenceJobModel.  # noqa: E501
        :type: int
        """

        self._min_replicas = min_replicas

    @property
    def max_concurrent_requests(self):
        """Gets the max_concurrent_requests of this InferenceJobModel.  # noqa: E501


        :return: The max_concurrent_requests of this InferenceJobModel.  # noqa: E501
        :rtype: int
        """
        return self._max_concurrent_requests

    @max_concurrent_requests.setter
    def max_concurrent_requests(self, max_concurrent_requests):
        """Sets the max_concurrent_requests of this InferenceJobModel.


        :param max_concurrent_requests: The max_concurrent_requests of this InferenceJobModel.  # noqa: E501
        :type: int
        """

        self._max_concurrent_requests = max_concurrent_requests

    @property
    def envs(self):
        """Gets the envs of this InferenceJobModel.  # noqa: E501


        :return: The envs of this InferenceJobModel.  # noqa: E501
        :rtype: CustomKVModel
        """
        return self._envs

    @envs.setter
    def envs(self, envs):
        """Sets the envs of this InferenceJobModel.


        :param envs: The envs of this InferenceJobModel.  # noqa: E501
        :type: CustomKVModel
        """

        self._envs = envs

    @property
    def resource_requirements(self):
        """Gets the resource_requirements of this InferenceJobModel.  # noqa: E501


        :return: The resource_requirements of this InferenceJobModel.  # noqa: E501
        :rtype: ResourceRequirements
        """
        return self._resource_requirements

    @resource_requirements.setter
    def resource_requirements(self, resource_requirements):
        """Sets the resource_requirements of this InferenceJobModel.


        :param resource_requirements: The resource_requirements of this InferenceJobModel.  # noqa: E501
        :type: ResourceRequirements
        """

        self._resource_requirements = resource_requirements

    @property
    def enable_logs(self):
        """Gets the enable_logs of this InferenceJobModel.  # noqa: E501


        :return: The enable_logs of this InferenceJobModel.  # noqa: E501
        :rtype: bool
        """
        return self._enable_logs

    @enable_logs.setter
    def enable_logs(self, enable_logs):
        """Sets the enable_logs of this InferenceJobModel.


        :param enable_logs: The enable_logs of this InferenceJobModel.  # noqa: E501
        :type: bool
        """

        self._enable_logs = enable_logs

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
        if issubclass(InferenceJobModel, dict):
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
        if not isinstance(other, InferenceJobModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
