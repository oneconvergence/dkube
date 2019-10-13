"""
Dkube packaged data science images which are readily available for datascientists to use.
Images are packed with useful libraries and tools.
"""
DKUBE_DS_TF_CPU_1_13_IMAGE_PATH = "ocdr/dkube-datascience-tf-cpu:v1.13"
DKUBE_DS_TF_CPU_1_14_IMAGE_PATH = "ocdr/dkube-datascience-tf-cpu:v1.14"
DKUBE_DS_TF_GPU_1_13_IMAGE_PATH = "ocdr/dkube-datascience-tf-gpu:v1.13"
DKUBE_DS_TF_GPU_1_14_IMAGE_PATH = "ocdr/dkube-datascience-tf-gpu:v1.14"


"""
Used when distributed training is not intended.
"""
DISTRIBUTION_STRATEGY_NONE = 'None'

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
