import enum

from .dsjob import *
from .common import *

class ServingDevice(enum.Enum):
    DEVICE_GPU  = "gpu"
    DEVICE_CPU  = "cpu"

    @staticmethod
    def from_str(self, label:str):
        if label == "cpu":
            return ServingDevice.DEVICE_CPU
        elif label == "gpu":
            return ServingDevice.DEVICE_GPU
        else:
            raise NotImplementedError

class ServingJobInput(object):
    def __init__(self):
        self.__device   = ServingDevice
        self.__model    = ''
        self.__owner    = ''

    @property
    def device(self):
        return self.__device
    @property
    def model(self):
        return self.__model
    @property
    def owner(self):
        return self.__owner

    @device.setter
    def device(self, data:ServingDevice):
        assert type(data) == ServingDevice, "type mismatch error"
        self.__device = data

    @model.setter
    def model(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__model = data

    @model.setter
    def owner(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__owner = data

    def to_json(self):
        return {'device': self.device.value, 'model': self.model, 'owner': self.owner}

    def from_json(self, data:dict):
        assert type(data) == dict, "type mismatch error"
        self.device.from_str(data['device'])
        self.model = data['model']
        self.owner = data['owner']

class Serving(object):
    def __init__(self):
        self.__type       = "inference"
        self.__input      = ServingJobInput()
        self.__generated  = JobGenerated()

    @property
    def input(self):
        return self.__input
    @property
    def type(self):
        return self.__type
    @property
    def generated(self):
        return self.__generated

    @input.setter
    def input(self, data:ServingJobInput):
        assert type(data) == ServingJobInput, "type mismatch error"
        self.__input = data

    def _generated(self, data: JobGenerated):
        assert type(data) == JobGenerated, "type mismatch error"
        self.__generated = data

    def to_json(self):
        return {'class': self.type, self.type : self.input.to_json()}

    def from_json(self, data:dict):
        self.input.from_json(data['training'])
        self.generated.from_json(data['generated'])
