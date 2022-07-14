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


class DeploymentImportRequestDef(object):
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
        'name': 'str',
        'description': 'str',
        'tags': 'list[str]',
        'cluster': 'str',
        'deployment_url': 'str',
        'model_reference': 'str',
        'namespace': 'str',
        'variant': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'tags': 'tags',
        'cluster': 'cluster',
        'deployment_url': 'deployment_url',
        'model_reference': 'model_reference',
        'namespace': 'namespace',
        'variant': 'variant'
    }

    def __init__(self, name=None, description=None, tags=None, cluster=None, deployment_url=None, model_reference=None, namespace=None, variant=None):  # noqa: E501
        """DeploymentImportRequestDef - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._description = None
        self._tags = None
        self._cluster = None
        self._deployment_url = None
        self._model_reference = None
        self._namespace = None
        self._variant = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if cluster is not None:
            self.cluster = cluster
        if deployment_url is not None:
            self.deployment_url = deployment_url
        if model_reference is not None:
            self.model_reference = model_reference
        if namespace is not None:
            self.namespace = namespace
        if variant is not None:
            self.variant = variant

    @property
    def name(self):
        """Gets the name of this DeploymentImportRequestDef.  # noqa: E501


        :return: The name of this DeploymentImportRequestDef.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeploymentImportRequestDef.


        :param name: The name of this DeploymentImportRequestDef.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this DeploymentImportRequestDef.  # noqa: E501


        :return: The description of this DeploymentImportRequestDef.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeploymentImportRequestDef.


        :param description: The description of this DeploymentImportRequestDef.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this DeploymentImportRequestDef.  # noqa: E501


        :return: The tags of this DeploymentImportRequestDef.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DeploymentImportRequestDef.


        :param tags: The tags of this DeploymentImportRequestDef.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def cluster(self):
        """Gets the cluster of this DeploymentImportRequestDef.  # noqa: E501


        :return: The cluster of this DeploymentImportRequestDef.  # noqa: E501
        :rtype: str
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this DeploymentImportRequestDef.


        :param cluster: The cluster of this DeploymentImportRequestDef.  # noqa: E501
        :type: str
        """

        self._cluster = cluster

    @property
    def deployment_url(self):
        """Gets the deployment_url of this DeploymentImportRequestDef.  # noqa: E501


        :return: The deployment_url of this DeploymentImportRequestDef.  # noqa: E501
        :rtype: str
        """
        return self._deployment_url

    @deployment_url.setter
    def deployment_url(self, deployment_url):
        """Sets the deployment_url of this DeploymentImportRequestDef.


        :param deployment_url: The deployment_url of this DeploymentImportRequestDef.  # noqa: E501
        :type: str
        """

        self._deployment_url = deployment_url

    @property
    def model_reference(self):
        """Gets the model_reference of this DeploymentImportRequestDef.  # noqa: E501


        :return: The model_reference of this DeploymentImportRequestDef.  # noqa: E501
        :rtype: str
        """
        return self._model_reference

    @model_reference.setter
    def model_reference(self, model_reference):
        """Sets the model_reference of this DeploymentImportRequestDef.


        :param model_reference: The model_reference of this DeploymentImportRequestDef.  # noqa: E501
        :type: str
        """

        self._model_reference = model_reference

    @property
    def namespace(self):
        """Gets the namespace of this DeploymentImportRequestDef.  # noqa: E501


        :return: The namespace of this DeploymentImportRequestDef.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this DeploymentImportRequestDef.


        :param namespace: The namespace of this DeploymentImportRequestDef.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def variant(self):
        """Gets the variant of this DeploymentImportRequestDef.  # noqa: E501


        :return: The variant of this DeploymentImportRequestDef.  # noqa: E501
        :rtype: str
        """
        return self._variant

    @variant.setter
    def variant(self, variant):
        """Sets the variant of this DeploymentImportRequestDef.


        :param variant: The variant of this DeploymentImportRequestDef.  # noqa: E501
        :type: str
        """

        self._variant = variant

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
        if issubclass(DeploymentImportRequestDef, dict):
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
        if not isinstance(other, DeploymentImportRequestDef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
