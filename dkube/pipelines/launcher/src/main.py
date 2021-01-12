import os
import sys

import click
from dkube.sdk.internal import dkube_api
from pyfiglet import Figlet

from preprocessing import preprocessing
from serving import serving
from storage import storage
from submit import submit
from training import training
from utils import debug_requests_on, validate_token


@click.group()
@click.pass_context
@click.argument("name")
@click.argument("token")
@click.argument("wfid")
@click.argument("runid")
def main(ctx, name, token, wfid, runid):
    f = Figlet(font="slant")
    print(f.renderText("Dkube {}".format(ctx.invoked_subcommand.capitalize())))

    # Configure API key authorization: d3apikey
    configuration = dkube_api.Configuration()
    configuration.api_key_prefix["Authorization"] = "Bearer"
    configuration.api_key["Authorization"] = token

    # Bug: Go via proxy since token-info API is not returning claims on direct http call
    # dkubeURL = 'http://dkube-controller-master.dkube:5000'
    dkubeURL = "https://dkube-proxy.dkube"
    configuration.host = "{}/dkube/v2/controller".format(dkubeURL)
    configuration.verify_ssl = False

    api = dkube_api.DkubeApi(dkube_api.ApiClient(configuration))
    user, role = validate_token(api, token)
    debug = os.environ.get("DKUBE_OP_DEBUG", "0")

    if debug == "1":
        debug_requests_on()

    ctx.obj = {
        "api": api,
        "name": name,
        "token": token,
        "workflowid": wfid,
        "runid": runid,
        "user": user,
        "role": role,
        "debug": debug,
    }


main.add_command(preprocessing)
main.add_command(training)
main.add_command(serving)
main.add_command(storage)
main.add_command(submit)

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
