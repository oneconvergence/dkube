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
            return ModelKind.trained
        else:
            raise NotImplementedError

class ModelUnsupported(object):
    def __init__(self):
        self.__format = 'unsupported'
        self.__reason = 'model not in standard tensorpb format'

    @property
    def format(self):
        return self.__format
    @property
    def reason(self):
        return self.__reason
    @reason.setter(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__reason = data

class ModelDeviceInfo(object):
    def __init__(self):
        self.__cpu = False
        self.__gpu = False

    @property
    def cpu(self):
        return self.__cpu
    @property
    def gpu(self):
        return self.__gpu

    @cpu.setter
    def cpu(self, data:bool):
        assert type(data) == bool, "type mismatch error"
        self.__cpu = data

    @gpu.setter
    def gpu(self, data:bool):
        assert type(data) == bool, "type mismatch error"
        self.__gpu = data

    def to_json(self):
        return {'cpu': self.cpu, 'gpu': self.gpu}

    def from_json(self, data:dict):
        assert type(data) == dict, "type mismatch error"
        self.cpu = data['cpu']
        self.gpu = data['gpu']

class ModelTensorpb(object):
    def __init__(self):
        self.__format = "tensorpb"
        self.__devicenodes = []
        self.__devices  = ModelDeviceInfo()
        self.__servable = False

    @property
    def format(self):
        return self.__format
    @property
    def devicenodes(self):
        return self.__devicenodes
    @property
    def devices(self):
        return self.__devices
    @property
    def servable(self):
        return self.__servable

    @devicenodes.setter
    def devicenodes(self, data:list):
        assert type(data) == list, "type mismatch error"
        self.__devicenodes = data

    @devices.setter
    def devices(self, data:ModelDeviceInfo):
        assert type(data) == ModelDeviceInfo, "type mismatch error"
        self.__devices = data

    @servable.setter
    def servable(self, data:bool):
        assert type(data) == bool, "type mismatch error"
        self.__servable = data

    def to_json(self):
        return {'devicenodes': self.devicenodes, 'devices': self.devices.to_json(), 'servable': self.servable}

    def from_json(self, data:dict):
        assert type(data) == dict, "type mismatch error"
        self.devicenodes = data['devicenodes']
        self.devices.from_json(data['devices'])
        self.servable = data['servable']

class ModelFormat(enum.Enum):
    unsupported = ModelUnsupported()
    tensorpb    = ModelTensorpb()

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
        self._format(ModelFormat.from_str(data['format']))
        self._kind(ModelKind.from_str(data['kind'].value))
        self._job(data['kind']['dkube_trained']['job'])


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
    @property
    def details(self):
        return self.__details

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

