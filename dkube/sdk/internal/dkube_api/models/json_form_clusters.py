# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class JsonFormClusters(object):
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
        'kind': 'str',
        'name': 'str',
        'login_required': 'bool',
        'opts': 'str'
    }

    attribute_map = {
        'kind': 'kind',
        'name': 'name',
        'login_required': 'login_required',
        'opts': 'opts'
    }

    def __init__(self, kind=None, name=None, login_required=False, opts=None):  # noqa: E501
        """JsonFormClusters - a model defined in Swagger"""  # noqa: E501

        self._kind = None
        self._name = None
        self._login_required = None
        self._opts = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if name is not None:
            self.name = name
        if login_required is not None:
            self.login_required = login_required
        if opts is not None:
            self.opts = opts

    @property
    def kind(self):
        """Gets the kind of this JsonFormClusters.  # noqa: E501


        :return: The kind of this JsonFormClusters.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this JsonFormClusters.


        :param kind: The kind of this JsonFormClusters.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def name(self):
        """Gets the name of this JsonFormClusters.  # noqa: E501


        :return: The name of this JsonFormClusters.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JsonFormClusters.


        :param name: The name of this JsonFormClusters.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def login_required(self):
        """Gets the login_required of this JsonFormClusters.  # noqa: E501


        :return: The login_required of this JsonFormClusters.  # noqa: E501
        :rtype: bool
        """
        return self._login_required

    @login_required.setter
    def login_required(self, login_required):
        """Sets the login_required of this JsonFormClusters.


        :param login_required: The login_required of this JsonFormClusters.  # noqa: E501
        :type: bool
        """

        self._login_required = login_required

    @property
    def opts(self):
        """Gets the opts of this JsonFormClusters.  # noqa: E501


        :return: The opts of this JsonFormClusters.  # noqa: E501
        :rtype: str
        """
        return self._opts

    @opts.setter
    def opts(self, opts):
        """Sets the opts of this JsonFormClusters.


        :param opts: The opts of this JsonFormClusters.  # noqa: E501
        :type: str
        """

        self._opts = opts

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
        if issubclass(JsonFormClusters, dict):
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
        if not isinstance(other, JsonFormClusters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
