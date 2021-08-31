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


class DataCopy(object):
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
        'src_path': 'str',
        'name': 'str',
        'job_uuid': 'str',
        'version': 'str',
        'target_path': 'str',
        'status': 'str',
        'uuid': 'str',
        'user': 'str',
        'progress': 'int'
    }

    attribute_map = {
        'src_path': 'src_path',
        'name': 'name',
        'job_uuid': 'Job_UUID',
        'version': 'version',
        'target_path': 'target_path',
        'status': 'status',
        'uuid': 'UUID',
        'user': 'user',
        'progress': 'progress'
    }

    def __init__(self, src_path=None, name=None, job_uuid=None, version=None, target_path=None, status=None, uuid=None, user=None, progress=None):  # noqa: E501
        """DataCopy - a model defined in Swagger"""  # noqa: E501

        self._src_path = None
        self._name = None
        self._job_uuid = None
        self._version = None
        self._target_path = None
        self._status = None
        self._uuid = None
        self._user = None
        self._progress = None
        self.discriminator = None

        if src_path is not None:
            self.src_path = src_path
        if name is not None:
            self.name = name
        if job_uuid is not None:
            self.job_uuid = job_uuid
        if version is not None:
            self.version = version
        if target_path is not None:
            self.target_path = target_path
        if status is not None:
            self.status = status
        if uuid is not None:
            self.uuid = uuid
        if user is not None:
            self.user = user
        if progress is not None:
            self.progress = progress

    @property
    def src_path(self):
        """Gets the src_path of this DataCopy.  # noqa: E501


        :return: The src_path of this DataCopy.  # noqa: E501
        :rtype: str
        """
        return self._src_path

    @src_path.setter
    def src_path(self, src_path):
        """Sets the src_path of this DataCopy.


        :param src_path: The src_path of this DataCopy.  # noqa: E501
        :type: str
        """

        self._src_path = src_path

    @property
    def name(self):
        """Gets the name of this DataCopy.  # noqa: E501


        :return: The name of this DataCopy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataCopy.


        :param name: The name of this DataCopy.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def job_uuid(self):
        """Gets the job_uuid of this DataCopy.  # noqa: E501


        :return: The job_uuid of this DataCopy.  # noqa: E501
        :rtype: str
        """
        return self._job_uuid

    @job_uuid.setter
    def job_uuid(self, job_uuid):
        """Sets the job_uuid of this DataCopy.


        :param job_uuid: The job_uuid of this DataCopy.  # noqa: E501
        :type: str
        """

        self._job_uuid = job_uuid

    @property
    def version(self):
        """Gets the version of this DataCopy.  # noqa: E501


        :return: The version of this DataCopy.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DataCopy.


        :param version: The version of this DataCopy.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def target_path(self):
        """Gets the target_path of this DataCopy.  # noqa: E501


        :return: The target_path of this DataCopy.  # noqa: E501
        :rtype: str
        """
        return self._target_path

    @target_path.setter
    def target_path(self, target_path):
        """Sets the target_path of this DataCopy.


        :param target_path: The target_path of this DataCopy.  # noqa: E501
        :type: str
        """

        self._target_path = target_path

    @property
    def status(self):
        """Gets the status of this DataCopy.  # noqa: E501


        :return: The status of this DataCopy.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DataCopy.


        :param status: The status of this DataCopy.  # noqa: E501
        :type: str
        """
        allowed_values = ["starting", "copying", "completed", "error", "aborted"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def uuid(self):
        """Gets the uuid of this DataCopy.  # noqa: E501


        :return: The uuid of this DataCopy.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this DataCopy.


        :param uuid: The uuid of this DataCopy.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def user(self):
        """Gets the user of this DataCopy.  # noqa: E501


        :return: The user of this DataCopy.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this DataCopy.


        :param user: The user of this DataCopy.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def progress(self):
        """Gets the progress of this DataCopy.  # noqa: E501

        Progress in percentage  # noqa: E501

        :return: The progress of this DataCopy.  # noqa: E501
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this DataCopy.

        Progress in percentage  # noqa: E501

        :param progress: The progress of this DataCopy.  # noqa: E501
        :type: int
        """

        self._progress = progress

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
        if issubclass(DataCopy, dict):
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
        if not isinstance(other, DataCopy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
