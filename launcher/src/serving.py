import json
import time

import click
from dkube.sdk import generate

from utils import print_json, run_outputs


def command_serving(
    api=None, run={}, name="", user="", runid="", workflowid="", **kwargs
):
    stagename = name

    runname = generate("plserving")

    run["name"] = runname
    run["parameters"]["class"] = "inference"

    # Update pipeline information
    run["parameters"]["generated"] = {
        "uuid": runid,
        "pipeline": {"runid": workflowid, "name": stagename},
    }

    inf = run["parameters"]["inference"]
    if (
        inf["serving_image"]["image"] is None
        or (inf["transformer"] is True and inf["transformer_image"]["image"] is None)
        or (inf["transformer"] is True and inf["transformer_project"] is None)
    ):

        if inf["version"] is None:
            response = api.datums_get_one_by_class(inf["owner"], "model", inf["model"])
            versions = response.to_dict()["data"]["versions"]
            v = versions[0]["version"]
            inf["version"] = v["uuid"]

        li = api.datums_get_one_version_lineage(
            inf["owner"], "model", inf["model"], inf["version"]
        )
        li = li.to_dict()["data"]

        if inf["serving_image"]["image"] is None:
            si = li["run"]["parameters"]["generated"]["serving_image"]["image"]
            inf["serving_image"]["image"] = dict(si)

        if inf["transformer"] is True and inf["transformer_image"]["image"] is None:
            ti = li["run"]["parameters"]["generated"]["training_image"]["image"]
            inf["transformer_image"]["image"] = dict(ti)

        if inf["transformer"] is True and inf["transformer_project"] is None:
            code = li["run"]["parameters"]["training"]["datums"]["workspace"]["data"]
            inf["transformer_project"] = code["name"]
            inf["transformer_commit_id"] = code["version"]

    run["parameters"]["inference"] = inf
    api.jobs_add_one(user, run, run="true")
    while True:
        response = api.jobs_get_collection_one(user, "inference", runname)
        status = response.to_dict()["data"]["job"]["parameters"]["generated"]["status"]
        state, reason = status["state"], status["reason"]
        if state.lower() in ["running", "failed", "error"]:
            print(
                "run {} - completed with state {} and reason {}".format(
                    runname, state, reason
                )
            )
            break
        else:
            print(
                "run {} - waiting for completion, current state {}".format(
                    runname, state
                )
            )
            time.sleep(10)

    # generate the outputs, next stage can pick from here
    run_outputs(api, user, "inference", runname)


@click.command()
@click.pass_obj
@click.argument("configuration")
def serving(obj, configuration):
    run = json.loads(configuration)
    print_json(run)
    command_serving(run=run, **obj)
