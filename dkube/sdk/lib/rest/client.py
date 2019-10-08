import requests
import json

def post(url:str, data:dict, token:str):
    jdata = data.to_json()
    rdata   = json.dumps(jdata)
    headers = {"Content-Type": "application/keyauth.api.v1+json", "Authorization": "Bearer {}".format(token)}
    resp = requests.post(url, data=rdata, headers=headers, timeout=(100, 100), verify=False)

    if resp.ok:
        print("POST req successful, for ip data : {}".format(rdata))
    elif resp.status_code == 401:
        print("POST req failed with 401")
    else:
        print("POST req failed with status - {}".format(resp.status_code))
