# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.5.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ClusterDetailsNodegroups(object):
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
        'node_group': 'NodeGroup',
        'nodes': 'list[NodeModel]'
    }

    attribute_map = {
        'node_group': 'node_group',
        'nodes': 'nodes'
    }

    def __init__(self, node_group=None, nodes=None):  # noqa: E501
        """ClusterDetailsNodegroups - a model defined in Swagger"""  # noqa: E501

        self._node_group = None
        self._nodes = None
        self.discriminator = None

        if node_group is not None:
            self.node_group = node_group
        if nodes is not None:
            self.nodes = nodes

    @property
    def node_group(self):
        """Gets the node_group of this ClusterDetailsNodegroups.  # noqa: E501


        :return: The node_group of this ClusterDetailsNodegroups.  # noqa: E501
        :rtype: NodeGroup
        """
        return self._node_group

    @node_group.setter
    def node_group(self, node_group):
        """Sets the node_group of this ClusterDetailsNodegroups.


        :param node_group: The node_group of this ClusterDetailsNodegroups.  # noqa: E501
        :type: NodeGroup
        """

        self._node_group = node_group

    @property
    def nodes(self):
        """Gets the nodes of this ClusterDetailsNodegroups.  # noqa: E501


        :return: The nodes of this ClusterDetailsNodegroups.  # noqa: E501
        :rtype: list[NodeModel]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this ClusterDetailsNodegroups.


        :param nodes: The nodes of this ClusterDetailsNodegroups.  # noqa: E501
        :type: list[NodeModel]
        """

        self._nodes = nodes

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
        if issubclass(ClusterDetailsNodegroups, dict):
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
        if not isinstance(other, ClusterDetailsNodegroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
