# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.5.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class WorkerModel(object):
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
        'role': 'str',
        'uuid': 'str',
        'containers': 'list[WorkerModelContainers]',
        'status': 'str',
        'reason': 'str',
        'event': 'str',
        'poduuid': 'str',
        'exit_code': 'int',
        'node': 'str'
    }

    attribute_map = {
        'version': 'version',
        'name': 'name',
        'role': 'role',
        'uuid': 'uuid',
        'containers': 'containers',
        'status': 'status',
        'reason': 'reason',
        'event': 'event',
        'poduuid': 'poduuid',
        'exit_code': 'exit_code',
        'node': 'node'
    }

    def __init__(self, version=None, name=None, role='SINGLETON', uuid=None, containers=None, status=None, reason=None, event=None, poduuid=None, exit_code=None, node=None):  # noqa: E501
        """WorkerModel - a model defined in Swagger"""  # noqa: E501

        self._version = None
        self._name = None
        self._role = None
        self._uuid = None
        self._containers = None
        self._status = None
        self._reason = None
        self._event = None
        self._poduuid = None
        self._exit_code = None
        self._node = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if name is not None:
            self.name = name
        if role is not None:
            self.role = role
        if uuid is not None:
            self.uuid = uuid
        if containers is not None:
            self.containers = containers
        if status is not None:
            self.status = status
        if reason is not None:
            self.reason = reason
        if event is not None:
            self.event = event
        if poduuid is not None:
            self.poduuid = poduuid
        if exit_code is not None:
            self.exit_code = exit_code
        if node is not None:
            self.node = node

    @property
    def version(self):
        """Gets the version of this WorkerModel.  # noqa: E501


        :return: The version of this WorkerModel.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this WorkerModel.


        :param version: The version of this WorkerModel.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def name(self):
        """Gets the name of this WorkerModel.  # noqa: E501


        :return: The name of this WorkerModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkerModel.


        :param name: The name of this WorkerModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def role(self):
        """Gets the role of this WorkerModel.  # noqa: E501


        :return: The role of this WorkerModel.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this WorkerModel.


        :param role: The role of this WorkerModel.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def uuid(self):
        """Gets the uuid of this WorkerModel.  # noqa: E501


        :return: The uuid of this WorkerModel.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this WorkerModel.


        :param uuid: The uuid of this WorkerModel.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def containers(self):
        """Gets the containers of this WorkerModel.  # noqa: E501


        :return: The containers of this WorkerModel.  # noqa: E501
        :rtype: list[WorkerModelContainers]
        """
        return self._containers

    @containers.setter
    def containers(self, containers):
        """Sets the containers of this WorkerModel.


        :param containers: The containers of this WorkerModel.  # noqa: E501
        :type: list[WorkerModelContainers]
        """

        self._containers = containers

    @property
    def status(self):
        """Gets the status of this WorkerModel.  # noqa: E501


        :return: The status of this WorkerModel.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WorkerModel.


        :param status: The status of this WorkerModel.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def reason(self):
        """Gets the reason of this WorkerModel.  # noqa: E501


        :return: The reason of this WorkerModel.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this WorkerModel.


        :param reason: The reason of this WorkerModel.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def event(self):
        """Gets the event of this WorkerModel.  # noqa: E501


        :return: The event of this WorkerModel.  # noqa: E501
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this WorkerModel.


        :param event: The event of this WorkerModel.  # noqa: E501
        :type: str
        """

        self._event = event

    @property
    def poduuid(self):
        """Gets the poduuid of this WorkerModel.  # noqa: E501


        :return: The poduuid of this WorkerModel.  # noqa: E501
        :rtype: str
        """
        return self._poduuid

    @poduuid.setter
    def poduuid(self, poduuid):
        """Sets the poduuid of this WorkerModel.


        :param poduuid: The poduuid of this WorkerModel.  # noqa: E501
        :type: str
        """

        self._poduuid = poduuid

    @property
    def exit_code(self):
        """Gets the exit_code of this WorkerModel.  # noqa: E501


        :return: The exit_code of this WorkerModel.  # noqa: E501
        :rtype: int
        """
        return self._exit_code

    @exit_code.setter
    def exit_code(self, exit_code):
        """Sets the exit_code of this WorkerModel.


        :param exit_code: The exit_code of this WorkerModel.  # noqa: E501
        :type: int
        """

        self._exit_code = exit_code

    @property
    def node(self):
        """Gets the node of this WorkerModel.  # noqa: E501


        :return: The node of this WorkerModel.  # noqa: E501
        :rtype: str
        """
        return self._node

    @node.setter
    def node(self, node):
        """Sets the node of this WorkerModel.


        :param node: The node of this WorkerModel.  # noqa: E501
        :type: str
        """

        self._node = node

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
        if issubclass(WorkerModel, dict):
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
        if not isinstance(other, WorkerModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
