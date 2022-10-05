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


class DeviceModel(object):
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
        'vendor': 'str',
        'model': 'str',
        'instance_type': 'str',
        'instance_profile': 'str',
        'uuid': 'str',
        'healthy': 'bool',
        'node': 'str',
        'created_at': 'TimeStamps'
    }

    attribute_map = {
        'version': 'version',
        'name': 'name',
        '_class': 'class',
        'vendor': 'vendor',
        'model': 'model',
        'instance_type': 'instance_type',
        'instance_profile': 'instance_profile',
        'uuid': 'UUID',
        'healthy': 'healthy',
        'node': 'node',
        'created_at': 'created_at'
    }

    def __init__(self, version=None, name=None, _class='gpu', vendor='nvidia', model=None, instance_type='gpu', instance_profile='gpu', uuid=None, healthy=True, node=None, created_at=None):  # noqa: E501
        """DeviceModel - a model defined in Swagger"""  # noqa: E501

        self._version = None
        self._name = None
        self.__class = None
        self._vendor = None
        self._model = None
        self._instance_type = None
        self._instance_profile = None
        self._uuid = None
        self._healthy = None
        self._node = None
        self._created_at = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if name is not None:
            self.name = name
        if _class is not None:
            self._class = _class
        if vendor is not None:
            self.vendor = vendor
        if model is not None:
            self.model = model
        if instance_type is not None:
            self.instance_type = instance_type
        if instance_profile is not None:
            self.instance_profile = instance_profile
        if uuid is not None:
            self.uuid = uuid
        if healthy is not None:
            self.healthy = healthy
        if node is not None:
            self.node = node
        if created_at is not None:
            self.created_at = created_at

    @property
    def version(self):
        """Gets the version of this DeviceModel.  # noqa: E501


        :return: The version of this DeviceModel.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DeviceModel.


        :param version: The version of this DeviceModel.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def name(self):
        """Gets the name of this DeviceModel.  # noqa: E501


        :return: The name of this DeviceModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceModel.


        :param name: The name of this DeviceModel.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def _class(self):
        """Gets the _class of this DeviceModel.  # noqa: E501


        :return: The _class of this DeviceModel.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this DeviceModel.


        :param _class: The _class of this DeviceModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["gpu"]  # noqa: E501
        if _class not in allowed_values:
            raise ValueError(
                "Invalid value for `_class` ({0}), must be one of {1}"  # noqa: E501
                .format(_class, allowed_values)
            )

        self.__class = _class

    @property
    def vendor(self):
        """Gets the vendor of this DeviceModel.  # noqa: E501


        :return: The vendor of this DeviceModel.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this DeviceModel.


        :param vendor: The vendor of this DeviceModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["nvidia"]  # noqa: E501
        if vendor not in allowed_values:
            raise ValueError(
                "Invalid value for `vendor` ({0}), must be one of {1}"  # noqa: E501
                .format(vendor, allowed_values)
            )

        self._vendor = vendor

    @property
    def model(self):
        """Gets the model of this DeviceModel.  # noqa: E501


        :return: The model of this DeviceModel.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this DeviceModel.


        :param model: The model of this DeviceModel.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def instance_type(self):
        """Gets the instance_type of this DeviceModel.  # noqa: E501


        :return: The instance_type of this DeviceModel.  # noqa: E501
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this DeviceModel.


        :param instance_type: The instance_type of this DeviceModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["gpu", "mig"]  # noqa: E501
        if instance_type not in allowed_values:
            raise ValueError(
                "Invalid value for `instance_type` ({0}), must be one of {1}"  # noqa: E501
                .format(instance_type, allowed_values)
            )

        self._instance_type = instance_type

    @property
    def instance_profile(self):
        """Gets the instance_profile of this DeviceModel.  # noqa: E501


        :return: The instance_profile of this DeviceModel.  # noqa: E501
        :rtype: str
        """
        return self._instance_profile

    @instance_profile.setter
    def instance_profile(self, instance_profile):
        """Sets the instance_profile of this DeviceModel.


        :param instance_profile: The instance_profile of this DeviceModel.  # noqa: E501
        :type: str
        """

        self._instance_profile = instance_profile

    @property
    def uuid(self):
        """Gets the uuid of this DeviceModel.  # noqa: E501


        :return: The uuid of this DeviceModel.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this DeviceModel.


        :param uuid: The uuid of this DeviceModel.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def healthy(self):
        """Gets the healthy of this DeviceModel.  # noqa: E501


        :return: The healthy of this DeviceModel.  # noqa: E501
        :rtype: bool
        """
        return self._healthy

    @healthy.setter
    def healthy(self, healthy):
        """Sets the healthy of this DeviceModel.


        :param healthy: The healthy of this DeviceModel.  # noqa: E501
        :type: bool
        """

        self._healthy = healthy

    @property
    def node(self):
        """Gets the node of this DeviceModel.  # noqa: E501


        :return: The node of this DeviceModel.  # noqa: E501
        :rtype: str
        """
        return self._node

    @node.setter
    def node(self, node):
        """Sets the node of this DeviceModel.


        :param node: The node of this DeviceModel.  # noqa: E501
        :type: str
        """

        self._node = node

    @property
    def created_at(self):
        """Gets the created_at of this DeviceModel.  # noqa: E501


        :return: The created_at of this DeviceModel.  # noqa: E501
        :rtype: TimeStamps
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DeviceModel.


        :param created_at: The created_at of this DeviceModel.  # noqa: E501
        :type: TimeStamps
        """

        self._created_at = created_at

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
        if issubclass(DeviceModel, dict):
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
        if not isinstance(other, DeviceModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
