import json
import logging
import os
from http.client import HTTPConnection

from flatten_json import flatten


def debug_requests_on():
    """Switches on logging of the requests module."""

    HTTPConnection.debuglevel = 1

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True


def validate_token(api, token):
    response = api.tokeninfo()
    claims = response.to_dict()["data"]
    user = claims["username"]
    role = claims["role"]

    return user, role


def run_outputs(api, user, _class, name):
    gresponse = api.jobs_get_collection_one(user, _class, name)

    job = gresponse.to_dict()["data"]["job"]
    uuid = job["parameters"]["generated"]["uuid"]

    with open("/tmp/rundetails", "w+") as op:
        op.write(json.dumps(job))

    lresponse = api.get_one_run_lineage(user, _class, uuid)
    if os.environ.get("DKUBE_OP_DEBUG") == "1":
        print(lresponse.to_dict())
    outputs = lresponse.to_dict()["data"]["outputs"]

    artifacts = []
    for output in outputs:
        entry = None
        if "featureset_version" in output and output["featureset_version"]:
            entry = {
                "datum": output["featureset_version"]["featureset_name"],
                "class": "featureset",
                "version": output["featureset_version"]["featureset_uuid"],
                "index": output["featureset_version"]["index"],
            }
        else:
            entry = {
                "datum": output["version"]["datum_name"],
                "class": output["version"]["datum_type"],
                "version": output["version"]["uuid"],
                "index": output["version"]["index"],
            }
        artifacts.append(entry)

    with open("/tmp/artifacts", "w+") as op:
        op.write(json.dumps(artifacts))


def print_json(config):
    config = flatten(config, separator=".")
    for k, v in config.items():
        if v is None or v == "" or v is []:
            continue
        print("{0: <65}: {1}".format(k, v))

    print("\n")
