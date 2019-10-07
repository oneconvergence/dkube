SDK for interfacing with Dkube Pipelines.
All the Dkube ops are supported as simple python funcs.
With dkube pipeline funcs, customized name can be provided for pipeline stages.

Example way to use the dkube pipeline components,

from dkube.pipelines import *
dkube_training_op       = DkubeTrainOp(name='mnist-training')
dkube_serving_op        = DkubeServeOp(name='mnist-serving')
dkube_viewer_op         = DkubeViewerOp(name='mnist-inference')
