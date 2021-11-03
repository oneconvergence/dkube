import os
import time
from pprint import pprint

from dkube.sdk.internal import dkube_api
from dkube.sdk.internal.dkube_api.models import *
from dkube.sdk.internal.dkube_api.models.feature_set_commit_def import \
    FeatureSetCommitDef
from dkube.sdk.internal.dkube_api.models.feature_set_commit_def_job import \
    FeatureSetCommitDefJob
from dkube.sdk.internal.dkube_api.rest import ApiException
from dkube.sdk.rsrcs.featureset import DKubeFeatureSetUtils
from dkube.sdk.rsrcs.training import DkubeTraining
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
        self._mmapi = dkube_api.ModelmonitorApi(dkube_api.ApiClient(configuration))
        self.common_tags = list_of_strs(common_tags)
        self.wait_interval = 10

    def dkubeinfo(self):
        response = self._api.dkubeinfo()
        return response.to_dict()['data']

    def update_tags(self, resource):
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

    def list_ides(self, category, user, shared=False, filters='*'):
        response = self._api.jobs_get_by_class(
            user, category, shared, run='false')
        return response.to_dict()['data']

    def delete_ide(self, category, user, name):
        self._api.jobs_list_delete_by_class(user, category, {'jobs': [name]})

    def update_inference(self, run):
        self._api.update_inference(run.user, run.job.name, run.serving_def)

    def create_run(self, run):
        if hasattr(run, 'execute'):
            response = self._api.jobs_add_one(
                user=run.user, data=run.job, run='true', execute=run.execute)
        else:
            response = self._api.jobs_add_one(
                user=run.user, data=run.job, run='true')

    def get_run(self, category, user, name, fields='*'):
        response = self._api.jobs_get_collection_one(user, category, name)

        if fields == '*':
            return response.to_dict()['data']
        elif fields == 'status':
            return response.to_dict()['data']['job']['parameters']['generated']['status']
        else:
            raise Exception('Unsupported fields parameter')

    def get_run_byuuid(self, uuid):
        response = self._api.jobs_get_one_by_uuid(uuid)
        return response.to_dict()['data']

    def list_runs(self, category, user, shared=False, filters='*'):
        # MAK - [HACK - TODO] - Correct from backend.
        # all=true is always returning training+preprocessing and ignoring
        # inference runs

        response = self._api.jobs_get_by_class(
            user, category, shared, run='true', all='false')
        return response.to_dict()['data']

    def delete_run(self, category, user, name):
        self._api.jobs_list_delete_by_class(user, category, {'jobs': [name]})

    def create_repo(self, repo):
        self.update_tags(repo.datum)
        response = self._api.datums_add_one(user=repo.user, data=repo.datum,extract=str(repo.extract).lower())
        print(response.to_dict())

    def get_repo(self, category, user, name, fields='*'):
        response = self._api.datums_get_one_by_class(user, category, name)

        if fields == '*':
            return response.to_dict()['data']
        elif fields == 'status':
            return response.to_dict()['data']['datum']['generated']['status']
        else:
            raise Exception('Unsupported fields parameter')

    def list_repos(self, category, user, shared=False, filters='*'):
        response = self._api.datums_get_by_class(user, category, shared)
        return response.to_dict()['data']

    def delete_repo(self, category, user, name, force=False):
        response = self._api.datums_delete_by_class(
            user, category, {'datums': [name]}, force=force)

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
        return response.to_dict()

    def commit_featureset(self, name, df, mount_path, dftype="Py"):
        # Make sure the dvs is setup

        path = None
        while True and name is not None:
            versions = self.get_featureset_versions(name)
            if versions is None:
                print("commit_featureset: waiting for featureset to be setup")
                time.sleep(self.wait_interval)
                continue

            # Only need to wait for the v1 to reach synced state
            if len(versions) > 1:
                break

            version_status = DKubeFeatureSetUtils().get_version_status(versions, 'v1')
            if version_status.lower() == 'synced':
                break
            print("commit_featureset: not ready, state:{} expected:synced".format(
                version_status.lower()))
            time.sleep(self.wait_interval)

        job_uuid = os.getenv('DKUBE_JOB_UUID')

        # commit api needs relative path from dkube store & featureset name

        if dftype == "Py" and df is not None:
            if mount_path is None:
                assert(name), 'name should be specified'
            path = DKubeFeatureSetUtils().features_write(name, df, mount_path)
            assert(path), "Dkube relative path can't be computed"
        else:
            path = DKubeFeatureSetUtils().features_write(name, df, mount_path, dftype)
            assert(path), "Dkube relative path can't be computed"

        if mount_path is not None and name is None:
            name = DKubeFeatureSetUtils().get_featureset_name_from_mountpath(mount_path, 'outputs')
            assert(name), "featureset can't be verified"

        if path is None:
            if mount_path is None and name is not None:
                mount_path = DKubeFeatureSetUtils().get_featureset_mountpath_from_name(name, 'outputs')
                assert(mount_path), 'No valid path for the featureset'
            assert(mount_path and os.path.isabs(mount_path)), "path is invalid"
            path = DKubeFeatureSetUtils().get_rel_path_for_commit(mount_path)
            assert(path), "Dkube relative path can't be computed"

        job = FeatureSetCommitDefJob(kind='dkube_run')
        body = FeatureSetCommitDef(
            job_uuid=job_uuid, job=job, featureset=name, path=path)

        response = self._api.featureset_commit_version(body)
        # Todo if the path is created, clean it up
        return response.to_dict()

    def read_featureset(self, name, version=None, path=None, dftype="Py"):
        # Todo: read even if not mounted
        if dftype == "Py":
            df, ismounted = DKubeFeatureSetUtils().features_read(name, path)
            if not df.empty or ismounted:
                return df

        if version is None:
            versions = self.get_featureset_versions(name)
            assert(versions), "no versions found"
            version = DKubeFeatureSetUtils().get_top_version(versions)
            print("read_featureset: No version specified, using the latest version {}".format(
                version))
            while True:
                # don't get the top version within this loop
                version_status = DKubeFeatureSetUtils().get_version_status(versions, version)
                if version_status is not None:
                    if version_status.lower() == 'synced':
                        break
                    print("read_featureset: version {} not ready, state:{} expected:synced".format(
                        version, version_status.lower()))
                time.sleep(self.wait_interval)
                versions = self.get_featureset_versions(name)

        copy_body = FeaturesetVersionCopyDef(job_class=os.getenv(
            "DKUBE_JOB_CLASS"), job_uuid=os.getenv("DKUBE_JOB_UUID"))
        # To call async - pass async_req=True
        r = self._api.featureset_copy_version(
            data=copy_body, featureset=name, version=version)
        data_copy_resp = DataCopy()

        while True:
            # check the status
            r = self._api.featureset_copy_version_status(
                featureset=name, data=copy_body, version=version)
            response = r.to_dict()
            if response['response']['code']:
                data_copy_resp = response['data']
                status = data_copy_resp['status']
                if status.lower() == 'completed':
                    break
                elif status.lower() == 'copying' or status.lower() == 'starting':
                    print(
                        "read_featureset: features not ready, status:{} expected:completed".format(status))
                    time.sleep(self.wait_interval)
                    continue
                else:
                    assert(status.lower() ==
                           'aborted' or status.lower() == 'error')
                    break
        if data_copy_resp['target_path']:
            path = DKubeFeatureSetUtils()._get_d3_full_path(
                data_copy_resp['target_path'])
            if dftype == "Py":
                df, _ = DKubeFeatureSetUtils().features_read(name, path)
            else:
                return path
        return df

    def delete_featureset(self, delete_list):
        response = self._api.featureset_delete({'featuresets': delete_list})
        return response.to_dict()

    def list_featureset(self, filter):
        if filter is None:
            response = self._api.featureset_list()
        else:
            response = self._api.featureset_list(query=filter)
        return response.to_dict()['data']

    def get_featureset(self, featureset):
        r = self._api.featureset_get(featureset)
        return r.to_dict()

    def get_featurespec(self, featureset):
        r = self._api.featureset_get(featureset)
        response = r.to_dict()
        if response['response']['code'] != 200:
            return None, False
        fset = response['data']
        return fset['featurespec'], True

    def get_featureset_versions(self, featureset):
        r = self._api.featureset_get(featureset)
        response = r.to_dict()
        if response['response']['code'] != 200:
            return None
        fset = response['data']
        return fset['versions']

    def get_datascience_capability(self):
        response = self._api.dl_frameworks()
        return response.to_dict()['data']

    def publish_model(self, user, model, version, details):
        response = self._api.datums_publish_one_model(
            user, model, version, details)

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
        
    def get_model_catalog(self, user, model):
        response = self._api.get_one_modelcatalog_model(user, model)
        return response.to_dict()['data']

    def list_published_models(self, user):
        response = self._api.get_all_published_models(user)
        return response.to_dict()['data']

    def is_model_catalog_enabled(self):
        response = self._api.dkubeinfo()
        return response.to_dict()['data']['model_catalog_enabled']

    def download_dataset(self, path, user, name, version):
        url = url + \
            "/dkube/v2/ext/users/{}/datums/class/dataset/datum/{}/version/{}/export".format(
                user, name, version)
        url = url_normalize(url)

        headers = {"Authorization": "Bearer {}".format(
            token), "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}
        resp = requests.get(url, headers=headers, verify=False)
        zf = "/tmp/{}.zip".format(name)
        with open(zf, 'wb') as f:
            f.write(resp.content)

        tempdir = tempfile.TemporaryDirectory()
        os.makedirs(path, exist_ok=True)
        with zipfile.ZipFile(zf, 'r') as zip_ref:
            zip_ref.extractall(tempdir.name)

        copy_tree("{}/{}/data".format(tempdir.name, version), path)
        # use temp_dir, and when done:
        tempdir.cleanup()

    def download_model(self, path, user, name, version):
        url = url + \
            "/dkube/v2/ext/users/{}/datums/class/model/datum/{}/version/{}/export".format(
                user, name, version)
        url = url_normalize(url)

        headers = {"Authorization": "Bearer {}".format(
            token), "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}
        resp = requests.get(url, headers=headers, verify=False)
        zf = "/tmp/{}.zip".format(name)
        with open(zf, 'wb') as f:
            f.write(resp.content)

        tempdir = tempfile.TemporaryDirectory()
        os.makedirs(path, exist_ok=True)
        with zipfile.ZipFile(zf, 'r') as zip_ref:
            zip_ref.extractall(tempdir.name)

        copy_tree("{}/{}/data".format(tempdir.name, version), path)
        # use temp_dir, and when done:
        tempdir.cleanup()

    def list_inference_endpoints(self):
        api = dkube_api.DkubeOperatorExclusiveApi(
            dkube_api.ApiClient(configuration))
        response = api.get_all_deployments()
        return response.to_dict()['data']
    
    def get_smtp_artifact(self):
        api = dkube_api.DkubeOperatorExclusiveApi(
            dkube_api.ApiClient(configuration))
        response = api.smtp_artifact_get()
        return response.to_dict()['data']

    def update_smtp_artifact(self,data):
        api = dkube_api.DkubeOperatorExclusiveApi(
            dkube_api.ApiClient(configuration))
        response = api.upsert_smtp_artifact(data)
        return response.to_dict()

   #### MODEL MONITOR APIS ###

    def create_model_monitor(self,modelmonitor):
        response = self._mmapi.modelmonitor_add_one(data=modelmonitor.modelmonitor)
        return response.to_dict()
    
    def get_modelmonitor(self,modelmonitor):
        response = self._mmapi.modelmonitor_get(modelmonitor)
        return response

    def list_modelmonitor(self,params):
        response = self._mmapi.modelmonitor_list(**params)
        return response.to_dict()['data']
    
    def get_modelmonitor_id(self,name):
        response = self._mmapi.modelmonitor_ids(name)
        return response

    def get_modelmonitor_configuration(self,modelmonitor_id):
        response = self._mmapi.modelmonitor_get(modelmonitor_id)
        return response.to_dict()['data']
    
    def get_modelmonitor_dataset(self,modelmonitor):
        response = self._mmapi.modelmonitor_datasets_list(modelmonitor)
        return response.to_dict()['data']

    def get_modelmonitor_alerts(self,modelmonitor_id):
        response = self._mmapi.modelmonitor_alerts_list(modelmonitor_id)
        return response.to_dict()['data']
    
    def get_modelmonitor_template(self):
        response = self._mmapi.modelmonitor_get_metrics_template()
        return response.to_dict()['data']

    def delete_modelmonitors(self,delete_list):
        response = self._mmapi.modelmonitor_delete({'data': delete_list})
        return response.to_dict()

    def delete_modelmonitor_dataset(self,mm_id,delete_dataset_list):
        response = self._mmapi.modelmonitor_delete_datasets(mm_id,{'data':delete_dataset_list})
        return response.to_dict()
    
    def delete_modelmonitor_alert(self,mm_data,delete_alerts_list):
        response = self._mmapi.modelmonitor_delete_alerts(mm_id,{data:delete_alerts_list})
        return response.to_dict()
   
    def modelmonitor_addalert(self,modelmonitor,alert_data):
        response = self._mmapi.modelmonitor_add_alerts(modelmonitor,alert_data)
        return response.to_dict()
    
    def modelmonitor_adddataset(self,modelmonitor,dataset):
        response = self._mmapi.modelmonitor_add_datasets(modelmonitor,dataset)
        return response.to_dict()

    def modelmonitor_archive(self,modelmonitor,archive):
        response = self._mmapi.modelmonitor_archive(modelmonitor,archive)
        return response.to_dict()

    def modelmonitor_state(self,modelmonitor,state):
        response = self._mmapi.modelmonitor_state(modelmonitor,state)
        return response.to_dict()
    
    def update_modelmonitor_dataset(self,modelmonitor,dataset,data):
        response = self._mmapi.modelmonitor_update_dataset(modelmonitor,dataset,data)
        return response.to_dict()
    
    def update_modelmonitor_alert(self,modelmonitor,alert,data):
        response = self._mmapi.modelmonitor_update_alert(modelmonitor,alert,data)
        return response.to_dict()
    
    def update_modelmonitor_config(self,modelmonitor,data):
        response = self._mmapi.modelmonitor_update(modelmonitor,data)
        return response.to_dict()



