# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.7.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ModelmonitorDataSourceDef(object):
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
        'timezone': 'str',
        'timestamp_col': 'str',
        'sql_query': 'str',
        's3_subpath': 'str',
        'version': 'str',
        'data_format': 'str',
        'groundtruth_col': 'str',
        'predict_col': 'str',
        'image_transformation': 'list[str]',
        'date_suffix': 'str'
    }

    attribute_map = {
        'id': 'id',
        '_class': 'class',
        'transformer_script': 'transformer_script',
        'name': 'name',
        'timezone': 'timezone',
        'timestamp_col': 'timestamp_col',
        'sql_query': 'sql_query',
        's3_subpath': 's3_subpath',
        'version': 'version',
        'data_format': 'data_format',
        'groundtruth_col': 'groundtruth_col',
        'predict_col': 'predict_col',
        'image_transformation': 'image_transformation',
        'date_suffix': 'date_suffix'
    }

    def __init__(self, id=None, _class=None, transformer_script=None, name=None, timezone=None, timestamp_col=None, sql_query=None, s3_subpath=None, version=None, data_format='tabular', groundtruth_col=None, predict_col=None, image_transformation=None, date_suffix='none'):  # noqa: E501
        """ModelmonitorDataSourceDef - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self.__class = None
        self._transformer_script = None
        self._name = None
        self._timezone = None
        self._timestamp_col = None
        self._sql_query = None
        self._s3_subpath = None
        self._version = None
        self._data_format = None
        self._groundtruth_col = None
        self._predict_col = None
        self._image_transformation = None
        self._date_suffix = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if _class is not None:
            self._class = _class
        if transformer_script is not None:
            self.transformer_script = transformer_script
        if name is not None:
            self.name = name
        if timezone is not None:
            self.timezone = timezone
        if timestamp_col is not None:
            self.timestamp_col = timestamp_col
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
        if image_transformation is not None:
            self.image_transformation = image_transformation
        if date_suffix is not None:
            self.date_suffix = date_suffix

    @property
    def id(self):
        """Gets the id of this ModelmonitorDataSourceDef.  # noqa: E501

        UUID4 id for the resource  # noqa: E501

        :return: The id of this ModelmonitorDataSourceDef.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelmonitorDataSourceDef.

        UUID4 id for the resource  # noqa: E501

        :param id: The id of this ModelmonitorDataSourceDef.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def _class(self):
        """Gets the _class of this ModelmonitorDataSourceDef.  # noqa: E501


        :return: The _class of this ModelmonitorDataSourceDef.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this ModelmonitorDataSourceDef.


        :param _class: The _class of this ModelmonitorDataSourceDef.  # noqa: E501
        :type: str
        """
        allowed_values = ["labelled", "metrics", "predict", "train"]  # noqa: E501
        if _class not in allowed_values:
            raise ValueError(
                "Invalid value for `_class` ({0}), must be one of {1}"  # noqa: E501
                .format(_class, allowed_values)
            )

        self.__class = _class

    @property
    def transformer_script(self):
        """Gets the transformer_script of this ModelmonitorDataSourceDef.  # noqa: E501

        Transformer Script for Preprocessing and Postprocessing for Train and Predict Data  # noqa: E501

        :return: The transformer_script of this ModelmonitorDataSourceDef.  # noqa: E501
        :rtype: str
        """
        return self._transformer_script

    @transformer_script.setter
    def transformer_script(self, transformer_script):
        """Sets the transformer_script of this ModelmonitorDataSourceDef.

        Transformer Script for Preprocessing and Postprocessing for Train and Predict Data  # noqa: E501

        :param transformer_script: The transformer_script of this ModelmonitorDataSourceDef.  # noqa: E501
        :type: str
        """

        self._transformer_script = transformer_script

    @property
    def name(self):
        """Gets the name of this ModelmonitorDataSourceDef.  # noqa: E501

        dkube dataset name  # noqa: E501

        :return: The name of this ModelmonitorDataSourceDef.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelmonitorDataSourceDef.

        dkube dataset name  # noqa: E501

        :param name: The name of this ModelmonitorDataSourceDef.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def timezone(self):
        """Gets the timezone of this ModelmonitorDataSourceDef.  # noqa: E501


        :return: The timezone of this ModelmonitorDataSourceDef.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this ModelmonitorDataSourceDef.


        :param timezone: The timezone of this ModelmonitorDataSourceDef.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def timestamp_col(self):
        """Gets the timestamp_col of this ModelmonitorDataSourceDef.  # noqa: E501


        :return: The timestamp_col of this ModelmonitorDataSourceDef.  # noqa: E501
        :rtype: str
        """
        return self._timestamp_col

    @timestamp_col.setter
    def timestamp_col(self, timestamp_col):
        """Sets the timestamp_col of this ModelmonitorDataSourceDef.


        :param timestamp_col: The timestamp_col of this ModelmonitorDataSourceDef.  # noqa: E501
        :type: str
        """

        self._timestamp_col = timestamp_col

    @property
    def sql_query(self):
        """Gets the sql_query of this ModelmonitorDataSourceDef.  # noqa: E501


        :return: The sql_query of this ModelmonitorDataSourceDef.  # noqa: E501
        :rtype: str
        """
        return self._sql_query

    @sql_query.setter
    def sql_query(self, sql_query):
        """Sets the sql_query of this ModelmonitorDataSourceDef.


        :param sql_query: The sql_query of this ModelmonitorDataSourceDef.  # noqa: E501
        :type: str
        """

        self._sql_query = sql_query

    @property
    def s3_subpath(self):
        """Gets the s3_subpath of this ModelmonitorDataSourceDef.  # noqa: E501


        :return: The s3_subpath of this ModelmonitorDataSourceDef.  # noqa: E501
        :rtype: str
        """
        return self._s3_subpath

    @s3_subpath.setter
    def s3_subpath(self, s3_subpath):
        """Sets the s3_subpath of this ModelmonitorDataSourceDef.


        :param s3_subpath: The s3_subpath of this ModelmonitorDataSourceDef.  # noqa: E501
        :type: str
        """

        self._s3_subpath = s3_subpath

    @property
    def version(self):
        """Gets the version of this ModelmonitorDataSourceDef.  # noqa: E501

        dkube dataset version  # noqa: E501

        :return: The version of this ModelmonitorDataSourceDef.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ModelmonitorDataSourceDef.

        dkube dataset version  # noqa: E501

        :param version: The version of this ModelmonitorDataSourceDef.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def data_format(self):
        """Gets the data_format of this ModelmonitorDataSourceDef.  # noqa: E501

        The format of the dataset  # noqa: E501

        :return: The data_format of this ModelmonitorDataSourceDef.  # noqa: E501
        :rtype: str
        """
        return self._data_format

    @data_format.setter
    def data_format(self, data_format):
        """Sets the data_format of this ModelmonitorDataSourceDef.

        The format of the dataset  # noqa: E501

        :param data_format: The data_format of this ModelmonitorDataSourceDef.  # noqa: E501
        :type: str
        """
        allowed_values = ["tabular", "cloudeventlogs", "sagemakerlogs", "image"]  # noqa: E501
        if data_format not in allowed_values:
            raise ValueError(
                "Invalid value for `data_format` ({0}), must be one of {1}"  # noqa: E501
                .format(data_format, allowed_values)
            )

        self._data_format = data_format

    @property
    def groundtruth_col(self):
        """Gets the groundtruth_col of this ModelmonitorDataSourceDef.  # noqa: E501

        Ground truth column name in labelled dataset  # noqa: E501

        :return: The groundtruth_col of this ModelmonitorDataSourceDef.  # noqa: E501
        :rtype: str
        """
        return self._groundtruth_col

    @groundtruth_col.setter
    def groundtruth_col(self, groundtruth_col):
        """Sets the groundtruth_col of this ModelmonitorDataSourceDef.

        Ground truth column name in labelled dataset  # noqa: E501

        :param groundtruth_col: The groundtruth_col of this ModelmonitorDataSourceDef.  # noqa: E501
        :type: str
        """

        self._groundtruth_col = groundtruth_col

    @property
    def predict_col(self):
        """Gets the predict_col of this ModelmonitorDataSourceDef.  # noqa: E501

        Predict column name in train dataset  # noqa: E501

        :return: The predict_col of this ModelmonitorDataSourceDef.  # noqa: E501
        :rtype: str
        """
        return self._predict_col

    @predict_col.setter
    def predict_col(self, predict_col):
        """Sets the predict_col of this ModelmonitorDataSourceDef.

        Predict column name in train dataset  # noqa: E501

        :param predict_col: The predict_col of this ModelmonitorDataSourceDef.  # noqa: E501
        :type: str
        """

        self._predict_col = predict_col

    @property
    def image_transformation(self):
        """Gets the image_transformation of this ModelmonitorDataSourceDef.  # noqa: E501


        :return: The image_transformation of this ModelmonitorDataSourceDef.  # noqa: E501
        :rtype: list[str]
        """
        return self._image_transformation

    @image_transformation.setter
    def image_transformation(self, image_transformation):
        """Sets the image_transformation of this ModelmonitorDataSourceDef.


        :param image_transformation: The image_transformation of this ModelmonitorDataSourceDef.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["standardisation", "normalization", "scaling"]  # noqa: E501
        if not set(image_transformation).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `image_transformation` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(image_transformation) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._image_transformation = image_transformation

    @property
    def date_suffix(self):
        """Gets the date_suffix of this ModelmonitorDataSourceDef.  # noqa: E501

        In case of datasource to be tabular and your datasource is arranged in the  directory structure of time fashion you can select either of the option yyyy/mm/dd/hh - in case of datsource is arranged in year/month/date/hour format yyyy/mm/dd    - in case of datsource is arranged in year/month/date format yyyy/mm       - in case of datsource is arranged in year/month format \"none\"        - in case data has no arranged fashion  # noqa: E501

        :return: The date_suffix of this ModelmonitorDataSourceDef.  # noqa: E501
        :rtype: str
        """
        return self._date_suffix

    @date_suffix.setter
    def date_suffix(self, date_suffix):
        """Sets the date_suffix of this ModelmonitorDataSourceDef.

        In case of datasource to be tabular and your datasource is arranged in the  directory structure of time fashion you can select either of the option yyyy/mm/dd/hh - in case of datsource is arranged in year/month/date/hour format yyyy/mm/dd    - in case of datsource is arranged in year/month/date format yyyy/mm       - in case of datsource is arranged in year/month format \"none\"        - in case data has no arranged fashion  # noqa: E501

        :param date_suffix: The date_suffix of this ModelmonitorDataSourceDef.  # noqa: E501
        :type: str
        """
        allowed_values = ["yyyy/mm/dd/hh", "yyyy/mm/dd", "yyyy/mm", "none"]  # noqa: E501
        if date_suffix not in allowed_values:
            raise ValueError(
                "Invalid value for `date_suffix` ({0}), must be one of {1}"  # noqa: E501
                .format(date_suffix, allowed_values)
            )

        self._date_suffix = date_suffix

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
        if issubclass(ModelmonitorDataSourceDef, dict):
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
        if not isinstance(other, ModelmonitorDataSourceDef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
