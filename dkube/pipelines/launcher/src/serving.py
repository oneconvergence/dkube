from utils import run_outputs, print_json
import json
from dkube.sdk import generate
import time
import click

def command_serving(api=None, run={}, name='', user='', runid='', workflowid='', **kwargs):
    stagename = name

    runname = generate('plserving')

    run['name'] = runname
    run['parameters']['class'] = 'inference'
    #run['parameters']['inference']['tags'].extend(['owner=pipeline', 'stage='+name, 'workflowid='+workflowid, 'runid='+runid])

    # Update pipeline information
    run['parameters']['generated'] = {'pipeline': {'runid': runid, 'name': stagename}}

    inf = run['parameters']['inference']
    if inf['serving_image']['image'] == None or (
            inf['transformer'] == True and inf['transformer_image']['image'] == None) or (
                inf['transformer'] == True and inf['transformer_project'] == None):

        if inf['version'] == None:
            v = api.get_model_latest_version(inf['owner'], inf['model'])
            inf['version'] = v['uuid']

        li = api.get_model_lineage(inf['owner'], inf['model'], inf['version'])
        if inf['serving_image']['image'] == None:
            si = li['run']['parameters']['generated']['serving_image']['image']
            inf['serving_image']['image'] = dict(si)

        if inf['transformer'] == True and inf['transformer_image']['image'] == None:
            ti = li['run']['parameters']['generated'][
                'training_image']['image']
            inf['transformer_image']['image'] = dict(ti)

        if inf['transformer'] == True and inf['transformer_project'] == None:
            code = li['run']['parameters']['training'][
                'datums']['workspace']['data']
            inf['transformer_project'] = code['name']
            inf['transformer_commit_id'] = code['version']

    run['parameters']['inference'] = inf
    api.jobs_add_one(user, run, run='true')
    while True:
        response = api.jobs_get_collection_one(user, 'inference', runname)
        status = response.to_dict()['data']['job']['parameters'][
            'generated']['status']
        state, reason = status['state'], status['reason']
        if state.lower() in ['running', 'failed', 'error']:
            print(
                "run {} - completed with state {} and reason {}".format(runname, state, reason))
            break
        else:
            print(
                "run {} - waiting for completion, current state {}".format(runname, state))
            time.sleep(10)

    # generate the outputs, next stage can pick from here
    run_outputs(api, user, 'inference', runname)



@click.command()
@click.pass_obj
@click.argument("configuration")
def serving(obj, configuration):
    run = json.loads(configuration)
    print_json(run)
    command_serving(run=run, **obj)