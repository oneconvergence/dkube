import os
import json
import kfp

from typing import NamedTuple

from ._kfpl import componentize
from .job_properties import JobProperties

from dkube.sdk.internal.dkube_api.models.job_model import JobModel


__all__ = [
    'launch_slurmjob',
    'dkube_slurmjob_op'
]


def launch_slurmjob(cluster: str, props: type(JobProperties),
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
    import kfp
    import json
    import yaml
    from pyfiglet import Figlet
    from url_normalize import url_normalize
    from collections import namedtuple
    from json import JSONDecodeError
    from dkube.sdk.internal.dkube_api.models.job_model import JobModel
    from dkube.sdk.internal.api_base import ApiBase
    from dkube.slurm.job_properties import JobProperties

    if isinstance(run, JobModel) == True:
        run = run.to_dict()
    elif isinstance(run, str) == True:
        run = ast.literal_eval(run)
    else:
        assert True, "type of parameter run can be either instance of JobModel or a string of dict"

    if isinstance(props, JobProperties) == True:
        props = props.to_dict()
    elif isinstance(props, str) == True:
        props = ast.literal_eval(props)
    else:
        assert True, "type of parameter props can be either instance of JobProperties or a string of dict"

    kind = run['parameters']['_class']
    assert kind in [
        "training", "preprocessing"], "Slurm job is supported only for Training/Preprocessing DKube job types"

    f = Figlet(font='slant', width=200)
    print(f.renderText('Dkube {}'.format("SlurmJob")))

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

    slurm = {
        "name": cluster,
        "kind": "CLUSTER_SLURMHPC_REMOTE",
        "scheduling_opts": {
                "slurmhpc": {
                    "file": {
                        "name": "properties.json",
                        "body": json.dumps({
                            "extra": json.dumps(props)})
                    }
                }
        }
    }

    run['parameters'][kind]["cluster"] = slurm

    name = run['name']
    api = ApiBase(url, token, [])
    api._api.jobs_add_one(user=user, data=run, run='true')

    # wait loop
    recorded = None
    while True:
        run = api.get_run(kind, user, name)['job']
        status = run['parameters']['generated']['status']
        state, reason = status['state'], status['reason']
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


dkube_slurmjob_op = componentize(launch_slurmjob,
                                 "dkube_slurmjob_launcher",
                                 "Launcher for slurmjob using DKube APIs.",
                                 "ocdr/dkube_launcher:slurm",
                                 {
                                     'platform': 'Dkube'
                                 },
                                 {
                                     'platform': 'Dkube',
                                     'stage': 'training',
                                     'logger': 'dkubepl',
                                     'dkube.garbagecollect': 'true',
                                     'dkube.garbagecollect.policy':
                                     'all'
                                 })
