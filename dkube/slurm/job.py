from __init__ import componentize

import os
import json
import kfp

from typing import NamedTuple

from job_properties import JobProperties
from dkube.sdk.internal.dkube_api.models.job_model import JobModel

__all__ = [
    'launch_slurmjob',
    'dkube_slurmjob_op'
]


def launch_slurmjob(slurm_cluster: str, slurm_jobprops: type(JobProperties),
                    dkube_user: str, dkube_token: str, dkube_job: type(JobModel),
                    dkube_url: str = 'https://dkube-proxy.dkube',
                    execution_id: str = "{{workflow.uid}}",
                    run_id: str = "{{pod.name}}") -> NamedTuple(
        'outputs',
        [
            ('artifacts', str),
            ('run_details', str)
        ]):

    import ast
    import time
    import os
    import json
    import kfp
    import json
    from pyfiglet import Figlet
    from dkube.sdk.internal import dkube_api
    from dkube.sdk.internal.dkube_api.rest import ApiException
    from url_normalize import url_normalize
    from collections import namedtuple
    from dkube.sdk.internal.dkube_api.models.job_model import JobModel
    from dkube.slurm.job_properties import *
    from json import JSONDecodeError

    def run_dict():
        if isinstance(dkube_job, JobModel) == True:
            return dkube_job.to_dict()
        elif isinstance(dkube_job, str):
            # try to json load
            try:
                return json.loads(dkube_job)
            except JSONDecodeError:
                # not a json str, attempt diff method
                return ast.literal_eval(dkube_job)
        else:
            assert True, "Unsupported type for dkube_job parameter."

    run = run_dict()
    _class = run['parameters']['_class']
    pipeline = run_id == os.getenv("HOSTNAME")
    assert _class in [
        "training", "preprocessing"], "Slurm job is supported only for Training/Preprocessing DKube job types"

    def display():
        f = Figlet(font='slant', width=200)
        print(f.renderText('Dkube {}'.format("SlurmJob")))

    display()

    def fill():
        if pipeline == True:
            run['name'] = run_id
            run['parameters']['training']['tags'].extend(
                ['owner=pipeline', 'workflowid=' + execution_id, 'runid=' + run_id])
            # Update pipeline information
            run['parameters']['generated'] = dict()
            run['parameters']['generated'].update(
                {'pipeline': {'runid': execution_id}})
        return run

    run = fill()
    run['parameters']['class'] = _class
    runname = run['name']

    def slurm_jobprops_dict():
        if isinstance(slurm_jobprops, JobProperties) == True:
            return slurm_jobprops.to_dict()
        elif isinstance(slurm_jobprops, str):
            # try to json load
            try:
                return json.loads(slurm_jobprops)
            except BaseException:
                # not a json str, attempt diff method
                return ast.literal_eval(slurm_jobprops)
        else:
            assert True, "Unsupported type for slurm_jobprops parameter."

    def cluster():
        slurm = {
            "name": slurm_cluster,
            "kind": "CLUSTER_SLURMHPC_REMOTE",
            "scheduling_opts": {
                "slurmhpc": {
                    "file": {
                        "name": "job_config.json",
                        "body": json.dumps({"extra": json.dumps(slurm_jobprops)})}}}}
        run['parameters'][_class]["cluster"] = slurm

    slurm_jobprops = slurm_jobprops_dict()
    cluster()

    def client():
        configuration = dkube_api.Configuration()
        configuration.api_key_prefix['Authorization'] = 'Bearer'
        configuration.host = url_normalize(
            '{}/dkube/v2/controller'.format(dkube_url))
        configuration.verify_ssl = False
        configuration.api_key['Authorization'] = dkube_token
        api = dkube_api.DkubeApi(dkube_api.ApiClient(configuration))
        return api

    api = client()
    print(run)
    api.jobs_add_one(dkube_user, run, run='true')

    def wait():
        while True:
            response = api.jobs_get_collection_one(dkube_user, _class, runname)
            status = response.to_dict(
            )['data']['job']['parameters']['generated']['status']
            run = response.to_dict()['data']['job']
            state, reason = status['state'], status['reason']
            if state.lower() in ['complete', 'failed', 'error']:
                print(
                    "run {} - completed with state {} and reason {}".format(runname, state, reason))
                return run
            else:
                print(
                    "run {} - waiting for completion, current state {}".format(runname, state))
            time.sleep(10)

    run = wait()

    rundetails = json.dumps(run)

    uuid = run['parameters']['generated']['uuid']
    lineage = api.get_one_run_lineage(dkube_user, _class, uuid)
    outputs = lineage.to_dict()['data']['outputs']
    artifacts = [
        {'datum': output['version']['datum_name'], 'class': output['version']['datum_type'],
         'version': output['version']['uuid'], 'index': output['version']['index']
         }
        for output in outputs
    ]

    artifacts = json.dumps(artifacts)

    output = namedtuple('Outputs', ['artifacts', 'run_details'])
    return output(artifacts, rundetails)


dkube_slurmjob_op = componentize(launch_slurmjob, "dkube_slurmjob_launcher", "Launcher for slurmjob using DKube APIs.",
                                 "ocdr/dkube_launcher:py", {'platform': 'Dkube'}, {'platform': 'Dkube'})
