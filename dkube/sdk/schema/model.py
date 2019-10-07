import enum
from .datum import *

class ModelKind(enum.Enum):
    downloaded  = "downloaded"
    trained     = "dkube_trained"

    @staticmethod
    def from_str(label):
        if label == "downloaded":
            return ModelKind.downloaded
        elif label == "dkube_trained":
            return ModelFormat.trained
        else:
            raise NotImplementedError


class ModelFormat(enum.Enum):
    unsupported = "unsupported"
    tensorpb    = "tensorpb"

    @staticmethod
    def from_str(label):
        if label == "unsupported":
            return ModelFormat.unsupported
        elif label == "tensorpb":
            return ModelFormat.tensorpb
        else:
            raise NotImplementedError

class ModelDetails(object):
    def __init__(self):
        self.__kind         = ModelKind.downloaded
        self.__format       = ModelFormat.unsupported
        self.__job          = ""

    @property
    def kind(self):
        return self.__kind.value
    @property
    def format(self):
        return self.__format.value
    @property
    def job(self):
        return self.__job

    def _format(self, data):
        assert type(data) == ModelFormat, "type mismatch error"
        self.__format = data

    def _kind(self, data):
        assert type(data) == ModelKind, "type mismatch error"
        self.__kind = data

    def _job(self, data):
        assert type(data) == str, "type mismatch error"
        self.__job = data

    def from_json(self, data:dict):
        self._format(ModelFormat.from_str(details['format']))
        self._kind(ModelKind.from_str(details['kind'].value))
        self._job(details['kind']['dkube_trained']['job'])


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
        res = {'class': self.type}
        res.update(self.input.to_json())
        return res

    def from_json(self, data:dict):
        self.input.from_json(data)
        self.generated.from_json(data['generated'])
        self.details.from_json(data['generated']['details']['model'])

