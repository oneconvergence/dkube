from . import *
from .helpers import *
from .schema import *

DKUBE_CONTAINERS = ["docker.io/ocdr/dkube-datascience-tf-cpu:v1.13",
                    "docker.io/ocdr/dkube-datascience-tf-cpu:v1.14",
                    "docker.io/ocdr/dkube-datascience-tf-gpu:v1.13",
                    "docker.io/ocdr/dkube-datascience-tf-gpu:v1.14"]

def run_create(user, run, conn):
    job = DkubeJob()
    job.name = run['name']
    job.params = JobParams.TRAINING

    training = job.params.value

    executor = 'custom'
    logger.debug('Run -> {}'.format(run))
    if run['container']['image'] in DKUBE_CONTAINERS:
        executor = 'dkube'
   
    training.input.executor.from_str(executor)
    if executor == 'dkube':
        training.input.executor.value.framework.value.version = run['container']['image'].split(':')[1]

    for ip in run['inputs']:
        if ip['clazz'] == 'project':
            training.input.workspace.data.name = '{}:{}'.format(user, ip['name'])
            training.input.workspace.script = run['script']

        if ip['clazz'] == 'dataset':
            training.input.datasets.append({'name':'{}:{}'.format(user, ip['name']), 'version': ip['version'], 'mountpath': ip['mountpath']})

        if ip['clazz'] == 'model':
            training.input.models.append({'name':'{}:{}'.format(user, ip['name']), 'version': ip['version'], 'mountpath': ip['mountpath']})

    for op in run['outputs']:
        training.input.outputs.append({'name':'{}:{}'.format(user, op['name']), 'mountpath': op['mountpath']})

    training.input.tags = run['tags']

    post_RUN(conn, user, job)

    logger.info("User {} Job {} created successfully \n".format(user, job.name))

    state, reason = wait_training_RUN(conn, user, job.name)
    logger.info("User {} Job {} finished with status {}, reason {} \n".format(user, runname, state, reason))


def run_get(user, name, conn):
    run = get_training_RUN( conn, user, name)
    logger.debug("Run -> {}".format(run.to_json()))

def run_list(user, conn):
    runs = list_RUNS(conn, user)
    logger.debug("Runs -> {}".format(runs))
    for run in runs:
        logger.debug("Class -> {}".format(run.name))

def run_delete(user, name, conn):
    pass
