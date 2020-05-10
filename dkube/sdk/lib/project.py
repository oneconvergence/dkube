from __future__ import print_function
import time
import sys

from dkube.sdk.internal import dkube_client
from dkube_client.rest import ApiException

from dkube_client.models.datum_model import DatumModel
from dkube_client.models.git_access_info import GitAccessInfo
from dkube_client.models.git_access_credentials import GitAccessCredentials

from pprint import pprint

class ProjectBase(object):
    def __init__(self):
        self.gitcreds = GitAccessCredentials(username=None, password=None, apikey=None, sshkey=None, private=True)
        self.gitaccess = GitAccessInfo(path=None, url=None, branch=None, credentials=self.gitcreds)
        self.datum = DatumModel(name=None, tags=None, _class='program', 
                                  dvs=None, source=None, url=None, remote=False, gitaccess=self.gitaccess)
