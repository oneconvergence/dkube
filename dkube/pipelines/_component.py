from kfp.components._yaml_utils import load_yaml
from kfp.components._yaml_utils import dump_yaml
from kfp import components

def DkubeTrainingOp(name, token, url, **kwargs):
    component = None
    with open('components/training.yaml', 'rb') as stream:
        cdict = load_yaml(stream)
        cdict['name'] = name
        cyaml = dump_yaml(cdict)
        component = components.load_component_from_text(cyaml)

    assert component == None, "Internal error, loading DKube training component failed"

    return component(token, container, **kwargs)
