import time

from . import *
from .rest import *
from .schema import *

def post_RUN(conn, user, job:DkubeJob):
    url = "{}/dkube/v2/controller/users/{}/jobs".format(conn.url, user)
    post(url, conn['token'], data=job.to_json())

def wait_training_RUN(conn, user, name):
    state = State.UNKNOWN.value
    reason = 'unknown'
    while State.is_final_state(state) == False:
        time.sleep(10)
        job = get_training_RUN(conn, user, name)
        state = job.params.value.generated.status.state.value
        reason = job.params.value.generated.status.reason
        logger.info("user {}, job {}, state {}, reason {}".format(user, name, state, reason))

    return state, reason

def get_training_RUN(conn,  user, name):
    url = "{}/dkube/v2/controller/users/{}/jobs/class/{}/job/{}/collection".format(conn.url, user, "training", name)
    data = get(url, conn['token'], query='run=true')
    return DkubeJob().from_json(data['data']['job'])

def list_RUNS(conn, user):
    url = "{}/dkube/v2/controller/users/{}/jobs/class/{}/".format(conn.url, user, "any")
    data = get(url, conn['token'], query='shared=false&run=true&all=true')
    runs = []
    for run in data['data'][0]['jobs']:
        job = DkubeJob().from_json(run)
        runs.append(job)
    return runs

def post_REPO(conn, user, repo:Repository):
    url = "{}/dkube/v2/controller/users/{}/datums".format(conn.url, user)
    post(url, conn['token'], data=repo.to_json())

def wait_REPO(conn, user, name, label):
    state = State.UNKNOWN.value
    reason = 'unknown'
    while State.is_final_state(state) == False:
        time.sleep(10)
        program = get_REPO(conn, user, name, label)
        state = program.generated.status.state.value
        reason = program.generated.status.reason
        logger.info("user {}, repo {}, state {}, reason {}".format(user, name, state, reason))

    return state, reason

def get_REPO(conn, user, name, label):
    url = "{}/dkube/v2/controller/users/{}/datums/class/{}/datum/{}".format(conn.url, user, label, name)
    data = get(url, conn['token'], query='run=true')
    return Repository().from_json(data['data']['datum'])

def list_REPOS(conn, user, label):
    url = "{}/dkube/v2/controller/users/{}/datums/class/{}/".format(conn.url, user, label)
    data = get(url, conn['token'], query='shared=false')
    repos = []
    for repo in data['data'][0]['datums']:
        program = Repository().from_json(repo)
        repos.append(program)
    return repos

def wait_REPO_HEAD_VERSION(conn, user, name, label):
    vers = []
    while len(vers) == 0:
        logger.info("user {}, repo {} - checking if version is generated \n".format(user, name))
        time.sleep(10)
        vers = list_VERSIONS(conn, user, label, name)

    logger.info("user {}, repo {}, version {} generated".format(user, name, vers[0].index))

def list_VERSIONS(conn, user, label, name):
    url = "{}/dkube/v2/controller/users/{}/datums/class/{}/datum/{}".format(conn.url, user, label, name)
    data = get(url, conn['token'], query='run=true')
    versions = []
    for ver in data['data']['versions']:
        version = Version().from_json(ver['version'])
        versions.append(version)
    return versions
