# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.2.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class S3AccessCredentials(object):
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
        'access_key_id': 'str',
        'access_key': 'str',
        'bucket': 'str',
        'prefix': 'str',
        'endpoint': 'str'
    }

    attribute_map = {
        'access_key_id': 'AccessKeyId',
        'access_key': 'AccessKey',
        'bucket': 'bucket',
        'prefix': 'prefix',
        'endpoint': 'endpoint'
    }

    def __init__(self, access_key_id=None, access_key=None, bucket=None, prefix=None, endpoint=None):  # noqa: E501
        """S3AccessCredentials - a model defined in Swagger"""  # noqa: E501

        self._access_key_id = None
        self._access_key = None
        self._bucket = None
        self._prefix = None
        self._endpoint = None
        self.discriminator = None

        if access_key_id is not None:
            self.access_key_id = access_key_id
        if access_key is not None:
            self.access_key = access_key
        if bucket is not None:
            self.bucket = bucket
        if prefix is not None:
            self.prefix = prefix
        if endpoint is not None:
            self.endpoint = endpoint

    @property
    def access_key_id(self):
        """Gets the access_key_id of this S3AccessCredentials.  # noqa: E501


        :return: The access_key_id of this S3AccessCredentials.  # noqa: E501
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        """Sets the access_key_id of this S3AccessCredentials.


        :param access_key_id: The access_key_id of this S3AccessCredentials.  # noqa: E501
        :type: str
        """

        self._access_key_id = access_key_id

    @property
    def access_key(self):
        """Gets the access_key of this S3AccessCredentials.  # noqa: E501


        :return: The access_key of this S3AccessCredentials.  # noqa: E501
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this S3AccessCredentials.


        :param access_key: The access_key of this S3AccessCredentials.  # noqa: E501
        :type: str
        """

        self._access_key = access_key

    @property
    def bucket(self):
        """Gets the bucket of this S3AccessCredentials.  # noqa: E501


        :return: The bucket of this S3AccessCredentials.  # noqa: E501
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this S3AccessCredentials.


        :param bucket: The bucket of this S3AccessCredentials.  # noqa: E501
        :type: str
        """

        self._bucket = bucket

    @property
    def prefix(self):
        """Gets the prefix of this S3AccessCredentials.  # noqa: E501


        :return: The prefix of this S3AccessCredentials.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this S3AccessCredentials.


        :param prefix: The prefix of this S3AccessCredentials.  # noqa: E501
        :type: str
        """

        self._prefix = prefix

    @property
    def endpoint(self):
        """Gets the endpoint of this S3AccessCredentials.  # noqa: E501


        :return: The endpoint of this S3AccessCredentials.  # noqa: E501
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this S3AccessCredentials.


        :param endpoint: The endpoint of this S3AccessCredentials.  # noqa: E501
        :type: str
        """

        self._endpoint = endpoint

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
        if issubclass(S3AccessCredentials, dict):
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
        if not isinstance(other, S3AccessCredentials):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
