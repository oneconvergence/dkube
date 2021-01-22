import kfp.compiler as compiler
import kfp
import kfp.components as kfplc
import json
import ast

from dkube.sdk import *
from dkube.slurm.job import *
from dkube.slurm.job_properties import *
from dkube.pipelines import *

dkube_servingop = kfplc.load_component_from_url(
    "https://raw.githubusercontent.com/oneconvergence/dkube/2.2.slurm/components/serving/component.yaml")


@kfplc.create_component_from_func
def extract_version(artifacts: str) -> str:
    import json
    print(artifacts)
    artifacts = json.loads(artifacts)
    version = artifacts[0]["version"]
    return version


@kfp.dsl.pipeline(
    name='slurm job pipeline',
    description='An example pipeline for launching slurm job.'
)
def slurm_pipeline(
        user=None,
        authtoken=None,
        code=None,
        dataset=None,
        model=None,
        slurm_cluster=None,
        slurm_jobprops: type(JobProperties) = JobProperties()):

    training_name = generate('mnist')
    training = DkubeTraining(
        str(user), name=training_name, description='triggered from dkube pl launcher')
    training.update_container(
        framework="tensorflow_1.14", image_url="ocdr/d3-datascience-tf-cpu:v1.14")
    training.update_startupscript('python model.py')
    training.add_code(str(code))
    training.add_input_dataset(str(dataset), mountpath='/opt/dkube/input')
    training.add_output_model(str(model), mountpath='/opt/dkube/output')

    slurm_task = dkube_slurmjob_op(
        slurm_cluster, slurm_jobprops, str(user), str(authtoken), training.job).set_display_name("training")

    extract_task = extract_version(
        slurm_task.outputs['artifacts']).after(slurm_task).set_display_name("extract_version")
    serving_task = dkube_servingop(
        str(authtoken), str(model),
        model_version=extract_task.output,
        serving_image=json.dumps({'image': 'ocdr/tensorflowserver:1.14'}),
        transformer_image=json.dumps(
            {'image': 'docker.io/ocdr/d3-datascience-tf-cpu:v1.14'}),
        transformer_project=str(code),
        transformer_code='tf/classification/mnist/digits/transformer/transformer.py').after(extract_task).set_display_name("serving")


compiler.Compiler().compile(slurm_pipeline, __file__ + '.tar.gz')
