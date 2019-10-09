import sys
import logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)

from .env import *
from .schema import *
from ._types import *
from ._helpers import *

def export_model(fspath:str, name:str, autogenerate=False,
                 environ=Environment().internal, 
                 framework:Framework=Framework.Tensorflow):

    assert fspath != '', "file system path cannot be empty"
    assert name != '', "name cannot be empty, with name-auto-generate=True, name will be used as prefix"

    if autogenerate==True:
        version = ""
        if framework == Framework.Tensorflow:
            #extract version from fspath
            version = get_tfmodel_version(fspath)
        if version == "":
            version = generate_version()
        name = "{}-{}".format(name, version)

    #upload data to dkube storage
    upload_to_dkube(environ, fspath, name)

    logger.info("data uploaded to dkube storage sucessfully")

    #create a model in dkube database
    model = Model()
    model.input.name    = name
    model.input.url     = "/model/{}".format(name)
    model.input.source  = DatumSource.dkube
    model.input.tags    = []
    model.input.remote  = False

    create_model(environ, model) 

    logger.debug("model created successfully in dkube")

