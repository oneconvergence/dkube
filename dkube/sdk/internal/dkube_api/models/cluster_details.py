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


class ClusterDetails(object):
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
        'cluster': 'Cluster',
        'nodegroups': 'list[ClusterDetailsNodegroups]'
    }

    attribute_map = {
        'cluster': 'cluster',
        'nodegroups': 'nodegroups'
    }

    def __init__(self, cluster=None, nodegroups=None):  # noqa: E501
        """ClusterDetails - a model defined in Swagger"""  # noqa: E501

        self._cluster = None
        self._nodegroups = None
        self.discriminator = None

        if cluster is not None:
            self.cluster = cluster
        if nodegroups is not None:
            self.nodegroups = nodegroups

    @property
    def cluster(self):
        """Gets the cluster of this ClusterDetails.  # noqa: E501


        :return: The cluster of this ClusterDetails.  # noqa: E501
        :rtype: Cluster
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this ClusterDetails.


        :param cluster: The cluster of this ClusterDetails.  # noqa: E501
        :type: Cluster
        """

        self._cluster = cluster

    @property
    def nodegroups(self):
        """Gets the nodegroups of this ClusterDetails.  # noqa: E501


        :return: The nodegroups of this ClusterDetails.  # noqa: E501
        :rtype: list[ClusterDetailsNodegroups]
        """
        return self._nodegroups

    @nodegroups.setter
    def nodegroups(self, nodegroups):
        """Sets the nodegroups of this ClusterDetails.


        :param nodegroups: The nodegroups of this ClusterDetails.  # noqa: E501
        :type: list[ClusterDetailsNodegroups]
        """

        self._nodegroups = nodegroups

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
        if issubclass(ClusterDetails, dict):
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
        if not isinstance(other, ClusterDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
