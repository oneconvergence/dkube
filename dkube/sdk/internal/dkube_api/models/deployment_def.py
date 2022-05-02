# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.3.0.10
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DeploymentDef(object):
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
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'tags': 'list[str]',
        'owner': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'archived': 'bool',
        'inferenceservice_deployment': 'JobModel',
        'imported_deployment': 'ExternalDeploymentDef',
        'modelmonitor': 'ModelmonitorDef'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'tags': 'tags',
        'owner': 'owner',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'archived': 'archived',
        'inferenceservice_deployment': 'inferenceservice_deployment',
        'imported_deployment': 'imported_deployment',
        'modelmonitor': 'modelmonitor'
    }

    def __init__(self, id=None, name=None, description=None, tags=None, owner=None, created_at=None, updated_at=None, archived=None, inferenceservice_deployment=None, imported_deployment=None, modelmonitor=None):  # noqa: E501
        """DeploymentDef - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._description = None
        self._tags = None
        self._owner = None
        self._created_at = None
        self._updated_at = None
        self._archived = None
        self._inferenceservice_deployment = None
        self._imported_deployment = None
        self._modelmonitor = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if owner is not None:
            self.owner = owner
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if archived is not None:
            self.archived = archived
        if inferenceservice_deployment is not None:
            self.inferenceservice_deployment = inferenceservice_deployment
        if imported_deployment is not None:
            self.imported_deployment = imported_deployment
        if modelmonitor is not None:
            self.modelmonitor = modelmonitor

    @property
    def id(self):
        """Gets the id of this DeploymentDef.  # noqa: E501

        uuid4 for the resource  # noqa: E501

        :return: The id of this DeploymentDef.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeploymentDef.

        uuid4 for the resource  # noqa: E501

        :param id: The id of this DeploymentDef.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DeploymentDef.  # noqa: E501


        :return: The name of this DeploymentDef.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeploymentDef.


        :param name: The name of this DeploymentDef.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this DeploymentDef.  # noqa: E501


        :return: The description of this DeploymentDef.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeploymentDef.


        :param description: The description of this DeploymentDef.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this DeploymentDef.  # noqa: E501


        :return: The tags of this DeploymentDef.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DeploymentDef.


        :param tags: The tags of this DeploymentDef.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def owner(self):
        """Gets the owner of this DeploymentDef.  # noqa: E501


        :return: The owner of this DeploymentDef.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this DeploymentDef.


        :param owner: The owner of this DeploymentDef.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def created_at(self):
        """Gets the created_at of this DeploymentDef.  # noqa: E501


        :return: The created_at of this DeploymentDef.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DeploymentDef.


        :param created_at: The created_at of this DeploymentDef.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this DeploymentDef.  # noqa: E501


        :return: The updated_at of this DeploymentDef.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this DeploymentDef.


        :param updated_at: The updated_at of this DeploymentDef.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def archived(self):
        """Gets the archived of this DeploymentDef.  # noqa: E501


        :return: The archived of this DeploymentDef.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this DeploymentDef.


        :param archived: The archived of this DeploymentDef.  # noqa: E501
        :type: bool
        """

        self._archived = archived

    @property
    def inferenceservice_deployment(self):
        """Gets the inferenceservice_deployment of this DeploymentDef.  # noqa: E501


        :return: The inferenceservice_deployment of this DeploymentDef.  # noqa: E501
        :rtype: JobModel
        """
        return self._inferenceservice_deployment

    @inferenceservice_deployment.setter
    def inferenceservice_deployment(self, inferenceservice_deployment):
        """Sets the inferenceservice_deployment of this DeploymentDef.


        :param inferenceservice_deployment: The inferenceservice_deployment of this DeploymentDef.  # noqa: E501
        :type: JobModel
        """

        self._inferenceservice_deployment = inferenceservice_deployment

    @property
    def imported_deployment(self):
        """Gets the imported_deployment of this DeploymentDef.  # noqa: E501


        :return: The imported_deployment of this DeploymentDef.  # noqa: E501
        :rtype: ExternalDeploymentDef
        """
        return self._imported_deployment

    @imported_deployment.setter
    def imported_deployment(self, imported_deployment):
        """Sets the imported_deployment of this DeploymentDef.


        :param imported_deployment: The imported_deployment of this DeploymentDef.  # noqa: E501
        :type: ExternalDeploymentDef
        """

        self._imported_deployment = imported_deployment

    @property
    def modelmonitor(self):
        """Gets the modelmonitor of this DeploymentDef.  # noqa: E501


        :return: The modelmonitor of this DeploymentDef.  # noqa: E501
        :rtype: ModelmonitorDef
        """
        return self._modelmonitor

    @modelmonitor.setter
    def modelmonitor(self, modelmonitor):
        """Sets the modelmonitor of this DeploymentDef.


        :param modelmonitor: The modelmonitor of this DeploymentDef.  # noqa: E501
        :type: ModelmonitorDef
        """

        self._modelmonitor = modelmonitor

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
        if issubclass(DeploymentDef, dict):
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
        if not isinstance(other, DeploymentDef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
