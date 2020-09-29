from __future__ import print_function
from pprint import pprint

import sys
import time

from dkube.sdk.internal import dkube_api
from dkube.sdk.internal.dkube_api.models.git_access_credentials import GitAccessCredentials
from dkube.sdk.internal.dkube_api.models.git_access_info import GitAccessInfo
from dkube.sdk.internal.dkube_api.models.datum_model import DatumModel
from dkube.sdk.internal.dkube_api.rest import ApiException

from .util import *

class DkubeProject(object):
    GIT_ACCESS_OPTS = ["apikey", "sshkey", "password"]

    def __init__(self, user, name=generate("project"), tags=None):
        self.gitcreds = GitAccessCredentials(
            username=None, password=None, apikey=None, sshkey=None, private=True)
        self.gitaccess = GitAccessInfo(
            path=None, url=None, branch=None, credentials=self.gitcreds)
        self.datum = DatumModel(name=None, tags=None, _class='program',
                                dvs=None, source='git', url=None, remote=False, gitaccess=self.gitaccess)

        self.update_basic(user, name, tags)

    def update_basic(self, user, name, tags):
        self.user = user
        self.name = name

        self.datum.name = name
        self.datum.tags = tags

    def update_git_details(self, url, branch=None, authopt=GIT_ACCESS_OPTS[0], authval=None):
        self.datum.url = url
        self.gitaccess.url = url
        self.gitaccess.branch = branch

        self.gitcreds.username = self.user

        if authmode == 'apikey':
            self.gitcreds.apikey = authval
        elif authmode == 'password':
            self.gitcreds.password = authval
        elif authmode == 'sshkey':
            self.gitcreds.sshkey = authval
