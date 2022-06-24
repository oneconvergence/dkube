# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.3.0.14
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ModelServingInfo(object):
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
        'images': 'ModelServingInfoImages',
        'transformer_code': 'ModelServingInfoTransformerCode'
    }

    attribute_map = {
        'images': 'images',
        'transformer_code': 'transformer_code'
    }

    def __init__(self, images=None, transformer_code=None):  # noqa: E501
        """ModelServingInfo - a model defined in Swagger"""  # noqa: E501

        self._images = None
        self._transformer_code = None
        self.discriminator = None

        if images is not None:
            self.images = images
        if transformer_code is not None:
            self.transformer_code = transformer_code

    @property
    def images(self):
        """Gets the images of this ModelServingInfo.  # noqa: E501


        :return: The images of this ModelServingInfo.  # noqa: E501
        :rtype: ModelServingInfoImages
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this ModelServingInfo.


        :param images: The images of this ModelServingInfo.  # noqa: E501
        :type: ModelServingInfoImages
        """

        self._images = images

    @property
    def transformer_code(self):
        """Gets the transformer_code of this ModelServingInfo.  # noqa: E501


        :return: The transformer_code of this ModelServingInfo.  # noqa: E501
        :rtype: ModelServingInfoTransformerCode
        """
        return self._transformer_code

    @transformer_code.setter
    def transformer_code(self, transformer_code):
        """Sets the transformer_code of this ModelServingInfo.


        :param transformer_code: The transformer_code of this ModelServingInfo.  # noqa: E501
        :type: ModelServingInfoTransformerCode
        """

        self._transformer_code = transformer_code

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
        if issubclass(ModelServingInfo, dict):
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
        if not isinstance(other, ModelServingInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
