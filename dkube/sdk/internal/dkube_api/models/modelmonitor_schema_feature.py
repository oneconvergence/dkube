# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.3.0.11
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ModelmonitorSchemaFeature(object):
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
        'selected': 'bool',
        '_class': 'str',
        'label': 'str',
        'type': 'str'
    }

    attribute_map = {
        'selected': 'selected',
        '_class': 'class',
        'label': 'label',
        'type': 'type'
    }

    def __init__(self, selected=None, _class=None, label=None, type=None):  # noqa: E501
        """ModelmonitorSchemaFeature - a model defined in Swagger"""  # noqa: E501

        self._selected = None
        self.__class = None
        self._label = None
        self._type = None
        self.discriminator = None

        if selected is not None:
            self.selected = selected
        if _class is not None:
            self._class = _class
        if label is not None:
            self.label = label
        if type is not None:
            self.type = type

    @property
    def selected(self):
        """Gets the selected of this ModelmonitorSchemaFeature.  # noqa: E501


        :return: The selected of this ModelmonitorSchemaFeature.  # noqa: E501
        :rtype: bool
        """
        return self._selected

    @selected.setter
    def selected(self, selected):
        """Sets the selected of this ModelmonitorSchemaFeature.


        :param selected: The selected of this ModelmonitorSchemaFeature.  # noqa: E501
        :type: bool
        """

        self._selected = selected

    @property
    def _class(self):
        """Gets the _class of this ModelmonitorSchemaFeature.  # noqa: E501


        :return: The _class of this ModelmonitorSchemaFeature.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this ModelmonitorSchemaFeature.


        :param _class: The _class of this ModelmonitorSchemaFeature.  # noqa: E501
        :type: str
        """
        allowed_values = ["Categorical", "Continuous"]  # noqa: E501
        if _class not in allowed_values:
            raise ValueError(
                "Invalid value for `_class` ({0}), must be one of {1}"  # noqa: E501
                .format(_class, allowed_values)
            )

        self.__class = _class

    @property
    def label(self):
        """Gets the label of this ModelmonitorSchemaFeature.  # noqa: E501


        :return: The label of this ModelmonitorSchemaFeature.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ModelmonitorSchemaFeature.


        :param label: The label of this ModelmonitorSchemaFeature.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this ModelmonitorSchemaFeature.  # noqa: E501


        :return: The type of this ModelmonitorSchemaFeature.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ModelmonitorSchemaFeature.


        :param type: The type of this ModelmonitorSchemaFeature.  # noqa: E501
        :type: str
        """
        allowed_values = ["InputFeature", "PredictionOutput", "Timestamp", "RowID"]  # noqa: E501
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
        if issubclass(ModelmonitorSchemaFeature, dict):
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
        if not isinstance(other, ModelmonitorSchemaFeature):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
