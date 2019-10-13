"""
This constant means non distributed training.
"""
NO_DISTRIBUTED_TRAINING_CONFIG = {'nworkers': 0, 'strategy': DISTRIBUTION_STRATEGY_NONE}


"""
This constant means non distributed training.
This is the default option chosen if distributed_training field is not passed
to dkube training component.
"""
DISTRIBUTED_TRAINING_DEFAULT = NO_DISTRIBUTED_TRAINING_CONFIG

"""
Used when distributed training is not intended.
DISTRIBUTION_STRATEGY_NONE = 'None'
"""

"""
Strategy is applied based on the chosen training framework.
TF_CONFIG based distribution is applied if framework == tensorflow
MPI Job based distribution is applied if framework == custom
"""
DISTRIBUTION_STRATEGY_DEFAULT = 'default'


"""
Same as DISTRIBUTION_STRATEGY_DEFAULT but only difference is Dkube will auto adjust the requested GPU count
based on the availability in the cluster.
If no gpus(s) are availabled then Dkube will choose to run without gpus.
Program must not assume availability of GPU device when this option is chosen.
"""
DISTRIBUTION_STRATEGY_AUTO = 'auto' 


"""
This will supported in future,
and will be based on https://www.tensorflow.org/guide/distributed_training#using_tfdistributestrategy_with_keras
This strategy definition can be used when framework == tensorflow
"""
DISTRIBUTION_STRATEGY_TF = 'unsupported'
