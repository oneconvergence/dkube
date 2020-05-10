SDK for interfacing with Dkube Pipelines.
All the Dkube ops are supported as simple python funcs.
With dkube pipeline funcs, customized name can be provided for pipeline stages.

Example way to use the dkube pipeline components,

from dkube.pipelines import *
dkube_training_op       = dkube_training_op(name='mnist-training')
dkube_preprocess_op     = dkube_preprocessing_op(name='mnist-preprocessing')
dkube_serving_op        = dkube_serving_op(name='mnist-serving')
