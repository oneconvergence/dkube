# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.5.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DkubeInfoLicense(object):
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
        'start_date': 'str',
        'end_date': 'str',
        'validity': 'int',
        'licensee': 'str',
        'gen_time': 'str',
        'expired': 'bool',
        'quota': 'int',
        'grace_period': 'int',
        'onboarded_user_count': 'int',
        'uuid': 'str'
    }

    attribute_map = {
        'start_date': 'startDate',
        'end_date': 'endDate',
        'validity': 'validity',
        'licensee': 'licensee',
        'gen_time': 'genTime',
        'expired': 'expired',
        'quota': 'quota',
        'grace_period': 'gracePeriod',
        'onboarded_user_count': 'onboardedUserCount',
        'uuid': 'uuid'
    }

    def __init__(self, start_date=None, end_date=None, validity=None, licensee=None, gen_time=None, expired=False, quota=None, grace_period=None, onboarded_user_count=None, uuid=None):  # noqa: E501
        """DkubeInfoLicense - a model defined in Swagger"""  # noqa: E501

        self._start_date = None
        self._end_date = None
        self._validity = None
        self._licensee = None
        self._gen_time = None
        self._expired = None
        self._quota = None
        self._grace_period = None
        self._onboarded_user_count = None
        self._uuid = None
        self.discriminator = None

        self.start_date = start_date
        self.end_date = end_date
        self.validity = validity
        self.licensee = licensee
        self.gen_time = gen_time
        self.expired = expired
        self.quota = quota
        self.grace_period = grace_period
        self.onboarded_user_count = onboarded_user_count
        self.uuid = uuid

    @property
    def start_date(self):
        """Gets the start_date of this DkubeInfoLicense.  # noqa: E501


        :return: The start_date of this DkubeInfoLicense.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this DkubeInfoLicense.


        :param start_date: The start_date of this DkubeInfoLicense.  # noqa: E501
        :type: str
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this DkubeInfoLicense.  # noqa: E501


        :return: The end_date of this DkubeInfoLicense.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this DkubeInfoLicense.


        :param end_date: The end_date of this DkubeInfoLicense.  # noqa: E501
        :type: str
        """
        if end_date is None:
            raise ValueError("Invalid value for `end_date`, must not be `None`")  # noqa: E501

        self._end_date = end_date

    @property
    def validity(self):
        """Gets the validity of this DkubeInfoLicense.  # noqa: E501


        :return: The validity of this DkubeInfoLicense.  # noqa: E501
        :rtype: int
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """Sets the validity of this DkubeInfoLicense.


        :param validity: The validity of this DkubeInfoLicense.  # noqa: E501
        :type: int
        """
        if validity is None:
            raise ValueError("Invalid value for `validity`, must not be `None`")  # noqa: E501

        self._validity = validity

    @property
    def licensee(self):
        """Gets the licensee of this DkubeInfoLicense.  # noqa: E501


        :return: The licensee of this DkubeInfoLicense.  # noqa: E501
        :rtype: str
        """
        return self._licensee

    @licensee.setter
    def licensee(self, licensee):
        """Sets the licensee of this DkubeInfoLicense.


        :param licensee: The licensee of this DkubeInfoLicense.  # noqa: E501
        :type: str
        """
        if licensee is None:
            raise ValueError("Invalid value for `licensee`, must not be `None`")  # noqa: E501

        self._licensee = licensee

    @property
    def gen_time(self):
        """Gets the gen_time of this DkubeInfoLicense.  # noqa: E501


        :return: The gen_time of this DkubeInfoLicense.  # noqa: E501
        :rtype: str
        """
        return self._gen_time

    @gen_time.setter
    def gen_time(self, gen_time):
        """Sets the gen_time of this DkubeInfoLicense.


        :param gen_time: The gen_time of this DkubeInfoLicense.  # noqa: E501
        :type: str
        """
        if gen_time is None:
            raise ValueError("Invalid value for `gen_time`, must not be `None`")  # noqa: E501

        self._gen_time = gen_time

    @property
    def expired(self):
        """Gets the expired of this DkubeInfoLicense.  # noqa: E501


        :return: The expired of this DkubeInfoLicense.  # noqa: E501
        :rtype: bool
        """
        return self._expired

    @expired.setter
    def expired(self, expired):
        """Sets the expired of this DkubeInfoLicense.


        :param expired: The expired of this DkubeInfoLicense.  # noqa: E501
        :type: bool
        """
        if expired is None:
            raise ValueError("Invalid value for `expired`, must not be `None`")  # noqa: E501

        self._expired = expired

    @property
    def quota(self):
        """Gets the quota of this DkubeInfoLicense.  # noqa: E501


        :return: The quota of this DkubeInfoLicense.  # noqa: E501
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this DkubeInfoLicense.


        :param quota: The quota of this DkubeInfoLicense.  # noqa: E501
        :type: int
        """
        if quota is None:
            raise ValueError("Invalid value for `quota`, must not be `None`")  # noqa: E501

        self._quota = quota

    @property
    def grace_period(self):
        """Gets the grace_period of this DkubeInfoLicense.  # noqa: E501


        :return: The grace_period of this DkubeInfoLicense.  # noqa: E501
        :rtype: int
        """
        return self._grace_period

    @grace_period.setter
    def grace_period(self, grace_period):
        """Sets the grace_period of this DkubeInfoLicense.


        :param grace_period: The grace_period of this DkubeInfoLicense.  # noqa: E501
        :type: int
        """
        if grace_period is None:
            raise ValueError("Invalid value for `grace_period`, must not be `None`")  # noqa: E501

        self._grace_period = grace_period

    @property
    def onboarded_user_count(self):
        """Gets the onboarded_user_count of this DkubeInfoLicense.  # noqa: E501


        :return: The onboarded_user_count of this DkubeInfoLicense.  # noqa: E501
        :rtype: int
        """
        return self._onboarded_user_count

    @onboarded_user_count.setter
    def onboarded_user_count(self, onboarded_user_count):
        """Sets the onboarded_user_count of this DkubeInfoLicense.


        :param onboarded_user_count: The onboarded_user_count of this DkubeInfoLicense.  # noqa: E501
        :type: int
        """
        if onboarded_user_count is None:
            raise ValueError("Invalid value for `onboarded_user_count`, must not be `None`")  # noqa: E501

        self._onboarded_user_count = onboarded_user_count

    @property
    def uuid(self):
        """Gets the uuid of this DkubeInfoLicense.  # noqa: E501


        :return: The uuid of this DkubeInfoLicense.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this DkubeInfoLicense.


        :param uuid: The uuid of this DkubeInfoLicense.  # noqa: E501
        :type: str
        """
        if uuid is None:
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        self._uuid = uuid

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
        if issubclass(DkubeInfoLicense, dict):
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
        if not isinstance(other, DkubeInfoLicense):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
