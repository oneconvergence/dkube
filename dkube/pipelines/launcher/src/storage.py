import click
import json
from utils import print_json

@click.command()
@click.pass_obj
@click.argument("command")
@click.argument("namespace")
@click.argument("claims")
def storage(obj, command, namespace, claims):
    print ("command: {}\nnamespace: {}\n".format(command, namespace))
    api = obj["api"]
    data = {
        "uid": obj["workflowid"],
        "namespace": namespace
    }
    if command == "reclaim":
        api.storage_volume_reclaim(data)
        return
    
    claims = json.loads(claims)
    print_json({"claims":claims})
    
    for kind in ["input","output","intermediate"]:
        data = {
            "uid": obj["workflowid"],
            "namespace": namespace,
            "kind": kind,
            "volumes": []
        }
        for claim in claims:
            if claim["kind"] == kind:
                data["volumes"].append(claim["volume"])

        if len(data["volumes"]) > 0:
            api.storage_volume_export(data)