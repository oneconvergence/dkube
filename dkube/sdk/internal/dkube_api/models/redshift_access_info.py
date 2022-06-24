# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.3.0.14
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class RedshiftAccessInfo(object):
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
        'endpoint': 'str',
        'username': 'str',
        'password': 'str',
        'database': 'str',
        'region': 'str',
        'cacert': 'CertFileModel',
        'insecure_ssl': 'bool'
    }

    attribute_map = {
        'endpoint': 'endpoint',
        'username': 'username',
        'password': 'password',
        'database': 'database',
        'region': 'region',
        'cacert': 'cacert',
        'insecure_ssl': 'insecureSSL'
    }

    def __init__(self, endpoint=None, username=None, password=None, database=None, region=None, cacert=None, insecure_ssl=None):  # noqa: E501
        """RedshiftAccessInfo - a model defined in Swagger"""  # noqa: E501

        self._endpoint = None
        self._username = None
        self._password = None
        self._database = None
        self._region = None
        self._cacert = None
        self._insecure_ssl = None
        self.discriminator = None

        if endpoint is not None:
            self.endpoint = endpoint
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if database is not None:
            self.database = database
        if region is not None:
            self.region = region
        if cacert is not None:
            self.cacert = cacert
        if insecure_ssl is not None:
            self.insecure_ssl = insecure_ssl

    @property
    def endpoint(self):
        """Gets the endpoint of this RedshiftAccessInfo.  # noqa: E501

        Redshift endpoint to connect to. Should be with protocol, host and port.  # noqa: E501

        :return: The endpoint of this RedshiftAccessInfo.  # noqa: E501
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this RedshiftAccessInfo.

        Redshift endpoint to connect to. Should be with protocol, host and port.  # noqa: E501

        :param endpoint: The endpoint of this RedshiftAccessInfo.  # noqa: E501
        :type: str
        """

        self._endpoint = endpoint

    @property
    def username(self):
        """Gets the username of this RedshiftAccessInfo.  # noqa: E501

        User authorized to connect to database.  # noqa: E501

        :return: The username of this RedshiftAccessInfo.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this RedshiftAccessInfo.

        User authorized to connect to database.  # noqa: E501

        :param username: The username of this RedshiftAccessInfo.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this RedshiftAccessInfo.  # noqa: E501

        Password to be used to connect to redshift.  # noqa: E501

        :return: The password of this RedshiftAccessInfo.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this RedshiftAccessInfo.

        Password to be used to connect to redshift.  # noqa: E501

        :param password: The password of this RedshiftAccessInfo.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def database(self):
        """Gets the database of this RedshiftAccessInfo.  # noqa: E501

        Database in the redshift that this dataset should point to.  # noqa: E501

        :return: The database of this RedshiftAccessInfo.  # noqa: E501
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this RedshiftAccessInfo.

        Database in the redshift that this dataset should point to.  # noqa: E501

        :param database: The database of this RedshiftAccessInfo.  # noqa: E501
        :type: str
        """

        self._database = database

    @property
    def region(self):
        """Gets the region of this RedshiftAccessInfo.  # noqa: E501

        Region where this database resides.  # noqa: E501

        :return: The region of this RedshiftAccessInfo.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this RedshiftAccessInfo.

        Region where this database resides.  # noqa: E501

        :param region: The region of this RedshiftAccessInfo.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def cacert(self):
        """Gets the cacert of this RedshiftAccessInfo.  # noqa: E501

        Certificate to be used while connecting to redshift.  # noqa: E501

        :return: The cacert of this RedshiftAccessInfo.  # noqa: E501
        :rtype: CertFileModel
        """
        return self._cacert

    @cacert.setter
    def cacert(self, cacert):
        """Sets the cacert of this RedshiftAccessInfo.

        Certificate to be used while connecting to redshift.  # noqa: E501

        :param cacert: The cacert of this RedshiftAccessInfo.  # noqa: E501
        :type: CertFileModel
        """

        self._cacert = cacert

    @property
    def insecure_ssl(self):
        """Gets the insecure_ssl of this RedshiftAccessInfo.  # noqa: E501


        :return: The insecure_ssl of this RedshiftAccessInfo.  # noqa: E501
        :rtype: bool
        """
        return self._insecure_ssl

    @insecure_ssl.setter
    def insecure_ssl(self, insecure_ssl):
        """Sets the insecure_ssl of this RedshiftAccessInfo.


        :param insecure_ssl: The insecure_ssl of this RedshiftAccessInfo.  # noqa: E501
        :type: bool
        """

        self._insecure_ssl = insecure_ssl

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
        if issubclass(RedshiftAccessInfo, dict):
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
        if not isinstance(other, RedshiftAccessInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
