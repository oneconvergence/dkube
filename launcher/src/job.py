import io
import json
import os
import shutil
import time
import zipfile

import click
import requests
from dkube.sdk import DkubeApi, DkubeDataset, DkubePreprocessing, generate

from utils import print_json, run_outputs


def downloadOutput(sdk, user, datasetName, output):
    dataset = sdk.get_dataset(user, datasetName)
    version = dataset["datum"]["generated"]["head_version"]

    base = f"http://dkube-downloader.dkube:9401/dkube/v2/users/{user}"
    url = f"{base}/datums/class/dataset/datum/{datasetName}/version/{version}/export"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    print("\nDownloading output status:", r.status_code)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    output_dir = "/tmp/output"
    z.extractall(output_dir)
    os.system(f"ls -lR {output_dir}")

    output = json.loads(output)
    open("/output", "w").write("No output from user code")
    open("/metadata.json", "w").write("{}")
    open("/metrics.json", "w").write("{}")
    for k, v in output.items():
        filename = v.split("/")[-1]
        if k == "output":
            shutil.copy(f"{output_dir}/{version}/data/{filename}", "/output")
        elif k == "mlpipeline-ui-metadata":
            shutil.copy(f"{output_dir}/{version}/data/{filename}", "/metadata.json")
        elif k == "mlpipeline-metrics":
            shutil.copy(f"{output_dir}/{version}/data/mlpipeline_metrics/{filename}", "/metrics.json")
        else:
            print(f"ERROR: output key{k} not supported.")


@click.command()
@click.pass_obj
@click.option("--container", required=True)
@click.option("--script", required=True)
@click.option("--program")
@click.option("--commit_id", default="")
@click.option("--datasets", default="[]")
@click.option("--input_dataset_mounts", default="[]")
@click.option("--input_dataset_versions", default="[]")
@click.option("--featuresets", default="[]")
@click.option("--input_featureset_mounts", default="[]")
@click.option("--input_featureset_versions", default="[]")
@click.option("--models", default="[]")
@click.option("--input_model_mounts", default="[]")
@click.option("--input_model_versions", default="[]")
@click.option("--envs", default="[]")
@click.option("--tags", default="[]")
@click.option("--output", default="{}")
def job(
    obj,
    container,
    script,
    program,
    commit_id,
    datasets,
    input_dataset_mounts,
    input_dataset_versions,
    featuresets,
    input_featureset_mounts,
    input_featureset_versions,
    models,
    input_model_mounts,
    input_model_versions,
    envs,
    tags,
    output,
):
    name = generate(obj["name"])
    tags = json.loads(tags)
    tags.extend(
        [
            "owner=pipeline",
            "stage=" + obj["name"],
            "workflowid=" + obj["workflowid"],
            "runid=" + obj["runid"],
        ]
    )

    p = DkubePreprocessing(obj["user"], name=name, tags=tags)

    container = json.loads(container)
    p.update_container(image_url=container["image"])
    if "username" in container:
        p.update_container(
            image_url=container["image"],
            login_uname=container["username"],
            login_pswd=container["password"],
        )
    p.update_startupscript(script)
    if program:
        p.add_code(program, commitid=commit_id)

    datasets = json.loads(datasets)
    mounts = json.loads(input_dataset_mounts)
    versions = json.loads(input_dataset_versions)
    for i, dataset in enumerate(datasets):
        version = ""
        if len(versions) > i:
            version = versions[i]
        p.add_input_dataset(dataset, mountpath=mounts[i], version=version)

    featuresets = json.loads(featuresets)
    mounts = json.loads(input_featureset_mounts)
    versions = json.loads(input_featureset_versions)
    for i, featureset in enumerate(featuresets):
        version = ""
        if len(versions) > i:
            version = versions[i]
        p.add_input_featureset(featureset, mountpath=mounts[i], version=version)

    models = json.loads(models)
    mounts = json.loads(input_model_mounts)
    versions = json.loads(input_model_versions)

    for i, model in enumerate(models):
        version = ""
        if len(versions) > i:
            version = versions[i]
        p.add_input_model(model, mountpath=mounts[i], version=version)

    api = obj["api"]
    user = obj["user"]
    sdk = DkubeApi(token=obj["token"])

    # create a dataset to pass the output from job to us
    if output != "{}":
        datasetName = name + "-output"
        dataset = DkubeDataset(user, name=datasetName, tags=tags)
        sdk.create_dataset(dataset)
        p.add_output_dataset(datasetName, mountpath="/output")

    job = p.job.to_dict()
    print_json(job)
    job["parameters"]["class"] = "preprocessing"
    job["parameters"]["generated"] = {
        "uuid": obj["runid"],
        "pipeline": {"runid": obj["workflowid"], "name": name},
    }

    api.jobs_add_one(obj["user"], job, run="true")

    while True:
        response = api.jobs_get_collection_one(user, "preprocessing", name)
        status = response.to_dict()["data"]["job"]["parameters"]["generated"]["status"]
        state, reason = status["state"], status["reason"]
        if state.lower() in ["complete", "failed", "error"]:
            if state.lower() == "complete":
                if output != "{}":
                    downloadOutput(sdk, user, datasetName, output)

            print(f"run {name} - completed with state {state} and reason {reason}")
            break
        else:
            print(f"run {name} - waiting for completion, current state {state}")
            time.sleep(10)

    if output != "{}":
        sdk.delete_dataset(user, datasetName, force=True)
    # generate the outputs, next stage can pick from here
    run_outputs(api, user, "preprocessing", name)
