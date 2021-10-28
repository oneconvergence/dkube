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


class CustomJobResultModel(object):
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
        'url': 'str',
        'outdir': 'str',
        'view': 'DSJobModelView'
    }

    attribute_map = {
        'url': 'url',
        'outdir': 'outdir',
        'view': 'view'
    }

    def __init__(self, url=None, outdir=None, view=None):  # noqa: E501
        """CustomJobResultModel - a model defined in Swagger"""  # noqa: E501

        self._url = None
        self._outdir = None
        self._view = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if outdir is not None:
            self.outdir = outdir
        if view is not None:
            self.view = view

    @property
    def url(self):
        """Gets the url of this CustomJobResultModel.  # noqa: E501

        Service url  # noqa: E501

        :return: The url of this CustomJobResultModel.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CustomJobResultModel.

        Service url  # noqa: E501

        :param url: The url of this CustomJobResultModel.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def outdir(self):
        """Gets the outdir of this CustomJobResultModel.  # noqa: E501

        Minio path where output is stored  # noqa: E501

        :return: The outdir of this CustomJobResultModel.  # noqa: E501
        :rtype: str
        """
        return self._outdir

    @outdir.setter
    def outdir(self, outdir):
        """Sets the outdir of this CustomJobResultModel.

        Minio path where output is stored  # noqa: E501

        :param outdir: The outdir of this CustomJobResultModel.  # noqa: E501
        :type: str
        """

        self._outdir = outdir

    @property
    def view(self):
        """Gets the view of this CustomJobResultModel.  # noqa: E501


        :return: The view of this CustomJobResultModel.  # noqa: E501
        :rtype: DSJobModelView
        """
        return self._view

    @view.setter
    def view(self, view):
        """Sets the view of this CustomJobResultModel.


        :param view: The view of this CustomJobResultModel.  # noqa: E501
        :type: DSJobModelView
        """

        self._view = view

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
        if issubclass(CustomJobResultModel, dict):
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
        if not isinstance(other, CustomJobResultModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
