import enum

from .dsjob import *
from .common import *

class TrainingDetails(object):
    def __init__(self):
        self.__model    = ''

    @property
    def model(self):
        return self.__model
    
    def _model(self, data: str):
        assert type(data) == str, "type mismatch error"
        self.__model = data

    def to_json(self):
        return {'model': self.model}

    def from_json(self, data:dict):
        assert type(data) == dict, "type mismatch error"
        self._model(data.get('model', ''))

class Training(object):
    def __init__(self):
        self.__type       = "training"
        self.__input      = DSJobInput()
        self.__generated  = JobGenerated()
        self.__details    = TrainingDetails()

    @property
    def input(self):
        return self.__input
    @property
    def type(self):
        return self.__type
    @property
    def generated(self):
        return self.__generated
    @property
    def details(self):
        return self.__details

    @input.setter
    def input(self, data:DSJobInput):
        assert type(data) == DSJobInput, "type mismatch error"
        self.__input = data

    def _generated(self, data: JobGenerated):
        assert type(data) == JobGenerated, "type mismatch error"
        self.__generated = data

    def _details(self, data: TrainingDetails):
        assert type(data) == TrainingDetails, "type mismatch error"
        self.__details = data

    def to_json(self):
        return {'class': self.type, self.type : self.input.to_json()}

    def from_json(self, data:dict):
        self.input.from_json(data['training'])
        self.generated.from_json(data['generated'])
        #MAK TODO - fix from server side, always return the field, make it empty
        self.details.from_json(data['generated']['details'].get('training', {}))
