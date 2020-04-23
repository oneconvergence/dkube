import enum
import random
import string

generate = lambda hint: "{}-{}".format(hint, ''.join([random.choice(string.digits) for n in range(4)]))

class Container(dict):
    def __init__(self, image, user='', password=''):
        super().__init__(image=image, user=user, password=password)

class Repo(dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class ProjectRef(Repo):
    def __init__(self, name, version='', mount=''):
        super().__init__(clazz='project', name=name, version=version, mountpath=mount)

class DatasetRef(Repo):
    def __init__(self, name, version='', mount=''):
        super().__init__(clazz='dataset', name=name, version=version, mountpath=mount)

class ModelRef(Repo):
    def __init__(self, name, version='', mount=''):
        super().__init__(clazz='model', name=name, version=version, mountpath=mount)

class Inputs(list):
    def add(self, repo):
        assert isinstance(repo, Repo), "Invalid value passed to repo"
        super().append(repo)

class Outputs(list):
    def add(self, repo):
        assert isinstance(repo, Repo), "Invalid value passed to repo"
        super().append(repo)

class Envs(list):
    def add(self, key:str, value:str):
        super().append({key:value})

class DKUBEContainers(enum.Enum):
    DKUBE_DATASCIENCE_TF_CPU_1_13 = Container("docker.io/ocdr/dkube-datascience-tf-cpu:v1.13")
    DKUBE_DATASCIENCE_TF_CPU_1_14 = Container("docker.io/ocdr/dkube-datascience-tf-cpu:v1.14")
    DKUBE_DATASCIENCE_TF_GPU_1_13 = Container("docker.io/ocdr/dkube-datascience-tf-gpu:v1.13")
    DKUBE_DATASCIENCE_TF_GPU_1_14 = Container("docker.io/ocdr/dkube-datascience-tf-gpu:v1.14")

class Config(dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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
    DISTRIBUTION_STRATEGY_DEFAULT = 'manual'


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

class Run(dict):
    def __init__(self, name=generate('run')):
        self.__name = name
        super().__init__(name=name)
        self._defaults()

    def _defaults(self):
        self.update(tags=[])
        self.update(container=DKUBEContainers.DKUBE_DATASCIENCE_TF_CPU_1_13.value)
        self.update(script="")
        self.update(envs=Envs())
        self.update(inputs=Inputs())
        self.update(outputs=Outputs())
        self.update(config=Config())
        self.update(gpus=0)
        self.update(distribution=DistributionStrategy.DISTRIBUTION_STRATEGY_NONE)
        self.update(worker=0)

    def add_tags(self, value:list):
        assert type(value) == list, "Invalid type for tags, must be a list"
        self.update(tags=value)

    def add_container(self, value:Container):
        assert type(value) == Container, "Invalid type of container value"
        self.update(container=value)

    def add_script(self, value:str):
        assert type(value) == str, "Invalid type of script value"
        self.update(script=value)

    def add_env(self, key:str, value:str):
        assert type(key) == str or type(value) == str, "Invalid type for key/val both must be strings"
        self['envs'].add(dict(key, value))

    def add_input_project(self, project:ProjectRef):
        assert type(project) == ProjectRef, "Invalid type for project argument"
        self['inputs'].add(project)

    def add_input_dataset(self, dataset:DatasetRef):
        assert type(dataset) == DatasetRef, "Invalid type for dataset argument"
        self['inputs'].add(dataset)

    def add_input_model(self, model:ModelRef):
        assert type(model) == ModelRef, "Invalid typr for model argument"
        self['inputs'].add(model)

    def add_output_dataset(self, dataset:DatasetRef):
        assert type(dataset) == DatasetRef, "Invalid type for dataset argument"
        self['outputs'].add(dataset)

    def add_output_model(self, model:ModelRef):
        assert type(model) == ModelRef, "Invalid type for model argument"
        self['outputs'].add(model)

    def add_config(self, name:str, content:str):
        assert valid_json(content), "Invalid type for content argument, must be a valid json str"
        self.update(config=Config(name=name, content=content))

class GitAuth(dict):
    def __init__(self, private=False, apikey='', sshkey='', username='', password=''):
        super().__init__(private=private, apikey=apikey, sshkey=sshkey, username=username, password=password)

class Github(dict):
    def __init__(self, url, branch, auth=GitAuth()):
        assert type(auth) == GitAuth, "Invalid type of argument auth"
        super().__init__(name='git', url=url, branch=branch, auth=auth)

class BitBucket(dict):
	def __init__(self, url, branch, auth=GitAuth()):
		assert type(auth) == GitAuth, "Invalid type of argument auth"
		super().__init__(name='git', url=url, branch=branch, auth=auth)

class AWSS3(dict):
	def __init__(self, bucket, prefix, key, secret, remote=False):
	    super().__init__(name='awss3', bucket=bucket, prefix=prefix, key=key, secret=secret, remote=remote)

class DVS(dict):
	def __init__(self):
	    super().__init__(name='dvs', url='')

class SupportedDataSourceTypes(enum.Enum):
    DATA_SOURCE_GITHUB = 'git'
    DATA_SOURCE_BITBUCKET = 'git'
    DATA_SOURCE_AWS_S3 = 'awss3'
    DATA_SOURCE_DVS = 'dvs'

class ProjectRepo(dict):
	def __init__(self, label='program', name=generate('project'), source=DVS()):
		assert source['name'] in [s.value for s in SupportedDataSourceTypes], "Invalid source {}".format(source.name)
		self.update(label=label, name=name, source=source)

class DatasetRepo(dict):
	def __init__(self, label='dataset', name=generate('dataset'), source=DVS()):
	    assert source['name'] in [s.value for s in SupportedDataSourceTypes], "Invalid source {}".format(source.name)
	    self.update(label=label, name=name, source=source)

class ModelRepo(dict):
	def __init__(self, label='model', name=generate('model'), source=DVS()):
	    assert source['name'] in [s.value for s in SupportedDataSourceTypes], "Invalid source {}".format(source.name)
	    self.update(label=label, name=name, source=source)

