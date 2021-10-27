# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0.0.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ModelmonitorDatasetDef(object):
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
        '_class': 'str',
        'transformer_script': 'str',
        'name': 'str',
        'sql_query': 'str',
        's3_subpath': 'str',
        'version': 'str',
        'data_format': 'str',
        'groundtruth_col': 'str',
        'predict_col': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        '_class': 'class',
        'transformer_script': 'transformer_script',
        'name': 'name',
        'sql_query': 'sql_query',
        's3_subpath': 's3_subpath',
        'version': 'version',
        'data_format': 'data_format',
        'groundtruth_col': 'groundtruth_col',
        'predict_col': 'predict_col',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, _class=None, transformer_script=None, name=None, sql_query=None, s3_subpath=None, version=None, data_format='csv', groundtruth_col=None, predict_col=None, created_at=None, updated_at=None):  # noqa: E501
        """ModelmonitorDatasetDef - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self.__class = None
        self._transformer_script = None
        self._name = None
        self._sql_query = None
        self._s3_subpath = None
        self._version = None
        self._data_format = None
        self._groundtruth_col = None
        self._predict_col = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if _class is not None:
            self._class = _class
        if transformer_script is not None:
            self.transformer_script = transformer_script
        if name is not None:
            self.name = name
        if sql_query is not None:
            self.sql_query = sql_query
        if s3_subpath is not None:
            self.s3_subpath = s3_subpath
        if version is not None:
            self.version = version
        if data_format is not None:
            self.data_format = data_format
        if groundtruth_col is not None:
            self.groundtruth_col = groundtruth_col
        if predict_col is not None:
            self.predict_col = predict_col
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this ModelmonitorDatasetDef.  # noqa: E501

        UUID4 id for the resource  # noqa: E501

        :return: The id of this ModelmonitorDatasetDef.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelmonitorDatasetDef.

        UUID4 id for the resource  # noqa: E501

        :param id: The id of this ModelmonitorDatasetDef.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def _class(self):
        """Gets the _class of this ModelmonitorDatasetDef.  # noqa: E501


        :return: The _class of this ModelmonitorDatasetDef.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this ModelmonitorDatasetDef.


        :param _class: The _class of this ModelmonitorDatasetDef.  # noqa: E501
        :type: str
        """
        allowed_values = ["TrainData", "PredictData", "MetricsData", "LabelledData"]  # noqa: E501
        if _class not in allowed_values:
            raise ValueError(
                "Invalid value for `_class` ({0}), must be one of {1}"  # noqa: E501
                .format(_class, allowed_values)
            )

        self.__class = _class

    @property
    def transformer_script(self):
        """Gets the transformer_script of this ModelmonitorDatasetDef.  # noqa: E501

        Transformer Script for Preprocessing and Postprocessing for Train and Predict Data  # noqa: E501

        :return: The transformer_script of this ModelmonitorDatasetDef.  # noqa: E501
        :rtype: str
        """
        return self._transformer_script

    @transformer_script.setter
    def transformer_script(self, transformer_script):
        """Sets the transformer_script of this ModelmonitorDatasetDef.

        Transformer Script for Preprocessing and Postprocessing for Train and Predict Data  # noqa: E501

        :param transformer_script: The transformer_script of this ModelmonitorDatasetDef.  # noqa: E501
        :type: str
        """

        self._transformer_script = transformer_script

    @property
    def name(self):
        """Gets the name of this ModelmonitorDatasetDef.  # noqa: E501

        dkube dataset name  # noqa: E501

        :return: The name of this ModelmonitorDatasetDef.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelmonitorDatasetDef.

        dkube dataset name  # noqa: E501

        :param name: The name of this ModelmonitorDatasetDef.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def sql_query(self):
        """Gets the sql_query of this ModelmonitorDatasetDef.  # noqa: E501


        :return: The sql_query of this ModelmonitorDatasetDef.  # noqa: E501
        :rtype: str
        """
        return self._sql_query

    @sql_query.setter
    def sql_query(self, sql_query):
        """Sets the sql_query of this ModelmonitorDatasetDef.


        :param sql_query: The sql_query of this ModelmonitorDatasetDef.  # noqa: E501
        :type: str
        """

        self._sql_query = sql_query

    @property
    def s3_subpath(self):
        """Gets the s3_subpath of this ModelmonitorDatasetDef.  # noqa: E501


        :return: The s3_subpath of this ModelmonitorDatasetDef.  # noqa: E501
        :rtype: str
        """
        return self._s3_subpath

    @s3_subpath.setter
    def s3_subpath(self, s3_subpath):
        """Sets the s3_subpath of this ModelmonitorDatasetDef.


        :param s3_subpath: The s3_subpath of this ModelmonitorDatasetDef.  # noqa: E501
        :type: str
        """

        self._s3_subpath = s3_subpath

    @property
    def version(self):
        """Gets the version of this ModelmonitorDatasetDef.  # noqa: E501

        dkube dataset version  # noqa: E501

        :return: The version of this ModelmonitorDatasetDef.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ModelmonitorDatasetDef.

        dkube dataset version  # noqa: E501

        :param version: The version of this ModelmonitorDatasetDef.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def data_format(self):
        """Gets the data_format of this ModelmonitorDatasetDef.  # noqa: E501

        The format of the dataset  # noqa: E501

        :return: The data_format of this ModelmonitorDatasetDef.  # noqa: E501
        :rtype: str
        """
        return self._data_format

    @data_format.setter
    def data_format(self, data_format):
        """Sets the data_format of this ModelmonitorDatasetDef.

        The format of the dataset  # noqa: E501

        :param data_format: The data_format of this ModelmonitorDatasetDef.  # noqa: E501
        :type: str
        """
        allowed_values = ["csv", "cloudevents", "sagemakerlogs"]  # noqa: E501
        if data_format not in allowed_values:
            raise ValueError(
                "Invalid value for `data_format` ({0}), must be one of {1}"  # noqa: E501
                .format(data_format, allowed_values)
            )

        self._data_format = data_format

    @property
    def groundtruth_col(self):
        """Gets the groundtruth_col of this ModelmonitorDatasetDef.  # noqa: E501

        Ground truth column name in labelled dataset  # noqa: E501

        :return: The groundtruth_col of this ModelmonitorDatasetDef.  # noqa: E501
        :rtype: str
        """
        return self._groundtruth_col

    @groundtruth_col.setter
    def groundtruth_col(self, groundtruth_col):
        """Sets the groundtruth_col of this ModelmonitorDatasetDef.

        Ground truth column name in labelled dataset  # noqa: E501

        :param groundtruth_col: The groundtruth_col of this ModelmonitorDatasetDef.  # noqa: E501
        :type: str
        """

        self._groundtruth_col = groundtruth_col

    @property
    def predict_col(self):
        """Gets the predict_col of this ModelmonitorDatasetDef.  # noqa: E501

        Predict column name in train dataset  # noqa: E501

        :return: The predict_col of this ModelmonitorDatasetDef.  # noqa: E501
        :rtype: str
        """
        return self._predict_col

    @predict_col.setter
    def predict_col(self, predict_col):
        """Sets the predict_col of this ModelmonitorDatasetDef.

        Predict column name in train dataset  # noqa: E501

        :param predict_col: The predict_col of this ModelmonitorDatasetDef.  # noqa: E501
        :type: str
        """

        self._predict_col = predict_col

    @property
    def created_at(self):
        """Gets the created_at of this ModelmonitorDatasetDef.  # noqa: E501


        :return: The created_at of this ModelmonitorDatasetDef.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ModelmonitorDatasetDef.


        :param created_at: The created_at of this ModelmonitorDatasetDef.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ModelmonitorDatasetDef.  # noqa: E501


        :return: The updated_at of this ModelmonitorDatasetDef.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ModelmonitorDatasetDef.


        :param updated_at: The updated_at of this ModelmonitorDatasetDef.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

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
        if issubclass(ModelmonitorDatasetDef, dict):
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
        if not isinstance(other, ModelmonitorDatasetDef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
