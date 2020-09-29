from __future__ import print_function
import time
import sys

from dkube.sdk.internal import dkube_api
from dkube.sdk.internal.dkube_api.rest import ApiException

from dkube.sdk.internal.dkube_api.models.datum_model import DatumModel
from dkube.sdk.internal.dkube_api.models.git_access_info import GitAccessInfo
from dkube.sdk.internal.dkube_api.models.git_access_credentials import GitAccessCredentials
from dkube.sdk.internal.dkube_api.models.s3_access_credentials import S3AccessCredentials
from dkube.sdk.internal.dkube_api.models.gcs_access_info import GCSAccessInfo
from dkube.sdk.internal.dkube_api.models.repo_gcs_access_info_secret import RepoGCSAccessInfoSecret
from dkube.sdk.internal.dkube_api.models.nfs_access_info import NFSAccessInfo
from dkube.sdk.internal.dkube_api.models.redshift_access_info import RedshiftAccessInfo
from dkube.sdk.internal.dkube_api.models.datum_model_k8svolume import DatumModelK8svolume

from pprint import pprint

from .util import *

class DkubeDataset(object):
    DATASET_SOURCES = ["dvs", "git", "aws_s3",
                       "s3", "gcs", "nfs", "redshift", "k8svolume"]
    GIT_ACCESS_OPTS = ["apikey", "sshkey", "password"]

    def __init__(self, user, name=generate("dataset"), tags=None):
        self.k8svolume = DatumModelK8svolume(name=None)

        self.redshift = RedshiftAccessInfo(
            endpoint=None, username=None, password=None, database=None, region=None, cacert=None, insecure_ssl=None)

        self.nfsaccess = NFSAccessInfo(server=None, path=None)

        self.gcssecret = GCSAccessInfoSecret(name=None, content=None)
        self.gcsaccess = GCSAccessInfo(
            bucket=None, prefix=None, secret=self.gcssecret)

        self.s3access = S3AccessCredentials(
            access_key_id=None, access_key=None, bucket=None, prefix=None, endpoint=None)

        self.gitcreds = GitAccessCredentials(
            username=None, password=None, apikey=None, sshkey=None, private=True)
        self.gitaccess = GitAccessInfo(
            path=None, url=None, branch=None, credentials=self.gitcreds)

        self.datum = DatumModel(name=None, tags=None, _class='dataset',
                                dvs=None, source=None, url=None, remote=False, gitaccess=self.gitaccess,
                                s3access=self.s3access, nfsaccess=self.nfsaccess, gcsaccess=self.gcsaccess)

        self.update_basic(user, name, tags)

    def update_basic(self, user, name, tags):
        self.user = user
        self.name = name

        self.datum.name = name
        self.datum.tags = tags

    def update_dataset_source(self, source=DATASET_SOURCES[0]):
        self.datum.source = source

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

    def update_awss3_details(self, bucket, prefix, key, secret):
        self.s3access.bucket = bucket
        self.s3access.prefix = prefix
        self.s3access.access_key_id = key
        self.s3access.access_key = secret

    def update_s3_details(self, endpoint, bucket, prefix, key, secret):
        self.s3access.endpoint = endpoint
        self.s3access.prefix = prefix
        self.s3access.bucket = bucket
        self.s3access.access_key_id = key
        self.s3access.access_key = secret

    def update_gcs_details(self, bucket, prefix, key, secret):
        self.gcsaccess.bucket = bucket
        self.gcsaccess.prefix = prefix
        self.gcssecret.name = key
        self.gcssecret.content = secret

    def update_nfs_details(self, server, path="/"):
        self.nfsaccess.path = path
        self.nfsaccess.server = server

    def update_redshift_details(self, endpoint, password, database, region):
        self.redshift.endpoint = endpoint
        self.redshift.username = self.user
        self.redshift.password = password
        self.redshift.database = database
        self.redshift.region = region
        self.insecure_ssl = True

    def update_k8svolume_details(self, name):
        self.k8svolume.name = name
