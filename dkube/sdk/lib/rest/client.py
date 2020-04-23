import requests
import json


from ..exceptions import *
from ..log import *

def post(url:str, token:str, data:dict={}):
    rdata   = json.dumps(data)
    headers = {"Content-Type": "application/keyauth.api.v1+json", "Authorization": "Bearer {}".format(token)}
    params  = {'run': 'true'}

    logger.debug("DATA -> {}".format(rdata))
    resp = requests.post(url, data=rdata, headers=headers, params=params, timeout=(100, 100), verify=False)

    if resp.ok:
        logger.info("POST -> {} successful".format(url))
    elif resp.status_code == 401:
        raise DkubeAPIException('POST', url, resp.status_code)
    else:
        raise DkubeAPIException('POST', url, resp.status_code)

def get(url:str, token:str, query:str=None):
    #MAK - TODO - Good to retry GETs on 503, 504 timeout errors
    headers = {"Content-Type": "application/keyauth.api.v1+json", "Authorization": "Bearer {}".format(token)}
    resp = requests.get(url, headers=headers, timeout=(100, 100), verify=False, params=query)

    if resp.ok:
        logger.info("GET -> {} successful".format(url))
        return json.loads(resp.content.decode())
    elif resp.status_code == 401:
        raise DkubeAPIException('GET', url, resp.status_code)
    else:
        raise DkubeAPIException('GET', url, resp.status_code)
