# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.3.0.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DatumJobDetails(object):
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
        'user': 'str',
        'jobid': 'str',
        '_class': 'str',
        'state': 'str',
        'tags': 'list[str]',
        'pipeline': 'DatumJobDetailsPipeline'
    }

    attribute_map = {
        'name': 'name',
        'user': 'user',
        'jobid': 'jobid',
        '_class': 'class',
        'state': 'state',
        'tags': 'tags',
        'pipeline': 'pipeline'
    }

    def __init__(self, name=None, user=None, jobid=None, _class=None, state=None, tags=None, pipeline=None):  # noqa: E501
        """DatumJobDetails - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._user = None
        self._jobid = None
        self.__class = None
        self._state = None
        self._tags = None
        self._pipeline = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if user is not None:
            self.user = user
        if jobid is not None:
            self.jobid = jobid
        if _class is not None:
            self._class = _class
        if state is not None:
            self.state = state
        if tags is not None:
            self.tags = tags
        if pipeline is not None:
            self.pipeline = pipeline

    @property
    def name(self):
        """Gets the name of this DatumJobDetails.  # noqa: E501

        Name of the job that uses the datum.  # noqa: E501

        :return: The name of this DatumJobDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DatumJobDetails.

        Name of the job that uses the datum.  # noqa: E501

        :param name: The name of this DatumJobDetails.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def user(self):
        """Gets the user of this DatumJobDetails.  # noqa: E501

        User to which this job belongs.  # noqa: E501

        :return: The user of this DatumJobDetails.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this DatumJobDetails.

        User to which this job belongs.  # noqa: E501

        :param user: The user of this DatumJobDetails.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def jobid(self):
        """Gets the jobid of this DatumJobDetails.  # noqa: E501

        Jobid of job that uses the datum.  # noqa: E501

        :return: The jobid of this DatumJobDetails.  # noqa: E501
        :rtype: str
        """
        return self._jobid

    @jobid.setter
    def jobid(self, jobid):
        """Sets the jobid of this DatumJobDetails.

        Jobid of job that uses the datum.  # noqa: E501

        :param jobid: The jobid of this DatumJobDetails.  # noqa: E501
        :type: str
        """

        self._jobid = jobid

    @property
    def _class(self):
        """Gets the _class of this DatumJobDetails.  # noqa: E501

        Class of job that uses the datum.  # noqa: E501

        :return: The _class of this DatumJobDetails.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this DatumJobDetails.

        Class of job that uses the datum.  # noqa: E501

        :param _class: The _class of this DatumJobDetails.  # noqa: E501
        :type: str
        """

        self.__class = _class

    @property
    def state(self):
        """Gets the state of this DatumJobDetails.  # noqa: E501

        State of the job  # noqa: E501

        :return: The state of this DatumJobDetails.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DatumJobDetails.

        State of the job  # noqa: E501

        :param state: The state of this DatumJobDetails.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def tags(self):
        """Gets the tags of this DatumJobDetails.  # noqa: E501


        :return: The tags of this DatumJobDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DatumJobDetails.


        :param tags: The tags of this DatumJobDetails.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def pipeline(self):
        """Gets the pipeline of this DatumJobDetails.  # noqa: E501


        :return: The pipeline of this DatumJobDetails.  # noqa: E501
        :rtype: DatumJobDetailsPipeline
        """
        return self._pipeline

    @pipeline.setter
    def pipeline(self, pipeline):
        """Sets the pipeline of this DatumJobDetails.


        :param pipeline: The pipeline of this DatumJobDetails.  # noqa: E501
        :type: DatumJobDetailsPipeline
        """

        self._pipeline = pipeline

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
        if issubclass(DatumJobDetails, dict):
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
        if not isinstance(other, DatumJobDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
