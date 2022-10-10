# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.3.0.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class JobClusterModel(object):
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
        'kind': 'str',
        'scheduling_opts': 'JobClusterModelSchedulingOpts'
    }

    attribute_map = {
        'name': 'name',
        'kind': 'kind',
        'scheduling_opts': 'scheduling_opts'
    }

    def __init__(self, name=None, kind=None, scheduling_opts=None):  # noqa: E501
        """JobClusterModel - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._kind = None
        self._scheduling_opts = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if kind is not None:
            self.kind = kind
        if scheduling_opts is not None:
            self.scheduling_opts = scheduling_opts

    @property
    def name(self):
        """Gets the name of this JobClusterModel.  # noqa: E501


        :return: The name of this JobClusterModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobClusterModel.


        :param name: The name of this JobClusterModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def kind(self):
        """Gets the kind of this JobClusterModel.  # noqa: E501


        :return: The kind of this JobClusterModel.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this JobClusterModel.


        :param kind: The kind of this JobClusterModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["CLUSTER_LOCAL", "CLUSTER_SLURMHPC_REMOTE"]  # noqa: E501
        if kind not in allowed_values:
            raise ValueError(
                "Invalid value for `kind` ({0}), must be one of {1}"  # noqa: E501
                .format(kind, allowed_values)
            )

        self._kind = kind

    @property
    def scheduling_opts(self):
        """Gets the scheduling_opts of this JobClusterModel.  # noqa: E501


        :return: The scheduling_opts of this JobClusterModel.  # noqa: E501
        :rtype: JobClusterModelSchedulingOpts
        """
        return self._scheduling_opts

    @scheduling_opts.setter
    def scheduling_opts(self, scheduling_opts):
        """Sets the scheduling_opts of this JobClusterModel.


        :param scheduling_opts: The scheduling_opts of this JobClusterModel.  # noqa: E501
        :type: JobClusterModelSchedulingOpts
        """

        self._scheduling_opts = scheduling_opts

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
        if issubclass(JobClusterModel, dict):
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
        if not isinstance(other, JobClusterModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
