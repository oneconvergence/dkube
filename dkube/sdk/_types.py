import enum

class Framework(enum.Enum):
    Custom      = "custom"
    Tensorflow  = "tensorflow"

class ExecutorType(enum.Enum):
    Dkube       = "dkube"
    Custom      = "custom"

    @staticmethod
    def from_str(label:str):
        if label =="dkube":
            return Executor.Dkube
        elif label == "custom":
            return Executor.Custom
        else:
            raise NotImplementedError

class ContainerImageDetails(object):
    def __init__(self, executor=ExecutorType.Dkube, path='', user='', password=''):
        self.__executor = executor
        self.__path = path
        self.__user = user
        self.__password = password

    @property
    def path(self):
        return self.__path
    @property
    def user(self):
        return self.__user
    @property
    def password(self):
        return self.__password
    @property
    def executor(self):
        return self.__executor.value
    @property
    def tag(self):
        try:
            return self.path.split(':')[1]
        except IndexError:
            return ''

    @path.setter
    def path(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__path = data

    @user.setter
    def user(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__user = data

    @password.setter
    def password(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__password = data

    @executor.setter
    def executor(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__executor = Executor.from_str(data)

    def from_dict(self, data:dict):
        assert type(data) == dict, "type mismatch error"
        #MAK - TODO - can we use the same keys in pipeline component def too?
        self.path = data['image']
        self.user = data.get('username', '')
        self.password = data.get('password', '')

    def to_dict(self):
        return {'image': self.path, 'username': self.user, 'password': self.password}

class ContainerImage(enum.Enum):
    DKUBE_DS_TF_CPU_1_13 = ContainerImageDetails(executor=ExecutorType.Dkube, path="docker.io/ocdr/dkube-datascience-tf-cpu:v1.13")
    DKUBE_DS_TF_CPU_1_14 = ContainerImageDetails(executor=ExecutorType.Dkube, path="docker.io/ocdr/dkube-datascience-tf-cpu:v1.14")
    DKUBE_DS_TF_GPU_1_13 = ContainerImageDetails(executor=ExecutorType.Dkube, path="docker.io/ocdr/dkube-datascience-tf-gpu:v1.13")
    DKUBE_DS_TF_GPU_1_14 = ContainerImageDetails(executor=ExecutorType.Dkube, path="docker.io/ocdr/dkube-datascience-tf-gpu:v1.14")
    CUSTOM_IMAGE         = ContainerImageDetails(executor=ExecutorType.Custom, path="docker.io/unknown/unknown:unknown")

    @staticmethod
    def from_dict(data:dict):
        if "ocdr/dkube-datascience-tf-cpu:v1.13" in data['image']:
            return ContainerImage.DKUBE_DS_TF_CPU_1_13
        elif "ocdr/dkube-datascience-tf-cpu:v1.14" in data['image']:
            return ContainerImage.DKUBE_DS_TF_CPU_1_14
        elif "ocdr/dkube-datascience-tf-gpu:v1.13" in data['image']:
            return ContainerImage.DKUBE_DS_TF_GPU_1_13
        elif "ocdr/dkube-datascience-tf-gpu:v1.14" in data['image']:
            return ContainerImage.DKUBE_DS_TF_GPU_1_14
        else:
            ci = ContainerImage.CUSTOM_IMAGE
            ci.value.from_dict(data)
            return ci

    @staticmethod
    def tensorflow(ver='1.14', gpu=False):
        if ver == '1.14':
            return ContainerImage.DKUBE_DS_TF_CPU_1_14 if gpu == False else ContainerImage.DKUBE_DS_TF_GPU_1_14
        elif ver == '1.13':
            return ContainerImage.DKUBE_DS_TF_CPU_1_13 if gpu == False else DKUBE_DS_TF_GPU_1_13
        else:
            raise NotImplementedError


class DistributionStrategy(enum.Enum):
    """
    Used when distributed training is not intended.
    """
    DISTRIBUTION_STRATEGY_NONE = 'None'

    """
    Strategy is applied based on the chosen training framework.
    TF_CONFIG based distribution is applied if framework == tensorflow
    MPI Job based distribution is applied if framework == custom
    """
    DISTRIBUTION_STRATEGY_DEFAULT = 'default'


    """
    Same as DISTRIBUTION_STRATEGY_DEFAULT but only difference is Dkube will auto adjust the requested GPU count
    based on the availability in the cluster.
    If no gpus(s) are availabled then Dkube will choose to run without gpus.
    Program must not assume availability of GPU device when this option is chosen.
    """
    DISTRIBUTION_STRATEGY_AUTO = 'auto'

    """
    This will supported in future,
    and will be based on https://www.tensorflow.org/guide/distributed_training#using_tfdistributestrategy_with_keras
    This strategy definition can be used when framework == tensorflow
    """
    DISTRIBUTION_STRATEGY_TF = 'unsupported'

    @staticmethod
    def from_str(label:str):
        if label == 'default':
            return DistributionStrategy.DISTRIBUTION_STRATEGY_DEFAULT
        elif label == 'auto':
            return DistributionStrategy.DISTRIBUTION_STRATEGY_AUTO
        else:
            raise NotImplementedError


class DistributeOpts(object):
    def __init__(self):
        self.__workers = 0
        self.__ps = self.__workers
        self.__strategy = DistributionStrategy.DISTRIBUTION_STRATEGY_NONE

    @property
    def workers(self):
        return self.__workers
    @property
    def ps(self):
        return self.__ps
    @property
    def strategy(self):
        return self.__strategy

    @workers.setter
    def workers(self, data:int):
        assert type(data) == int, "type mismatch error"
        self.__workers =data

    @ps.setter
    def ps(self, data:int):
        raise NotImplementedError

    @strategy.setter
    def strategy(self, data:enum.Enum):
        assert type(data) == enum.Enum, "type mismatch error"
        self.__strategy = data

    def from_dict(self, data:dict):
        assert type(data) == dict, "type mismatch error"
        self.workers = data['workers']
        self.strategy = DistributionStrategy.from_str(data['strategy'])
