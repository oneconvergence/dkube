from __future__ import print_function
import time
import sys

from dkube.sdk.internal import dkube_client
from dkube_client.rest import ApiException

from dkube_client.models.datum_model import DatumModel
from dkube_client.models.git_access_info import GitAccessInfo
from dkube_client.models.git_access_credentials import GitAccessCredentials
from dkube_client.models.s3_access_credentials import S3AccessCredentials
from dkube_client.models.gcs_access_info import GCSAccessInfo
from dkube_client.models.gcs_access_info_secret import GCSAccessInfoSecret

from pprint import pprint

class ModelBase(object):
    def __init__(self):

        self.gcssecret = GCSAccessInfoSecret(name=None, content=None)
        self.gcsaccess = GCSAccessInfo(bucket=None, prefix=None, secret=self.gcssecret)

        self.s3access = S3AccessCredentials(access_key_id=None, access_key=None, bucket=None, prefix=None, endpoint=None)

        self.gitcreds = GitAccessCredentials(username=None, password=None, apikey=None, sshkey=None, private=True)
        self.gitaccess = GitAccessInfo(path=None, url=None, branch=None, credentials=self.gitcreds)

        self.datum = DatumModel(name=None, tags=None, _class='model', 
                                  dvs=None, source=None, url=None, remote=False, gitaccess=self.gitaccess,
                                  s3access=self.s3access, gcsaccess=self.gcsaccess)
