import enum
from .datum import *

class ModelKind(enum.Enum):
    downloaded  = "downloaded"
    trained     = "dkube_trained"

class ModelFormat(enum.Enum):
    unsupported = "unsupported"
    tensorpb    = "tensorpb"

class ModelDetails(object):
    def __init__(self):
        self.__kind   = ModelKind.downloaded
        self.__format = ModelFormat.unsupported

    @property
    def kind(self):
        return self.__kind.value
    @property
    def format(self):
        return self.__format.value

    def _format(self, data):
        assert type(data) == ModelFormat, "type mismatch error"
        self.__format = data

    def _kind(self, data):
        assert type(data) == ModelKind, "type mismatch error"
        self.__kind = data


class Model(object):
    def __init__(self):
        self.__type       = "model"
        self.__input      = DatumInput()
        self.__generated  = DatumGenerated()
        self.__details    = ModelDetails()

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

    def _details(self, data: ModelDetails):
        assert type(data) == ModelDetails, "type mismatch error"
        self.__details = data

    def to_json(self):
        return {
                "class": self.type,
                "name": self.input.name,
                "remote": self.input.remote,
                "source": self.input.source.name,
                "tags": self.input.tags,
                "url": self.input.url
                }
