import enum
from .datum import *

class Dataset(object):
    def __init__(self):
        self.__type       = "program"
        self.__input      = DatumInput()
        self.__generated  = DatumGenerated()

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
    def input(self, data:DatumInput):
        assert type(data) == DatumInput, "type mismatch error"
        self.__input = data

    def _generated(self, data: DatumGenerated):
        assert type(data) == DatumGenerated, "type mismatch error"
        self.__generated = data

    def to_json(self):
        res = {'class': self.type}
        res.update(self.input.to_json())
        return res

    def from_json(self, data:dict):
        self.input.from_json(data)
        self.generated.from_json(data['generated'])
