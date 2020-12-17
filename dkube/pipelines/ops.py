"""

.. module:: DKubePiplineOps
   :synopsis: Defines pipeline components for dkube ops. Pipeline writer can use these ops to write and submit jobs to DKube platform.

.. moduleauthor:: Ahmed Khan <github.com/mak-454>

"""

import json

from dkube.sdk import *

from .components import *


def dkube_training_op(name=generate('training'), authtoken=None, training=DkubeTraining):

    """
        DKube Op to define a training job as a stage in pipeline.
        When run this op submits a job on DKube platform and waits for it to be completed.

        *Inputs*

            name
                Name of the stage. The passed name will be set as display_name for the stage.

            authtoken
                API authentication token. User can get this find under DeveloperSettings in DKube UI.

            training
                Instance of :bash:`dkube.sdk.rsrcs.DkubeTraining` class.
                All the properties of the job can defined in this object.
	"""

    assert type(training) == DkubeTraining, "Invalid type for training argument, must be instance of dkube.sdk.rsrcs:DkubeTraining"
    assert authtoken == None, "Auth token is must"

    return dkube_op(name, authtoken, 'training', training=json.dumps(training.job.to_dict()))

def dkube_preprocessing_op(name=generate('data'), authtoken=None, preprocessing=DkubePreprocessing):

    """
        DKube Op to define a preprocessing job as a stage in pipeline.
        When run this op submits a job on DKube platform and waits for it to be completed.

        *Inputs*

            name
                Name of the stage. The passed name will be set as display_name for the stage.

            authtoken
                API authentication token. User can get this find under DeveloperSettings in DKube UI.

            preprocessing
                Instance of :bash:`dkube.sdk.rsrcs.DkubePreprocessing` class.
                All the properties of the job can defined in this object.
	"""

    assert type(preprocessing) == DkubePreprocessing, "Invalid type for preprocessing argument, must be instance of dkube.sdk.rsrcs:DkubePreprocessing"
    assert authtoken == None, "Auth token is must"

    return dkube_op(name, authtoken, 'preprocessing', preprocessing=json.dumps(preprocesing.job.to_dict()))

def dkube_serving_op(name=generate('serving'), authtoken=None, serving=DkubeServing):

    """
        DKube Op to deploy a model for serving in a stage in pipeline.
        When run this op submits a job on DKube platform and waits for it to be deployed.

        *Inputs*

            name
                Name of the stage. The passed name will be set as display_name for the stage.

            authtoken
                API authentication token. User can get this find under DeveloperSettings in DKube UI.

            serving
                Instance of :bash:`dkube.sdk.rsrcs.DkubeServing` class.
                All the properties of the job can defined in this object.
    """

    assert type(serving) == DkubeServing, "Invalid type for serving argument, must be instance of dkube.sdk.rsrcs:DkubeServing"
    assert authtoken == None, "Auth token is must"

    return dkube_op(name, authtoken, 'serving', serving=json.dumps(serving.job.to_dict()))
