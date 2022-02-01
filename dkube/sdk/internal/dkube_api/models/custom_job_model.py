# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.1.0.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CustomJobModel(object):
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
        'datums': 'JobDatumModel',
        'tags': 'list[str]',
        'config': 'JobConfigModel',
        'service': 'CustomJobModelService',
        'container': 'CustomContainerModel'
    }

    attribute_map = {
        'datums': 'datums',
        'tags': 'tags',
        'config': 'config',
        'service': 'service',
        'container': 'container'
    }

    def __init__(self, datums=None, tags=None, config=None, service=None, container=None):  # noqa: E501
        """CustomJobModel - a model defined in Swagger"""  # noqa: E501

        self._datums = None
        self._tags = None
        self._config = None
        self._service = None
        self._container = None
        self.discriminator = None

        if datums is not None:
            self.datums = datums
        if tags is not None:
            self.tags = tags
        if config is not None:
            self.config = config
        if service is not None:
            self.service = service
        if container is not None:
            self.container = container

    @property
    def datums(self):
        """Gets the datums of this CustomJobModel.  # noqa: E501


        :return: The datums of this CustomJobModel.  # noqa: E501
        :rtype: JobDatumModel
        """
        return self._datums

    @datums.setter
    def datums(self, datums):
        """Sets the datums of this CustomJobModel.


        :param datums: The datums of this CustomJobModel.  # noqa: E501
        :type: JobDatumModel
        """

        self._datums = datums

    @property
    def tags(self):
        """Gets the tags of this CustomJobModel.  # noqa: E501

        Custom tags set by user for the job.  # noqa: E501

        :return: The tags of this CustomJobModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CustomJobModel.

        Custom tags set by user for the job.  # noqa: E501

        :param tags: The tags of this CustomJobModel.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def config(self):
        """Gets the config of this CustomJobModel.  # noqa: E501


        :return: The config of this CustomJobModel.  # noqa: E501
        :rtype: JobConfigModel
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this CustomJobModel.


        :param config: The config of this CustomJobModel.  # noqa: E501
        :type: JobConfigModel
        """

        self._config = config

    @property
    def service(self):
        """Gets the service of this CustomJobModel.  # noqa: E501


        :return: The service of this CustomJobModel.  # noqa: E501
        :rtype: CustomJobModelService
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this CustomJobModel.


        :param service: The service of this CustomJobModel.  # noqa: E501
        :type: CustomJobModelService
        """

        self._service = service

    @property
    def container(self):
        """Gets the container of this CustomJobModel.  # noqa: E501


        :return: The container of this CustomJobModel.  # noqa: E501
        :rtype: CustomContainerModel
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this CustomJobModel.


        :param container: The container of this CustomJobModel.  # noqa: E501
        :type: CustomContainerModel
        """

        self._container = container

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
        if issubclass(CustomJobModel, dict):
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
        if not isinstance(other, CustomJobModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
