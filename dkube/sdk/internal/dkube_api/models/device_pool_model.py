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


class DevicePoolModel(object):
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
        'name': 'str',
        '_class': 'str',
        'instance_type': 'str',
        'ndevices': 'int',
        'created_at': 'TimeStamps',
        'generated': 'ModelCatalogItemGenerated'
    }

    attribute_map = {
        'version': 'version',
        'name': 'name',
        '_class': 'class',
        'instance_type': 'instance_type',
        'ndevices': 'ndevices',
        'created_at': 'created_at',
        'generated': 'generated'
    }

    def __init__(self, version=None, name=None, _class=None, instance_type='gpu', ndevices=None, created_at=None, generated=None):  # noqa: E501
        """DevicePoolModel - a model defined in Swagger"""  # noqa: E501

        self._version = None
        self._name = None
        self.__class = None
        self._instance_type = None
        self._ndevices = None
        self._created_at = None
        self._generated = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if name is not None:
            self.name = name
        if _class is not None:
            self._class = _class
        if instance_type is not None:
            self.instance_type = instance_type
        if ndevices is not None:
            self.ndevices = ndevices
        if created_at is not None:
            self.created_at = created_at
        if generated is not None:
            self.generated = generated

    @property
    def version(self):
        """Gets the version of this DevicePoolModel.  # noqa: E501


        :return: The version of this DevicePoolModel.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DevicePoolModel.


        :param version: The version of this DevicePoolModel.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def name(self):
        """Gets the name of this DevicePoolModel.  # noqa: E501


        :return: The name of this DevicePoolModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DevicePoolModel.


        :param name: The name of this DevicePoolModel.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def _class(self):
        """Gets the _class of this DevicePoolModel.  # noqa: E501

        Model of devices - homogenous pool  # noqa: E501

        :return: The _class of this DevicePoolModel.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this DevicePoolModel.

        Model of devices - homogenous pool  # noqa: E501

        :param _class: The _class of this DevicePoolModel.  # noqa: E501
        :type: str
        """

        self.__class = _class

    @property
    def instance_type(self):
        """Gets the instance_type of this DevicePoolModel.  # noqa: E501

        instance type of the  devices in the pool  # noqa: E501

        :return: The instance_type of this DevicePoolModel.  # noqa: E501
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this DevicePoolModel.

        instance type of the  devices in the pool  # noqa: E501

        :param instance_type: The instance_type of this DevicePoolModel.  # noqa: E501
        :type: str
        """

        self._instance_type = instance_type

    @property
    def ndevices(self):
        """Gets the ndevices of this DevicePoolModel.  # noqa: E501

        Number of devices in the pool  # noqa: E501

        :return: The ndevices of this DevicePoolModel.  # noqa: E501
        :rtype: int
        """
        return self._ndevices

    @ndevices.setter
    def ndevices(self, ndevices):
        """Sets the ndevices of this DevicePoolModel.

        Number of devices in the pool  # noqa: E501

        :param ndevices: The ndevices of this DevicePoolModel.  # noqa: E501
        :type: int
        """

        self._ndevices = ndevices

    @property
    def created_at(self):
        """Gets the created_at of this DevicePoolModel.  # noqa: E501


        :return: The created_at of this DevicePoolModel.  # noqa: E501
        :rtype: TimeStamps
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DevicePoolModel.


        :param created_at: The created_at of this DevicePoolModel.  # noqa: E501
        :type: TimeStamps
        """

        self._created_at = created_at

    @property
    def generated(self):
        """Gets the generated of this DevicePoolModel.  # noqa: E501


        :return: The generated of this DevicePoolModel.  # noqa: E501
        :rtype: ModelCatalogItemGenerated
        """
        return self._generated

    @generated.setter
    def generated(self, generated):
        """Sets the generated of this DevicePoolModel.


        :param generated: The generated of this DevicePoolModel.  # noqa: E501
        :type: ModelCatalogItemGenerated
        """

        self._generated = generated

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
        if issubclass(DevicePoolModel, dict):
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
        if not isinstance(other, DevicePoolModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
