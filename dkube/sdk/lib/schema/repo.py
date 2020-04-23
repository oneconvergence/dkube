import enum
from .datum import *

class Repository(object):
    def __init__(self):
        self.__type         = "program"
        self.__input        = DatumInput()
        self.__generated    = DatumGenerated()
        self.__headversion  = ''
        self.__versions     = []

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
    def headversion(self):
        return self.__headversion

    @property
    def versions(self):
        return self.__versions

    @type.setter
    def type(self, value:str):
        assert value in ['program', 'dataset', 'model'], "invalid value {}".format(value)
        self.__type = value

    @input.setter
    def input(self, data:DatumInput):
        assert type(data) == DatumInput, "type mismatch error"
        self.__input = data

    @versions.setter
    def versions(self, data:list):
        assert type(data) == list, "type mismatch error"
        self.__versions = data

    @headversion.setter
    def headversion(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__headversion = data


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
        for version in data.get('versions', []):
            self.__versions.append(Version.from_json(version))

        return self
