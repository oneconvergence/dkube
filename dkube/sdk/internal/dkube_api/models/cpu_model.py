# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.3.0.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CpuModel(object):
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
        'cpus': 'str',
        'architecture': 'str',
        'cpu_op_models': 'str',
        'byte_order': 'str',
        'threads_per_core': 'int',
        'cores_per_socket': 'int',
        'sockets': 'int',
        'vendor': 'str',
        'model_number': 'str',
        'cores': 'int',
        'model_name': 'str',
        'frequency': 'str',
        'frequency_max': 'str',
        'frequency_min': 'str',
        'virtualization': 'str',
        'family': 'str',
        'l1d_cache': 'str',
        'l1i_cache': 'str',
        'l2_cache': 'str',
        'l3_cache': 'str'
    }

    attribute_map = {
        'version': 'version',
        'cpus': 'cpus',
        'architecture': 'architecture',
        'cpu_op_models': 'cpu_op_models',
        'byte_order': 'byte_order',
        'threads_per_core': 'threads_per_core',
        'cores_per_socket': 'cores_per_socket',
        'sockets': 'sockets',
        'vendor': 'vendor',
        'model_number': 'modelNumber',
        'cores': 'cores',
        'model_name': 'modelName',
        'frequency': 'frequency',
        'frequency_max': 'frequency_max',
        'frequency_min': 'frequency_min',
        'virtualization': 'virtualization',
        'family': 'family',
        'l1d_cache': 'l1d_cache',
        'l1i_cache': 'l1i_cache',
        'l2_cache': 'l2_cache',
        'l3_cache': 'l3_cache'
    }

    def __init__(self, version=None, cpus=None, architecture=None, cpu_op_models=None, byte_order=None, threads_per_core=None, cores_per_socket=None, sockets=None, vendor=None, model_number=None, cores=None, model_name=None, frequency=None, frequency_max=None, frequency_min=None, virtualization=None, family=None, l1d_cache=None, l1i_cache=None, l2_cache=None, l3_cache=None):  # noqa: E501
        """CpuModel - a model defined in Swagger"""  # noqa: E501

        self._version = None
        self._cpus = None
        self._architecture = None
        self._cpu_op_models = None
        self._byte_order = None
        self._threads_per_core = None
        self._cores_per_socket = None
        self._sockets = None
        self._vendor = None
        self._model_number = None
        self._cores = None
        self._model_name = None
        self._frequency = None
        self._frequency_max = None
        self._frequency_min = None
        self._virtualization = None
        self._family = None
        self._l1d_cache = None
        self._l1i_cache = None
        self._l2_cache = None
        self._l3_cache = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if cpus is not None:
            self.cpus = cpus
        if architecture is not None:
            self.architecture = architecture
        if cpu_op_models is not None:
            self.cpu_op_models = cpu_op_models
        if byte_order is not None:
            self.byte_order = byte_order
        if threads_per_core is not None:
            self.threads_per_core = threads_per_core
        if cores_per_socket is not None:
            self.cores_per_socket = cores_per_socket
        if sockets is not None:
            self.sockets = sockets
        if vendor is not None:
            self.vendor = vendor
        if model_number is not None:
            self.model_number = model_number
        if cores is not None:
            self.cores = cores
        if model_name is not None:
            self.model_name = model_name
        if frequency is not None:
            self.frequency = frequency
        if frequency_max is not None:
            self.frequency_max = frequency_max
        if frequency_min is not None:
            self.frequency_min = frequency_min
        if virtualization is not None:
            self.virtualization = virtualization
        if family is not None:
            self.family = family
        if l1d_cache is not None:
            self.l1d_cache = l1d_cache
        if l1i_cache is not None:
            self.l1i_cache = l1i_cache
        if l2_cache is not None:
            self.l2_cache = l2_cache
        if l3_cache is not None:
            self.l3_cache = l3_cache

    @property
    def version(self):
        """Gets the version of this CpuModel.  # noqa: E501


        :return: The version of this CpuModel.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CpuModel.


        :param version: The version of this CpuModel.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def cpus(self):
        """Gets the cpus of this CpuModel.  # noqa: E501


        :return: The cpus of this CpuModel.  # noqa: E501
        :rtype: str
        """
        return self._cpus

    @cpus.setter
    def cpus(self, cpus):
        """Sets the cpus of this CpuModel.


        :param cpus: The cpus of this CpuModel.  # noqa: E501
        :type: str
        """

        self._cpus = cpus

    @property
    def architecture(self):
        """Gets the architecture of this CpuModel.  # noqa: E501


        :return: The architecture of this CpuModel.  # noqa: E501
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """Sets the architecture of this CpuModel.


        :param architecture: The architecture of this CpuModel.  # noqa: E501
        :type: str
        """

        self._architecture = architecture

    @property
    def cpu_op_models(self):
        """Gets the cpu_op_models of this CpuModel.  # noqa: E501


        :return: The cpu_op_models of this CpuModel.  # noqa: E501
        :rtype: str
        """
        return self._cpu_op_models

    @cpu_op_models.setter
    def cpu_op_models(self, cpu_op_models):
        """Sets the cpu_op_models of this CpuModel.


        :param cpu_op_models: The cpu_op_models of this CpuModel.  # noqa: E501
        :type: str
        """

        self._cpu_op_models = cpu_op_models

    @property
    def byte_order(self):
        """Gets the byte_order of this CpuModel.  # noqa: E501


        :return: The byte_order of this CpuModel.  # noqa: E501
        :rtype: str
        """
        return self._byte_order

    @byte_order.setter
    def byte_order(self, byte_order):
        """Sets the byte_order of this CpuModel.


        :param byte_order: The byte_order of this CpuModel.  # noqa: E501
        :type: str
        """

        self._byte_order = byte_order

    @property
    def threads_per_core(self):
        """Gets the threads_per_core of this CpuModel.  # noqa: E501


        :return: The threads_per_core of this CpuModel.  # noqa: E501
        :rtype: int
        """
        return self._threads_per_core

    @threads_per_core.setter
    def threads_per_core(self, threads_per_core):
        """Sets the threads_per_core of this CpuModel.


        :param threads_per_core: The threads_per_core of this CpuModel.  # noqa: E501
        :type: int
        """

        self._threads_per_core = threads_per_core

    @property
    def cores_per_socket(self):
        """Gets the cores_per_socket of this CpuModel.  # noqa: E501


        :return: The cores_per_socket of this CpuModel.  # noqa: E501
        :rtype: int
        """
        return self._cores_per_socket

    @cores_per_socket.setter
    def cores_per_socket(self, cores_per_socket):
        """Sets the cores_per_socket of this CpuModel.


        :param cores_per_socket: The cores_per_socket of this CpuModel.  # noqa: E501
        :type: int
        """

        self._cores_per_socket = cores_per_socket

    @property
    def sockets(self):
        """Gets the sockets of this CpuModel.  # noqa: E501


        :return: The sockets of this CpuModel.  # noqa: E501
        :rtype: int
        """
        return self._sockets

    @sockets.setter
    def sockets(self, sockets):
        """Sets the sockets of this CpuModel.


        :param sockets: The sockets of this CpuModel.  # noqa: E501
        :type: int
        """

        self._sockets = sockets

    @property
    def vendor(self):
        """Gets the vendor of this CpuModel.  # noqa: E501


        :return: The vendor of this CpuModel.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this CpuModel.


        :param vendor: The vendor of this CpuModel.  # noqa: E501
        :type: str
        """

        self._vendor = vendor

    @property
    def model_number(self):
        """Gets the model_number of this CpuModel.  # noqa: E501


        :return: The model_number of this CpuModel.  # noqa: E501
        :rtype: str
        """
        return self._model_number

    @model_number.setter
    def model_number(self, model_number):
        """Sets the model_number of this CpuModel.


        :param model_number: The model_number of this CpuModel.  # noqa: E501
        :type: str
        """

        self._model_number = model_number

    @property
    def cores(self):
        """Gets the cores of this CpuModel.  # noqa: E501


        :return: The cores of this CpuModel.  # noqa: E501
        :rtype: int
        """
        return self._cores

    @cores.setter
    def cores(self, cores):
        """Sets the cores of this CpuModel.


        :param cores: The cores of this CpuModel.  # noqa: E501
        :type: int
        """

        self._cores = cores

    @property
    def model_name(self):
        """Gets the model_name of this CpuModel.  # noqa: E501


        :return: The model_name of this CpuModel.  # noqa: E501
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        """Sets the model_name of this CpuModel.


        :param model_name: The model_name of this CpuModel.  # noqa: E501
        :type: str
        """

        self._model_name = model_name

    @property
    def frequency(self):
        """Gets the frequency of this CpuModel.  # noqa: E501


        :return: The frequency of this CpuModel.  # noqa: E501
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this CpuModel.


        :param frequency: The frequency of this CpuModel.  # noqa: E501
        :type: str
        """

        self._frequency = frequency

    @property
    def frequency_max(self):
        """Gets the frequency_max of this CpuModel.  # noqa: E501


        :return: The frequency_max of this CpuModel.  # noqa: E501
        :rtype: str
        """
        return self._frequency_max

    @frequency_max.setter
    def frequency_max(self, frequency_max):
        """Sets the frequency_max of this CpuModel.


        :param frequency_max: The frequency_max of this CpuModel.  # noqa: E501
        :type: str
        """

        self._frequency_max = frequency_max

    @property
    def frequency_min(self):
        """Gets the frequency_min of this CpuModel.  # noqa: E501


        :return: The frequency_min of this CpuModel.  # noqa: E501
        :rtype: str
        """
        return self._frequency_min

    @frequency_min.setter
    def frequency_min(self, frequency_min):
        """Sets the frequency_min of this CpuModel.


        :param frequency_min: The frequency_min of this CpuModel.  # noqa: E501
        :type: str
        """

        self._frequency_min = frequency_min

    @property
    def virtualization(self):
        """Gets the virtualization of this CpuModel.  # noqa: E501


        :return: The virtualization of this CpuModel.  # noqa: E501
        :rtype: str
        """
        return self._virtualization

    @virtualization.setter
    def virtualization(self, virtualization):
        """Sets the virtualization of this CpuModel.


        :param virtualization: The virtualization of this CpuModel.  # noqa: E501
        :type: str
        """

        self._virtualization = virtualization

    @property
    def family(self):
        """Gets the family of this CpuModel.  # noqa: E501


        :return: The family of this CpuModel.  # noqa: E501
        :rtype: str
        """
        return self._family

    @family.setter
    def family(self, family):
        """Sets the family of this CpuModel.


        :param family: The family of this CpuModel.  # noqa: E501
        :type: str
        """

        self._family = family

    @property
    def l1d_cache(self):
        """Gets the l1d_cache of this CpuModel.  # noqa: E501


        :return: The l1d_cache of this CpuModel.  # noqa: E501
        :rtype: str
        """
        return self._l1d_cache

    @l1d_cache.setter
    def l1d_cache(self, l1d_cache):
        """Sets the l1d_cache of this CpuModel.


        :param l1d_cache: The l1d_cache of this CpuModel.  # noqa: E501
        :type: str
        """

        self._l1d_cache = l1d_cache

    @property
    def l1i_cache(self):
        """Gets the l1i_cache of this CpuModel.  # noqa: E501


        :return: The l1i_cache of this CpuModel.  # noqa: E501
        :rtype: str
        """
        return self._l1i_cache

    @l1i_cache.setter
    def l1i_cache(self, l1i_cache):
        """Sets the l1i_cache of this CpuModel.


        :param l1i_cache: The l1i_cache of this CpuModel.  # noqa: E501
        :type: str
        """

        self._l1i_cache = l1i_cache

    @property
    def l2_cache(self):
        """Gets the l2_cache of this CpuModel.  # noqa: E501


        :return: The l2_cache of this CpuModel.  # noqa: E501
        :rtype: str
        """
        return self._l2_cache

    @l2_cache.setter
    def l2_cache(self, l2_cache):
        """Sets the l2_cache of this CpuModel.


        :param l2_cache: The l2_cache of this CpuModel.  # noqa: E501
        :type: str
        """

        self._l2_cache = l2_cache

    @property
    def l3_cache(self):
        """Gets the l3_cache of this CpuModel.  # noqa: E501


        :return: The l3_cache of this CpuModel.  # noqa: E501
        :rtype: str
        """
        return self._l3_cache

    @l3_cache.setter
    def l3_cache(self, l3_cache):
        """Sets the l3_cache of this CpuModel.


        :param l3_cache: The l3_cache of this CpuModel.  # noqa: E501
        :type: str
        """

        self._l3_cache = l3_cache

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
        if issubclass(CpuModel, dict):
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
        if not isinstance(other, CpuModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
