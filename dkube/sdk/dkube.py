from .defs import *
from .conn import *

from .lib.run import *
from .lib.repo import *

def create_run(user, run:Run, conn=Connection()):
    assert type(run) == Run, "Invalid type argument run"
    run_create(user, run, conn=conn)

def get_run(user, name, conn=Connection()):
    return run_get(user, name, conn=conn)

def list_run(user, conn=Connection()):
    return run_list(user, conn=conn)

def delete_run(user, name, conn=Connection()):
    run_delete(name,user,  conn=conn)

def create_repo(user, repo, conn=Connection()):
    assert type(repo) == ProjectRepo or DatasetRepo or ModelRepo, "Invalid type for repo argument"
    repo_create(user, repo, conn=conn)

def get_repo(user, name, label, conn=Connection()):
    if label == 'project': label = 'program'
    assert label in ['program', 'dataset', 'repo'], "Invalid label type {}".format(label)
    return repo_get(user, name, label, conn=conn) 

def list_repo(user, label, conn=Connection()):
    if label == 'project': label = 'program'
    assert label in ['program', 'dataset', 'repo'], "Invalid label type {}".format(label)
    return repo_list(user, label, conn=conn)

def delete_repo(user, name, label, conn=Connection()):
    if label == 'project': label = 'program'
    assert label in ['program', 'dataset', 'repo'], "Invalid label type {}".format(label)
    repo_delete(user, name, label, conn=conn)

def list_versions(user, repo, conn=Connection()):
    assert type(repo) == ProjectRepo or DatasetRepo or ModelRepo, "Invalid type for repo argument"
    return versions_list(user, repo['label'], repo['name'], conn=conn)
