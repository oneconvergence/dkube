import enum

from .training import *
from .serving import *

class JobParams(enum.Enum):
    TRAINING        = Training()
    SERVING         = Serving()
    #CUSTOM          = Custom()
    #PREPROCESSING   = Preprocessing()
    #NOTEBOOK        = Notebook()

    @staticmethod
    def from_str(label:str):
        assert type(label) == str, "type mismatch error"
        if label == "training":
            return JobParams.TRAINING
        if label == "serving":
            return JobParams.SERVING
        if label == "custom":
            return JobParams.CUSTOM

class DkubeJob(object):
    def __init__(self):
        self.__name = ''
        self.__params = JobParams.TRAINING
        self.__version = ''

    @property
    def name(self):
        return self.__name
    @property
    def params(self):
        return self.__params
    @property
    def version(self):
        return self.__version

    @name.setter
    def name(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__name = data

    @params.setter
    def params(self, data:JobParams):
        assert type(data) == JobParams, "type mismatch error"
        self.__params = data

    @params.setter
    def version(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__version = data

    def to_json(self):
        return {'name': self.name, 'parameters': self.params.value.to_json()}

    def from_json(self, data:dict):
        assert type(data) == dict, "type mismatch error"
        self.name = data['name']
        self.version = data['version']
        self.params = JobParams.from_str(data['parameters']['class'])
        self.params.value.from_json(data['parameters'])
        return self
