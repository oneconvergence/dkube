# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.2.1.13
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DLFrameworks(object):
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
        'nb_ide': 'DLFrameworkModel',
        'r_ide': 'DLFrameworkModel',
        'training': 'DLFrameworkModel',
        'preprocessing': 'DLFrameworkModel',
        'eval': 'DLFrameworkModel',
        'serving': 'DLFrameworkModel',
        'project': 'DLFrameworkProject',
        'frameworks': 'list[DLFramework]',
        'images': 'list[str]'
    }

    attribute_map = {
        'nb_ide': 'nb-ide',
        'r_ide': 'r-ide',
        'training': 'training',
        'preprocessing': 'preprocessing',
        'eval': 'eval',
        'serving': 'serving',
        'project': 'project',
        'frameworks': 'frameworks',
        'images': 'images'
    }

    def __init__(self, nb_ide=None, r_ide=None, training=None, preprocessing=None, eval=None, serving=None, project=None, frameworks=None, images=None):  # noqa: E501
        """DLFrameworks - a model defined in Swagger"""  # noqa: E501

        self._nb_ide = None
        self._r_ide = None
        self._training = None
        self._preprocessing = None
        self._eval = None
        self._serving = None
        self._project = None
        self._frameworks = None
        self._images = None
        self.discriminator = None

        if nb_ide is not None:
            self.nb_ide = nb_ide
        if r_ide is not None:
            self.r_ide = r_ide
        if training is not None:
            self.training = training
        if preprocessing is not None:
            self.preprocessing = preprocessing
        if eval is not None:
            self.eval = eval
        if serving is not None:
            self.serving = serving
        if project is not None:
            self.project = project
        if frameworks is not None:
            self.frameworks = frameworks
        if images is not None:
            self.images = images

    @property
    def nb_ide(self):
        """Gets the nb_ide of this DLFrameworks.  # noqa: E501


        :return: The nb_ide of this DLFrameworks.  # noqa: E501
        :rtype: DLFrameworkModel
        """
        return self._nb_ide

    @nb_ide.setter
    def nb_ide(self, nb_ide):
        """Sets the nb_ide of this DLFrameworks.


        :param nb_ide: The nb_ide of this DLFrameworks.  # noqa: E501
        :type: DLFrameworkModel
        """

        self._nb_ide = nb_ide

    @property
    def r_ide(self):
        """Gets the r_ide of this DLFrameworks.  # noqa: E501


        :return: The r_ide of this DLFrameworks.  # noqa: E501
        :rtype: DLFrameworkModel
        """
        return self._r_ide

    @r_ide.setter
    def r_ide(self, r_ide):
        """Sets the r_ide of this DLFrameworks.


        :param r_ide: The r_ide of this DLFrameworks.  # noqa: E501
        :type: DLFrameworkModel
        """

        self._r_ide = r_ide

    @property
    def training(self):
        """Gets the training of this DLFrameworks.  # noqa: E501


        :return: The training of this DLFrameworks.  # noqa: E501
        :rtype: DLFrameworkModel
        """
        return self._training

    @training.setter
    def training(self, training):
        """Sets the training of this DLFrameworks.


        :param training: The training of this DLFrameworks.  # noqa: E501
        :type: DLFrameworkModel
        """

        self._training = training

    @property
    def preprocessing(self):
        """Gets the preprocessing of this DLFrameworks.  # noqa: E501


        :return: The preprocessing of this DLFrameworks.  # noqa: E501
        :rtype: DLFrameworkModel
        """
        return self._preprocessing

    @preprocessing.setter
    def preprocessing(self, preprocessing):
        """Sets the preprocessing of this DLFrameworks.


        :param preprocessing: The preprocessing of this DLFrameworks.  # noqa: E501
        :type: DLFrameworkModel
        """

        self._preprocessing = preprocessing

    @property
    def eval(self):
        """Gets the eval of this DLFrameworks.  # noqa: E501


        :return: The eval of this DLFrameworks.  # noqa: E501
        :rtype: DLFrameworkModel
        """
        return self._eval

    @eval.setter
    def eval(self, eval):
        """Sets the eval of this DLFrameworks.


        :param eval: The eval of this DLFrameworks.  # noqa: E501
        :type: DLFrameworkModel
        """

        self._eval = eval

    @property
    def serving(self):
        """Gets the serving of this DLFrameworks.  # noqa: E501


        :return: The serving of this DLFrameworks.  # noqa: E501
        :rtype: DLFrameworkModel
        """
        return self._serving

    @serving.setter
    def serving(self, serving):
        """Sets the serving of this DLFrameworks.


        :param serving: The serving of this DLFrameworks.  # noqa: E501
        :type: DLFrameworkModel
        """

        self._serving = serving

    @property
    def project(self):
        """Gets the project of this DLFrameworks.  # noqa: E501


        :return: The project of this DLFrameworks.  # noqa: E501
        :rtype: DLFrameworkProject
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this DLFrameworks.


        :param project: The project of this DLFrameworks.  # noqa: E501
        :type: DLFrameworkProject
        """

        self._project = project

    @property
    def frameworks(self):
        """Gets the frameworks of this DLFrameworks.  # noqa: E501


        :return: The frameworks of this DLFrameworks.  # noqa: E501
        :rtype: list[DLFramework]
        """
        return self._frameworks

    @frameworks.setter
    def frameworks(self, frameworks):
        """Sets the frameworks of this DLFrameworks.


        :param frameworks: The frameworks of this DLFrameworks.  # noqa: E501
        :type: list[DLFramework]
        """

        self._frameworks = frameworks

    @property
    def images(self):
        """Gets the images of this DLFrameworks.  # noqa: E501


        :return: The images of this DLFrameworks.  # noqa: E501
        :rtype: list[str]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this DLFrameworks.


        :param images: The images of this DLFrameworks.  # noqa: E501
        :type: list[str]
        """

        self._images = images

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
        if issubclass(DLFrameworks, dict):
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
        if not isinstance(other, DLFrameworks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
