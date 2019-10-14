from dkube.sdk.dkube import *
from . import *

#For component_args please check the definition @./components/training.yaml, use value of 'name' field as key
def dkube_training_op(
        env=Environment().internal,
        framework=Framework.Tensorflow,
        name='dkube-training',
        **component_args):

    token       = env.token
    framework   = framework.value
    url         = env.url

    component_args['accessurl'] = url

    return DkubeTrainingOp(name, token, framework, url, **component_args)

"""
def DkubeTrainingOp(name='dkube-training'):
    with open('./components/training.yaml', 'rb') as stream:
        cdict = load_yaml(stream)
        cdict['name'] = name
        cyaml = dump_yaml(cdict)
        return components.load_component_from_text(cyaml)

def DkubePreprocessOp(name='dkube-preprocessing'):
    with open('./components/preprocess.yaml', 'rb') as stream:
        cdict = load_yaml(stream)
        cdict['name'] = name
        cyaml = dump_yaml(cdict)
        return components.load_component_from_text(cyaml)

def DkubeServingOp(name='dkube-serving'):
    with open('./components/serving.yaml', 'rb') as stream:
        cdict = load_yaml(stream)
        cdict['name'] = name
        cyaml = dump_yaml(cdict)
        return components.load_component_from_text(cyaml)

def DkubeViewerOp(name='dkube-viewer'):
    with open('./components/viewer.yaml', 'rb') as stream:
        cdict = load_yaml(stream)
        cdict['name'] = name
        cyaml = dump_yaml(cdict)
        return components.load_component_from_text(cyaml)
"""
