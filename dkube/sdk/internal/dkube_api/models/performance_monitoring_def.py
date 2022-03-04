# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.3.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PerformanceMonitoringDef(object):
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
        'enabled': 'bool',
        'frequency': 'int',
        'row_id': 'str',
        'prediction_timestamp_col_name': 'str',
        'source_type': 'str',
        'docker_image': 'str',
        'startup_script': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'frequency': 'frequency',
        'row_id': 'row_id',
        'prediction_timestamp_col_name': 'prediction_timestamp_col_name',
        'source_type': 'source_type',
        'docker_image': 'docker_image',
        'startup_script': 'startup_script'
    }

    def __init__(self, enabled=None, frequency=None, row_id=None, prediction_timestamp_col_name=None, source_type=None, docker_image=None, startup_script=None):  # noqa: E501
        """PerformanceMonitoringDef - a model defined in Swagger"""  # noqa: E501

        self._enabled = None
        self._frequency = None
        self._row_id = None
        self._prediction_timestamp_col_name = None
        self._source_type = None
        self._docker_image = None
        self._startup_script = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if frequency is not None:
            self.frequency = frequency
        if row_id is not None:
            self.row_id = row_id
        if prediction_timestamp_col_name is not None:
            self.prediction_timestamp_col_name = prediction_timestamp_col_name
        if source_type is not None:
            self.source_type = source_type
        if docker_image is not None:
            self.docker_image = docker_image
        if startup_script is not None:
            self.startup_script = startup_script

    @property
    def enabled(self):
        """Gets the enabled of this PerformanceMonitoringDef.  # noqa: E501


        :return: The enabled of this PerformanceMonitoringDef.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this PerformanceMonitoringDef.


        :param enabled: The enabled of this PerformanceMonitoringDef.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def frequency(self):
        """Gets the frequency of this PerformanceMonitoringDef.  # noqa: E501

        frequency in minutes, minimum 5 minutes  # noqa: E501

        :return: The frequency of this PerformanceMonitoringDef.  # noqa: E501
        :rtype: int
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this PerformanceMonitoringDef.

        frequency in minutes, minimum 5 minutes  # noqa: E501

        :param frequency: The frequency of this PerformanceMonitoringDef.  # noqa: E501
        :type: int
        """

        self._frequency = frequency

    @property
    def row_id(self):
        """Gets the row_id of this PerformanceMonitoringDef.  # noqa: E501

        required in case of modelmonitor.input_data_type is image  # noqa: E501

        :return: The row_id of this PerformanceMonitoringDef.  # noqa: E501
        :rtype: str
        """
        return self._row_id

    @row_id.setter
    def row_id(self, row_id):
        """Sets the row_id of this PerformanceMonitoringDef.

        required in case of modelmonitor.input_data_type is image  # noqa: E501

        :param row_id: The row_id of this PerformanceMonitoringDef.  # noqa: E501
        :type: str
        """

        self._row_id = row_id

    @property
    def prediction_timestamp_col_name(self):
        """Gets the prediction_timestamp_col_name of this PerformanceMonitoringDef.  # noqa: E501


        :return: The prediction_timestamp_col_name of this PerformanceMonitoringDef.  # noqa: E501
        :rtype: str
        """
        return self._prediction_timestamp_col_name

    @prediction_timestamp_col_name.setter
    def prediction_timestamp_col_name(self, prediction_timestamp_col_name):
        """Sets the prediction_timestamp_col_name of this PerformanceMonitoringDef.


        :param prediction_timestamp_col_name: The prediction_timestamp_col_name of this PerformanceMonitoringDef.  # noqa: E501
        :type: str
        """

        self._prediction_timestamp_col_name = prediction_timestamp_col_name

    @property
    def source_type(self):
        """Gets the source_type of this PerformanceMonitoringDef.  # noqa: E501


        :return: The source_type of this PerformanceMonitoringDef.  # noqa: E501
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this PerformanceMonitoringDef.


        :param source_type: The source_type of this PerformanceMonitoringDef.  # noqa: E501
        :type: str
        """
        allowed_values = ["labelled_data", "metrics", "custom"]  # noqa: E501
        if source_type not in allowed_values:
            raise ValueError(
                "Invalid value for `source_type` ({0}), must be one of {1}"  # noqa: E501
                .format(source_type, allowed_values)
            )

        self._source_type = source_type

    @property
    def docker_image(self):
        """Gets the docker_image of this PerformanceMonitoringDef.  # noqa: E501


        :return: The docker_image of this PerformanceMonitoringDef.  # noqa: E501
        :rtype: str
        """
        return self._docker_image

    @docker_image.setter
    def docker_image(self, docker_image):
        """Sets the docker_image of this PerformanceMonitoringDef.


        :param docker_image: The docker_image of this PerformanceMonitoringDef.  # noqa: E501
        :type: str
        """

        self._docker_image = docker_image

    @property
    def startup_script(self):
        """Gets the startup_script of this PerformanceMonitoringDef.  # noqa: E501


        :return: The startup_script of this PerformanceMonitoringDef.  # noqa: E501
        :rtype: str
        """
        return self._startup_script

    @startup_script.setter
    def startup_script(self, startup_script):
        """Sets the startup_script of this PerformanceMonitoringDef.


        :param startup_script: The startup_script of this PerformanceMonitoringDef.  # noqa: E501
        :type: str
        """

        self._startup_script = startup_script

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
        if issubclass(PerformanceMonitoringDef, dict):
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
        if not isinstance(other, PerformanceMonitoringDef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
