import enum


class TensorflowDetails(object):
    def __init__(self):
        self.__type     = "tensorflow"
        self.__version  = ""

    @property
    def type(self):
        return self.__type
    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__version = data

    def to_json(self):
        return {'choice': self.type, 'details': {'tfversion': self.version}}

    def from_json(self, data:dict):
        assert type(data) == dict, "type mismatch error"
        self.version = data['tfversion']

class PytorchDetails(object):
    def __init__(self):
        self.__type = "pytorch"

class Framework(enum.Enum):
    Tensorflow  = TensorflowDetails()
    Pytorch     = PytorchDetails()

    @staticmethod
    def from_dict(data):
        if data['choice'] == "tensorflow":
            return Framework.Tensorflow
        elif data['choice'] == "pytorch":
            return Framework.Pytorch
        else:
            raise NotImplementedError

class DkubeExecutor(object):
    def __init__(self):
        self.__name = "dkube"
        self.__framework = Framework.Tensorflow

    @property
    def name(self):
        return self.__name
    @property
    def framework(self):
        return self.__framework

    @framework.setter
    def framework(self, data:Framework):
        assert type(data) == Framework, "type mismatch error"
        self.__framework = data

    def to_json(self):
        return {'choice': self.name, 'dkube': {'framework': self.framework.value.to_json()}}

    def from_json(self, data:dict):
        assert type(data) == dict, "type mismatch error"
        self.framework = Framework.from_dict(data['dkube']['framework'])
        self.framework.value.from_json(data['dkube']['framework']['details'])

class CustomContainerImage(object):
    def __init__(self):
        self.__password = ''
        self.__path = ''
        self.__runas = ''
        self.__username = ''

    @property
    def password(self):
        return self.__password
    @property
    def path(self):
        return self.__path
    @property
    def runas(self):
        return self.__runas
    @property
    def username(self):
        return self.__username

    @password.setter
    def password(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__password = data

    @path.setter
    def path(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__path = data

    @runas.setter
    def runas(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__runas = data

    @username.setter
    def username(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__username = data

    def to_json(self):
        return {'password': self.password,
                'path': self.path,
                'runas': self.runas,
                'username': self.username
                }

        def from_json(self, data:dict):
            assert type(data) == dict, "type mismatch error"
            self.password = data['password']
            self.path = data['path']
            self.runas = data['runas']
            self.username = data['username']
        
class CustomExecutor(object):
    def __init__(self):
        self.__name  = "custom"
        self.__image = CustomContainerImage()

    @property
    def name(self):
        return self.__name
    @property
    def image(self):
        return self.__image
    @image.setter
    def image(self, data:CustomContainerImage):
        assert type(data) == CustomContainerImage, "type mismatch error"
        self.__image = data

    def to_json(self):
        return {'choice':self.name, 'custom':{'image': self.image.to_json()}}

    def from_json(self, data:dict):
        assert type(data) == dict, "type mismatch error"
        self.image.from_json(data['custom']['image'])


class Executor(enum.Enum):
    Dkube   = DkubeExecutor()
    Custom  = CustomExecutor()

    @staticmethod
    def from_dict(data:dict):
        if data['choice'] == "dkube":
            return ModelFormat.Dkube
        elif data['choice'] == "custom":
            return ModelFormat.Custom
        else:
            raise NotImplementedError

    @staticmethod
    def from_str(data:str):
        if data == "dkube":
            return Executor.Dkube
        elif data == "custom":
            return Executor.Custom
        else:
            raise NotImplementedError

class WorkspaceDetails(object):
    def __init__(self):
        self.__program = ''
        self.__script  = ''

    @property
    def program(self):
        return self.__program
    @property
    def script(self):
        return self.__script

    @program.setter
    def program(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__program = data

    @script.setter
    def script(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__script = data

    def to_json(self):
        return {'program': self.program, 'script': self.script}

    def from_json(self, data:dict):
        assert type(data) == dict, "type mismatch error"
        self.program = data['program']
        self.script = data['script']

class ConfigFile(object):
    def __init__(self):
        self.__name = ""
        self.__body = ""

    @property
    def name(self):
        return self.__name
    @property
    def body(self):
        return self.__body

    @name.setter
    def name(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__name = data

    @body.setter
    def body(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__body = data

    def to_json(self):
        #MAK TODO - Special condition here, handle this at server side
        if self.body == "":
            return {}
        else:
            return {'name': self.name, 'body': self.body}

    def from_json(self, data:dict):
        assert type(data) == dict, "type mismatch error"
        if data == {}: return
        self.name = data['name']
        self.body = dta['body']

class HyperParams(object):
    def __init__(self):
        self.__epochs = 0
        self.__steps  = 0
        self.__batchsize = 0
        self.__customkv = []
        self.__file = ConfigFile()

    @property
    def epochs(self):
        return self.__epochs
    @property
    def steps(self):
        return self.__steps
    @property
    def batchsize(self):
        return self.__batchsize
    @property
    def customkv(self):
        return self.__customkv
    @property
    def file(self):
        return self.__file

    @epochs.setter
    def epochs(self, data:int):
        assert type(data) == int, "type mismatch error"
        self.__epochs = data

    @steps.setter
    def steps(self, data:int):
        assert type(data) == int, "type mismatch error"
        self.__steps = data

    @batchsize.setter
    def batchsize(self, data:int):
        assert type(data) == int, "type mismatch error"
        self.__batchsize = data

    @customkv.setter
    def customkv(self, data:list):
        assert type(data) == list, "type mismatch error"
        self.__customkv = data

    @file.setter
    def file(self, data:ConfigFile):
        assert type(data) == ConfigFile, "type mismatch error"
        self.__file = data

    def to_json(self):
        return {'epochs': self.epochs, 'steps': self.steps, 'batchsize': self.batchsize, 
                'customkv': self.customkv, 'file': self.file.to_json()}

    def from_json(self, data:dict):
        assert type(data) == dict, "type mismatch error"
        self.epochs = data['epochs']
        self.steps  = data['steps']
        self.batchsize = data['batchsize']
        self.customkv = data['customkv']
        self.file.from_json(data['file'])

        
class DSJobInput(object):
    def __init__(self):
        self.__executor  = Executor.Dkube
        self.__workspace = WorkspaceDetails()
        self.__models    = []
        self.__datasets  = []
        self.__tags      = []
        self.__hptuning  = ConfigFile()
        self.__hparams   = HyperParams()
        self.__nworkers  = 0
        self.__ngpus     = 0
        self.__gpus_override = False

    @property
    def executor(self):
        return self.__executor
    @property
    def workspace(self):
        return self.__workspace
    @property
    def models(self):
        return self.__models
    @property
    def datasets(self):
        return self.__datasets
    @property
    def tags(self):
        return self.__tags
    @property
    def hptuning(self):
        return self.__hptuning
    @property
    def hparams(self):
        return self.__hparams
    @property
    def nworkers(self):
        return self.__nworkers
    @property
    def ngpus(self):
        return self.__ngpus
    @property
    def gpus_override(self):
        return self.__gpus_override

    @workspace.setter
    def workspace(self, data:WorkspaceDetails):
        assert type(data) == WorkspaceDetails, "type mismatch error"
        self.__workspace = data

    @models.setter
    def models(self, data:list):
        assert type(data) == list, "type mismatch error"
        self.__models = data

    @datasets.setter
    def datasets(self, data:list):
        assert type(data) == list, "type mismatch error"
        self.__datasets = data

    @tags.setter
    def tags(self, data:list):
        assert type(data) == list, "type mismatch error"
        self.__tags = data

    @nworkers.setter
    def nworkers(self, data:int):
        assert type(data) == int, "type mismatch error"
        self.__nworkers = data

    @ngpus.setter
    def ngpus(self, data:int):
        assert type(data) == int, "type mismatch error"
        self.__ngpus = data

    @gpus_override.setter
    def gpus_override(self, data:bool):
        assert type(data) == bool, "type mistmatch error"
        self.__gpus_override = data

    @executor.setter
    def executor(self, data:Executor):
        assert type(data) == Executor, "type mismatch error"
        self.__executor = data

    def to_json(self):
        return {'executor': self.executor.value.to_json(),
                'workspace': self.workspace.to_json(),
                'models': self.models,
                'datasets': self.datasets,
                'tags': self.tags,
                'hptuning': self.hptuning.to_json(),
                'hyperparams': self.hparams.to_json(),
                'nworkers': self.nworkers,
                'ngpus': self.ngpus,
                }

    def from_json(self, data:dict):
        assert type(data) == dict, "type mismatch error"
        self.executor = Executor.from_str(data['executor']['choice'])
        self.executor.value.from_json(data['executor'])
        self.workspace.from_json(data['workspace'])
        self.models = data['models']
        self.datasets = data['datasets']
        self.tags = data['tags']
        self.hptuning.from_json(data['hptuning'])
        self.hparams.from_json(data['hyperparams'])
        self.nworkers = data.get('nworkers', 0)
        self.ngpus = data.get('ngpus', 0)

