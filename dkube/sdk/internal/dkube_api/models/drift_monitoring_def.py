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


class DriftMonitoringDef(object):
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
        'image_train_data_savedfile_format': 'str',
        'image_predict_data_savedfile_format': 'str',
        'algorithm': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'frequency': 'frequency',
        'image_train_data_savedfile_format': 'image_train_data_savedfile_format',
        'image_predict_data_savedfile_format': 'image_predict_data_savedfile_format',
        'algorithm': 'algorithm'
    }

    def __init__(self, enabled=None, frequency=None, image_train_data_savedfile_format=None, image_predict_data_savedfile_format=None, algorithm=None):  # noqa: E501
        """DriftMonitoringDef - a model defined in Swagger"""  # noqa: E501

        self._enabled = None
        self._frequency = None
        self._image_train_data_savedfile_format = None
        self._image_predict_data_savedfile_format = None
        self._algorithm = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if frequency is not None:
            self.frequency = frequency
        if image_train_data_savedfile_format is not None:
            self.image_train_data_savedfile_format = image_train_data_savedfile_format
        if image_predict_data_savedfile_format is not None:
            self.image_predict_data_savedfile_format = image_predict_data_savedfile_format
        if algorithm is not None:
            self.algorithm = algorithm

    @property
    def enabled(self):
        """Gets the enabled of this DriftMonitoringDef.  # noqa: E501


        :return: The enabled of this DriftMonitoringDef.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this DriftMonitoringDef.


        :param enabled: The enabled of this DriftMonitoringDef.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def frequency(self):
        """Gets the frequency of this DriftMonitoringDef.  # noqa: E501

        frequency in minutes, minimum 5 minutes  # noqa: E501

        :return: The frequency of this DriftMonitoringDef.  # noqa: E501
        :rtype: int
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this DriftMonitoringDef.

        frequency in minutes, minimum 5 minutes  # noqa: E501

        :param frequency: The frequency of this DriftMonitoringDef.  # noqa: E501
        :type: int
        """

        self._frequency = frequency

    @property
    def image_train_data_savedfile_format(self):
        """Gets the image_train_data_savedfile_format of this DriftMonitoringDef.  # noqa: E501

        Describe how the train datasource is organized - bin_numpy_array             : binary numpy array - img_files_labels_csv        : image files, and labels in csv - images_in_labelled_folder   : directory name same as labels  # noqa: E501

        :return: The image_train_data_savedfile_format of this DriftMonitoringDef.  # noqa: E501
        :rtype: str
        """
        return self._image_train_data_savedfile_format

    @image_train_data_savedfile_format.setter
    def image_train_data_savedfile_format(self, image_train_data_savedfile_format):
        """Sets the image_train_data_savedfile_format of this DriftMonitoringDef.

        Describe how the train datasource is organized - bin_numpy_array             : binary numpy array - img_files_labels_csv        : image files, and labels in csv - images_in_labelled_folder   : directory name same as labels  # noqa: E501

        :param image_train_data_savedfile_format: The image_train_data_savedfile_format of this DriftMonitoringDef.  # noqa: E501
        :type: str
        """
        allowed_values = ["bin_numpy_array", "img_files_labels_csv", "images_in_labelled_folder"]  # noqa: E501
        if image_train_data_savedfile_format not in allowed_values:
            raise ValueError(
                "Invalid value for `image_train_data_savedfile_format` ({0}), must be one of {1}"  # noqa: E501
                .format(image_train_data_savedfile_format, allowed_values)
            )

        self._image_train_data_savedfile_format = image_train_data_savedfile_format

    @property
    def image_predict_data_savedfile_format(self):
        """Gets the image_predict_data_savedfile_format of this DriftMonitoringDef.  # noqa: E501

        Describe how the predict datasource is organized - bin_numpy_array             : binary numpy array - img_files_labels_csv        : image files, and labels in csv - images_in_labelled_folder   : directory name same as labels  # noqa: E501

        :return: The image_predict_data_savedfile_format of this DriftMonitoringDef.  # noqa: E501
        :rtype: str
        """
        return self._image_predict_data_savedfile_format

    @image_predict_data_savedfile_format.setter
    def image_predict_data_savedfile_format(self, image_predict_data_savedfile_format):
        """Sets the image_predict_data_savedfile_format of this DriftMonitoringDef.

        Describe how the predict datasource is organized - bin_numpy_array             : binary numpy array - img_files_labels_csv        : image files, and labels in csv - images_in_labelled_folder   : directory name same as labels  # noqa: E501

        :param image_predict_data_savedfile_format: The image_predict_data_savedfile_format of this DriftMonitoringDef.  # noqa: E501
        :type: str
        """
        allowed_values = ["bin_numpy_array", "img_files_labels_csv", "images_in_labelled_folder"]  # noqa: E501
        if image_predict_data_savedfile_format not in allowed_values:
            raise ValueError(
                "Invalid value for `image_predict_data_savedfile_format` ({0}), must be one of {1}"  # noqa: E501
                .format(image_predict_data_savedfile_format, allowed_values)
            )

        self._image_predict_data_savedfile_format = image_predict_data_savedfile_format

    @property
    def algorithm(self):
        """Gets the algorithm of this DriftMonitoringDef.  # noqa: E501


        :return: The algorithm of this DriftMonitoringDef.  # noqa: E501
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """Sets the algorithm of this DriftMonitoringDef.


        :param algorithm: The algorithm of this DriftMonitoringDef.  # noqa: E501
        :type: str
        """
        allowed_values = ["auto", "kolmogorov-smirnov", "chi squared", "kolmogorov-smirnov & chi squared"]  # noqa: E501
        if algorithm not in allowed_values:
            raise ValueError(
                "Invalid value for `algorithm` ({0}), must be one of {1}"  # noqa: E501
                .format(algorithm, allowed_values)
            )

        self._algorithm = algorithm

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
        if issubclass(DriftMonitoringDef, dict):
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
        if not isinstance(other, DriftMonitoringDef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
