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


class ModelmonitorDef(object):
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
        'status': 'ModelmonitorStatusDef',
        'schema': 'ModelmonitorFeaturesSpecDef',
        'pipeline_component': 'ModelmonitorComponentDef',
        'owner': 'str',
        'emails': 'str',
        'name': 'str',
        'description': 'str',
        'tags': 'list[str]',
        'train_metrics': 'str',
        'model': 'str',
        'version': 'str',
        'endpoint_url': 'str',
        'model_type': 'str',
        'model_category': 'str',
        'model_framework': 'str',
        'drift_detection_run_frequency_hrs': 'int',
        'drift_detection_algorithm': 'str',
        'performance_metrics_template': 'str',
        'default_thresholds': 'list[ModelmonitorDefaultThresholdDef]',
        'datasets': 'list[ModelmonitorDatasetDef]',
        'created_at': 'str',
        'updated_at': 'str',
        'alerts': 'list[ModelmonitorAlertDef]'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'schema': 'schema',
        'pipeline_component': 'pipeline_component',
        'owner': 'owner',
        'emails': 'emails',
        'name': 'name',
        'description': 'description',
        'tags': 'tags',
        'train_metrics': 'train_metrics',
        'model': 'model',
        'version': 'version',
        'endpoint_url': 'endpoint_url',
        'model_type': 'model_type',
        'model_category': 'model_category',
        'model_framework': 'model_framework',
        'drift_detection_run_frequency_hrs': 'drift_detection_run_frequency_hrs',
        'drift_detection_algorithm': 'drift_detection_algorithm',
        'performance_metrics_template': 'performance_metrics_template',
        'default_thresholds': 'default_thresholds',
        'datasets': 'datasets',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'alerts': 'alerts'
    }

    def __init__(self, id=None, status=None, schema=None, pipeline_component=None, owner=None, emails=None, name=None, description=None, tags=None, train_metrics=None, model=None, version=None, endpoint_url=None, model_type=None, model_category=None, model_framework=None, drift_detection_run_frequency_hrs=None, drift_detection_algorithm='Auto', performance_metrics_template=None, default_thresholds=None, datasets=None, created_at=None, updated_at=None, alerts=None):  # noqa: E501
        """ModelmonitorDef - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._status = None
        self._schema = None
        self._pipeline_component = None
        self._owner = None
        self._emails = None
        self._name = None
        self._description = None
        self._tags = None
        self._train_metrics = None
        self._model = None
        self._version = None
        self._endpoint_url = None
        self._model_type = None
        self._model_category = None
        self._model_framework = None
        self._drift_detection_run_frequency_hrs = None
        self._drift_detection_algorithm = None
        self._performance_metrics_template = None
        self._default_thresholds = None
        self._datasets = None
        self._created_at = None
        self._updated_at = None
        self._alerts = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if schema is not None:
            self.schema = schema
        if pipeline_component is not None:
            self.pipeline_component = pipeline_component
        if owner is not None:
            self.owner = owner
        if emails is not None:
            self.emails = emails
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if train_metrics is not None:
            self.train_metrics = train_metrics
        if model is not None:
            self.model = model
        if version is not None:
            self.version = version
        if endpoint_url is not None:
            self.endpoint_url = endpoint_url
        if model_type is not None:
            self.model_type = model_type
        if model_category is not None:
            self.model_category = model_category
        if model_framework is not None:
            self.model_framework = model_framework
        if drift_detection_run_frequency_hrs is not None:
            self.drift_detection_run_frequency_hrs = drift_detection_run_frequency_hrs
        if drift_detection_algorithm is not None:
            self.drift_detection_algorithm = drift_detection_algorithm
        if performance_metrics_template is not None:
            self.performance_metrics_template = performance_metrics_template
        if default_thresholds is not None:
            self.default_thresholds = default_thresholds
        if datasets is not None:
            self.datasets = datasets
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if alerts is not None:
            self.alerts = alerts

    @property
    def id(self):
        """Gets the id of this ModelmonitorDef.  # noqa: E501

        UUID4 id for the resource  # noqa: E501

        :return: The id of this ModelmonitorDef.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelmonitorDef.

        UUID4 id for the resource  # noqa: E501

        :param id: The id of this ModelmonitorDef.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def status(self):
        """Gets the status of this ModelmonitorDef.  # noqa: E501


        :return: The status of this ModelmonitorDef.  # noqa: E501
        :rtype: ModelmonitorStatusDef
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ModelmonitorDef.


        :param status: The status of this ModelmonitorDef.  # noqa: E501
        :type: ModelmonitorStatusDef
        """

        self._status = status

    @property
    def schema(self):
        """Gets the schema of this ModelmonitorDef.  # noqa: E501


        :return: The schema of this ModelmonitorDef.  # noqa: E501
        :rtype: ModelmonitorFeaturesSpecDef
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this ModelmonitorDef.


        :param schema: The schema of this ModelmonitorDef.  # noqa: E501
        :type: ModelmonitorFeaturesSpecDef
        """

        self._schema = schema

    @property
    def pipeline_component(self):
        """Gets the pipeline_component of this ModelmonitorDef.  # noqa: E501


        :return: The pipeline_component of this ModelmonitorDef.  # noqa: E501
        :rtype: ModelmonitorComponentDef
        """
        return self._pipeline_component

    @pipeline_component.setter
    def pipeline_component(self, pipeline_component):
        """Sets the pipeline_component of this ModelmonitorDef.


        :param pipeline_component: The pipeline_component of this ModelmonitorDef.  # noqa: E501
        :type: ModelmonitorComponentDef
        """

        self._pipeline_component = pipeline_component

    @property
    def owner(self):
        """Gets the owner of this ModelmonitorDef.  # noqa: E501

        owner name of modelmonitor  # noqa: E501

        :return: The owner of this ModelmonitorDef.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ModelmonitorDef.

        owner name of modelmonitor  # noqa: E501

        :param owner: The owner of this ModelmonitorDef.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def emails(self):
        """Gets the emails of this ModelmonitorDef.  # noqa: E501

        Comman separated emails  # noqa: E501

        :return: The emails of this ModelmonitorDef.  # noqa: E501
        :rtype: str
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this ModelmonitorDef.

        Comman separated emails  # noqa: E501

        :param emails: The emails of this ModelmonitorDef.  # noqa: E501
        :type: str
        """

        self._emails = emails

    @property
    def name(self):
        """Gets the name of this ModelmonitorDef.  # noqa: E501


        :return: The name of this ModelmonitorDef.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelmonitorDef.


        :param name: The name of this ModelmonitorDef.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this ModelmonitorDef.  # noqa: E501


        :return: The description of this ModelmonitorDef.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModelmonitorDef.


        :param description: The description of this ModelmonitorDef.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 255:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501
        if description is not None and len(description) < 1:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this ModelmonitorDef.  # noqa: E501


        :return: The tags of this ModelmonitorDef.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ModelmonitorDef.


        :param tags: The tags of this ModelmonitorDef.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def train_metrics(self):
        """Gets the train_metrics of this ModelmonitorDef.  # noqa: E501

        JSON string  # noqa: E501

        :return: The train_metrics of this ModelmonitorDef.  # noqa: E501
        :rtype: str
        """
        return self._train_metrics

    @train_metrics.setter
    def train_metrics(self, train_metrics):
        """Sets the train_metrics of this ModelmonitorDef.

        JSON string  # noqa: E501

        :param train_metrics: The train_metrics of this ModelmonitorDef.  # noqa: E501
        :type: str
        """

        self._train_metrics = train_metrics

    @property
    def model(self):
        """Gets the model of this ModelmonitorDef.  # noqa: E501


        :return: The model of this ModelmonitorDef.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this ModelmonitorDef.


        :param model: The model of this ModelmonitorDef.  # noqa: E501
        :type: str
        """
        if model is not None and len(model) > 255:
            raise ValueError("Invalid value for `model`, length must be less than or equal to `255`")  # noqa: E501
        if model is not None and len(model) < 1:
            raise ValueError("Invalid value for `model`, length must be greater than or equal to `1`")  # noqa: E501

        self._model = model

    @property
    def version(self):
        """Gets the version of this ModelmonitorDef.  # noqa: E501


        :return: The version of this ModelmonitorDef.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ModelmonitorDef.


        :param version: The version of this ModelmonitorDef.  # noqa: E501
        :type: str
        """
        if version is not None and len(version) > 255:
            raise ValueError("Invalid value for `version`, length must be less than or equal to `255`")  # noqa: E501
        if version is not None and len(version) < 1:
            raise ValueError("Invalid value for `version`, length must be greater than or equal to `1`")  # noqa: E501

        self._version = version

    @property
    def endpoint_url(self):
        """Gets the endpoint_url of this ModelmonitorDef.  # noqa: E501


        :return: The endpoint_url of this ModelmonitorDef.  # noqa: E501
        :rtype: str
        """
        return self._endpoint_url

    @endpoint_url.setter
    def endpoint_url(self, endpoint_url):
        """Sets the endpoint_url of this ModelmonitorDef.


        :param endpoint_url: The endpoint_url of this ModelmonitorDef.  # noqa: E501
        :type: str
        """
        if endpoint_url is not None and len(endpoint_url) > 255:
            raise ValueError("Invalid value for `endpoint_url`, length must be less than or equal to `255`")  # noqa: E501
        if endpoint_url is not None and len(endpoint_url) < 1:
            raise ValueError("Invalid value for `endpoint_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._endpoint_url = endpoint_url

    @property
    def model_type(self):
        """Gets the model_type of this ModelmonitorDef.  # noqa: E501

        Model prediction type - regression or classification  # noqa: E501

        :return: The model_type of this ModelmonitorDef.  # noqa: E501
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this ModelmonitorDef.

        Model prediction type - regression or classification  # noqa: E501

        :param model_type: The model_type of this ModelmonitorDef.  # noqa: E501
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
        """Gets the model_category of this ModelmonitorDef.  # noqa: E501

        Model category - AutoEncoder, TimeSeries, or Other  # noqa: E501

        :return: The model_category of this ModelmonitorDef.  # noqa: E501
        :rtype: str
        """
        return self._model_category

    @model_category.setter
    def model_category(self, model_category):
        """Sets the model_category of this ModelmonitorDef.

        Model category - AutoEncoder, TimeSeries, or Other  # noqa: E501

        :param model_category: The model_category of this ModelmonitorDef.  # noqa: E501
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
        """Gets the model_framework of this ModelmonitorDef.  # noqa: E501

        Model Framework - TensorFlow-1x or TensorFlow-2x or PyTorch or SkLearn or Other  # noqa: E501

        :return: The model_framework of this ModelmonitorDef.  # noqa: E501
        :rtype: str
        """
        return self._model_framework

    @model_framework.setter
    def model_framework(self, model_framework):
        """Sets the model_framework of this ModelmonitorDef.

        Model Framework - TensorFlow-1x or TensorFlow-2x or PyTorch or SkLearn or Other  # noqa: E501

        :param model_framework: The model_framework of this ModelmonitorDef.  # noqa: E501
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
    def drift_detection_run_frequency_hrs(self):
        """Gets the drift_detection_run_frequency_hrs of this ModelmonitorDef.  # noqa: E501

        monitor frequency in hours  # noqa: E501

        :return: The drift_detection_run_frequency_hrs of this ModelmonitorDef.  # noqa: E501
        :rtype: int
        """
        return self._drift_detection_run_frequency_hrs

    @drift_detection_run_frequency_hrs.setter
    def drift_detection_run_frequency_hrs(self, drift_detection_run_frequency_hrs):
        """Sets the drift_detection_run_frequency_hrs of this ModelmonitorDef.

        monitor frequency in hours  # noqa: E501

        :param drift_detection_run_frequency_hrs: The drift_detection_run_frequency_hrs of this ModelmonitorDef.  # noqa: E501
        :type: int
        """
        if drift_detection_run_frequency_hrs is not None and drift_detection_run_frequency_hrs > 168:  # noqa: E501
            raise ValueError("Invalid value for `drift_detection_run_frequency_hrs`, must be a value less than or equal to `168`")  # noqa: E501
        if drift_detection_run_frequency_hrs is not None and drift_detection_run_frequency_hrs < 1:  # noqa: E501
            raise ValueError("Invalid value for `drift_detection_run_frequency_hrs`, must be a value greater than or equal to `1`")  # noqa: E501

        self._drift_detection_run_frequency_hrs = drift_detection_run_frequency_hrs

    @property
    def drift_detection_algorithm(self):
        """Gets the drift_detection_algorithm of this ModelmonitorDef.  # noqa: E501


        :return: The drift_detection_algorithm of this ModelmonitorDef.  # noqa: E501
        :rtype: str
        """
        return self._drift_detection_algorithm

    @drift_detection_algorithm.setter
    def drift_detection_algorithm(self, drift_detection_algorithm):
        """Sets the drift_detection_algorithm of this ModelmonitorDef.


        :param drift_detection_algorithm: The drift_detection_algorithm of this ModelmonitorDef.  # noqa: E501
        :type: str
        """
        allowed_values = ["Auto", "Kolmogorov-Smirnov", "Chi Squared", "Kolmogorov-Smirnov & Chi Squared"]  # noqa: E501
        if drift_detection_algorithm not in allowed_values:
            raise ValueError(
                "Invalid value for `drift_detection_algorithm` ({0}), must be one of {1}"  # noqa: E501
                .format(drift_detection_algorithm, allowed_values)
            )

        self._drift_detection_algorithm = drift_detection_algorithm

    @property
    def performance_metrics_template(self):
        """Gets the performance_metrics_template of this ModelmonitorDef.  # noqa: E501

        Choose the template for the Performance Metrics, which will be used to report model performance decay.  # noqa: E501

        :return: The performance_metrics_template of this ModelmonitorDef.  # noqa: E501
        :rtype: str
        """
        return self._performance_metrics_template

    @performance_metrics_template.setter
    def performance_metrics_template(self, performance_metrics_template):
        """Sets the performance_metrics_template of this ModelmonitorDef.

        Choose the template for the Performance Metrics, which will be used to report model performance decay.  # noqa: E501

        :param performance_metrics_template: The performance_metrics_template of this ModelmonitorDef.  # noqa: E501
        :type: str
        """
        if performance_metrics_template is not None and len(performance_metrics_template) > 255:
            raise ValueError("Invalid value for `performance_metrics_template`, length must be less than or equal to `255`")  # noqa: E501
        if performance_metrics_template is not None and len(performance_metrics_template) < 1:
            raise ValueError("Invalid value for `performance_metrics_template`, length must be greater than or equal to `1`")  # noqa: E501

        self._performance_metrics_template = performance_metrics_template

    @property
    def default_thresholds(self):
        """Gets the default_thresholds of this ModelmonitorDef.  # noqa: E501

        model monitor default thresholds  # noqa: E501

        :return: The default_thresholds of this ModelmonitorDef.  # noqa: E501
        :rtype: list[ModelmonitorDefaultThresholdDef]
        """
        return self._default_thresholds

    @default_thresholds.setter
    def default_thresholds(self, default_thresholds):
        """Sets the default_thresholds of this ModelmonitorDef.

        model monitor default thresholds  # noqa: E501

        :param default_thresholds: The default_thresholds of this ModelmonitorDef.  # noqa: E501
        :type: list[ModelmonitorDefaultThresholdDef]
        """

        self._default_thresholds = default_thresholds

    @property
    def datasets(self):
        """Gets the datasets of this ModelmonitorDef.  # noqa: E501

        model monitor datasets  # noqa: E501

        :return: The datasets of this ModelmonitorDef.  # noqa: E501
        :rtype: list[ModelmonitorDatasetDef]
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets):
        """Sets the datasets of this ModelmonitorDef.

        model monitor datasets  # noqa: E501

        :param datasets: The datasets of this ModelmonitorDef.  # noqa: E501
        :type: list[ModelmonitorDatasetDef]
        """

        self._datasets = datasets

    @property
    def created_at(self):
        """Gets the created_at of this ModelmonitorDef.  # noqa: E501


        :return: The created_at of this ModelmonitorDef.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ModelmonitorDef.


        :param created_at: The created_at of this ModelmonitorDef.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ModelmonitorDef.  # noqa: E501


        :return: The updated_at of this ModelmonitorDef.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ModelmonitorDef.


        :param updated_at: The updated_at of this ModelmonitorDef.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def alerts(self):
        """Gets the alerts of this ModelmonitorDef.  # noqa: E501

        model monitor alerts  # noqa: E501

        :return: The alerts of this ModelmonitorDef.  # noqa: E501
        :rtype: list[ModelmonitorAlertDef]
        """
        return self._alerts

    @alerts.setter
    def alerts(self, alerts):
        """Sets the alerts of this ModelmonitorDef.

        model monitor alerts  # noqa: E501

        :param alerts: The alerts of this ModelmonitorDef.  # noqa: E501
        :type: list[ModelmonitorAlertDef]
        """

        self._alerts = alerts

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
        if issubclass(ModelmonitorDef, dict):
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
        if not isinstance(other, ModelmonitorDef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
