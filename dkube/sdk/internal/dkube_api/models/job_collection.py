# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.5.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class JobCollection(object):
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
        'children': 'list[JobModel]',
        'job': 'JobModel',
        'workers': 'list[WorkerModel]',
        'devices': 'list[JobCollectionDevices]'
    }

    attribute_map = {
        'children': 'children',
        'job': 'job',
        'workers': 'workers',
        'devices': 'devices'
    }

    def __init__(self, children=None, job=None, workers=None, devices=None):  # noqa: E501
        """JobCollection - a model defined in Swagger"""  # noqa: E501

        self._children = None
        self._job = None
        self._workers = None
        self._devices = None
        self.discriminator = None

        if children is not None:
            self.children = children
        if job is not None:
            self.job = job
        if workers is not None:
            self.workers = workers
        if devices is not None:
            self.devices = devices

    @property
    def children(self):
        """Gets the children of this JobCollection.  # noqa: E501


        :return: The children of this JobCollection.  # noqa: E501
        :rtype: list[JobModel]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this JobCollection.


        :param children: The children of this JobCollection.  # noqa: E501
        :type: list[JobModel]
        """

        self._children = children

    @property
    def job(self):
        """Gets the job of this JobCollection.  # noqa: E501


        :return: The job of this JobCollection.  # noqa: E501
        :rtype: JobModel
        """
        return self._job

    @job.setter
    def job(self, job):
        """Sets the job of this JobCollection.


        :param job: The job of this JobCollection.  # noqa: E501
        :type: JobModel
        """

        self._job = job

    @property
    def workers(self):
        """Gets the workers of this JobCollection.  # noqa: E501


        :return: The workers of this JobCollection.  # noqa: E501
        :rtype: list[WorkerModel]
        """
        return self._workers

    @workers.setter
    def workers(self, workers):
        """Sets the workers of this JobCollection.


        :param workers: The workers of this JobCollection.  # noqa: E501
        :type: list[WorkerModel]
        """

        self._workers = workers

    @property
    def devices(self):
        """Gets the devices of this JobCollection.  # noqa: E501


        :return: The devices of this JobCollection.  # noqa: E501
        :rtype: list[JobCollectionDevices]
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this JobCollection.


        :param devices: The devices of this JobCollection.  # noqa: E501
        :type: list[JobCollectionDevices]
        """

        self._devices = devices

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
        if issubclass(JobCollection, dict):
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
        if not isinstance(other, JobCollection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
