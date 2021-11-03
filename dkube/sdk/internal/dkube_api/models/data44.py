# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0.0.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Data44(object):
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
        'emails': 'str',
        'tags': 'list[str]',
        'endpoint_url': 'str',
        'model': 'str',
        'train_metrics': 'str',
        'description': 'str',
        'schema': 'ModelmonitorFeaturesSpecDef',
        'model_type': 'str',
        'model_category': 'str',
        'model_framework': 'str',
        'default_thresholds': 'list[ModelmonitorDefaultThresholdDef]',
        'drift_detection_run_frequency_hrs': 'int'
    }

    attribute_map = {
        'version': 'version',
        'emails': 'emails',
        'tags': 'tags',
        'endpoint_url': 'endpoint_url',
        'model': 'model',
        'train_metrics': 'train_metrics',
        'description': 'description',
        'schema': 'schema',
        'model_type': 'model_type',
        'model_category': 'model_category',
        'model_framework': 'model_framework',
        'default_thresholds': 'default_thresholds',
        'drift_detection_run_frequency_hrs': 'drift_detection_run_frequency_hrs'
    }

    def __init__(self, version=None, emails=None, tags=None, endpoint_url=None, model=None, train_metrics=None, description=None, schema=None, model_type=None, model_category=None, model_framework=None, default_thresholds=None, drift_detection_run_frequency_hrs=None):  # noqa: E501
        """Data44 - a model defined in Swagger"""  # noqa: E501

        self._version = None
        self._emails = None
        self._tags = None
        self._endpoint_url = None
        self._model = None
        self._train_metrics = None
        self._description = None
        self._schema = None
        self._model_type = None
        self._model_category = None
        self._model_framework = None
        self._default_thresholds = None
        self._drift_detection_run_frequency_hrs = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if emails is not None:
            self.emails = emails
        if tags is not None:
            self.tags = tags
        if endpoint_url is not None:
            self.endpoint_url = endpoint_url
        if model is not None:
            self.model = model
        if train_metrics is not None:
            self.train_metrics = train_metrics
        if description is not None:
            self.description = description
        if schema is not None:
            self.schema = schema
        if model_type is not None:
            self.model_type = model_type
        if model_category is not None:
            self.model_category = model_category
        if model_framework is not None:
            self.model_framework = model_framework
        if default_thresholds is not None:
            self.default_thresholds = default_thresholds
        if drift_detection_run_frequency_hrs is not None:
            self.drift_detection_run_frequency_hrs = drift_detection_run_frequency_hrs

    @property
    def version(self):
        """Gets the version of this Data44.  # noqa: E501

        Model Version  # noqa: E501

        :return: The version of this Data44.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Data44.

        Model Version  # noqa: E501

        :param version: The version of this Data44.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def emails(self):
        """Gets the emails of this Data44.  # noqa: E501

        Comma separated emails  # noqa: E501

        :return: The emails of this Data44.  # noqa: E501
        :rtype: str
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this Data44.

        Comma separated emails  # noqa: E501

        :param emails: The emails of this Data44.  # noqa: E501
        :type: str
        """

        self._emails = emails

    @property
    def tags(self):
        """Gets the tags of this Data44.  # noqa: E501


        :return: The tags of this Data44.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Data44.


        :param tags: The tags of this Data44.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def endpoint_url(self):
        """Gets the endpoint_url of this Data44.  # noqa: E501

        Model Deploymeny URL  # noqa: E501

        :return: The endpoint_url of this Data44.  # noqa: E501
        :rtype: str
        """
        return self._endpoint_url

    @endpoint_url.setter
    def endpoint_url(self, endpoint_url):
        """Sets the endpoint_url of this Data44.

        Model Deploymeny URL  # noqa: E501

        :param endpoint_url: The endpoint_url of this Data44.  # noqa: E501
        :type: str
        """
        if endpoint_url is not None and len(endpoint_url) > 255:
            raise ValueError("Invalid value for `endpoint_url`, length must be less than or equal to `255`")  # noqa: E501
        if endpoint_url is not None and len(endpoint_url) < 1:
            raise ValueError("Invalid value for `endpoint_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._endpoint_url = endpoint_url

    @property
    def model(self):
        """Gets the model of this Data44.  # noqa: E501


        :return: The model of this Data44.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this Data44.


        :param model: The model of this Data44.  # noqa: E501
        :type: str
        """
        if model is not None and len(model) > 255:
            raise ValueError("Invalid value for `model`, length must be less than or equal to `255`")  # noqa: E501
        if model is not None and len(model) < 1:
            raise ValueError("Invalid value for `model`, length must be greater than or equal to `1`")  # noqa: E501

        self._model = model

    @property
    def train_metrics(self):
        """Gets the train_metrics of this Data44.  # noqa: E501

        A JSON string  # noqa: E501

        :return: The train_metrics of this Data44.  # noqa: E501
        :rtype: str
        """
        return self._train_metrics

    @train_metrics.setter
    def train_metrics(self, train_metrics):
        """Sets the train_metrics of this Data44.

        A JSON string  # noqa: E501

        :param train_metrics: The train_metrics of this Data44.  # noqa: E501
        :type: str
        """

        self._train_metrics = train_metrics

    @property
    def description(self):
        """Gets the description of this Data44.  # noqa: E501


        :return: The description of this Data44.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Data44.


        :param description: The description of this Data44.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 255:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501
        if description is not None and len(description) < 1:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def schema(self):
        """Gets the schema of this Data44.  # noqa: E501


        :return: The schema of this Data44.  # noqa: E501
        :rtype: ModelmonitorFeaturesSpecDef
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this Data44.


        :param schema: The schema of this Data44.  # noqa: E501
        :type: ModelmonitorFeaturesSpecDef
        """

        self._schema = schema

    @property
    def model_type(self):
        """Gets the model_type of this Data44.  # noqa: E501

        Model prediction type - regression or classification  # noqa: E501

        :return: The model_type of this Data44.  # noqa: E501
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this Data44.

        Model prediction type - regression or classification  # noqa: E501

        :param model_type: The model_type of this Data44.  # noqa: E501
        :type: str
        """
        allowed_values = ["Regression", "Classification"]  # noqa: E501
        if model_type not in allowed_values:
            raise ValueError(
                "Invalid value for `model_type` ({0}), must be one of {1}"  # noqa: E501
                .format(model_type, allowed_values)
            )

        self._model_type = model_type

    @property
    def model_category(self):
        """Gets the model_category of this Data44.  # noqa: E501

        Model category - TimeSeries, or Other  # noqa: E501

        :return: The model_category of this Data44.  # noqa: E501
        :rtype: str
        """
        return self._model_category

    @model_category.setter
    def model_category(self, model_category):
        """Sets the model_category of this Data44.

        Model category - TimeSeries, or Other  # noqa: E501

        :param model_category: The model_category of this Data44.  # noqa: E501
        :type: str
        """
        allowed_values = ["TimeSeries", "Other"]  # noqa: E501
        if model_category not in allowed_values:
            raise ValueError(
                "Invalid value for `model_category` ({0}), must be one of {1}"  # noqa: E501
                .format(model_category, allowed_values)
            )

        self._model_category = model_category

    @property
    def model_framework(self):
        """Gets the model_framework of this Data44.  # noqa: E501

        Model Framework - TensorFlow-1x or TensorFlow-2x or PyTorch or SkLearn or Other  # noqa: E501

        :return: The model_framework of this Data44.  # noqa: E501
        :rtype: str
        """
        return self._model_framework

    @model_framework.setter
    def model_framework(self, model_framework):
        """Sets the model_framework of this Data44.

        Model Framework - TensorFlow-1x or TensorFlow-2x or PyTorch or SkLearn or Other  # noqa: E501

        :param model_framework: The model_framework of this Data44.  # noqa: E501
        :type: str
        """
        allowed_values = ["Tensorflow-1x", "Tensorflow-2x", "PyTorch", "SkLearn", "Other"]  # noqa: E501
        if model_framework not in allowed_values:
            raise ValueError(
                "Invalid value for `model_framework` ({0}), must be one of {1}"  # noqa: E501
                .format(model_framework, allowed_values)
            )

        self._model_framework = model_framework

    @property
    def default_thresholds(self):
        """Gets the default_thresholds of this Data44.  # noqa: E501

        model monitor default thresholds  # noqa: E501

        :return: The default_thresholds of this Data44.  # noqa: E501
        :rtype: list[ModelmonitorDefaultThresholdDef]
        """
        return self._default_thresholds

    @default_thresholds.setter
    def default_thresholds(self, default_thresholds):
        """Sets the default_thresholds of this Data44.

        model monitor default thresholds  # noqa: E501

        :param default_thresholds: The default_thresholds of this Data44.  # noqa: E501
        :type: list[ModelmonitorDefaultThresholdDef]
        """

        self._default_thresholds = default_thresholds

    @property
    def drift_detection_run_frequency_hrs(self):
        """Gets the drift_detection_run_frequency_hrs of this Data44.  # noqa: E501

        monitor frequency in hours  # noqa: E501

        :return: The drift_detection_run_frequency_hrs of this Data44.  # noqa: E501
        :rtype: int
        """
        return self._drift_detection_run_frequency_hrs

    @drift_detection_run_frequency_hrs.setter
    def drift_detection_run_frequency_hrs(self, drift_detection_run_frequency_hrs):
        """Sets the drift_detection_run_frequency_hrs of this Data44.

        monitor frequency in hours  # noqa: E501

        :param drift_detection_run_frequency_hrs: The drift_detection_run_frequency_hrs of this Data44.  # noqa: E501
        :type: int
        """
        if drift_detection_run_frequency_hrs is not None and drift_detection_run_frequency_hrs > 168:  # noqa: E501
            raise ValueError("Invalid value for `drift_detection_run_frequency_hrs`, must be a value less than or equal to `168`")  # noqa: E501
        if drift_detection_run_frequency_hrs is not None and drift_detection_run_frequency_hrs < 1:  # noqa: E501
            raise ValueError("Invalid value for `drift_detection_run_frequency_hrs`, must be a value greater than or equal to `1`")  # noqa: E501

        self._drift_detection_run_frequency_hrs = drift_detection_run_frequency_hrs

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
        if issubclass(Data44, dict):
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
        if not isinstance(other, Data44):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
