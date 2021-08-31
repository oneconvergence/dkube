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


class JobModelParametersGeneratedInputFeaturesetRefs(object):
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
        'fsetuuid': 'str',
        'version_uuid': 'str',
        'version_name': 'str',
        'version_index': 'int'
    }

    attribute_map = {
        'fsetuuid': 'fsetuuid',
        'version_uuid': 'version_uuid',
        'version_name': 'version_name',
        'version_index': 'version_index'
    }

    def __init__(self, fsetuuid=None, version_uuid=None, version_name=None, version_index=None):  # noqa: E501
        """JobModelParametersGeneratedInputFeaturesetRefs - a model defined in Swagger"""  # noqa: E501

        self._fsetuuid = None
        self._version_uuid = None
        self._version_name = None
        self._version_index = None
        self.discriminator = None

        if fsetuuid is not None:
            self.fsetuuid = fsetuuid
        if version_uuid is not None:
            self.version_uuid = version_uuid
        if version_name is not None:
            self.version_name = version_name
        if version_index is not None:
            self.version_index = version_index

    @property
    def fsetuuid(self):
        """Gets the fsetuuid of this JobModelParametersGeneratedInputFeaturesetRefs.  # noqa: E501


        :return: The fsetuuid of this JobModelParametersGeneratedInputFeaturesetRefs.  # noqa: E501
        :rtype: str
        """
        return self._fsetuuid

    @fsetuuid.setter
    def fsetuuid(self, fsetuuid):
        """Sets the fsetuuid of this JobModelParametersGeneratedInputFeaturesetRefs.


        :param fsetuuid: The fsetuuid of this JobModelParametersGeneratedInputFeaturesetRefs.  # noqa: E501
        :type: str
        """

        self._fsetuuid = fsetuuid

    @property
    def version_uuid(self):
        """Gets the version_uuid of this JobModelParametersGeneratedInputFeaturesetRefs.  # noqa: E501


        :return: The version_uuid of this JobModelParametersGeneratedInputFeaturesetRefs.  # noqa: E501
        :rtype: str
        """
        return self._version_uuid

    @version_uuid.setter
    def version_uuid(self, version_uuid):
        """Sets the version_uuid of this JobModelParametersGeneratedInputFeaturesetRefs.


        :param version_uuid: The version_uuid of this JobModelParametersGeneratedInputFeaturesetRefs.  # noqa: E501
        :type: str
        """

        self._version_uuid = version_uuid

    @property
    def version_name(self):
        """Gets the version_name of this JobModelParametersGeneratedInputFeaturesetRefs.  # noqa: E501


        :return: The version_name of this JobModelParametersGeneratedInputFeaturesetRefs.  # noqa: E501
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        """Sets the version_name of this JobModelParametersGeneratedInputFeaturesetRefs.


        :param version_name: The version_name of this JobModelParametersGeneratedInputFeaturesetRefs.  # noqa: E501
        :type: str
        """

        self._version_name = version_name

    @property
    def version_index(self):
        """Gets the version_index of this JobModelParametersGeneratedInputFeaturesetRefs.  # noqa: E501


        :return: The version_index of this JobModelParametersGeneratedInputFeaturesetRefs.  # noqa: E501
        :rtype: int
        """
        return self._version_index

    @version_index.setter
    def version_index(self, version_index):
        """Sets the version_index of this JobModelParametersGeneratedInputFeaturesetRefs.


        :param version_index: The version_index of this JobModelParametersGeneratedInputFeaturesetRefs.  # noqa: E501
        :type: int
        """

        self._version_index = version_index

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
        if issubclass(JobModelParametersGeneratedInputFeaturesetRefs, dict):
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
        if not isinstance(other, JobModelParametersGeneratedInputFeaturesetRefs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
