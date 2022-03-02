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


class ModelmonitorComponentDef(object):
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
        'run_id': 'str',
        'status_info': 'str',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'run_id': 'run_id',
        'status_info': 'status_info',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, run_id=None, status_info=None, status=None, type=None):  # noqa: E501
        """ModelmonitorComponentDef - a model defined in Swagger"""  # noqa: E501

        self._run_id = None
        self._status_info = None
        self._status = None
        self._type = None
        self.discriminator = None

        if run_id is not None:
            self.run_id = run_id
        if status_info is not None:
            self.status_info = status_info
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type

    @property
    def run_id(self):
        """Gets the run_id of this ModelmonitorComponentDef.  # noqa: E501

        Unique id of the run component  # noqa: E501

        :return: The run_id of this ModelmonitorComponentDef.  # noqa: E501
        :rtype: str
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """Sets the run_id of this ModelmonitorComponentDef.

        Unique id of the run component  # noqa: E501

        :param run_id: The run_id of this ModelmonitorComponentDef.  # noqa: E501
        :type: str
        """

        self._run_id = run_id

    @property
    def status_info(self):
        """Gets the status_info of this ModelmonitorComponentDef.  # noqa: E501

        JSON Blob  # noqa: E501

        :return: The status_info of this ModelmonitorComponentDef.  # noqa: E501
        :rtype: str
        """
        return self._status_info

    @status_info.setter
    def status_info(self, status_info):
        """Sets the status_info of this ModelmonitorComponentDef.

        JSON Blob  # noqa: E501

        :param status_info: The status_info of this ModelmonitorComponentDef.  # noqa: E501
        :type: str
        """

        self._status_info = status_info

    @property
    def status(self):
        """Gets the status of this ModelmonitorComponentDef.  # noqa: E501


        :return: The status of this ModelmonitorComponentDef.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ModelmonitorComponentDef.


        :param status: The status of this ModelmonitorComponentDef.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def type(self):
        """Gets the type of this ModelmonitorComponentDef.  # noqa: E501


        :return: The type of this ModelmonitorComponentDef.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ModelmonitorComponentDef.


        :param type: The type of this ModelmonitorComponentDef.  # noqa: E501
        :type: str
        """
        allowed_values = ["baseline", "data_drift", "performance_drift", "deployment_health"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(ModelmonitorComponentDef, dict):
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
        if not isinstance(other, ModelmonitorComponentDef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
