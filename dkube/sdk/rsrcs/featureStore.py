import json
import os

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from dkube.sdk.internal import api_base, dkube_api
from dkube.sdk.internal.dkube_api.models.datum_model import DatumModel
from dkube.sdk.internal.dkube_api.models.datum_model_k8svolume import \
    DatumModelK8svolume
from dkube.sdk.internal.dkube_api.models.gcs_access_info import GCSAccessInfo
from dkube.sdk.internal.dkube_api.models.git_access_credentials import \
    GitAccessCredentials
from dkube.sdk.internal.dkube_api.models.git_access_info import GitAccessInfo
from dkube.sdk.internal.dkube_api.models.nfs_access_info import NFSAccessInfo
from dkube.sdk.internal.dkube_api.models.redshift_access_info import \
    RedshiftAccessInfo
from dkube.sdk.internal.dkube_api.models.repo_gcs_access_info_secret import \
    RepoGCSAccessInfoSecret
from dkube.sdk.internal.dkube_api.models.s3_access_credentials import \
    S3AccessCredentials
from dkube.sdk.rsrcs import *


class FeatureStore(object):
    FEATURESTORE_SOURCES = ["dvs", "git", "aws_s3",
                            "s3", "gcs", "nfs", "redshift", "k8svolume"]

    def __init__(self, config_file=None, user, name=generate("featurestore"), tags=None):
        self.CONFIG_FILE = config_file
        self.configuration = api_base.ApiBase.configuration
        self.k8svolume = DatumModelK8svolume(name=None)

        self.redshift = RedshiftAccessInfo(
            endpoint=None, username=None, password=None, database=None, region=None, cacert=None, insecure_ssl=None)

        self.nfsaccess = NFSAccessInfo(server=None, path=None)

        self.gcssecret = RepoGCSAccessInfoSecret(name=None, content=None)
        self.gcsaccess = GCSAccessInfo(
            bucket=None, prefix=None, secret=self.gcssecret)

        self.s3access = S3AccessCredentials(
            access_key_id=None, access_key=None, bucket=None, prefix=None, endpoint=None)

        self.gitcreds = GitAccessCredentials(
            username=None, password=None, apikey=None, sshkey=None, private=True)
        self.gitaccess = GitAccessInfo(
            path=None, url=None, branch=None, credentials=self.gitcreds)

        self.datum = DatumModel(name=None, tags=None, _class='dataset',
                                dvs=None, source='dvs', url=None, remote=False, gitaccess=self.gitaccess,
                                s3access=self.s3access, nfsaccess=self.nfsaccess, gcsaccess=self.gcsaccess)

        self.update_basic(user, name, tags)

    def update_basic(self, user, name, tags):
        tags = list_of_strs(tags)

        self.user = user
        self.name = name

        self.datum.name = name
        self.datum.tags = tags

    def update_dataset_source(self, source=DATASET_SOURCES[0]):
        """
            Method to update the source for this dataset.
            It should be one of the choice mentioned in DATASET_SOURCES
            Default value is **git**
        """
        self.datum.source = source

    def list_fs(self):
        fs = []
        try:
            with open(self.CONFIG_FILE) as json_file:
                fsconfig = json.load(json_file)
            featuresets = fsconfig["inputs"]["featuresets"]
            for each_feature in featuresets:
                fs.append([each_feature["name"], each_feature["location"]])
            return fs
        except Exception as e:
            return e

    def read(self, featureset, path=None):
        df_empty = pd.DataFrame({'A': []})
        if path is None and self.CONFIG_FILE is None:
            return return {"data": df_empty, "status": -1, "error": "Path of featureset not found"}
        if path is None:
            with open(self.CONFIG_FILE) as json_file:
                fsconfig = json.load(json_file)
            featuresets = fsconfig["inputs"]["featuresets"]
            for each_feature in featuresets:
                if each_feature["name"] == featureset:
                    path = each_feature["location"]
        if path is None:
            return {"data": df_empty, "status": -1, "error": "Featureset doesn't exist"}
        try:
            table = pq.read_table(os.path.join(path, 'example.parquet'))
            feature_df = table.to_pandas()
            return {"data": feature_df, "status": 0, "error": None}
        except Exception as e:
            return {"data": df_empty, "status": -1, "error": e}

    def write(self, dataframe, featureset, path=None):
        if path is None and self.CONFIG_FILE is None:
            return return {"status": -1, "error": "Path of featureset not found"}
        if path is None:
            with open(self.CONFIG_FILE) as json_file:
                fsconfig = json.load(json_file)
            featuresets = fsconfig["outputs"]["featuresets"]
            for each_feature in featuresets:
                if each_feature["name"] == featureset:
                    path = each_feature["location"]
        if path is None:
            return {"status": -1, "error": "Featureset doesn't exist"}
        try:
            table = pa.Table.from_pandas(dataframe)
            pq.write_table(table, os.path.join(path, 'example.parquet'))
            return {"status": 0, "error": None}
        except Exception as e:
            return {"status": -1, "error": e}

    def commit(self, featureset, path=None):
        if path is None and self.CONFIG_FILE is None:
            return return {"error": "Path of featureset not found"}
        if path is None:
            with open(self.CONFIG_FILE) as json_file:
                fsconfig = json.load(json_file)
            featuresets = fsconfig["outputs"]["featuresets"]
            for each_feature in featuresets:
                if each_feature["name"] == featureset:
                    path = each_feature["location"]
        if path is None:
            return {"status": -1, "error": "Featureset doesn't exist"}
        api = dkube_api.DkubeApi(dkube_api.ApiClient(self.configuration))
        response = api.featureset_commit_version(featureset, path)
        return {"error": response}

    def update_git_details(self, url, branch=None, authopt=GIT_ACCESS_OPTS[0], authval=None):
        """
            Method to update the details of git datasource.

            *Inputs*

                url
                    A valid Git URL. Following are considered as valid URLs.

                    - CloneURL : https://github.com/oneconvergence/dkube.git

                    - TreeURL : https://github.com/oneconvergence/dkube/tree/2.1.dev/dkube

                    - BlobURL : https://github.com/oneconvergence/dkube/blob/2.1.dev/dkube/sdk/api.py

                    - ZipURL : https://github.com/oneconvergence/dkube/archive/2.1.dev.zip

                branch
                    Valid branch of git repo. If not provided then **master** branch is used by default.

                authopt
                    One of the valid option from **GIT_ACCESS_OPTS**

                authval
                    Value corresponding to the authopt
        """

        self.datum.source = "git"
        self.datum.url = url
        self.gitaccess.url = url
        self.gitaccess.branch = branch

        self.gitcreds.username = self.user

        if authopt == 'apikey':
            self.gitcreds.apikey = authval
        elif authopt == 'password':
            self.gitcreds.password = authval
        elif authopt == 'sshkey':
            self.gitcreds.sshkey = authval

    def update_awss3_details(self, bucket, prefix, key, secret):
        """
            Method to update details of aws s3 data source.

            *Inputs*

                bucket
                    Valid bucket in aws s3

                prefix
                    Path to an object in the bucket. Dkube will fetch recursively all objects under this prefix.

                key
                    AWS s3 access key id

                secret
                    AWS s3 access key secret
        """

        self.datum.source = "aws_s3"
        self.s3access.bucket = bucket
        self.s3access.prefix = prefix
        self.s3access.access_key_id = key
        self.s3access.access_key = secret

    def update_s3_details(self, endpoint, bucket, prefix, key, secret):
        """
            Method to update details of s3 data source like minio.

            *Inputs*

                bucket
                    Valid bucket name in s3 store

                prefix
                    Path to an object in the bucket. Dkube will fetch recursively all objects under this prefix.

                key
                    S3 access key id

                secret
                    s3 access key secret
        """

        self.datum.source = "s3"
        self.s3access.endpoint = endpoint
        self.s3access.prefix = prefix
        self.s3access.bucket = bucket
        self.s3access.access_key_id = key
        self.s3access.access_key = secret

    def update_gcs_details(self, bucket, prefix, key, secret):
        """
            Method to update details of google cloud storage.

            *Inputs*

                bucket
                    Valid bucket in GCS

                prefix
                    Path to an object in bucket. Dkube will fetch recursively all objects under this prefix.

                key
                    Name of the GCS secret

                secret
                    Content of the secret
        """

        self.datum.source = "gcs"
        self.gcsaccess.bucket = bucket
        self.gcsaccess.prefix = prefix
        self.gcssecret.name = key
        self.gcssecret.content = secret

    def update_nfs_details(self, server, path="/"):
        """
            Method to update details of nfs data source.

            *Inputs*

                server
                    IP address of the nfs server.

                path
                    Path in the nfs export. This path is directly mounted for the user program.

        """

        self.datum.source = "nfs"
        self.nfsaccess.path = path
        self.nfsaccess.server = server

    def update_redshift_details(self, endpoint, password, database, region):
        self.datum.source = "redshift"
        self.redshift.endpoint = endpoint
        self.redshift.username = self.user
        self.redshift.password = password
        self.redshift.database = database
        self.redshift.region = region
        self.insecure_ssl = True

    def update_k8svolume_details(self, name):
        """
            Method to update details of k8s volume data source.

            *Inputs*

                name
                    Name of the kubernetes volume. Volume should not be already **Bound**.
        """

        self.datum.source = "k8svolume"
        self.k8svolume.name = name
