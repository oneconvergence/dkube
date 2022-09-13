# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class JobModelParametersGenerated(object):
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
        'deleted': 'bool',
        'archived': 'bool',
        'private': 'str',
        'category': 'str',
        'cicdstatus': 'CICDStatusModel',
        'pipeline': 'JobModelParametersGeneratedPipeline',
        'subclass': 'str',
        'hp_tuning_info': 'str',
        'training_image': 'CustomContainerModel',
        'serving_image': 'CustomContainerModel',
        'scheduled': 'bool',
        'affinity': 'str',
        'user': 'str',
        'jobid': 'str',
        'uuid': 'str',
        'status': 'JobStatusModel',
        'timestamps': 'TimeStamps',
        'runtime': 'TimeStamps',
        'ngpus_alloc': 'int',
        'ngpus_max': 'int',
        'tbref': 'str',
        'studyref': 'str',
        'trialref': 'str',
        'best_trial_id': 'str',
        'best_objective_value': 'float',
        'accelerator': 'str',
        'versions': 'JobModelParametersGeneratedVersions',
        'tracking': 'list[str]',
        'input_datum_refs': 'list[JobModelParametersGeneratedInputDatumRefs]',
        'input_featureset_refs': 'list[JobModelParametersGeneratedInputFeaturesetRefs]',
        'details': 'JobModelParametersGeneratedDetails'
    }

    attribute_map = {
        'deleted': 'deleted',
        'archived': 'archived',
        'private': 'private',
        'category': 'category',
        'cicdstatus': 'cicdstatus',
        'pipeline': 'pipeline',
        'subclass': 'subclass',
        'hp_tuning_info': 'hp_tuning_info',
        'training_image': 'training_image',
        'serving_image': 'serving_image',
        'scheduled': 'scheduled',
        'affinity': 'affinity',
        'user': 'user',
        'jobid': 'jobid',
        'uuid': 'uuid',
        'status': 'status',
        'timestamps': 'timestamps',
        'runtime': 'runtime',
        'ngpus_alloc': 'ngpus_alloc',
        'ngpus_max': 'ngpus_max',
        'tbref': 'tbref',
        'studyref': 'studyref',
        'trialref': 'trialref',
        'best_trial_id': 'best_trial_id',
        'best_objective_value': 'best_objective_value',
        'accelerator': 'accelerator',
        'versions': 'versions',
        'tracking': 'tracking',
        'input_datum_refs': 'inputDatumRefs',
        'input_featureset_refs': 'inputFeaturesetRefs',
        'details': 'details'
    }

    def __init__(self, deleted=False, archived=False, private=None, category=None, cicdstatus=None, pipeline=None, subclass=None, hp_tuning_info=None, training_image=None, serving_image=None, scheduled=None, affinity=None, user=None, jobid=None, uuid=None, status=None, timestamps=None, runtime=None, ngpus_alloc=None, ngpus_max=None, tbref=None, studyref=None, trialref=None, best_trial_id=None, best_objective_value=None, accelerator=None, versions=None, tracking=None, input_datum_refs=None, input_featureset_refs=None, details=None):  # noqa: E501
        """JobModelParametersGenerated - a model defined in Swagger"""  # noqa: E501

        self._deleted = None
        self._archived = None
        self._private = None
        self._category = None
        self._cicdstatus = None
        self._pipeline = None
        self._subclass = None
        self._hp_tuning_info = None
        self._training_image = None
        self._serving_image = None
        self._scheduled = None
        self._affinity = None
        self._user = None
        self._jobid = None
        self._uuid = None
        self._status = None
        self._timestamps = None
        self._runtime = None
        self._ngpus_alloc = None
        self._ngpus_max = None
        self._tbref = None
        self._studyref = None
        self._trialref = None
        self._best_trial_id = None
        self._best_objective_value = None
        self._accelerator = None
        self._versions = None
        self._tracking = None
        self._input_datum_refs = None
        self._input_featureset_refs = None
        self._details = None
        self.discriminator = None

        if deleted is not None:
            self.deleted = deleted
        if archived is not None:
            self.archived = archived
        if private is not None:
            self.private = private
        if category is not None:
            self.category = category
        if cicdstatus is not None:
            self.cicdstatus = cicdstatus
        if pipeline is not None:
            self.pipeline = pipeline
        if subclass is not None:
            self.subclass = subclass
        if hp_tuning_info is not None:
            self.hp_tuning_info = hp_tuning_info
        if training_image is not None:
            self.training_image = training_image
        if serving_image is not None:
            self.serving_image = serving_image
        if scheduled is not None:
            self.scheduled = scheduled
        if affinity is not None:
            self.affinity = affinity
        if user is not None:
            self.user = user
        if jobid is not None:
            self.jobid = jobid
        if uuid is not None:
            self.uuid = uuid
        if status is not None:
            self.status = status
        if timestamps is not None:
            self.timestamps = timestamps
        if runtime is not None:
            self.runtime = runtime
        if ngpus_alloc is not None:
            self.ngpus_alloc = ngpus_alloc
        if ngpus_max is not None:
            self.ngpus_max = ngpus_max
        if tbref is not None:
            self.tbref = tbref
        if studyref is not None:
            self.studyref = studyref
        if trialref is not None:
            self.trialref = trialref
        if best_trial_id is not None:
            self.best_trial_id = best_trial_id
        if best_objective_value is not None:
            self.best_objective_value = best_objective_value
        if accelerator is not None:
            self.accelerator = accelerator
        if versions is not None:
            self.versions = versions
        if tracking is not None:
            self.tracking = tracking
        if input_datum_refs is not None:
            self.input_datum_refs = input_datum_refs
        if input_featureset_refs is not None:
            self.input_featureset_refs = input_featureset_refs
        if details is not None:
            self.details = details

    @property
    def deleted(self):
        """Gets the deleted of this JobModelParametersGenerated.  # noqa: E501


        :return: The deleted of this JobModelParametersGenerated.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this JobModelParametersGenerated.


        :param deleted: The deleted of this JobModelParametersGenerated.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def archived(self):
        """Gets the archived of this JobModelParametersGenerated.  # noqa: E501


        :return: The archived of this JobModelParametersGenerated.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this JobModelParametersGenerated.


        :param archived: The archived of this JobModelParametersGenerated.  # noqa: E501
        :type: bool
        """

        self._archived = archived

    @property
    def private(self):
        """Gets the private of this JobModelParametersGenerated.  # noqa: E501


        :return: The private of this JobModelParametersGenerated.  # noqa: E501
        :rtype: str
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this JobModelParametersGenerated.


        :param private: The private of this JobModelParametersGenerated.  # noqa: E501
        :type: str
        """

        self._private = private

    @property
    def category(self):
        """Gets the category of this JobModelParametersGenerated.  # noqa: E501


        :return: The category of this JobModelParametersGenerated.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this JobModelParametersGenerated.


        :param category: The category of this JobModelParametersGenerated.  # noqa: E501
        :type: str
        """
        allowed_values = ["template", "run"]  # noqa: E501
        if category not in allowed_values:
            raise ValueError(
                "Invalid value for `category` ({0}), must be one of {1}"  # noqa: E501
                .format(category, allowed_values)
            )

        self._category = category

    @property
    def cicdstatus(self):
        """Gets the cicdstatus of this JobModelParametersGenerated.  # noqa: E501


        :return: The cicdstatus of this JobModelParametersGenerated.  # noqa: E501
        :rtype: CICDStatusModel
        """
        return self._cicdstatus

    @cicdstatus.setter
    def cicdstatus(self, cicdstatus):
        """Sets the cicdstatus of this JobModelParametersGenerated.


        :param cicdstatus: The cicdstatus of this JobModelParametersGenerated.  # noqa: E501
        :type: CICDStatusModel
        """

        self._cicdstatus = cicdstatus

    @property
    def pipeline(self):
        """Gets the pipeline of this JobModelParametersGenerated.  # noqa: E501


        :return: The pipeline of this JobModelParametersGenerated.  # noqa: E501
        :rtype: JobModelParametersGeneratedPipeline
        """
        return self._pipeline

    @pipeline.setter
    def pipeline(self, pipeline):
        """Sets the pipeline of this JobModelParametersGenerated.


        :param pipeline: The pipeline of this JobModelParametersGenerated.  # noqa: E501
        :type: JobModelParametersGeneratedPipeline
        """

        self._pipeline = pipeline

    @property
    def subclass(self):
        """Gets the subclass of this JobModelParametersGenerated.  # noqa: E501


        :return: The subclass of this JobModelParametersGenerated.  # noqa: E501
        :rtype: str
        """
        return self._subclass

    @subclass.setter
    def subclass(self, subclass):
        """Sets the subclass of this JobModelParametersGenerated.


        :param subclass: The subclass of this JobModelParametersGenerated.  # noqa: E501
        :type: str
        """
        allowed_values = ["training", "inference", "notebook", "rstudio", "vscode", "study", "studytrial", "dkube", "ssh"]  # noqa: E501
        if subclass not in allowed_values:
            raise ValueError(
                "Invalid value for `subclass` ({0}), must be one of {1}"  # noqa: E501
                .format(subclass, allowed_values)
            )

        self._subclass = subclass

    @property
    def hp_tuning_info(self):
        """Gets the hp_tuning_info of this JobModelParametersGenerated.  # noqa: E501

        Tuning hyperparam json string  # noqa: E501

        :return: The hp_tuning_info of this JobModelParametersGenerated.  # noqa: E501
        :rtype: str
        """
        return self._hp_tuning_info

    @hp_tuning_info.setter
    def hp_tuning_info(self, hp_tuning_info):
        """Sets the hp_tuning_info of this JobModelParametersGenerated.

        Tuning hyperparam json string  # noqa: E501

        :param hp_tuning_info: The hp_tuning_info of this JobModelParametersGenerated.  # noqa: E501
        :type: str
        """

        self._hp_tuning_info = hp_tuning_info

    @property
    def training_image(self):
        """Gets the training_image of this JobModelParametersGenerated.  # noqa: E501


        :return: The training_image of this JobModelParametersGenerated.  # noqa: E501
        :rtype: CustomContainerModel
        """
        return self._training_image

    @training_image.setter
    def training_image(self, training_image):
        """Sets the training_image of this JobModelParametersGenerated.


        :param training_image: The training_image of this JobModelParametersGenerated.  # noqa: E501
        :type: CustomContainerModel
        """

        self._training_image = training_image

    @property
    def serving_image(self):
        """Gets the serving_image of this JobModelParametersGenerated.  # noqa: E501


        :return: The serving_image of this JobModelParametersGenerated.  # noqa: E501
        :rtype: CustomContainerModel
        """
        return self._serving_image

    @serving_image.setter
    def serving_image(self, serving_image):
        """Sets the serving_image of this JobModelParametersGenerated.


        :param serving_image: The serving_image of this JobModelParametersGenerated.  # noqa: E501
        :type: CustomContainerModel
        """

        self._serving_image = serving_image

    @property
    def scheduled(self):
        """Gets the scheduled of this JobModelParametersGenerated.  # noqa: E501

        identifing job scheduled or not  # noqa: E501

        :return: The scheduled of this JobModelParametersGenerated.  # noqa: E501
        :rtype: bool
        """
        return self._scheduled

    @scheduled.setter
    def scheduled(self, scheduled):
        """Sets the scheduled of this JobModelParametersGenerated.

        identifing job scheduled or not  # noqa: E501

        :param scheduled: The scheduled of this JobModelParametersGenerated.  # noqa: E501
        :type: bool
        """

        self._scheduled = scheduled

    @property
    def affinity(self):
        """Gets the affinity of this JobModelParametersGenerated.  # noqa: E501

        Affinity of this job.  # noqa: E501

        :return: The affinity of this JobModelParametersGenerated.  # noqa: E501
        :rtype: str
        """
        return self._affinity

    @affinity.setter
    def affinity(self, affinity):
        """Sets the affinity of this JobModelParametersGenerated.

        Affinity of this job.  # noqa: E501

        :param affinity: The affinity of this JobModelParametersGenerated.  # noqa: E501
        :type: str
        """

        self._affinity = affinity

    @property
    def user(self):
        """Gets the user of this JobModelParametersGenerated.  # noqa: E501

        user to which this job belongs  # noqa: E501

        :return: The user of this JobModelParametersGenerated.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this JobModelParametersGenerated.

        user to which this job belongs  # noqa: E501

        :param user: The user of this JobModelParametersGenerated.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def jobid(self):
        """Gets the jobid of this JobModelParametersGenerated.  # noqa: E501

        6Char alphanumeric ID unique per user  # noqa: E501

        :return: The jobid of this JobModelParametersGenerated.  # noqa: E501
        :rtype: str
        """
        return self._jobid

    @jobid.setter
    def jobid(self, jobid):
        """Sets the jobid of this JobModelParametersGenerated.

        6Char alphanumeric ID unique per user  # noqa: E501

        :param jobid: The jobid of this JobModelParametersGenerated.  # noqa: E501
        :type: str
        """

        self._jobid = jobid

    @property
    def uuid(self):
        """Gets the uuid of this JobModelParametersGenerated.  # noqa: E501


        :return: The uuid of this JobModelParametersGenerated.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this JobModelParametersGenerated.


        :param uuid: The uuid of this JobModelParametersGenerated.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def status(self):
        """Gets the status of this JobModelParametersGenerated.  # noqa: E501


        :return: The status of this JobModelParametersGenerated.  # noqa: E501
        :rtype: JobStatusModel
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this JobModelParametersGenerated.


        :param status: The status of this JobModelParametersGenerated.  # noqa: E501
        :type: JobStatusModel
        """

        self._status = status

    @property
    def timestamps(self):
        """Gets the timestamps of this JobModelParametersGenerated.  # noqa: E501


        :return: The timestamps of this JobModelParametersGenerated.  # noqa: E501
        :rtype: TimeStamps
        """
        return self._timestamps

    @timestamps.setter
    def timestamps(self, timestamps):
        """Sets the timestamps of this JobModelParametersGenerated.


        :param timestamps: The timestamps of this JobModelParametersGenerated.  # noqa: E501
        :type: TimeStamps
        """

        self._timestamps = timestamps

    @property
    def runtime(self):
        """Gets the runtime of this JobModelParametersGenerated.  # noqa: E501


        :return: The runtime of this JobModelParametersGenerated.  # noqa: E501
        :rtype: TimeStamps
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this JobModelParametersGenerated.


        :param runtime: The runtime of this JobModelParametersGenerated.  # noqa: E501
        :type: TimeStamps
        """

        self._runtime = runtime

    @property
    def ngpus_alloc(self):
        """Gets the ngpus_alloc of this JobModelParametersGenerated.  # noqa: E501

        Actual number of gpus allocated to this job, will determined when jobs get to running  # noqa: E501

        :return: The ngpus_alloc of this JobModelParametersGenerated.  # noqa: E501
        :rtype: int
        """
        return self._ngpus_alloc

    @ngpus_alloc.setter
    def ngpus_alloc(self, ngpus_alloc):
        """Sets the ngpus_alloc of this JobModelParametersGenerated.

        Actual number of gpus allocated to this job, will determined when jobs get to running  # noqa: E501

        :param ngpus_alloc: The ngpus_alloc of this JobModelParametersGenerated.  # noqa: E501
        :type: int
        """

        self._ngpus_alloc = ngpus_alloc

    @property
    def ngpus_max(self):
        """Gets the ngpus_max of this JobModelParametersGenerated.  # noqa: E501

        Max number of gpus this job could get allocated with.  # noqa: E501

        :return: The ngpus_max of this JobModelParametersGenerated.  # noqa: E501
        :rtype: int
        """
        return self._ngpus_max

    @ngpus_max.setter
    def ngpus_max(self, ngpus_max):
        """Sets the ngpus_max of this JobModelParametersGenerated.

        Max number of gpus this job could get allocated with.  # noqa: E501

        :param ngpus_max: The ngpus_max of this JobModelParametersGenerated.  # noqa: E501
        :type: int
        """

        self._ngpus_max = ngpus_max

    @property
    def tbref(self):
        """Gets the tbref of this JobModelParametersGenerated.  # noqa: E501

        UUID of TB resouruce  # noqa: E501

        :return: The tbref of this JobModelParametersGenerated.  # noqa: E501
        :rtype: str
        """
        return self._tbref

    @tbref.setter
    def tbref(self, tbref):
        """Sets the tbref of this JobModelParametersGenerated.

        UUID of TB resouruce  # noqa: E501

        :param tbref: The tbref of this JobModelParametersGenerated.  # noqa: E501
        :type: str
        """

        self._tbref = tbref

    @property
    def studyref(self):
        """Gets the studyref of this JobModelParametersGenerated.  # noqa: E501

        Unique id of study job  # noqa: E501

        :return: The studyref of this JobModelParametersGenerated.  # noqa: E501
        :rtype: str
        """
        return self._studyref

    @studyref.setter
    def studyref(self, studyref):
        """Sets the studyref of this JobModelParametersGenerated.

        Unique id of study job  # noqa: E501

        :param studyref: The studyref of this JobModelParametersGenerated.  # noqa: E501
        :type: str
        """

        self._studyref = studyref

    @property
    def trialref(self):
        """Gets the trialref of this JobModelParametersGenerated.  # noqa: E501

        Unique id of a studyjob trial  # noqa: E501

        :return: The trialref of this JobModelParametersGenerated.  # noqa: E501
        :rtype: str
        """
        return self._trialref

    @trialref.setter
    def trialref(self, trialref):
        """Sets the trialref of this JobModelParametersGenerated.

        Unique id of a studyjob trial  # noqa: E501

        :param trialref: The trialref of this JobModelParametersGenerated.  # noqa: E501
        :type: str
        """

        self._trialref = trialref

    @property
    def best_trial_id(self):
        """Gets the best_trial_id of this JobModelParametersGenerated.  # noqa: E501

        Unique id of best studyjob trial  # noqa: E501

        :return: The best_trial_id of this JobModelParametersGenerated.  # noqa: E501
        :rtype: str
        """
        return self._best_trial_id

    @best_trial_id.setter
    def best_trial_id(self, best_trial_id):
        """Sets the best_trial_id of this JobModelParametersGenerated.

        Unique id of best studyjob trial  # noqa: E501

        :param best_trial_id: The best_trial_id of this JobModelParametersGenerated.  # noqa: E501
        :type: str
        """

        self._best_trial_id = best_trial_id

    @property
    def best_objective_value(self):
        """Gets the best_objective_value of this JobModelParametersGenerated.  # noqa: E501

        Objective value of best studyjob trial  # noqa: E501

        :return: The best_objective_value of this JobModelParametersGenerated.  # noqa: E501
        :rtype: float
        """
        return self._best_objective_value

    @best_objective_value.setter
    def best_objective_value(self, best_objective_value):
        """Sets the best_objective_value of this JobModelParametersGenerated.

        Objective value of best studyjob trial  # noqa: E501

        :param best_objective_value: The best_objective_value of this JobModelParametersGenerated.  # noqa: E501
        :type: float
        """

        self._best_objective_value = best_objective_value

    @property
    def accelerator(self):
        """Gets the accelerator of this JobModelParametersGenerated.  # noqa: E501

        Node affinity  # noqa: E501

        :return: The accelerator of this JobModelParametersGenerated.  # noqa: E501
        :rtype: str
        """
        return self._accelerator

    @accelerator.setter
    def accelerator(self, accelerator):
        """Sets the accelerator of this JobModelParametersGenerated.

        Node affinity  # noqa: E501

        :param accelerator: The accelerator of this JobModelParametersGenerated.  # noqa: E501
        :type: str
        """

        self._accelerator = accelerator

    @property
    def versions(self):
        """Gets the versions of this JobModelParametersGenerated.  # noqa: E501


        :return: The versions of this JobModelParametersGenerated.  # noqa: E501
        :rtype: JobModelParametersGeneratedVersions
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this JobModelParametersGenerated.


        :param versions: The versions of this JobModelParametersGenerated.  # noqa: E501
        :type: JobModelParametersGeneratedVersions
        """

        self._versions = versions

    @property
    def tracking(self):
        """Gets the tracking of this JobModelParametersGenerated.  # noqa: E501


        :return: The tracking of this JobModelParametersGenerated.  # noqa: E501
        :rtype: list[str]
        """
        return self._tracking

    @tracking.setter
    def tracking(self, tracking):
        """Sets the tracking of this JobModelParametersGenerated.


        :param tracking: The tracking of this JobModelParametersGenerated.  # noqa: E501
        :type: list[str]
        """

        self._tracking = tracking

    @property
    def input_datum_refs(self):
        """Gets the input_datum_refs of this JobModelParametersGenerated.  # noqa: E501


        :return: The input_datum_refs of this JobModelParametersGenerated.  # noqa: E501
        :rtype: list[JobModelParametersGeneratedInputDatumRefs]
        """
        return self._input_datum_refs

    @input_datum_refs.setter
    def input_datum_refs(self, input_datum_refs):
        """Sets the input_datum_refs of this JobModelParametersGenerated.


        :param input_datum_refs: The input_datum_refs of this JobModelParametersGenerated.  # noqa: E501
        :type: list[JobModelParametersGeneratedInputDatumRefs]
        """

        self._input_datum_refs = input_datum_refs

    @property
    def input_featureset_refs(self):
        """Gets the input_featureset_refs of this JobModelParametersGenerated.  # noqa: E501


        :return: The input_featureset_refs of this JobModelParametersGenerated.  # noqa: E501
        :rtype: list[JobModelParametersGeneratedInputFeaturesetRefs]
        """
        return self._input_featureset_refs

    @input_featureset_refs.setter
    def input_featureset_refs(self, input_featureset_refs):
        """Sets the input_featureset_refs of this JobModelParametersGenerated.


        :param input_featureset_refs: The input_featureset_refs of this JobModelParametersGenerated.  # noqa: E501
        :type: list[JobModelParametersGeneratedInputFeaturesetRefs]
        """

        self._input_featureset_refs = input_featureset_refs

    @property
    def details(self):
        """Gets the details of this JobModelParametersGenerated.  # noqa: E501


        :return: The details of this JobModelParametersGenerated.  # noqa: E501
        :rtype: JobModelParametersGeneratedDetails
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this JobModelParametersGenerated.


        :param details: The details of this JobModelParametersGenerated.  # noqa: E501
        :type: JobModelParametersGeneratedDetails
        """

        self._details = details

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
        if issubclass(JobModelParametersGenerated, dict):
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
        if not isinstance(other, JobModelParametersGenerated):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
