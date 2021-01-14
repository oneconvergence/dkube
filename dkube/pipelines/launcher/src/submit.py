import base64
import json
import zipfile

import boto3
import click
import kfp

# Debug logging
import requests
from botocore.client import Config
from json2html import json2html

from utils import debug_requests_on


def download_s3_file(bucket, remote_file, local_file):
    s3 = boto3.resource(
        "s3",
        endpoint_url="http://dkube-minio-server.dkube-infra:9000",
        aws_access_key_id="dkube",
        aws_secret_access_key="l06dands19s",
        config=Config(signature_version="s3v4"),
    )
    s3.meta.client.download_file(bucket, remote_file, local_file)


def get_run_metadata(run_id):
    client = kfp.Client()
    run = client.get_run(run_id)
    workflow = json.loads(run.pipeline_runtime.workflow_manifest)
    pipeline_name = workflow["metadata"]["annotations"][
        "pipelines.kubeflow.org/run_name"
    ]

    metadata = {
        "type": "pipeline",
        "url": "pipeline/#/runs/details/{}".format(run_id),
        "id": run_id,
        "name": pipeline_name,
        "template": workflow["spec"]["templates"],
    }
    return metadata


@click.command()
@click.argument("project_id")
@click.argument("input_file", type=click.Path(exists=True))
@click.pass_obj
def submit(obj, project_id, input_file):

    run_id = obj["workflowid"]
    token = obj["token"]
    url = "http://{}.dkube.svc.cluster.local.".format(project_id)
    headers = {
        "Authorization": "Bearer " + token,
    }
    metadata = get_run_metadata(run_id)

    files = {
        "file": open(input_file, "rb"),
        "meta": json.dumps(metadata).encode("utf8"),
    }
    if obj["debug"] == "1":
        debug_requests_on()

    r = requests.post(url + "/submit/predictions/", headers=headers, files=files)

    if r.status_code == 200:
        response = r.json()

        if response["stdout"]:
            stdout = base64.b64decode(response["stdout"]).decode("ascii")
            print("Output from eval script:\n" + stdout)
        if response["stderr"]:
            stderr = base64.b64decode(response["stderr"]).decode("ascii")
            print("Error from eval script:\n" + stderr)

        if "metrics" in response:
            table = json2html.convert(json=response["metrics"])
            metadata = {
                "outputs": [
                    {
                        "storage": "inline",
                        "type": "web-app",
                        "source": table,
                    }
                ],
            }
            with open("/metadata.json", "w") as f:
                json.dump(metadata, f)
        if "artifacts_url" in response:
            download_s3_file("dkube", response["artifacts_url"], "/results.zip")

            with zipfile.ZipFile("/results.zip", "r") as zip_ref:
                zip_ref.extractall("/results")
                print("/extracted artifactes in /results")
    else:
        print("Error in submitting request: code {} \n{}".format(r.status_code, r.text))


if __name__ == "__main__":
    # token = os.environ.get("DKUBE_TOKEN","")
    # eval(["requirements.txt", "-t", token])
    eval()
