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


    #1. upload model
    name = generate(inputs["model"])
    fpath = inputs["fpath"]
    api.upload_model(user, name, fpath, extract=True)

    #2. create transformer code
    transformer = inputs["transformer"]
    if transformer["enable"] == True:
        code = DkubeCode(user, name=name + "-transformer")
        code.update_git_details(transformer["code"]["url"], branch=transformer["code"]["branch"])
        api.create_code(code)

    #3. publish model
    publish = DkubeServing(user, name="publish-"+name, description='model published from siteA')
    publish.update_serving_model(name)
    publish.update_serving_image(image_url=inputs["predictor"]["image"])
    if transformer["enable"] == True:
        publish.set_transformer(True, script=transformer["script"])
        publish.update_transformer_code(code.name)
        publish.update_transformer_image(image_url=transformer["image"])

    api.publish_model("publish-"+name, "model published from siteA", publish)


if __name__ == "__main__":
    warnings.filterwarnings("ignore")

    parser = argparse.ArgumentParser(description='Argument parser')
    parser.add_argument('url',
                        metavar='url',
                        type=str,
                        help='URL to DKube platform.')
    parser.add_argument('token',
                        metavar='token',
                        type=str,
                        help='DKube access token.')

    flags = parser.parse_args()

    url   = flags.url
    token = flags.token
    export_and_publish_model(url, token)
