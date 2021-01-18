import kfp.compiler as compiler
import kfp
import kfp.components as kfplc
import json

from dkube.sdk import *
from dkube.slurm.job import *
from dkube.slurm.job_properties import *
from dkube.pipelines import *


@kfplc.create_component_from_func
def print_op(artifacts: str):
    print(artifacts)


@kfp.dsl.pipeline(
    name='slurm job pipeline',
    description='An example pipeline for launching slurm job.'
)
def slurm_pipeline(
        user = None,
        token = None,
        code = None,
        dataset = None,
        model = None,
        slurm_cluster = None,
        slurm_jobprops = json.dumps(JobProperties().to_dict())):

    training_name = generate('mnist')
    training = DkubeTraining(
        str(user), name=training_name, description='triggered from dkube pl launcher')
    training.update_container(
        framework="tensorflow_1.14", image_url="ocdr/d3-datascience-tf-cpu:v1.14")
    training.update_startupscript('python model.py')
    training.add_code(str(code))
    training.add_input_dataset(str(dataset), mountpath='/opt/dkube/input')
    training.add_output_model(str(model), mountpath='/opt/dkube/output')

    slurm_job = dkube_slurmjob_op(
        slurm_cluster, slurm_jobprops, str(user), str(token), training.job)

    print_artifacts = print_op(slurm_job.outputs['artifacts']).after(slurm_job)

    serving_name = generate(str(model))
    serving = DkubeServing(str(user), name=serving_name,
                           description='triggered from dkube pl launcher')
    serving.set_transformer(
        True, script='tensorflow/classification/mnist/digits/transformer/transformer.py')
    serving.update_serving_model(str(model))

    serving_op = dkube_serving_op(
        name='mnist-serving',
        authtoken=token,
        serving=serving).after(print_artifacts)


compiler.Compiler().compile(slurm_pipeline, __file__ + '.tar.gz')
