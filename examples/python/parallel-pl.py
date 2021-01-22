import kfp.compiler as compiler
import kfp
import kfp.components as kfplc
import json

from dkube.sdk import *
from dkube.pipelines import *


@kfp.dsl.pipeline(
    name='Parallel stages pipeline',
    description='An example pipeline to launch number of stages in parallel'
)
def parallel_pipeline(
        user = None,
        authtoken = None,
        code = None,
        dataset = None,
        model = None):

    count = 2
    for i in range(count):
        training_name = 'parallel-pl-{}'.format(i)
        training = DkubeTraining(
            str(user), name=training_name, description='triggered from dkube pl launcher')
        training.update_container(
            framework="tensorflow_1.14", image_url="ocdr/d3-datascience-tf-cpu:v1.14")
        training.update_startupscript('sleep 30')
        training.add_code(str(code))
        training.add_input_dataset(str(dataset), mountpath='/opt/dkube/input')
        training.add_output_model(str(model), mountpath='/opt/dkube/output')

        training_op = dkube_training_op(
                    name=training_name,
                    authtoken=authtoken,
                    training=training)

compiler.Compiler().compile(parallel_pipeline, __file__ + '.tar.gz')
