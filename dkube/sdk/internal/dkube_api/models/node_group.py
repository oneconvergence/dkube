# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.3.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class NodeGroup(object):
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
        'state': 'str',
        'nodes': 'list[str]',
        'blob': 'str',
        'generated': 'ModelCatalogItemGenerated'
    }

    attribute_map = {
        'name': 'name',
        'state': 'state',
        'nodes': 'nodes',
        'blob': 'blob',
        'generated': 'generated'
    }

    def __init__(self, name=None, state=None, nodes=None, blob=None, generated=None):  # noqa: E501
        """NodeGroup - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._state = None
        self._nodes = None
        self._blob = None
        self._generated = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if state is not None:
            self.state = state
        if nodes is not None:
            self.nodes = nodes
        if blob is not None:
            self.blob = blob
        if generated is not None:
            self.generated = generated

    @property
    def name(self):
        """Gets the name of this NodeGroup.  # noqa: E501


        :return: The name of this NodeGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NodeGroup.


        :param name: The name of this NodeGroup.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def state(self):
        """Gets the state of this NodeGroup.  # noqa: E501


        :return: The state of this NodeGroup.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this NodeGroup.


        :param state: The state of this NodeGroup.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def nodes(self):
        """Gets the nodes of this NodeGroup.  # noqa: E501


        :return: The nodes of this NodeGroup.  # noqa: E501
        :rtype: list[str]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this NodeGroup.


        :param nodes: The nodes of this NodeGroup.  # noqa: E501
        :type: list[str]
        """

        self._nodes = nodes

    @property
    def blob(self):
        """Gets the blob of this NodeGroup.  # noqa: E501


        :return: The blob of this NodeGroup.  # noqa: E501
        :rtype: str
        """
        return self._blob

    @blob.setter
    def blob(self, blob):
        """Sets the blob of this NodeGroup.


        :param blob: The blob of this NodeGroup.  # noqa: E501
        :type: str
        """

        self._blob = blob

    @property
    def generated(self):
        """Gets the generated of this NodeGroup.  # noqa: E501


        :return: The generated of this NodeGroup.  # noqa: E501
        :rtype: ModelCatalogItemGenerated
        """
        return self._generated

    @generated.setter
    def generated(self, generated):
        """Sets the generated of this NodeGroup.


        :param generated: The generated of this NodeGroup.  # noqa: E501
        :type: ModelCatalogItemGenerated
        """

        self._generated = generated

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
        if issubclass(NodeGroup, dict):
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
        if not isinstance(other, NodeGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
