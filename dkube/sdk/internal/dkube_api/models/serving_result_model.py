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


class ServingResultModel(object):
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
        'modeldir': 'str',
        'servingurl': 'str',
        'curlcmd': 'str',
        'api_prefix': 'str'
    }

    attribute_map = {
        'modeldir': 'modeldir',
        'servingurl': 'servingurl',
        'curlcmd': 'curlcmd',
        'api_prefix': 'apiPrefix'
    }

    def __init__(self, modeldir=None, servingurl=None, curlcmd=None, api_prefix=None):  # noqa: E501
        """ServingResultModel - a model defined in Swagger"""  # noqa: E501

        self._modeldir = None
        self._servingurl = None
        self._curlcmd = None
        self._api_prefix = None
        self.discriminator = None

        if modeldir is not None:
            self.modeldir = modeldir
        if servingurl is not None:
            self.servingurl = servingurl
        if curlcmd is not None:
            self.curlcmd = curlcmd
        if api_prefix is not None:
            self.api_prefix = api_prefix

    @property
    def modeldir(self):
        """Gets the modeldir of this ServingResultModel.  # noqa: E501

        Name of dir where the artificats of this model are stored  # noqa: E501

        :return: The modeldir of this ServingResultModel.  # noqa: E501
        :rtype: str
        """
        return self._modeldir

    @modeldir.setter
    def modeldir(self, modeldir):
        """Sets the modeldir of this ServingResultModel.

        Name of dir where the artificats of this model are stored  # noqa: E501

        :param modeldir: The modeldir of this ServingResultModel.  # noqa: E501
        :type: str
        """

        self._modeldir = modeldir

    @property
    def servingurl(self):
        """Gets the servingurl of this ServingResultModel.  # noqa: E501


        :return: The servingurl of this ServingResultModel.  # noqa: E501
        :rtype: str
        """
        return self._servingurl

    @servingurl.setter
    def servingurl(self, servingurl):
        """Sets the servingurl of this ServingResultModel.


        :param servingurl: The servingurl of this ServingResultModel.  # noqa: E501
        :type: str
        """

        self._servingurl = servingurl

    @property
    def curlcmd(self):
        """Gets the curlcmd of this ServingResultModel.  # noqa: E501


        :return: The curlcmd of this ServingResultModel.  # noqa: E501
        :rtype: str
        """
        return self._curlcmd

    @curlcmd.setter
    def curlcmd(self, curlcmd):
        """Sets the curlcmd of this ServingResultModel.


        :param curlcmd: The curlcmd of this ServingResultModel.  # noqa: E501
        :type: str
        """

        self._curlcmd = curlcmd

    @property
    def api_prefix(self):
        """Gets the api_prefix of this ServingResultModel.  # noqa: E501


        :return: The api_prefix of this ServingResultModel.  # noqa: E501
        :rtype: str
        """
        return self._api_prefix

    @api_prefix.setter
    def api_prefix(self, api_prefix):
        """Sets the api_prefix of this ServingResultModel.


        :param api_prefix: The api_prefix of this ServingResultModel.  # noqa: E501
        :type: str
        """

        self._api_prefix = api_prefix

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
        if issubclass(ServingResultModel, dict):
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
        if not isinstance(other, ServingResultModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
