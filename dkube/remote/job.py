import os
import json

from typing import NamedTuple

from dkube.sdk.internal.dkube_api.models.job_model import JobModel


__all__ = [
    'launch_remotejob'
]


ClusterKindSlurmRemote = "slurm-remote"
ClusterKindLsfRemote = "lsf-remote"

def launch_remotejob(cluster: str, cluster_kind: str, props,
                    user: str, token: str, run: type(JobModel),
                    url: str = 'https://dkube-proxy.dkube') -> NamedTuple(

        'outputs',
        [
            ('artifacts', str),
            ('run_details', str)
        ]):

    import pprint
    import ast
    import time
    import os
    import json
    import json
    import yaml
    from pyfiglet import Figlet
    from url_normalize import url_normalize
    from collections import namedtuple
    from json import JSONDecodeError
    from dkube.sdk.internal.dkube_api.models.job_model import JobModel
    from dkube.sdk.internal.api_base import ApiBase
    from dkube.remote.job_properties import SLURM_JobProperties, LSF_JobProperties

    if isinstance(run, JobModel) == True:
        run = run.to_dict()
    elif isinstance(run, str) == True:
        run = ast.literal_eval(run)
    else:
        assert True, "type of parameter run can be either instance of JobModel or a string of dict"

    assert cluster_kind in [ClusterKindSlurmRemote, ClusterKindLsfRemote], "Not a valid cluster kind: {}".format(cluster_kind)

    if isinstance(props, SLURM_JobProperties) == True or isinstance(props, LSF_JobProperties) == True:
        props = props.to_dict()
    elif isinstance(props, str) == True:
        props = json.loads(props)
        #props = ast.literal_eval(props)
    else:
        assert True, "type of parameter props can be either instance of SLURM_JobProperties, LSF_JobProperties or a string of dict"

    kind = run['parameters']['_class']
    assert kind in [
        "training", "preprocessing"], "{} job is supported only for Training/Preprocessing DKube job types".format(cluster_kind)

    f = Figlet(font='slant', width=200)
    figletMsg = ""
    if cluster_kind == ClusterKindSlurmRemote:
        figletMsg = 'Dkube {}'.format("SlurmJob")
    else:
        figletMsg = 'Dkube {}'.format("LsfJob")
    print(f.renderText(figletMsg))

    print("... Input (run) ...")
    print(yaml.dump(run))
    print()
    print("... Input (properties) ...")
    print(yaml.dump(props))
    print("...................")

    run['parameters']['class'] = kind
    # check if am running as pipeline component
    if os.getenv('pipeline', 'false').lower() == 'true':
        wfid, runid = os.getenv("wfid"), os.getenv("runid")
        run['name'] = runid
        run['parameters']['training']['tags'].extend(
            ['owner=pipeline', 'workflowid=' + wfid, 'runid=' + runid])
        if run['parameters']['generated'] is None:
            run['parameters']['generated'] = dict()
        run['parameters']['generated']['uuid'] = runid
        run['parameters']['generated'].update({'pipeline': {'runid': wfid}})

    if cluster_kind == ClusterKindSlurmRemote:
        props = {"extra": json.dumps(props)}
    cluster = {
        "name": cluster,
        "kind": cluster_kind,
        "scheduling_opts": {
                "hpc": {
                    "file": {
                        "name": "properties.json",
                        "body": json.dumps(props)
                    }
                }
        }
    }

    run['parameters'][kind]["cluster"] = cluster

    name = run['name']
    api = ApiBase(url, token, [])
    api._api.jobs_add_one(user=user, data=run, run='true')

    # wait loop
    recorded = None
    while True:
        status = {}
        try:
            run = api.get_run(kind, user, name)['job']
            status = run['parameters']['generated']['status']
            state, reason = status['state'], status['reason']
        except ValueError as ve:
            ve_without_num = "".join(i for i in str(ve) if not i.isdigit()).lower()
            if "Invalid value for `state` (Waiting for  gpu(s))".lower() in ve_without_num or "versioning" in ve_without_num or "login_required" in ve_without_num or "pending" in ve_without_num:
                num = "".join(i for i in str(ve) if i.isdigit())
                status["state"] = "Waiting for {} gpu(s)".format(num)
                status["reason"] = ""
            else:
                raise ve

        if state.lower() in ['complete', 'failed', 'error']:
            print(
                "run {} - completed with state {} and reason {}".format(name, state, reason))
            break
        else:
            if recorded != state:
                print(
                    "run {} - waiting for completion, current state {}".format(name, state))
        recorded = state
        time.sleep(10)

    rundetails = json.dumps(run)

    uuid = run['parameters']['generated']['uuid']
    lineage = api.get_run_lineage(kind, user, uuid)
    outputs = lineage['outputs']
    artifacts = [
        {'datum': output['version']['datum_name'], 'class': output['version']['datum_type'],
         'version': output['version']['uuid'], 'index': output['version']['index']
         }
        for output in outputs
    ]

    artifacts = json.dumps(artifacts)

    output = namedtuple('Outputs', ['artifacts', 'run_details'])
    return output(artifacts, rundetails)
