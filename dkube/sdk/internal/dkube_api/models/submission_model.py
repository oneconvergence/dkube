# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.2.1.13
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SubmissionModel(object):
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
        'project_id': 'str',
        'group_name': 'str',
        'user': 'str',
        'eval_run': 'str',
        'eval_run_name': 'str',
        'experiment_name': 'str',
        'pipeline_name': 'str',
        'metrics': 'object',
        'artifacts_url': 'str',
        'timestamp': 'str'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'group_name': 'group_name',
        'user': 'user',
        'eval_run': 'eval_run',
        'eval_run_name': 'eval_run_name',
        'experiment_name': 'experiment_name',
        'pipeline_name': 'pipeline_name',
        'metrics': 'metrics',
        'artifacts_url': 'artifacts_url',
        'timestamp': 'timestamp'
    }

    def __init__(self, id=None, project_id=None, group_name=None, user=None, eval_run=None, eval_run_name=None, experiment_name=None, pipeline_name=None, metrics=None, artifacts_url=None, timestamp=None):  # noqa: E501
        """SubmissionModel - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._project_id = None
        self._group_name = None
        self._user = None
        self._eval_run = None
        self._eval_run_name = None
        self._experiment_name = None
        self._pipeline_name = None
        self._metrics = None
        self._artifacts_url = None
        self._timestamp = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if group_name is not None:
            self.group_name = group_name
        if user is not None:
            self.user = user
        if eval_run is not None:
            self.eval_run = eval_run
        if eval_run_name is not None:
            self.eval_run_name = eval_run_name
        if experiment_name is not None:
            self.experiment_name = experiment_name
        if pipeline_name is not None:
            self.pipeline_name = pipeline_name
        if metrics is not None:
            self.metrics = metrics
        if artifacts_url is not None:
            self.artifacts_url = artifacts_url
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def id(self):
        """Gets the id of this SubmissionModel.  # noqa: E501


        :return: The id of this SubmissionModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubmissionModel.


        :param id: The id of this SubmissionModel.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this SubmissionModel.  # noqa: E501


        :return: The project_id of this SubmissionModel.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this SubmissionModel.


        :param project_id: The project_id of this SubmissionModel.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def group_name(self):
        """Gets the group_name of this SubmissionModel.  # noqa: E501


        :return: The group_name of this SubmissionModel.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this SubmissionModel.


        :param group_name: The group_name of this SubmissionModel.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

    @property
    def user(self):
        """Gets the user of this SubmissionModel.  # noqa: E501


        :return: The user of this SubmissionModel.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this SubmissionModel.


        :param user: The user of this SubmissionModel.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def eval_run(self):
        """Gets the eval_run of this SubmissionModel.  # noqa: E501


        :return: The eval_run of this SubmissionModel.  # noqa: E501
        :rtype: str
        """
        return self._eval_run

    @eval_run.setter
    def eval_run(self, eval_run):
        """Sets the eval_run of this SubmissionModel.


        :param eval_run: The eval_run of this SubmissionModel.  # noqa: E501
        :type: str
        """

        self._eval_run = eval_run

    @property
    def eval_run_name(self):
        """Gets the eval_run_name of this SubmissionModel.  # noqa: E501


        :return: The eval_run_name of this SubmissionModel.  # noqa: E501
        :rtype: str
        """
        return self._eval_run_name

    @eval_run_name.setter
    def eval_run_name(self, eval_run_name):
        """Sets the eval_run_name of this SubmissionModel.


        :param eval_run_name: The eval_run_name of this SubmissionModel.  # noqa: E501
        :type: str
        """

        self._eval_run_name = eval_run_name

    @property
    def experiment_name(self):
        """Gets the experiment_name of this SubmissionModel.  # noqa: E501


        :return: The experiment_name of this SubmissionModel.  # noqa: E501
        :rtype: str
        """
        return self._experiment_name

    @experiment_name.setter
    def experiment_name(self, experiment_name):
        """Sets the experiment_name of this SubmissionModel.


        :param experiment_name: The experiment_name of this SubmissionModel.  # noqa: E501
        :type: str
        """

        self._experiment_name = experiment_name

    @property
    def pipeline_name(self):
        """Gets the pipeline_name of this SubmissionModel.  # noqa: E501


        :return: The pipeline_name of this SubmissionModel.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_name

    @pipeline_name.setter
    def pipeline_name(self, pipeline_name):
        """Sets the pipeline_name of this SubmissionModel.


        :param pipeline_name: The pipeline_name of this SubmissionModel.  # noqa: E501
        :type: str
        """

        self._pipeline_name = pipeline_name

    @property
    def metrics(self):
        """Gets the metrics of this SubmissionModel.  # noqa: E501


        :return: The metrics of this SubmissionModel.  # noqa: E501
        :rtype: object
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this SubmissionModel.


        :param metrics: The metrics of this SubmissionModel.  # noqa: E501
        :type: object
        """

        self._metrics = metrics

    @property
    def artifacts_url(self):
        """Gets the artifacts_url of this SubmissionModel.  # noqa: E501


        :return: The artifacts_url of this SubmissionModel.  # noqa: E501
        :rtype: str
        """
        return self._artifacts_url

    @artifacts_url.setter
    def artifacts_url(self, artifacts_url):
        """Sets the artifacts_url of this SubmissionModel.


        :param artifacts_url: The artifacts_url of this SubmissionModel.  # noqa: E501
        :type: str
        """

        self._artifacts_url = artifacts_url

    @property
    def timestamp(self):
        """Gets the timestamp of this SubmissionModel.  # noqa: E501


        :return: The timestamp of this SubmissionModel.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this SubmissionModel.


        :param timestamp: The timestamp of this SubmissionModel.  # noqa: E501
        :type: str
        """

        self._timestamp = timestamp

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
        if issubclass(SubmissionModel, dict):
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
        if not isinstance(other, SubmissionModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
