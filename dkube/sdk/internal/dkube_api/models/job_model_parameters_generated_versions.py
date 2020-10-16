# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.2.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class JobModelParametersGeneratedVersions(object):
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
        'cuda': 'str',
        'dkube': 'str',
        'nvidia': 'str'
    }

    attribute_map = {
        'cuda': 'cuda',
        'dkube': 'dkube',
        'nvidia': 'nvidia'
    }

    def __init__(self, cuda=None, dkube=None, nvidia=None):  # noqa: E501
        """JobModelParametersGeneratedVersions - a model defined in Swagger"""  # noqa: E501

        self._cuda = None
        self._dkube = None
        self._nvidia = None
        self.discriminator = None

        if cuda is not None:
            self.cuda = cuda
        if dkube is not None:
            self.dkube = dkube
        if nvidia is not None:
            self.nvidia = nvidia

    @property
    def cuda(self):
        """Gets the cuda of this JobModelParametersGeneratedVersions.  # noqa: E501


        :return: The cuda of this JobModelParametersGeneratedVersions.  # noqa: E501
        :rtype: str
        """
        return self._cuda

    @cuda.setter
    def cuda(self, cuda):
        """Sets the cuda of this JobModelParametersGeneratedVersions.


        :param cuda: The cuda of this JobModelParametersGeneratedVersions.  # noqa: E501
        :type: str
        """

        self._cuda = cuda

    @property
    def dkube(self):
        """Gets the dkube of this JobModelParametersGeneratedVersions.  # noqa: E501


        :return: The dkube of this JobModelParametersGeneratedVersions.  # noqa: E501
        :rtype: str
        """
        return self._dkube

    @dkube.setter
    def dkube(self, dkube):
        """Sets the dkube of this JobModelParametersGeneratedVersions.


        :param dkube: The dkube of this JobModelParametersGeneratedVersions.  # noqa: E501
        :type: str
        """

        self._dkube = dkube

    @property
    def nvidia(self):
        """Gets the nvidia of this JobModelParametersGeneratedVersions.  # noqa: E501


        :return: The nvidia of this JobModelParametersGeneratedVersions.  # noqa: E501
        :rtype: str
        """
        return self._nvidia

    @nvidia.setter
    def nvidia(self, nvidia):
        """Sets the nvidia of this JobModelParametersGeneratedVersions.


        :param nvidia: The nvidia of this JobModelParametersGeneratedVersions.  # noqa: E501
        :type: str
        """

        self._nvidia = nvidia

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
        if issubclass(JobModelParametersGeneratedVersions, dict):
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
        if not isinstance(other, JobModelParametersGeneratedVersions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other