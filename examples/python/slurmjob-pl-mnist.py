import kfp
import kfp.components as kfplc
import json

from dkube.sdk import *
from dkube.slurm.job import *
from dkube.slurm.job_properties import *

@kfplc.create_component_from_func
def print_op(artifacts: str):
    print(artifacts)

@kfp.dsl.pipeline(
  name='slurm job pipeline',
  description='An example pipeline for launching slurm job.'
)
def slurm_pipeline():
    training_name= generate('mnist')
    training = DkubeTraining("ravih1", name=training_name, description='triggered from dkube pl launcher')
    training.update_container(framework="tensorflow_1.14", image_url="ocdr/d3-datascience-tf-cpu:v1.14")
    training.update_startupscript('python model.py')
    training.add_project("mn")
    training.add_input_dataset("tf-mnist", mountpath='/opt/dkube/input')
    training.add_output_model("mn", mountpath='/opt/dkube/output')

    props = JobProperties(partition="C-16Cpu-30GB")
        
    slurm_job = dkube_slurmjob_op("dap20", props, "ravih1", "eyJhbGciOiJSUzI1NiIsImtpZCI6Ijc0YmNkZjBmZWJmNDRiOGRhZGQxZWIyOGM2MjhkYWYxIn0.eyJ1c2VybmFtZSI6InJhdmloMSIsInJvbGUiOiJkYXRhc2NpZW50aXN0LG1sZSxwZSIsImV4cCI6NDg0NTUxMzY0MCwiaWF0IjoxNjA1NTEzNjQwLCJpc3MiOiJES3ViZSJ9.J3gLupMf9oJ0LFr7khHJ8ClfCpp-ClI8sav6GHwO76p1Oae_DVO7LEYWLpULtEiFvDAXjwHtZrJhs69TTSvS4QElM27F3Pi67t9nbku5y3XaowvbwZwmLxQwWfKITA_u0BKdnEyUHg9ON7Ncdb1GW8qlYNh9L5Y3hEKMJsXqXtJF1wPSKxvsjOV_zEwsX90JVkXUluAUrtZaA4yYTDXQUYPsYSWScZvPwQ_mJBL-ghWZomzVx4yLFliwBn_iANA4iCCOoSs7Y9pU1PlBMr24_2nrSQ1HSdsGX5pX-9zj9JCo6i5XhKFTqLak_4UD2ME7c6WibRujjTK4vvVwxwhGDw", training.job)
    
    print_artifacts = print_op(slurm_job.outputs['artifacts'])


import kfp.compiler as compiler
compiler.Compiler().compile(slurm_pipeline, __file__ + '.tar.gz')
