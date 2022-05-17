import os
import sys
import json
import warnings
import jwt
import argparse

from dkube.sdk import *

def export_and_publish_model(url, token):
    payload = jwt.decode(token, options={"verify_signature": False})
    user = payload['username']

    api = DkubeApi(URL=url, token=token)

    with open("inputs.json") as f:
        inputs = json.load(f)


    name = generate(inputs["name"])
    afs = inputs["artifact-store"]
    #1. download model

    model = DkubeModel(user, name=name + "-model")
    model.update_s3_details(afs["endpoint"], afs["bucket"], afs["model_prefix"], afs["accesskeyid"], afs["accesskey"])
    api.create_model(model)

    #2. download dataset
    dataset = DkubeDataset(user, name=name + "-dataset")
    dataset.update_s3_details(afs["endpoint"], afs["bucket"], afs["traindata_prefix"], afs["accesskeyid"], afs["accesskey"])
    api.create_dataset(dataset)

    #3. create transformer code
    transformer = inputs["transformer"]
    if transformer["enable"] == True:
        code = DkubeCode(user, name=name + "-transformer")
        code.update_git_details(transformer["code"]["url"], branch=transformer["code"]["branch"])
        api.create_code(code)

    #4. publish model
    publish = DkubeServing(user, name="publish-"+name, description='model published from siteA')
    publish.update_serving_model(name + "-model")
    publish.update_serving_image(image_url=inputs["predictor"]["image"])
    if transformer["enable"] == True:
        publish.set_transformer(True, script=transformer["script"])
        publish.update_transformer_code(code.name)
        publish.update_transformer_image(image_url=transformer["image"])

    api.publish_model("publish-"+name, "model published from siteA", publish)

    puburl = "{}/#/ds/repos/models/published/user/{}/{}".format(url, user, name+"-model")
    print("\n")
    print("\033[1;31m Imported Resource Details Below  \033[0m \n")
    print("\033[1;30m \t Imported model - %s \033[0m " % (name+"-model"))
    print("\033[1;30m \t Imported dataset - %s \033[0m " % (name+"-dataset"))
    print("\033[1;30m \t Transformer code - %s \033[0m " % (name+"-transformer"))
    print("\033[1;30m \t Published model link - %s \033[0m " % puburl)


if __name__ == "__main__":
    warnings.filterwarnings("ignore")

    parser = argparse.ArgumentParser(description='Argument parser')
    parser.add_argument('url',
                        metavar='url',
                        type=str,
                        help='URL to DKube platform.')

    if os.getenv("DKUBE_JOB_CLASS") != "notebook":
        parser.add_argument('token',
                            metavar='token',
                            type=str,
                            help='DKube access token.')

    flags = parser.parse_args()

    url   = flags.url
    try:
        token = flags.token
    except AttributeError:
        token = os.getenv("DKUBE_USER_ACCESS_TOKEN")
    export_and_publish_model(url, token)
