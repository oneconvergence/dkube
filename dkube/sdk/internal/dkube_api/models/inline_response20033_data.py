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


class InlineResponse20033Data(object):
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
        'datum': 'DatumModel',
        'version': 'VersionModel',
        'run': 'JobModel'
    }

    attribute_map = {
        'datum': 'datum',
        'version': 'version',
        'run': 'run'
    }

    def __init__(self, datum=None, version=None, run=None):  # noqa: E501
        """InlineResponse20033Data - a model defined in Swagger"""  # noqa: E501

        self._datum = None
        self._version = None
        self._run = None
        self.discriminator = None

        if datum is not None:
            self.datum = datum
        if version is not None:
            self.version = version
        if run is not None:
            self.run = run

    @property
    def datum(self):
        """Gets the datum of this InlineResponse20033Data.  # noqa: E501


        :return: The datum of this InlineResponse20033Data.  # noqa: E501
        :rtype: DatumModel
        """
        return self._datum

    @datum.setter
    def datum(self, datum):
        """Sets the datum of this InlineResponse20033Data.


        :param datum: The datum of this InlineResponse20033Data.  # noqa: E501
        :type: DatumModel
        """

        self._datum = datum

    @property
    def version(self):
        """Gets the version of this InlineResponse20033Data.  # noqa: E501


        :return: The version of this InlineResponse20033Data.  # noqa: E501
        :rtype: VersionModel
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this InlineResponse20033Data.


        :param version: The version of this InlineResponse20033Data.  # noqa: E501
        :type: VersionModel
        """

        self._version = version

    @property
    def run(self):
        """Gets the run of this InlineResponse20033Data.  # noqa: E501


        :return: The run of this InlineResponse20033Data.  # noqa: E501
        :rtype: JobModel
        """
        return self._run

    @run.setter
    def run(self, run):
        """Sets the run of this InlineResponse20033Data.


        :param run: The run of this InlineResponse20033Data.  # noqa: E501
        :type: JobModel
        """

        self._run = run

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
        if issubclass(InlineResponse20033Data, dict):
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
        if not isinstance(other, InlineResponse20033Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
