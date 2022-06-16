import logging
import os
from . import *

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def create_run(url=None, token=None, user=None, name=None, code=None, code_version=None, dataset=None, dataset_version=None, model=None, model_version=None, output=None):
    print("creating mlflow run")

    user = user or os.getenv("DKUBE_USER_LOGIN_NAME", None)
    assert (user), "User must be provided."

    assert (output), "Output must be provided."

    api = DkubeApi(URL=url, token=token)

    if name is None:
        name = "mlflow"
    training_name = generate(name)
    logger.info("Creating a training run (" +
                training_name + ") for user " + user)
    training = DkubeTraining(user, name=training_name,
                             description='Mlflow training run')
    training.update_container(
        framework="tensorflow_2.0.0", image_url="ocdr/dkube-datascience-tf-cpu:v2.0.0")
    if code is not None:
        training.add_code(code, code_version)
    if dataset is not None:
        training. add_input_dataset(datset, dataset_version)
    if model is not None:
        training.add_input_model(model, model_version)
    training.add_output_model(output)
    training.disable_execution()

    api.create_training_run(training, wait_for_completion=False)

    run_response = api.get_training_run(user, training_name)
    run_id = run_response["job"]["parameters"]["generated"]["uuid"]

    logger.info("DKube run id (" + run_id +
                "), metrics can be reported against it")

    return run_id
