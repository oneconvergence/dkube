from .env import *
from .schema import *
from ._types import *

from . import _helpers as util

def export_model(fspath:str, name:str, autogenerate=False,
                 environ=Environment().internal, 
                 framework:Framework=Framework.Tensorflow):

    assert fspath != '', "file system path cannot be empty"
    assert name != '', "name cannot be empty, with name-auto-generate=True, name will be used as prefix"

    if autogenerate==True:
        version = ""
        if framework == Framework.Tensorflow:
            #extract version from fspath
            version = util._get_tfmodel_version(fspath)
        if version == "":
            version = util._generate_version()
        name = "{}-{}".format(name, version)

    #upload data to dkube storage
    util._upload_to_dkube(environ, fspath, name)

    #create a model in dkube database
    model = Model()
    model.input.name    = name
    model.input.url     = "/model/{}".format(name)
    model.input.source  = DatumSource.dkube
    model.input.tags    = []
    model.input.remote  = False

    util._create_model(environ, model) 

