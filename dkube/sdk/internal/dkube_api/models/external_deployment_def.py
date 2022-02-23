# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.3.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ExternalDeploymentDef(object):
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
        'namespace': 'str',
        'variant': 'str',
        'cluster': 'Cluster',
        'reference_model': 'str',
        'deployment_url': 'str',
        'status': 'str'
    }

    attribute_map = {
        'namespace': 'namespace',
        'variant': 'variant',
        'cluster': 'cluster',
        'reference_model': 'reference_model',
        'deployment_url': 'deployment_url',
        'status': 'status'
    }

    def __init__(self, namespace=None, variant=None, cluster=None, reference_model=None, deployment_url=None, status=None):  # noqa: E501
        """ExternalDeploymentDef - a model defined in Swagger"""  # noqa: E501

        self._namespace = None
        self._variant = None
        self._cluster = None
        self._reference_model = None
        self._deployment_url = None
        self._status = None
        self.discriminator = None

        if namespace is not None:
            self.namespace = namespace
        if variant is not None:
            self.variant = variant
        if cluster is not None:
            self.cluster = cluster
        if reference_model is not None:
            self.reference_model = reference_model
        if deployment_url is not None:
            self.deployment_url = deployment_url
        if status is not None:
            self.status = status

    @property
    def namespace(self):
        """Gets the namespace of this ExternalDeploymentDef.  # noqa: E501


        :return: The namespace of this ExternalDeploymentDef.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ExternalDeploymentDef.


        :param namespace: The namespace of this ExternalDeploymentDef.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def variant(self):
        """Gets the variant of this ExternalDeploymentDef.  # noqa: E501


        :return: The variant of this ExternalDeploymentDef.  # noqa: E501
        :rtype: str
        """
        return self._variant

    @variant.setter
    def variant(self, variant):
        """Sets the variant of this ExternalDeploymentDef.


        :param variant: The variant of this ExternalDeploymentDef.  # noqa: E501
        :type: str
        """

        self._variant = variant

    @property
    def cluster(self):
        """Gets the cluster of this ExternalDeploymentDef.  # noqa: E501


        :return: The cluster of this ExternalDeploymentDef.  # noqa: E501
        :rtype: Cluster
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this ExternalDeploymentDef.


        :param cluster: The cluster of this ExternalDeploymentDef.  # noqa: E501
        :type: Cluster
        """

        self._cluster = cluster

    @property
    def reference_model(self):
        """Gets the reference_model of this ExternalDeploymentDef.  # noqa: E501


        :return: The reference_model of this ExternalDeploymentDef.  # noqa: E501
        :rtype: str
        """
        return self._reference_model

    @reference_model.setter
    def reference_model(self, reference_model):
        """Sets the reference_model of this ExternalDeploymentDef.


        :param reference_model: The reference_model of this ExternalDeploymentDef.  # noqa: E501
        :type: str
        """

        self._reference_model = reference_model

    @property
    def deployment_url(self):
        """Gets the deployment_url of this ExternalDeploymentDef.  # noqa: E501


        :return: The deployment_url of this ExternalDeploymentDef.  # noqa: E501
        :rtype: str
        """
        return self._deployment_url

    @deployment_url.setter
    def deployment_url(self, deployment_url):
        """Sets the deployment_url of this ExternalDeploymentDef.


        :param deployment_url: The deployment_url of this ExternalDeploymentDef.  # noqa: E501
        :type: str
        """

        self._deployment_url = deployment_url

    @property
    def status(self):
        """Gets the status of this ExternalDeploymentDef.  # noqa: E501


        :return: The status of this ExternalDeploymentDef.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ExternalDeploymentDef.


        :param status: The status of this ExternalDeploymentDef.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(ExternalDeploymentDef, dict):
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
        if not isinstance(other, ExternalDeploymentDef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
