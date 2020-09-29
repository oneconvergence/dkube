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
    def __init__(self, url, user, token):
        configuration.host = url_normalize('{}/dkube/v2/controller'.format(url))
        configuration.api_key['Authorization'] = token
        configuration.verify_ssl = False

    def validate_token(self):
        api = dkube_api.DkubeApi(dkube_api.ApiClient(configuration))
        response = api.tokeninfo()
        return response.to_dict()['data']

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
        response = api.jobs_get_by_class(user, category, False, all='true')
        pprint(response)
        return response.to_dict()

    def delete_run(self, category, user, name):
        api = dkube_api.DkubeApi(dkube_api.ApiClient(configuration))
        api.jobs_list_delete_by_class(user, category, list(name))

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
        return response.to_dict()

    def delete_repo(self, category, user, name):
        api = dkube_api.DkubeApi(dkube_api.ApiClient(configuration))
        response = api.datums_delete_by_class(user, category, list(name))

    def get_head_version(self, category, user, repo):
        pass

    def get_latest_version(self, category, user, repo):
        pass

    def list_versions(self, category, user, repo):
        pass

    def get_version(self,category, user, repo, version):
        pass

    def get_run_lineage(self, category, user, runuuid):
        api = dkube_api.DkubeApi(dkube_api.ApiClient(configuration))
        response = api.get_one_run_lineage(user, category, runuuid)
        return response.to_dict()['data']
