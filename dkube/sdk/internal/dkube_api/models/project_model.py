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


class ProjectModel(object):
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
        'name': 'str',
        'description': 'str',
        'image': 'str',
        'leaderboard': 'bool',
        'id': 'str',
        'owner': 'str',
        'group': 'str',
        'last_updated': 'str',
        'details': 'str',
        'eval_repo': 'str',
        'eval_commit_id': 'str',
        'eval_image': 'str',
        'eval_script': 'str',
        'eval_details': 'str',
        'feast_enabled': 'bool',
        'offline_dataset': 'str',
        'submissions': 'list[SubmissionModel]',
        'status': 'ProjectStatusModel',
        'eval_dataset': 'ProjectEvalDatumModel'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'image': 'image',
        'leaderboard': 'leaderboard',
        'id': 'id',
        'owner': 'owner',
        'group': 'group',
        'last_updated': 'last_updated',
        'details': 'details',
        'eval_repo': 'eval_repo',
        'eval_commit_id': 'eval_commit_id',
        'eval_image': 'eval_image',
        'eval_script': 'eval_script',
        'eval_details': 'eval_details',
        'feast_enabled': 'feastEnabled',
        'offline_dataset': 'offline_dataset',
        'submissions': 'submissions',
        'status': 'status',
        'eval_dataset': 'eval_dataset'
    }

    def __init__(self, name=None, description=None, image=None, leaderboard=False, id=None, owner=None, group=None, last_updated=None, details=None, eval_repo=None, eval_commit_id=None, eval_image=None, eval_script=None, eval_details=None, feast_enabled=False, offline_dataset=None, submissions=None, status=None, eval_dataset=None):  # noqa: E501
        """ProjectModel - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._description = None
        self._image = None
        self._leaderboard = None
        self._id = None
        self._owner = None
        self._group = None
        self._last_updated = None
        self._details = None
        self._eval_repo = None
        self._eval_commit_id = None
        self._eval_image = None
        self._eval_script = None
        self._eval_details = None
        self._feast_enabled = None
        self._offline_dataset = None
        self._submissions = None
        self._status = None
        self._eval_dataset = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if image is not None:
            self.image = image
        if leaderboard is not None:
            self.leaderboard = leaderboard
        if id is not None:
            self.id = id
        if owner is not None:
            self.owner = owner
        if group is not None:
            self.group = group
        if last_updated is not None:
            self.last_updated = last_updated
        if details is not None:
            self.details = details
        if eval_repo is not None:
            self.eval_repo = eval_repo
        if eval_commit_id is not None:
            self.eval_commit_id = eval_commit_id
        if eval_image is not None:
            self.eval_image = eval_image
        if eval_script is not None:
            self.eval_script = eval_script
        if eval_details is not None:
            self.eval_details = eval_details
        if feast_enabled is not None:
            self.feast_enabled = feast_enabled
        if offline_dataset is not None:
            self.offline_dataset = offline_dataset
        if submissions is not None:
            self.submissions = submissions
        if status is not None:
            self.status = status
        if eval_dataset is not None:
            self.eval_dataset = eval_dataset

    @property
    def name(self):
        """Gets the name of this ProjectModel.  # noqa: E501


        :return: The name of this ProjectModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectModel.


        :param name: The name of this ProjectModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ProjectModel.  # noqa: E501


        :return: The description of this ProjectModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProjectModel.


        :param description: The description of this ProjectModel.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def image(self):
        """Gets the image of this ProjectModel.  # noqa: E501


        :return: The image of this ProjectModel.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this ProjectModel.


        :param image: The image of this ProjectModel.  # noqa: E501
        :type: str
        """
        if image is not None and len(image) > 2083:
            raise ValueError("Invalid value for `image`, length must be less than or equal to `2083`")  # noqa: E501
        if image is not None and len(image) < 1:
            raise ValueError("Invalid value for `image`, length must be greater than or equal to `1`")  # noqa: E501

        self._image = image

    @property
    def leaderboard(self):
        """Gets the leaderboard of this ProjectModel.  # noqa: E501


        :return: The leaderboard of this ProjectModel.  # noqa: E501
        :rtype: bool
        """
        return self._leaderboard

    @leaderboard.setter
    def leaderboard(self, leaderboard):
        """Sets the leaderboard of this ProjectModel.


        :param leaderboard: The leaderboard of this ProjectModel.  # noqa: E501
        :type: bool
        """

        self._leaderboard = leaderboard

    @property
    def id(self):
        """Gets the id of this ProjectModel.  # noqa: E501


        :return: The id of this ProjectModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectModel.


        :param id: The id of this ProjectModel.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def owner(self):
        """Gets the owner of this ProjectModel.  # noqa: E501


        :return: The owner of this ProjectModel.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ProjectModel.


        :param owner: The owner of this ProjectModel.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def group(self):
        """Gets the group of this ProjectModel.  # noqa: E501


        :return: The group of this ProjectModel.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this ProjectModel.


        :param group: The group of this ProjectModel.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def last_updated(self):
        """Gets the last_updated of this ProjectModel.  # noqa: E501


        :return: The last_updated of this ProjectModel.  # noqa: E501
        :rtype: str
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this ProjectModel.


        :param last_updated: The last_updated of this ProjectModel.  # noqa: E501
        :type: str
        """

        self._last_updated = last_updated

    @property
    def details(self):
        """Gets the details of this ProjectModel.  # noqa: E501


        :return: The details of this ProjectModel.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this ProjectModel.


        :param details: The details of this ProjectModel.  # noqa: E501
        :type: str
        """

        self._details = details

    @property
    def eval_repo(self):
        """Gets the eval_repo of this ProjectModel.  # noqa: E501


        :return: The eval_repo of this ProjectModel.  # noqa: E501
        :rtype: str
        """
        return self._eval_repo

    @eval_repo.setter
    def eval_repo(self, eval_repo):
        """Sets the eval_repo of this ProjectModel.


        :param eval_repo: The eval_repo of this ProjectModel.  # noqa: E501
        :type: str
        """

        self._eval_repo = eval_repo

    @property
    def eval_commit_id(self):
        """Gets the eval_commit_id of this ProjectModel.  # noqa: E501


        :return: The eval_commit_id of this ProjectModel.  # noqa: E501
        :rtype: str
        """
        return self._eval_commit_id

    @eval_commit_id.setter
    def eval_commit_id(self, eval_commit_id):
        """Sets the eval_commit_id of this ProjectModel.


        :param eval_commit_id: The eval_commit_id of this ProjectModel.  # noqa: E501
        :type: str
        """

        self._eval_commit_id = eval_commit_id

    @property
    def eval_image(self):
        """Gets the eval_image of this ProjectModel.  # noqa: E501


        :return: The eval_image of this ProjectModel.  # noqa: E501
        :rtype: str
        """
        return self._eval_image

    @eval_image.setter
    def eval_image(self, eval_image):
        """Sets the eval_image of this ProjectModel.


        :param eval_image: The eval_image of this ProjectModel.  # noqa: E501
        :type: str
        """

        self._eval_image = eval_image

    @property
    def eval_script(self):
        """Gets the eval_script of this ProjectModel.  # noqa: E501


        :return: The eval_script of this ProjectModel.  # noqa: E501
        :rtype: str
        """
        return self._eval_script

    @eval_script.setter
    def eval_script(self, eval_script):
        """Sets the eval_script of this ProjectModel.


        :param eval_script: The eval_script of this ProjectModel.  # noqa: E501
        :type: str
        """

        self._eval_script = eval_script

    @property
    def eval_details(self):
        """Gets the eval_details of this ProjectModel.  # noqa: E501


        :return: The eval_details of this ProjectModel.  # noqa: E501
        :rtype: str
        """
        return self._eval_details

    @eval_details.setter
    def eval_details(self, eval_details):
        """Sets the eval_details of this ProjectModel.


        :param eval_details: The eval_details of this ProjectModel.  # noqa: E501
        :type: str
        """

        self._eval_details = eval_details

    @property
    def feast_enabled(self):
        """Gets the feast_enabled of this ProjectModel.  # noqa: E501


        :return: The feast_enabled of this ProjectModel.  # noqa: E501
        :rtype: bool
        """
        return self._feast_enabled

    @feast_enabled.setter
    def feast_enabled(self, feast_enabled):
        """Sets the feast_enabled of this ProjectModel.


        :param feast_enabled: The feast_enabled of this ProjectModel.  # noqa: E501
        :type: bool
        """

        self._feast_enabled = feast_enabled

    @property
    def offline_dataset(self):
        """Gets the offline_dataset of this ProjectModel.  # noqa: E501


        :return: The offline_dataset of this ProjectModel.  # noqa: E501
        :rtype: str
        """
        return self._offline_dataset

    @offline_dataset.setter
    def offline_dataset(self, offline_dataset):
        """Sets the offline_dataset of this ProjectModel.


        :param offline_dataset: The offline_dataset of this ProjectModel.  # noqa: E501
        :type: str
        """

        self._offline_dataset = offline_dataset

    @property
    def submissions(self):
        """Gets the submissions of this ProjectModel.  # noqa: E501


        :return: The submissions of this ProjectModel.  # noqa: E501
        :rtype: list[SubmissionModel]
        """
        return self._submissions

    @submissions.setter
    def submissions(self, submissions):
        """Sets the submissions of this ProjectModel.


        :param submissions: The submissions of this ProjectModel.  # noqa: E501
        :type: list[SubmissionModel]
        """

        self._submissions = submissions

    @property
    def status(self):
        """Gets the status of this ProjectModel.  # noqa: E501


        :return: The status of this ProjectModel.  # noqa: E501
        :rtype: ProjectStatusModel
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ProjectModel.


        :param status: The status of this ProjectModel.  # noqa: E501
        :type: ProjectStatusModel
        """

        self._status = status

    @property
    def eval_dataset(self):
        """Gets the eval_dataset of this ProjectModel.  # noqa: E501


        :return: The eval_dataset of this ProjectModel.  # noqa: E501
        :rtype: ProjectEvalDatumModel
        """
        return self._eval_dataset

    @eval_dataset.setter
    def eval_dataset(self, eval_dataset):
        """Sets the eval_dataset of this ProjectModel.


        :param eval_dataset: The eval_dataset of this ProjectModel.  # noqa: E501
        :type: ProjectEvalDatumModel
        """

        self._eval_dataset = eval_dataset

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
        if issubclass(ProjectModel, dict):
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
        if not isinstance(other, ProjectModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
