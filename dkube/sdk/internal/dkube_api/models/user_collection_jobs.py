# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.8.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class UserCollectionJobs(object):
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
        'notebooks': 'UserCollectionJobsNotebooks',
        'jobs': 'UserCollectionJobsNotebooks',
        'inferences': 'UserCollectionJobsNotebooks',
        'preprocessing': 'UserCollectionJobsNotebooks'
    }

    attribute_map = {
        'notebooks': 'notebooks',
        'jobs': 'jobs',
        'inferences': 'inferences',
        'preprocessing': 'preprocessing'
    }

    def __init__(self, notebooks=None, jobs=None, inferences=None, preprocessing=None):  # noqa: E501
        """UserCollectionJobs - a model defined in Swagger"""  # noqa: E501

        self._notebooks = None
        self._jobs = None
        self._inferences = None
        self._preprocessing = None
        self.discriminator = None

        if notebooks is not None:
            self.notebooks = notebooks
        if jobs is not None:
            self.jobs = jobs
        if inferences is not None:
            self.inferences = inferences
        if preprocessing is not None:
            self.preprocessing = preprocessing

    @property
    def notebooks(self):
        """Gets the notebooks of this UserCollectionJobs.  # noqa: E501


        :return: The notebooks of this UserCollectionJobs.  # noqa: E501
        :rtype: UserCollectionJobsNotebooks
        """
        return self._notebooks

    @notebooks.setter
    def notebooks(self, notebooks):
        """Sets the notebooks of this UserCollectionJobs.


        :param notebooks: The notebooks of this UserCollectionJobs.  # noqa: E501
        :type: UserCollectionJobsNotebooks
        """

        self._notebooks = notebooks

    @property
    def jobs(self):
        """Gets the jobs of this UserCollectionJobs.  # noqa: E501


        :return: The jobs of this UserCollectionJobs.  # noqa: E501
        :rtype: UserCollectionJobsNotebooks
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this UserCollectionJobs.


        :param jobs: The jobs of this UserCollectionJobs.  # noqa: E501
        :type: UserCollectionJobsNotebooks
        """

        self._jobs = jobs

    @property
    def inferences(self):
        """Gets the inferences of this UserCollectionJobs.  # noqa: E501


        :return: The inferences of this UserCollectionJobs.  # noqa: E501
        :rtype: UserCollectionJobsNotebooks
        """
        return self._inferences

    @inferences.setter
    def inferences(self, inferences):
        """Sets the inferences of this UserCollectionJobs.


        :param inferences: The inferences of this UserCollectionJobs.  # noqa: E501
        :type: UserCollectionJobsNotebooks
        """

        self._inferences = inferences

    @property
    def preprocessing(self):
        """Gets the preprocessing of this UserCollectionJobs.  # noqa: E501


        :return: The preprocessing of this UserCollectionJobs.  # noqa: E501
        :rtype: UserCollectionJobsNotebooks
        """
        return self._preprocessing

    @preprocessing.setter
    def preprocessing(self, preprocessing):
        """Sets the preprocessing of this UserCollectionJobs.


        :param preprocessing: The preprocessing of this UserCollectionJobs.  # noqa: E501
        :type: UserCollectionJobsNotebooks
        """

        self._preprocessing = preprocessing

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
        if issubclass(UserCollectionJobs, dict):
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
        if not isinstance(other, UserCollectionJobs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
