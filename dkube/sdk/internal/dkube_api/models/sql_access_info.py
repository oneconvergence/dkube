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


class SQLAccessInfo(object):
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
        'host': 'str',
        'port': 'int',
        'username': 'str',
        'password': 'str',
        'database': 'str',
        'odbc_connection_string': 'str',
        'jdbc_connection_string': 'str',
        'cacert': 'CertFileModel',
        'provider': 'str'
    }

    attribute_map = {
        'host': 'host',
        'port': 'port',
        'username': 'username',
        'password': 'password',
        'database': 'database',
        'odbc_connection_string': 'ODBCConnectionString',
        'jdbc_connection_string': 'JDBCConnectionString',
        'cacert': 'cacert',
        'provider': 'provider'
    }

    def __init__(self, host=None, port=None, username=None, password=None, database=None, odbc_connection_string=None, jdbc_connection_string=None, cacert=None, provider=None):  # noqa: E501
        """SQLAccessInfo - a model defined in Swagger"""  # noqa: E501

        self._host = None
        self._port = None
        self._username = None
        self._password = None
        self._database = None
        self._odbc_connection_string = None
        self._jdbc_connection_string = None
        self._cacert = None
        self._provider = None
        self.discriminator = None

        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if database is not None:
            self.database = database
        if odbc_connection_string is not None:
            self.odbc_connection_string = odbc_connection_string
        if jdbc_connection_string is not None:
            self.jdbc_connection_string = jdbc_connection_string
        if cacert is not None:
            self.cacert = cacert
        if provider is not None:
            self.provider = provider

    @property
    def host(self):
        """Gets the host of this SQLAccessInfo.  # noqa: E501


        :return: The host of this SQLAccessInfo.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this SQLAccessInfo.


        :param host: The host of this SQLAccessInfo.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def port(self):
        """Gets the port of this SQLAccessInfo.  # noqa: E501


        :return: The port of this SQLAccessInfo.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this SQLAccessInfo.


        :param port: The port of this SQLAccessInfo.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def username(self):
        """Gets the username of this SQLAccessInfo.  # noqa: E501

        User authorized to connect to the database.  # noqa: E501

        :return: The username of this SQLAccessInfo.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this SQLAccessInfo.

        User authorized to connect to the database.  # noqa: E501

        :param username: The username of this SQLAccessInfo.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this SQLAccessInfo.  # noqa: E501

        Password to be used to connect to the database.  # noqa: E501

        :return: The password of this SQLAccessInfo.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this SQLAccessInfo.

        Password to be used to connect to the database.  # noqa: E501

        :param password: The password of this SQLAccessInfo.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def database(self):
        """Gets the database of this SQLAccessInfo.  # noqa: E501

        Database that this dataset should point to.  # noqa: E501

        :return: The database of this SQLAccessInfo.  # noqa: E501
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this SQLAccessInfo.

        Database that this dataset should point to.  # noqa: E501

        :param database: The database of this SQLAccessInfo.  # noqa: E501
        :type: str
        """

        self._database = database

    @property
    def odbc_connection_string(self):
        """Gets the odbc_connection_string of this SQLAccessInfo.  # noqa: E501


        :return: The odbc_connection_string of this SQLAccessInfo.  # noqa: E501
        :rtype: str
        """
        return self._odbc_connection_string

    @odbc_connection_string.setter
    def odbc_connection_string(self, odbc_connection_string):
        """Sets the odbc_connection_string of this SQLAccessInfo.


        :param odbc_connection_string: The odbc_connection_string of this SQLAccessInfo.  # noqa: E501
        :type: str
        """

        self._odbc_connection_string = odbc_connection_string

    @property
    def jdbc_connection_string(self):
        """Gets the jdbc_connection_string of this SQLAccessInfo.  # noqa: E501


        :return: The jdbc_connection_string of this SQLAccessInfo.  # noqa: E501
        :rtype: str
        """
        return self._jdbc_connection_string

    @jdbc_connection_string.setter
    def jdbc_connection_string(self, jdbc_connection_string):
        """Sets the jdbc_connection_string of this SQLAccessInfo.


        :param jdbc_connection_string: The jdbc_connection_string of this SQLAccessInfo.  # noqa: E501
        :type: str
        """

        self._jdbc_connection_string = jdbc_connection_string

    @property
    def cacert(self):
        """Gets the cacert of this SQLAccessInfo.  # noqa: E501

        Optional certificate to be used while connecting to the DB.  # noqa: E501

        :return: The cacert of this SQLAccessInfo.  # noqa: E501
        :rtype: CertFileModel
        """
        return self._cacert

    @cacert.setter
    def cacert(self, cacert):
        """Sets the cacert of this SQLAccessInfo.

        Optional certificate to be used while connecting to the DB.  # noqa: E501

        :param cacert: The cacert of this SQLAccessInfo.  # noqa: E501
        :type: CertFileModel
        """

        self._cacert = cacert

    @property
    def provider(self):
        """Gets the provider of this SQLAccessInfo.  # noqa: E501

        DB provider (MYSQL/MSSQL/ORACLE)  # noqa: E501

        :return: The provider of this SQLAccessInfo.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this SQLAccessInfo.

        DB provider (MYSQL/MSSQL/ORACLE)  # noqa: E501

        :param provider: The provider of this SQLAccessInfo.  # noqa: E501
        :type: str
        """

        self._provider = provider

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
        if issubclass(SQLAccessInfo, dict):
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
        if not isinstance(other, SQLAccessInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
