from __future__ import print_function

import os
import time
from pprint import pprint

from dkube.sdk.internal import dkube_api
from dkube.sdk.internal.dkube_api.models.feature_set_commit_def import \
    FeatureSetCommitDef
from dkube.sdk.internal.dkube_api.models.feature_set_commit_def_job import \
    FeatureSetCommitDefJob
from dkube.sdk.internal.dkube_api.models import *
from dkube.sdk.rsrcs.featureset import DKubeFeatureSetUtils
from dkube.sdk.internal.dkube_api.rest import ApiException
from dkube.sdk.rsrcs.util import list_of_strs
from url_normalize import url_normalize

# Configure API key authorization: d3apikey
configuration = dkube_api.Configuration()
configuration.api_key_prefix['Authorization'] = 'Bearer'


class ApiBase(object):

    def __init__(self, url, token, common_tags):
        configuration.host = url_normalize(
            '{}/dkube/v2/controller'.format(url))
        configuration.api_key['Authorization'] = token
        configuration.verify_ssl = False
        self._api = dkube_api.DkubeApi(dkube_api.ApiClient(configuration))
        self.common_tags = list_of_strs(common_tags)
        
    def update_tags (self, resource):
        if len(self.common_tags):
            if resource.tags:
                resource.tags.extend(self.common_tags)
            else:
                resource.tags = self.common_tags

    def validate_token(self):
        response = self._api.tokeninfo()
        return response.to_dict()['data']

    def launch_jupyter_ide(self, ide):
        self.update_tags(ide.notebook_def)
        response = self._api.jobs_add_one(ide.user, data=ide.job, run='false')

    def launch_rstudio_ide(self, ide):
        self.update_tags(ide.notebook_def)
        response = self._api.jobs_add_one(
            ide.user, data=ide.job, run='false', subclass='rstudio')

    def get_ide(self, category, user, name, fields='*'):
        response = self._api.jobs_get_collection_one(user, category, job=name)

        if fields == '*':
            return response.to_dict()['data']
        elif fields == 'status':
            return response.to_dict()['data']['job']['parameters']['generated']['status']
        else:
            raise Exception('Unsupported fields parameter')

    def list_ides(self, category, user, filters='*'):
        response = self._api.jobs_get_by_class(
            user, category, False, run='false')
        return response.to_dict()['data']

    def delete_ide(self, category, user, name):
        self._api.jobs_list_delete_by_class(user, category, {'jobs': [name]})

    def create_run(self, run):
        response = self._api.jobs_add_one(user=run.user, data=run.job, run='true')

    def get_run(self, category, user, name, fields='*'):
        response = self._api.jobs_get_collection_one(user, category, name)

        if fields == '*':
            return response.to_dict()['data']
        elif fields == 'status':
            return response.to_dict()['data']['job']['parameters']['generated']['status']
        else:
            raise Exception('Unsupported fields parameter')

    def list_runs(self, category, user, filters='*'):
        # MAK - [HACK - TODO] - Correct from backend.
        # all=true is always returning training+preprocessing and ignoring
        # inference runs
        if category == 'inference':
            all = 'false'
        else:
            all = 'true'
        response = self._api.jobs_get_by_class(
            user, category, False, run='true', all=all)
        return response.to_dict()['data']

    def delete_run(self, category, user, name):
        self._api.jobs_list_delete_by_class(user, category, {'jobs': [name]})

    def create_repo(self, repo):
        self.update_tags(repo.datum)
        response = self._api.datums_add_one(user=repo.user, data=repo.datum)
        print(response.to_dict())

    def get_repo(self, category, user, name, fields='*'):
        response = self._api.datums_get_one_by_class(user, category, name)

        if fields == '*':
            return response.to_dict()['data']
        elif fields == 'status':
            return response.to_dict()['data']['datum']['generated']['status']
        else:
            raise Exception('Unsupported fields parameter')

    def list_repos(self, category, user, filters='*'):
        response = self._api.datums_get_by_class(user, category, False)
        return response.to_dict()['data']

    def delete_repo(self, category, user, name):
        response = self._api.datums_delete_by_class(
            user, category, {'datums': [name]})

    def get_run_lineage(self, category, user, runid):
        response = self._api.get_one_run_lineage(user, category, runid)
        return response.to_dict()['data']

    def get_datum_lineage(self, category, user, name, version):
        response = self._api.datums_get_one_version_lineage(
            user, category, name, version)
        return response.to_dict()['data']

    def trigger_runs(self, condition):
        response = self._api.trigger_runs_by_condition(condition)
        return response.to_dict()['data']

    def create_featureset(self, featureset):
        self.update_tags(featureset.featureset)
        response = self._api.featureset_add_one(featureset.featureset)
        print(response.to_dict())
        return response.to_dict()
    

    def commit_featureset(self, name, df):
        job_uuid = os.getenv('DKUBE_JOB_UUID')
        path = DKubeFeatureSetUtils().features_write(name, df, None)
        assert(path), "path can't be found"
        job = FeatureSetCommitDefJob(kind='dkube_run')
        body = FeatureSetCommitDef(job_uuid=job_uuid, job=job, featureset=name, path=path)
       
        response = self._api.featureset_commit_version(body=body)
        # Todo if the path is created, clean it up
        return response.to_dict()

    def read_featureset(self, name, version=None, path=None):
        # Todo: read even if not mounted
        
        if version is None:
            # Get the latest version. How?
            version = 'v2'
        df, ismounted = DKubeFeatureSetUtils().features_read(name, path)
        if not df.empty or ismounted:
            return df

        copybody = Body81(job_class=os.getenv("DKUBE_JOB_CLASS"), job_uuid=os.getenv("DKUBE_JOB_UUID"))
        # To call async - pass async_req=True
        r = self._api.featureset_copy_version(body=copybody, featureset=name, version=version)
        data_copy_resp = InlineResponse20055()
        while True:
            # check the status
            copystatus = Body85(job_class=os.getenv("DKUBE_JOB_CLASS"), job_uuid=os.getenv("DKUBE_JOB_ID"))
            r = self._api.featureset_copy_version_status(featureset=name, body=copystatus, version=version)
            response = r.to_dict()
            if respone['status'] == 200:
                data_copy_resp = response['data']
                status = data_copy_resp['status']
                if status == 'completed':
                    break
                elif status == 'copying' or status == 'starting':
                    time.sleep(5)
                    continue
                else:
                    assert(status == 'aborted' or status == 'error')
                    break
        if data_copy_resp['target_path']:
            path = os.path.join(os.getenv("DKUBE_USER_STORE"), data_copy_resp['target_path'])
            df, _ = DKubeFeatureSetUtils().features_read(name, version, path)
        return df
            

    def delete_featureset(self, delete_list):
        response = self._api.featureset_delete({'featuresets': delete_list})
        print(response)
        return response.to_dict()

    def list_featureset(self, filter):
        if filter is None:
            response = self._api.featureset_list()
        else:
            response = self._api.featureset_list(query=filter)
        return response.to_dict()['data']

    def get_featurespec(self, featureset):
        r = self._api.featureset_get(featureset)
        response = r.to_dict()
        if response['response']['code'] != 200:
            return None, False
        fset = response['data']
        return fset['featurespec'], True

    def get_datascience_capability(self):
        response = self._api.dl_frameworks()
        return response.to_dict()['data']

    def publish_model(self, user, model, version, details):
        response = self._api.datums_publish_one_model(user, model, version, details)

    def release_model(self, user, model, version):
        response = self._api.datums_release_one_model(user, model, version)

    def deploy_model(self, serving):
        model, version = serving.serving_def.model, serving.serving_def.version
        deployment = {'name': serving.name,
                      'description': serving.description, 'serving': serving.serving_def}
        response = self._api.datums_deploy_one_model(
            serving.user, model, version, deployment)

    def stage_model(self, serving):
        model, version = serving.serving_def.model, serving.serving_def.version
        deployment = {'name': serving.name,
                      'description': serving.description, 'serving': serving.serving_def}
        response = self._api.datums_testdeploy_one_model(
            serving.user, model, version, deployment)

    def modelcatalog(self, user):
        api = dkube_api.DkubeOperatorExclusiveApi(
            dkube_api.ApiClient(configuration))
        response = api.get_model_catalog(user)
        return response.to_dict()['data']
