# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.3.0.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Data40(object):
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
        'version': 'str',
        'name': 'str',
        'description': 'str',
        'tags': 'list[str]',
        'arguments': 'list[str]',
        'component': 'str',
        'container_image': 'str'
    }

    attribute_map = {
        'version': 'version',
        'name': 'name',
        'description': 'description',
        'tags': 'tags',
        'arguments': 'arguments',
        'component': 'component',
        'container_image': 'container_image'
    }

    def __init__(self, version=None, name=None, description=None, tags=None, arguments=None, component=None, container_image=None):  # noqa: E501
        """Data40 - a model defined in Swagger"""  # noqa: E501

        self._version = None
        self._name = None
        self._description = None
        self._tags = None
        self._arguments = None
        self._component = None
        self._container_image = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if arguments is not None:
            self.arguments = arguments
        if component is not None:
            self.component = component
        if container_image is not None:
            self.container_image = container_image

    @property
    def version(self):
        """Gets the version of this Data40.  # noqa: E501


        :return: The version of this Data40.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Data40.


        :param version: The version of this Data40.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def name(self):
        """Gets the name of this Data40.  # noqa: E501


        :return: The name of this Data40.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Data40.


        :param name: The name of this Data40.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Data40.  # noqa: E501


        :return: The description of this Data40.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Data40.


        :param description: The description of this Data40.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this Data40.  # noqa: E501


        :return: The tags of this Data40.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Data40.


        :param tags: The tags of this Data40.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def arguments(self):
        """Gets the arguments of this Data40.  # noqa: E501


        :return: The arguments of this Data40.  # noqa: E501
        :rtype: list[str]
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this Data40.


        :param arguments: The arguments of this Data40.  # noqa: E501
        :type: list[str]
        """

        self._arguments = arguments

    @property
    def component(self):
        """Gets the component of this Data40.  # noqa: E501


        :return: The component of this Data40.  # noqa: E501
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this Data40.


        :param component: The component of this Data40.  # noqa: E501
        :type: str
        """

        self._component = component

    @property
    def container_image(self):
        """Gets the container_image of this Data40.  # noqa: E501


        :return: The container_image of this Data40.  # noqa: E501
        :rtype: str
        """
        return self._container_image

    @container_image.setter
    def container_image(self, container_image):
        """Sets the container_image of this Data40.


        :param container_image: The container_image of this Data40.  # noqa: E501
        :type: str
        """

        self._container_image = container_image

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
        if issubclass(Data40, dict):
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
        if not isinstance(other, Data40):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
