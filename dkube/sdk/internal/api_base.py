from __future__ import print_function
import time

from dkube.sdk.internal import dkube_api
from dkube.sdk.internal.dkube_api.rest import ApiException
from pprint import pprint

from url_normalize import url_normalize

# Configure API key authorization: d3apikey
configuration = dkube_api.Configuration()
configuration.api_key_prefix['Authorization'] = 'Bearer'


class ApiBase(object):

    def __init__(self, url, token):
        configuration.host = url_normalize(
            '{}/dkube/v2/controller'.format(url))
        configuration.api_key['Authorization'] = token
        configuration.verify_ssl = False

    def validate_token(self):
        api = dkube_api.DkubeApi(dkube_api.ApiClient(configuration))
        response = api.tokeninfo()
        return response.to_dict()['data']

    def launch_jupyter_ide(self, ide):
        api = dkube_api.DkubeApi(dkube_api.ApiClient(configuration))
        response = api.jobs_add_one(ide.user, ide.job, run='false')

    def launch_rstudio_ide(self, ide):
        api = dkube_api.DkubeApi(dkube_api.ApiClient(configuration))
        response = api.jobs_add_one(
            ide.user, ide.job, run='false', subclass='rstudio')

    def get_ide(self, category, user, name, fields='*'):
        api = dkube_api.DkubeApi(dkube_api.ApiClient(configuration))
        response = api.jobs_get_collection_one(user, category, name)

        if fields == '*':
            return response.to_dict()['data']
        elif fields == 'status':
            return response.to_dict()['data']['job']['parameters']['generated']['status']
        else:
            raise Exception('Unsupported fields parameter')

    def list_ides(self, category, user, filters='*'):
        api = dkube_api.DkubeApi(dkube_api.ApiClient(configuration))
        response = api.jobs_get_by_class(
            user, category, False, run='false')
        return response.to_dict()['data']

    def delete_ide(self, category, user, name):
        api = dkube_api.DkubeApi(dkube_api.ApiClient(configuration))
        api.jobs_list_delete_by_class(user, category, {'jobs': [name]})

    def create_run(self, run):
        api = dkube_api.DkubeApi(dkube_api.ApiClient(configuration))
        response = api.jobs_add_one(run.user, run.job, run='true')

    def get_run(self, category, user, name, fields='*'):
        api = dkube_api.DkubeApi(dkube_api.ApiClient(configuration))
        response = api.jobs_get_collection_one(user, category, name)

        if fields == '*':
            return response.to_dict()['data']
        elif fields == 'status':
            return response.to_dict()['data']['job']['parameters']['generated']['status']
        else:
            raise Exception('Unsupported fields parameter')

    def list_runs(self, category, user, filters='*'):
        api = dkube_api.DkubeApi(dkube_api.ApiClient(configuration))
        response = api.jobs_get_by_class(
            user, category, False, run='true', all='true')
        return response.to_dict()['data']

    def delete_run(self, category, user, name):
        api = dkube_api.DkubeApi(dkube_api.ApiClient(configuration))
        api.jobs_list_delete_by_class(user, category, {'jobs': [name]})

    def create_repo(self, repo):
        api = dkube_api.DkubeApi(dkube_api.ApiClient(configuration))
        response = api.datums_add_one(repo.user, repo.datum)
        print(response.to_dict())

    def get_repo(self, category, user, name, fields='*'):
        api = dkube_api.DkubeApi(dkube_api.ApiClient(configuration))
        response = api.datums_get_one_by_class(user, category, name)

        if fields == '*':
            return response.to_dict()['data']
        elif fields == 'status':
            return response.to_dict()['data']['datum']['generated']['status']
        else:
            raise Exception('Unsupported fields parameter')

    def list_repos(self, category, user, filters='*'):
        api = dkube_api.DkubeApi(dkube_api.ApiClient(configuration))
        response = api.datums_get_by_class(user, category, False)
        return response.to_dict()['data']

    def delete_repo(self, category, user, name):
        api = dkube_api.DkubeApi(dkube_api.ApiClient(configuration))
        response = api.datums_delete_by_class(
            user, category, {'datums': [name]})

    def get_run_lineage(self, category, user, runid):
        api = dkube_api.DkubeApi(dkube_api.ApiClient(configuration))
        response = api.get_one_run_lineage(user, category, runid)
        return response.to_dict()['data']

    def get_datum_lineage(self, category, user, name, version):
        api = dkube_api.DkubeApi(dkube_api.ApiClient(configuration))
        response = api.datums_get_one_version_lineage(
            user, category, name, version)
        return response.to_dict()['data']

    def trigger_runs(self, condition):
        api = dkube_api.DkubeApi(dkube_api.ApiClient(configuration))
        response = api.trigger_runs_by_condition(condition)
        return response.to_dict()['data']

    def get_datascience_capability(self):
        api = dkube_api.DkubeApi(dkube_api.ApiClient(configuration))
        response = api.dl_frameworks()
        return response.to_dict()['data']

    def publish_model(self, user, model, version, details):
        api = dkube_api.DkubeApi(dkube_api.ApiClient(configuration))
        response = api.datums_publish_one_model(user, model, version, details)

    def release_model(self, user, model, version):
        api = dkube_api.DkubeApi(dkube_api.ApiClient(configuration))
        response = api.datums_release_one_model(user, model, version)

    def deploy_model(self, serving):
        api = dkube_api.DkubeApi(dkube_api.ApiClient(configuration))
        model, version = serving.serving_def.model, serving.serving_def.version
        deployment = {'name': serving.name,
                      'description': serving.description, 'serving': serving.serving_def}
        response = api.datums_deploy_one_model(
            serving.user, model, version, deployment)

    def stage_model(self, serving):
        api = dkube_api.DkubeApi(dkube_api.ApiClient(configuration))
        model, version = serving.serving_def.model, serving.serving_def.version
        deployment = {'name': serving.name,
                      'description': serving.description, 'serving': serving.serving_def}
        response = api.datums_testdeploy_one_model(
            serving.user, model, version, deployment)

    def modelcatalog(self, user):
        api = dkube_api.DkubeOperatorExclusiveApi(
            dkube_api.ApiClient(configuration))
        response = api.get_model_catalog(user)
        return response['data']
