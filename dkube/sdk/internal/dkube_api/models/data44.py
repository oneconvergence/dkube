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


class Data44(object):
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
        'version': 'str',
        'emails': 'str',
        'tags': 'list[str]',
        'endpoint_url': 'str',
        'description': 'str',
        'schema': 'ModelmonitorFeaturesSpecDef'
    }

    attribute_map = {
        'version': 'version',
        'emails': 'emails',
        'tags': 'tags',
        'endpoint_url': 'endpoint_url',
        'description': 'description',
        'schema': 'schema'
    }

    def __init__(self, version=None, emails=None, tags=None, endpoint_url=None, description=None, schema=None):  # noqa: E501
        """Data44 - a model defined in Swagger"""  # noqa: E501

        self._version = None
        self._emails = None
        self._tags = None
        self._endpoint_url = None
        self._description = None
        self._schema = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if emails is not None:
            self.emails = emails
        if tags is not None:
            self.tags = tags
        if endpoint_url is not None:
            self.endpoint_url = endpoint_url
        if description is not None:
            self.description = description
        if schema is not None:
            self.schema = schema

    @property
    def version(self):
        """Gets the version of this Data44.  # noqa: E501

        Model Version  # noqa: E501

        :return: The version of this Data44.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Data44.

        Model Version  # noqa: E501

        :param version: The version of this Data44.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def emails(self):
        """Gets the emails of this Data44.  # noqa: E501

        Comma separated emails  # noqa: E501

        :return: The emails of this Data44.  # noqa: E501
        :rtype: str
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this Data44.

        Comma separated emails  # noqa: E501

        :param emails: The emails of this Data44.  # noqa: E501
        :type: str
        """

        self._emails = emails

    @property
    def tags(self):
        """Gets the tags of this Data44.  # noqa: E501


        :return: The tags of this Data44.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Data44.


        :param tags: The tags of this Data44.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def endpoint_url(self):
        """Gets the endpoint_url of this Data44.  # noqa: E501

        Model Deploymeny URL  # noqa: E501

        :return: The endpoint_url of this Data44.  # noqa: E501
        :rtype: str
        """
        return self._endpoint_url

    @endpoint_url.setter
    def endpoint_url(self, endpoint_url):
        """Sets the endpoint_url of this Data44.

        Model Deploymeny URL  # noqa: E501

        :param endpoint_url: The endpoint_url of this Data44.  # noqa: E501
        :type: str
        """
        if endpoint_url is not None and len(endpoint_url) > 255:
            raise ValueError("Invalid value for `endpoint_url`, length must be less than or equal to `255`")  # noqa: E501
        if endpoint_url is not None and len(endpoint_url) < 1:
            raise ValueError("Invalid value for `endpoint_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._endpoint_url = endpoint_url

    @property
    def description(self):
        """Gets the description of this Data44.  # noqa: E501


        :return: The description of this Data44.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Data44.


        :param description: The description of this Data44.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 255:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501
        if description is not None and len(description) < 1:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def schema(self):
        """Gets the schema of this Data44.  # noqa: E501


        :return: The schema of this Data44.  # noqa: E501
        :rtype: ModelmonitorFeaturesSpecDef
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this Data44.


        :param schema: The schema of this Data44.  # noqa: E501
        :type: ModelmonitorFeaturesSpecDef
        """

        self._schema = schema

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
        if issubclass(Data44, dict):
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
        if not isinstance(other, Data44):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
