import string
import random
from dkube.sdk.internal import dkube_api
from dkube.sdk.internal.dkube_api.models.config_file_model import \
    ConfigFileModel
from url_normalize import url_normalize
import os

generate = lambda hint: "{}-{}".format(hint, ''.join([random.choice(string.digits) for n in range(4)]))

def list_of_strs(x):
    if x != None:
        if type(x) == list:
            #make sure each element is of type str
            x = [str(y) for y in x]
        else:
            x = [str(x)]
    return x

def get_frameworks() :
    token = os.getenv("DKUBE_USER_ACCESS_TOKEN")
    dkube_url = os.getenv("DKUBE_URL")
    configuration = dkube_api.Configuration()
    configuration.api_key_prefix['Authorization'] = 'Bearer'
    configuration.host = url_normalize(
        '{}/dkube/v2/controller'.format(dkube_url))
    configuration.api_key['Authorization'] = token
    configuration.verify_ssl = False
    api = dkube_api.DkubeApi(dkube_api.ApiClient(configuration))
    response = api.dl_frameworks()
    fw_opts = []
    fws =  response.to_dict()['data']
    for fw in fws ['training']['frameworks'] :
                                                                                                                    1,5           Top
