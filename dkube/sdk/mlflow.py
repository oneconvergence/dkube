import logging
import os
from . import *
from dkube.sdk.internal.api_base import *

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def create_run(url=None, token=None, user=None, name=None, code=None, code_version=None, dataset=None, dataset_version=None, model=None, model_version=None, output=None):
    token = token or os.getenv("DKUBE_USER_ACCESS_TOKEN", None)
    assert (token), "Token must be provided."

    api = DkubeApi(URL=url, token=token)

    run_id = os.getenv('DKUBE_MLFLOW_RUN_ID', None)
    if run_id:
        try:
            run = ApiBase.get_run_byuuid(api, run_id)
        except Exception as e:
            raise e
        run_class = run['parameters']['_class']
        if run_class != "notebook":
            logger.info("DKube run id (" + run_id +
                        "), use it as mlflow run id")
            return run_id

    user = user or os.getenv("DKUBE_USER_LOGIN_NAME", None)
    assert (user), "User must be provided."
    assert (output), "Output must be provided."

    if name is None:
        name = "mlflow"
    training_name = generate(name)
    logger.info("Creating a training run (" +
                training_name + ") for user " + user)
    training = DkubeTraining(user, name=training_name,
                             description='Mlflow training run')
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
                "), use it as mlflow run id")

    return run_id
