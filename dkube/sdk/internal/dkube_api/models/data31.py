# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.3.0.11
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Data31(object):
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
        'uid': 'str',
        'kind': 'str',
        'namespace': 'str',
        'volumes': 'list[ArtifactVolume]'
    }

    attribute_map = {
        'uid': 'uid',
        'kind': 'kind',
        'namespace': 'namespace',
        'volumes': 'volumes'
    }

    def __init__(self, uid=None, kind=None, namespace=None, volumes=None):  # noqa: E501
        """Data31 - a model defined in Swagger"""  # noqa: E501

        self._uid = None
        self._kind = None
        self._namespace = None
        self._volumes = None
        self.discriminator = None

        if uid is not None:
            self.uid = uid
        if kind is not None:
            self.kind = kind
        if namespace is not None:
            self.namespace = namespace
        if volumes is not None:
            self.volumes = volumes

    @property
    def uid(self):
        """Gets the uid of this Data31.  # noqa: E501

        Unique id which relates all the volumes  # noqa: E501

        :return: The uid of this Data31.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this Data31.

        Unique id which relates all the volumes  # noqa: E501

        :param uid: The uid of this Data31.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def kind(self):
        """Gets the kind of this Data31.  # noqa: E501

        Kind of volume to be exported  # noqa: E501

        :return: The kind of this Data31.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this Data31.

        Kind of volume to be exported  # noqa: E501

        :param kind: The kind of this Data31.  # noqa: E501
        :type: str
        """
        allowed_values = ["input", "output", "intermediate"]  # noqa: E501
        if kind not in allowed_values:
            raise ValueError(
                "Invalid value for `kind` ({0}), must be one of {1}"  # noqa: E501
                .format(kind, allowed_values)
            )

        self._kind = kind

    @property
    def namespace(self):
        """Gets the namespace of this Data31.  # noqa: E501

        K8S namespace in which these vols must be provided  # noqa: E501

        :return: The namespace of this Data31.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this Data31.

        K8S namespace in which these vols must be provided  # noqa: E501

        :param namespace: The namespace of this Data31.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def volumes(self):
        """Gets the volumes of this Data31.  # noqa: E501


        :return: The volumes of this Data31.  # noqa: E501
        :rtype: list[ArtifactVolume]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this Data31.


        :param volumes: The volumes of this Data31.  # noqa: E501
        :type: list[ArtifactVolume]
        """

        self._volumes = volumes

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
        if issubclass(Data31, dict):
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
        if not isinstance(other, Data31):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
