# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.3.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ModelMetricsInner(object):
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
        '_class': 'str',
        'name': 'str',
        'curve': 'ModelMetricsInnerCurve',
        'table': 'ModelMetricsInnerCurve',
        'scalar': 'str',
        'confusion_matrix': 'ModelMetricsInnerCurve'
    }

    attribute_map = {
        '_class': 'class',
        'name': 'name',
        'curve': 'curve',
        'table': 'table',
        'scalar': 'scalar',
        'confusion_matrix': 'confusion_matrix'
    }

    def __init__(self, _class=None, name=None, curve=None, table=None, scalar=None, confusion_matrix=None):  # noqa: E501
        """ModelMetricsInner - a model defined in Swagger"""  # noqa: E501

        self.__class = None
        self._name = None
        self._curve = None
        self._table = None
        self._scalar = None
        self._confusion_matrix = None
        self.discriminator = None

        if _class is not None:
            self._class = _class
        if name is not None:
            self.name = name
        if curve is not None:
            self.curve = curve
        if table is not None:
            self.table = table
        if scalar is not None:
            self.scalar = scalar
        if confusion_matrix is not None:
            self.confusion_matrix = confusion_matrix

    @property
    def _class(self):
        """Gets the _class of this ModelMetricsInner.  # noqa: E501


        :return: The _class of this ModelMetricsInner.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this ModelMetricsInner.


        :param _class: The _class of this ModelMetricsInner.  # noqa: E501
        :type: str
        """
        allowed_values = ["CURVE", "SCALAR", "TABLE", "CONFUSION_MATRIX"]  # noqa: E501
        if _class not in allowed_values:
            raise ValueError(
                "Invalid value for `_class` ({0}), must be one of {1}"  # noqa: E501
                .format(_class, allowed_values)
            )

        self.__class = _class

    @property
    def name(self):
        """Gets the name of this ModelMetricsInner.  # noqa: E501


        :return: The name of this ModelMetricsInner.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelMetricsInner.


        :param name: The name of this ModelMetricsInner.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def curve(self):
        """Gets the curve of this ModelMetricsInner.  # noqa: E501


        :return: The curve of this ModelMetricsInner.  # noqa: E501
        :rtype: ModelMetricsInnerCurve
        """
        return self._curve

    @curve.setter
    def curve(self, curve):
        """Sets the curve of this ModelMetricsInner.


        :param curve: The curve of this ModelMetricsInner.  # noqa: E501
        :type: ModelMetricsInnerCurve
        """

        self._curve = curve

    @property
    def table(self):
        """Gets the table of this ModelMetricsInner.  # noqa: E501


        :return: The table of this ModelMetricsInner.  # noqa: E501
        :rtype: ModelMetricsInnerCurve
        """
        return self._table

    @table.setter
    def table(self, table):
        """Sets the table of this ModelMetricsInner.


        :param table: The table of this ModelMetricsInner.  # noqa: E501
        :type: ModelMetricsInnerCurve
        """

        self._table = table

    @property
    def scalar(self):
        """Gets the scalar of this ModelMetricsInner.  # noqa: E501


        :return: The scalar of this ModelMetricsInner.  # noqa: E501
        :rtype: str
        """
        return self._scalar

    @scalar.setter
    def scalar(self, scalar):
        """Sets the scalar of this ModelMetricsInner.


        :param scalar: The scalar of this ModelMetricsInner.  # noqa: E501
        :type: str
        """

        self._scalar = scalar

    @property
    def confusion_matrix(self):
        """Gets the confusion_matrix of this ModelMetricsInner.  # noqa: E501


        :return: The confusion_matrix of this ModelMetricsInner.  # noqa: E501
        :rtype: ModelMetricsInnerCurve
        """
        return self._confusion_matrix

    @confusion_matrix.setter
    def confusion_matrix(self, confusion_matrix):
        """Sets the confusion_matrix of this ModelMetricsInner.


        :param confusion_matrix: The confusion_matrix of this ModelMetricsInner.  # noqa: E501
        :type: ModelMetricsInnerCurve
        """

        self._confusion_matrix = confusion_matrix

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
        if issubclass(ModelMetricsInner, dict):
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
        if not isinstance(other, ModelMetricsInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
