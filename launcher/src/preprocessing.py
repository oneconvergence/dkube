import json
import time

import click
from dkube.sdk import generate

from utils import print_json, run_outputs


def command_preprocessing(
    api=None, run={}, name="", user="", runid="", workflowid="", **kwargs
):
    stagename = name
    runname = generate("pldata")

    run["name"] = runname
    run["parameters"]["class"] = "preprocessing"
    run["parameters"]["preprocessing"]["tags"].extend(
        [
            "owner=pipeline",
            "stage=" + stagename,
            "workflowid=" + workflowid,
            "runid=" + runid,
        ]
    )

    # Update pipeline information
    run["parameters"]["generated"] = {
        "uuid": runid,
        "pipeline": {"runid": workflowid, "name": stagename},
    }

    api.jobs_add_one(user, run, run="true")
    while True:
        response = api.jobs_get_collection_one(user, "preprocessing", runname)
        status = response.to_dict()["data"]["job"]["parameters"]["generated"]["status"]
        state, reason = status["state"], status["reason"]
        if state.lower() in ["complete", "failed", "error"]:
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
    run_outputs(api, user, "preprocessing", runname)


@click.command()
@click.pass_obj
@click.argument("configuration")
def preprocessing(obj, configuration):
    run = json.loads(configuration)
    print_json(run)
    command_preprocessing(run=run, **obj)
