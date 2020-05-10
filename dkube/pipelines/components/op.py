from pathlib import Path

import json

from kfp.components._yaml_utils import load_yaml
from kfp.components._yaml_utils import dump_yaml
from kfp import components

VALID_STAGES = ['training', 'preprocessing', 'serving', 'custom']
def dkube_op(name, token, stage, **kwargs):
    assert stage in VALID_STAGES, "Invalid value for stage, must be one of training/preprocessing/serving/custom"

    component = None
    path = Path(__file__).parent
    with open('{}/dkube.yaml'.format(path), 'rb') as stream:
        cdict = load_yaml(stream)
        cdict['name'] = name
        cdict['metadata']['labels']['stage'] = stage
        cyaml = dump_yaml(cdict)
        component = components.load_component_from_text(cyaml)

    assert component != None, "Internal error, loading DKube component failed"

    return component(name, token, stage, **kwargs)
