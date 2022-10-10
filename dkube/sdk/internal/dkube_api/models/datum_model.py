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


class DatumModel(object):
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
        'description': 'str',
        'tags': 'list[str]',
        '_class': 'str',
        'group': 'str',
        'project': 'str',
        'dvs': 'str',
        'source': 'str',
        'url': 'str',
        'remote': 'bool',
        'gitaccess': 'GitAccessInfo',
        'redshift': 'RedshiftAccessInfo',
        'sql': 'SQLAccessInfo',
        's3access': 'S3AccessCredentials',
        'k8svolume': 'DatumModelK8svolume',
        'hostpath': 'DatumModelHostpath',
        'nfsaccess': 'NFSAccessInfo',
        'gcsaccess': 'GCSAccessInfo',
        'fsx': 'Fsx',
        'generated': 'DatumModelGenerated'
    }

    attribute_map = {
        'version': 'version',
        'name': 'name',
        'description': 'description',
        'tags': 'tags',
        '_class': 'class',
        'group': 'group',
        'project': 'project',
        'dvs': 'dvs',
        'source': 'source',
        'url': 'url',
        'remote': 'remote',
        'gitaccess': 'gitaccess',
        'redshift': 'redshift',
        'sql': 'sql',
        's3access': 's3access',
        'k8svolume': 'k8svolume',
        'hostpath': 'hostpath',
        'nfsaccess': 'nfsaccess',
        'gcsaccess': 'gcsaccess',
        'fsx': 'fsx',
        'generated': 'generated'
    }

    def __init__(self, version=None, name=None, description=None, tags=None, _class=None, group=None, project=None, dvs=None, source=None, url=None, remote=False, gitaccess=None, redshift=None, sql=None, s3access=None, k8svolume=None, hostpath=None, nfsaccess=None, gcsaccess=None, fsx=None, generated=None):  # noqa: E501
        """DatumModel - a model defined in Swagger"""  # noqa: E501

        self._version = None
        self._name = None
        self._description = None
        self._tags = None
        self.__class = None
        self._group = None
        self._project = None
        self._dvs = None
        self._source = None
        self._url = None
        self._remote = None
        self._gitaccess = None
        self._redshift = None
        self._sql = None
        self._s3access = None
        self._k8svolume = None
        self._hostpath = None
        self._nfsaccess = None
        self._gcsaccess = None
        self._fsx = None
        self._generated = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if _class is not None:
            self._class = _class
        if group is not None:
            self.group = group
        if project is not None:
            self.project = project
        if dvs is not None:
            self.dvs = dvs
        if source is not None:
            self.source = source
        if url is not None:
            self.url = url
        if remote is not None:
            self.remote = remote
        if gitaccess is not None:
            self.gitaccess = gitaccess
        if redshift is not None:
            self.redshift = redshift
        if sql is not None:
            self.sql = sql
        if s3access is not None:
            self.s3access = s3access
        if k8svolume is not None:
            self.k8svolume = k8svolume
        if hostpath is not None:
            self.hostpath = hostpath
        if nfsaccess is not None:
            self.nfsaccess = nfsaccess
        if gcsaccess is not None:
            self.gcsaccess = gcsaccess
        if fsx is not None:
            self.fsx = fsx
        if generated is not None:
            self.generated = generated

    @property
    def version(self):
        """Gets the version of this DatumModel.  # noqa: E501


        :return: The version of this DatumModel.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DatumModel.


        :param version: The version of this DatumModel.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def name(self):
        """Gets the name of this DatumModel.  # noqa: E501


        :return: The name of this DatumModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DatumModel.


        :param name: The name of this DatumModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this DatumModel.  # noqa: E501


        :return: The description of this DatumModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DatumModel.


        :param description: The description of this DatumModel.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this DatumModel.  # noqa: E501


        :return: The tags of this DatumModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DatumModel.


        :param tags: The tags of this DatumModel.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def _class(self):
        """Gets the _class of this DatumModel.  # noqa: E501


        :return: The _class of this DatumModel.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this DatumModel.


        :param _class: The _class of this DatumModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["model", "dataset", "program"]  # noqa: E501
        if _class not in allowed_values:
            raise ValueError(
                "Invalid value for `_class` ({0}), must be one of {1}"  # noqa: E501
                .format(_class, allowed_values)
            )

        self.__class = _class

    @property
    def group(self):
        """Gets the group of this DatumModel.  # noqa: E501


        :return: The group of this DatumModel.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this DatumModel.


        :param group: The group of this DatumModel.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def project(self):
        """Gets the project of this DatumModel.  # noqa: E501


        :return: The project of this DatumModel.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this DatumModel.


        :param project: The project of this DatumModel.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def dvs(self):
        """Gets the dvs of this DatumModel.  # noqa: E501


        :return: The dvs of this DatumModel.  # noqa: E501
        :rtype: str
        """
        return self._dvs

    @dvs.setter
    def dvs(self, dvs):
        """Sets the dvs of this DatumModel.


        :param dvs: The dvs of this DatumModel.  # noqa: E501
        :type: str
        """

        self._dvs = dvs

    @property
    def source(self):
        """Gets the source of this DatumModel.  # noqa: E501

        Enum of supported sources. git - If the datum is in github repo, aws-s3 - If the datum is in aws_s3 bucket, pub_url - If the datum is accessible over a public url, s3 - If datum is in any other s3 storage say like storage provided by minio, dkube - If datum is in dkube s3 storage itself  # noqa: E501

        :return: The source of this DatumModel.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this DatumModel.

        Enum of supported sources. git - If the datum is in github repo, aws-s3 - If the datum is in aws_s3 bucket, pub_url - If the datum is accessible over a public url, s3 - If datum is in any other s3 storage say like storage provided by minio, dkube - If datum is in dkube s3 storage itself  # noqa: E501

        :param source: The source of this DatumModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["git", "aws_s3", "s3", "pub_url", "k8s_volume", "dkube", "nfs", "gcs", "dvs", "workstation", "redshift", "hostpath", "sql", "fsx"]  # noqa: E501
        if source not in allowed_values:
            raise ValueError(
                "Invalid value for `source` ({0}), must be one of {1}"  # noqa: E501
                .format(source, allowed_values)
            )

        self._source = source

    @property
    def url(self):
        """Gets the url of this DatumModel.  # noqa: E501

        Actual URL to download/access from based on the source.  # noqa: E501

        :return: The url of this DatumModel.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this DatumModel.

        Actual URL to download/access from based on the source.  # noqa: E501

        :param url: The url of this DatumModel.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def remote(self):
        """Gets the remote of this DatumModel.  # noqa: E501

        Set to 'true' if datum should not be downloaded and only accessed remotely. Say data in AWS S3 bucket which can be mounted and accessed.  # noqa: E501

        :return: The remote of this DatumModel.  # noqa: E501
        :rtype: bool
        """
        return self._remote

    @remote.setter
    def remote(self, remote):
        """Sets the remote of this DatumModel.

        Set to 'true' if datum should not be downloaded and only accessed remotely. Say data in AWS S3 bucket which can be mounted and accessed.  # noqa: E501

        :param remote: The remote of this DatumModel.  # noqa: E501
        :type: bool
        """

        self._remote = remote

    @property
    def gitaccess(self):
        """Gets the gitaccess of this DatumModel.  # noqa: E501


        :return: The gitaccess of this DatumModel.  # noqa: E501
        :rtype: GitAccessInfo
        """
        return self._gitaccess

    @gitaccess.setter
    def gitaccess(self, gitaccess):
        """Sets the gitaccess of this DatumModel.


        :param gitaccess: The gitaccess of this DatumModel.  # noqa: E501
        :type: GitAccessInfo
        """

        self._gitaccess = gitaccess

    @property
    def redshift(self):
        """Gets the redshift of this DatumModel.  # noqa: E501


        :return: The redshift of this DatumModel.  # noqa: E501
        :rtype: RedshiftAccessInfo
        """
        return self._redshift

    @redshift.setter
    def redshift(self, redshift):
        """Sets the redshift of this DatumModel.


        :param redshift: The redshift of this DatumModel.  # noqa: E501
        :type: RedshiftAccessInfo
        """

        self._redshift = redshift

    @property
    def sql(self):
        """Gets the sql of this DatumModel.  # noqa: E501


        :return: The sql of this DatumModel.  # noqa: E501
        :rtype: SQLAccessInfo
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        """Sets the sql of this DatumModel.


        :param sql: The sql of this DatumModel.  # noqa: E501
        :type: SQLAccessInfo
        """

        self._sql = sql

    @property
    def s3access(self):
        """Gets the s3access of this DatumModel.  # noqa: E501


        :return: The s3access of this DatumModel.  # noqa: E501
        :rtype: S3AccessCredentials
        """
        return self._s3access

    @s3access.setter
    def s3access(self, s3access):
        """Sets the s3access of this DatumModel.


        :param s3access: The s3access of this DatumModel.  # noqa: E501
        :type: S3AccessCredentials
        """

        self._s3access = s3access

    @property
    def k8svolume(self):
        """Gets the k8svolume of this DatumModel.  # noqa: E501


        :return: The k8svolume of this DatumModel.  # noqa: E501
        :rtype: DatumModelK8svolume
        """
        return self._k8svolume

    @k8svolume.setter
    def k8svolume(self, k8svolume):
        """Sets the k8svolume of this DatumModel.


        :param k8svolume: The k8svolume of this DatumModel.  # noqa: E501
        :type: DatumModelK8svolume
        """

        self._k8svolume = k8svolume

    @property
    def hostpath(self):
        """Gets the hostpath of this DatumModel.  # noqa: E501


        :return: The hostpath of this DatumModel.  # noqa: E501
        :rtype: DatumModelHostpath
        """
        return self._hostpath

    @hostpath.setter
    def hostpath(self, hostpath):
        """Sets the hostpath of this DatumModel.


        :param hostpath: The hostpath of this DatumModel.  # noqa: E501
        :type: DatumModelHostpath
        """

        self._hostpath = hostpath

    @property
    def nfsaccess(self):
        """Gets the nfsaccess of this DatumModel.  # noqa: E501


        :return: The nfsaccess of this DatumModel.  # noqa: E501
        :rtype: NFSAccessInfo
        """
        return self._nfsaccess

    @nfsaccess.setter
    def nfsaccess(self, nfsaccess):
        """Sets the nfsaccess of this DatumModel.


        :param nfsaccess: The nfsaccess of this DatumModel.  # noqa: E501
        :type: NFSAccessInfo
        """

        self._nfsaccess = nfsaccess

    @property
    def gcsaccess(self):
        """Gets the gcsaccess of this DatumModel.  # noqa: E501


        :return: The gcsaccess of this DatumModel.  # noqa: E501
        :rtype: GCSAccessInfo
        """
        return self._gcsaccess

    @gcsaccess.setter
    def gcsaccess(self, gcsaccess):
        """Sets the gcsaccess of this DatumModel.


        :param gcsaccess: The gcsaccess of this DatumModel.  # noqa: E501
        :type: GCSAccessInfo
        """

        self._gcsaccess = gcsaccess

    @property
    def fsx(self):
        """Gets the fsx of this DatumModel.  # noqa: E501


        :return: The fsx of this DatumModel.  # noqa: E501
        :rtype: Fsx
        """
        return self._fsx

    @fsx.setter
    def fsx(self, fsx):
        """Sets the fsx of this DatumModel.


        :param fsx: The fsx of this DatumModel.  # noqa: E501
        :type: Fsx
        """

        self._fsx = fsx

    @property
    def generated(self):
        """Gets the generated of this DatumModel.  # noqa: E501


        :return: The generated of this DatumModel.  # noqa: E501
        :rtype: DatumModelGenerated
        """
        return self._generated

    @generated.setter
    def generated(self, generated):
        """Sets the generated of this DatumModel.


        :param generated: The generated of this DatumModel.  # noqa: E501
        :type: DatumModelGenerated
        """

        self._generated = generated

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
        if issubclass(DatumModel, dict):
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
        if not isinstance(other, DatumModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
