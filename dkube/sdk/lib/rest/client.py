import requests
import json


from ..exceptions import *
from ..log import *

def post(url:str, token:str, data:dict={}):
    #jdata = data.to_json()
    rdata   = json.dumps(data)
    headers = {"Content-Type": "application/keyauth.api.v1+json", "Authorization": "Bearer {}".format(token)}
    resp = requests.post(url, data=rdata, headers=headers, timeout=(100, 100), verify=False)

    if resp.ok:
        logger.info("POST -> {} successful".format(url))
    elif resp.status_code == 401:
        raise DkubeAPIException('POST', url, resp.status_code)
    else:
        raise DkubeAPIException('POST', url, resp.status_code)

def get(url:str, token:str, query:str=None):
    headers = {"Content-Type": "application/keyauth.api.v1+json", "Authorization": "Bearer {}".format(token)}
    resp = requests.get(url, headers=headers, timeout=(100, 100), verify=False)

    if resp.ok:
        logger.info("GET -> {} successful".format(url))
        return json.loads(resp.content)
    elif resp.status_code == 401:
        raise DkubeAPIException('GET', url, resp.status_code)
    else:
        raise DkubeAPIException('GET', url, resp.status_code)
