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


class RepoModel(object):
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
        'tags': 'list[str]',
        'description': 'str',
        'gitaccess': 'GitAccessCredentials',
        's3access': 'RepoS3AccessCredentials',
        'k8svolume': 'K8SVolumeInfo',
        'nfsaccess': 'NFSAccessInfo',
        'gcsaccess': 'RepoGCSAccessInfo',
        'redshift': 'RedshiftAccessInfo',
        'sql': 'SQLAccessInfo'
    }

    attribute_map = {
        'name': 'name',
        'tags': 'tags',
        'description': 'description',
        'gitaccess': 'gitaccess',
        's3access': 's3access',
        'k8svolume': 'k8svolume',
        'nfsaccess': 'nfsaccess',
        'gcsaccess': 'gcsaccess',
        'redshift': 'redshift',
        'sql': 'sql'
    }

    def __init__(self, name=None, tags=None, description=None, gitaccess=None, s3access=None, k8svolume=None, nfsaccess=None, gcsaccess=None, redshift=None, sql=None):  # noqa: E501
        """RepoModel - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._tags = None
        self._description = None
        self._gitaccess = None
        self._s3access = None
        self._k8svolume = None
        self._nfsaccess = None
        self._gcsaccess = None
        self._redshift = None
        self._sql = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if tags is not None:
            self.tags = tags
        if description is not None:
            self.description = description
        if gitaccess is not None:
            self.gitaccess = gitaccess
        if s3access is not None:
            self.s3access = s3access
        if k8svolume is not None:
            self.k8svolume = k8svolume
        if nfsaccess is not None:
            self.nfsaccess = nfsaccess
        if gcsaccess is not None:
            self.gcsaccess = gcsaccess
        if redshift is not None:
            self.redshift = redshift
        if sql is not None:
            self.sql = sql

    @property
    def name(self):
        """Gets the name of this RepoModel.  # noqa: E501


        :return: The name of this RepoModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RepoModel.


        :param name: The name of this RepoModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def tags(self):
        """Gets the tags of this RepoModel.  # noqa: E501


        :return: The tags of this RepoModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this RepoModel.


        :param tags: The tags of this RepoModel.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def description(self):
        """Gets the description of this RepoModel.  # noqa: E501


        :return: The description of this RepoModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RepoModel.


        :param description: The description of this RepoModel.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def gitaccess(self):
        """Gets the gitaccess of this RepoModel.  # noqa: E501


        :return: The gitaccess of this RepoModel.  # noqa: E501
        :rtype: GitAccessCredentials
        """
        return self._gitaccess

    @gitaccess.setter
    def gitaccess(self, gitaccess):
        """Sets the gitaccess of this RepoModel.


        :param gitaccess: The gitaccess of this RepoModel.  # noqa: E501
        :type: GitAccessCredentials
        """

        self._gitaccess = gitaccess

    @property
    def s3access(self):
        """Gets the s3access of this RepoModel.  # noqa: E501


        :return: The s3access of this RepoModel.  # noqa: E501
        :rtype: RepoS3AccessCredentials
        """
        return self._s3access

    @s3access.setter
    def s3access(self, s3access):
        """Sets the s3access of this RepoModel.


        :param s3access: The s3access of this RepoModel.  # noqa: E501
        :type: RepoS3AccessCredentials
        """

        self._s3access = s3access

    @property
    def k8svolume(self):
        """Gets the k8svolume of this RepoModel.  # noqa: E501


        :return: The k8svolume of this RepoModel.  # noqa: E501
        :rtype: K8SVolumeInfo
        """
        return self._k8svolume

    @k8svolume.setter
    def k8svolume(self, k8svolume):
        """Sets the k8svolume of this RepoModel.


        :param k8svolume: The k8svolume of this RepoModel.  # noqa: E501
        :type: K8SVolumeInfo
        """

        self._k8svolume = k8svolume

    @property
    def nfsaccess(self):
        """Gets the nfsaccess of this RepoModel.  # noqa: E501


        :return: The nfsaccess of this RepoModel.  # noqa: E501
        :rtype: NFSAccessInfo
        """
        return self._nfsaccess

    @nfsaccess.setter
    def nfsaccess(self, nfsaccess):
        """Sets the nfsaccess of this RepoModel.


        :param nfsaccess: The nfsaccess of this RepoModel.  # noqa: E501
        :type: NFSAccessInfo
        """

        self._nfsaccess = nfsaccess

    @property
    def gcsaccess(self):
        """Gets the gcsaccess of this RepoModel.  # noqa: E501


        :return: The gcsaccess of this RepoModel.  # noqa: E501
        :rtype: RepoGCSAccessInfo
        """
        return self._gcsaccess

    @gcsaccess.setter
    def gcsaccess(self, gcsaccess):
        """Sets the gcsaccess of this RepoModel.


        :param gcsaccess: The gcsaccess of this RepoModel.  # noqa: E501
        :type: RepoGCSAccessInfo
        """

        self._gcsaccess = gcsaccess

    @property
    def redshift(self):
        """Gets the redshift of this RepoModel.  # noqa: E501


        :return: The redshift of this RepoModel.  # noqa: E501
        :rtype: RedshiftAccessInfo
        """
        return self._redshift

    @redshift.setter
    def redshift(self, redshift):
        """Sets the redshift of this RepoModel.


        :param redshift: The redshift of this RepoModel.  # noqa: E501
        :type: RedshiftAccessInfo
        """

        self._redshift = redshift

    @property
    def sql(self):
        """Gets the sql of this RepoModel.  # noqa: E501


        :return: The sql of this RepoModel.  # noqa: E501
        :rtype: SQLAccessInfo
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        """Sets the sql of this RepoModel.


        :param sql: The sql of this RepoModel.  # noqa: E501
        :type: SQLAccessInfo
        """

        self._sql = sql

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
        if issubclass(RepoModel, dict):
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
        if not isinstance(other, RepoModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
