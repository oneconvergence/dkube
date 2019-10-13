import sys

#import logging
#logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
#logger = logging.getLogger(__name__)

from .lib import logger

from .env import *
from .schema import *
from ._types import *
from ._helpers import *

def launch_training_job(name:str, autogenerate=False,
                        environ=Environment().internal,
                        framework:Framework=Framework.Tensorflow,
                        tags=[],
                        container:ContainerImageDetails=ContainerImage.DKUBE_DS_TF_CPU_1_14,
                        workspace:str='',
                        script:str='',
                        models:list=[],
                        datasets:list=[],
                        hptuning:str='',
                        steps:int=100,
                        batchsize:int=100,
                        epochs:int=1,
                        customkv:dict={},
                        ngpus:int=0,
                        distributeopts:DistributeOpts=DistributeOpts()):
    assert name != '', "name cannot be empty, with name-auto-generate=True, name will be used as prefix"

    if autogenerate==True:
        name = "{}-{}".format(name, generate_version())

    job = DkubeJob()
    job.name = name
    job.params = JobParams.TRAINING
 
    training = job.params.value

    executor = container.value.executor
    training.input.executor.from_str(executor)

    if executor == ExecutorType.Dkube.value:
        training.input.executor.value.framework.value.version = container.value.tag

    if workspace != '':
        training.input.workspace.program = '{}:{}'.format(environ.user,workspace)

    training.input.workspace.script = script

    models = ['{}:{}'.format(environ.user, model) for model in models]
    training.input.models = models

    datasets = ['{}:{}'.format(environ.user, dataset) for dataset in datasets]
    training.input.datasets = datasets

    training.input.tags = tags

    if hptuning != '':
        training.input.hptuning.name = 'hptuning.json'
        training.input.hptuning.body = hptuning

    training.input.hparams.epochs = epochs
    training.input.hparams.steps  = steps
    training.input.hparams.batchsize = batchsize
    if customkv != {}:
        training.input.hparams.customkv  = [customkv]

    training.input.ngpus = ngpus

    training.input.nworkers = distributeopts.workers
    training.input.gpus_override = distributeopts.strategy == DistributionStrategy.DISTRIBUTION_STRATEGY_AUTO

    create_training_job(environ, job)
    logger.info("User {} Job {} created successfully \n".format(environ.user, job.name))

    state, reason = wait_for_training_job(environ, name)
    logger.info("User {} Job {} finished with status {}, reason {} \n".format(environ.user, job.name, state, reason))



def export_model(fspath:str, name:str, autogenerate=False,
                 environ=Environment().internal, 
                 framework:Framework=Framework.Tensorflow):

    assert fspath != '', "file system path cannot be empty"
    assert name != '', "name cannot be empty, with name-auto-generate=True, name will be used as prefix"

    if autogenerate==True:
        version = ""
        if framework == Framework.Tensorflow:
            #extract version from fspath
            version = get_tfmodel_version(fspath)
        if version == "":
            version = generate_version()
        name = "{}-{}".format(name, version)

    #upload data to dkube storage
    upload_to_dkube(environ, fspath, name)

    logger.info("data uploaded to dkube storage sucessfully")

    #create a model in dkube database
    model = Model()
    model.input.name    = name
    model.input.url     = "/model/{}".format(name)
    model.input.source  = DatumSource.dkube
    model.input.tags    = []
    model.input.remote  = False

    create_model(environ, model) 

    logger.debug("model created successfully in dkube")

