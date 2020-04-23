from . import *

def repo_create(user, repo, conn):
    req = Repository()

    req.type = repo['label']
    req.input.name = repo['name']
    req.input.url  = repo['source']['url']

    source = {'source': repo['source']['name']}
    if repo['source']['name'] == 'git':
        source.update({'gitaccess': {'url': req.input.url, 'credentials': repo['source']['auth']}})

    req.input.source = DatumSource.from_dict(source)
    req.input.tags = []
    req.input.remote = False

    post_REPO(conn, user, req)

    logger.info("User {} Repo {} created successfully \n".format(user, repo['name']))

    state, reason = wait_REPO(conn, user, repo['name'], repo['label'])

    logger.info("User {} Repo {} created with status {}, reason {} \n".format(user, repo['name'], state, reason))

    logger.info("Waiting for first version to get created....")

    if repo['label'] != 'program':
        wait_REPO_HEAD_VERSION(conn, user, repo['name'], repo['label'])

    logger.info("User {} Repo {} head version generated \n".format(user, repo['name']))


def repo_get(user, name, label, conn):
    repo = get_REPO(conn, user, name, label)
    logger.debug("Repo -> {}".format(repo.to_json()))
    return repo

def repo_list(user, label, conn):
    repos = list_REPOS(conn, user, label)
    logger.debug("Repos -> {}".format(repos))
    for repo in repos:
        logger.debug("Repo -> {}".format(repo.name))
    return repos

def repo_delete(user, name, conn):
    pass

def versions_list(user, label, name, conn):
    vers = list_VERSIONS(conn, user, label, name)
    logger.debug("Versions -> {}".format(vers))
    for ver in vers:
        logger.debug("Version -> {}".format(ver.name))
    return vers

