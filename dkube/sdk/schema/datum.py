import enum
from typing import List

from .timestamps import *
from .status import *

#from timestamps import *
#from status import *

class DatumGitSource(object):
    def __init__(self):
        self.apikey     = ""
        self.password   = ""
        self.private    = False
        self.username   = ""

    @property
    def apikey(self):
        return self.__apikey
    @property
    def password(self):
        return self.__password
    @property
    def private(self):
        return self.__private
    @property
    def username(self):
        return self.__username

    @apikey.setter
    def apikey(self, data :str):
        assert type(data) == str, "type mismatch error"
        self.__apikey = data

    @password.setter
    def password(self, data :str):
        assert type(data) == str, "type mismatch error"
        self.__password = data

    @private.setter
    def private(self, data :bool):
        assert type(data) == bool, "type mismatch error"
        self.__private = data

    @username.setter
    def username(self, data :str):
        assert type(data) == str, "type mismatch error"
        self.__username = data

    def from_json(self, data :dict):
        assert type(data) == dict, "type mismatch error"
        #fill fields from input json

    def to_json(self):
        #return json for this object
        pass


class DatumAwsSource(object):
    def __init__(self):
        self.accesskey  = ""
        self.accessid   = ""
        self.bucket     = ""
        self.endpoint   = ""
        self.prefix     = ""

    @property
    def accesskey(self):
        return self.__accesskey
    @property
    def accessid(self):
        return self.__accessid
    @property
    def bucket(self):
        return self.__bucket
    @property
    def endpoint(self):
        return self.__endpoint
    @property
    def prefix(self):
        return self.__prefix

    @accesskey.setter
    def accesskey(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__accesskey = data

    @accessid.setter
    def accessid(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__accessid = data

    @bucket.setter
    def bucket(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__bucket = data

    @endpoint.setter
    def endpoint(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__endpoint = data

    @prefix.setter
    def prefix(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__prefix = data

    def from_json(self, data:dict):
        assert type(data) == dict, "type mismatch error"
        #fill fields from input json

    def to_json(self):
        #return json for this object
        pass

class DatumMinioSource(DatumAwsSource):
    def __init__(self):
        super().__init__()

class DatumURLSource(object):
    def __init__(self):
        pass

class DatumDkubeSource(object):
    def __init__(self):
        self.__name = "dkube"

    @property
    def name(self):
        return self.__name

class DatumSource(enum.Enum):
    default = None
    git     = DatumGitSource()
    aws     = DatumAwsSource()
    minio   = DatumMinioSource()
    url     = DatumURLSource()
    dkube   = DatumDkubeSource()

class DatumInput(object):
    def __init__(self):
        self.__source = DatumSource.default
        self.__tags   = []
        self.__url    = ""
        self.__remote = False
        self.__name   = ""

    @property
    def source(self):
        return self.__source
    @property
    def tags(self):
        return self.__tags
    @property
    def url(self):
        return self.__url
    @property
    def remote(self):
        return self.__remote
    @property
    def name(self):
        return self.__name

    @source.setter
    def source(self, data:DatumSource):
        assert type(data) == DatumSource, "type mismatch error"
        self.__source = data

    @tags.setter
    def tags(self, data:List[str]) :
        assert type(data) == list, "type mismatch error"
        self.__tags = data

    @url.setter
    def url(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__url = data

    @remote.setter
    def remote(self, data:bool):
        assert type(data) == bool, "type mismatch error"
        self.__remote = data

    @name.setter
    def name(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__name = data



class DatumGenerated(object):
    def __init__(self):
        self.__uuid           = ""
        self.__progress       = 0
        self.__size           = ""
        self.__storagepath    = ""
        self.__timestamps     = TimeStamps()
        self.__status         = Status()

    @property
    def uuid(self):
        return self.__uuid
    @property
    def progress(self):
        return self.__progress
    @property
    def size(self):
        return self.__size
    @property
    def storagepath(self):
        return self.__storagepath
    @property
    def timestamps(self):
        return self.__timestamps
    @property
    def status(self):
        return self.__status

    def _uuid(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__uuid = data

    def _progress(self, data:int):
        assert type(data) == int, "type mismatch error"
        self.__progress = data

    def _size(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__size = data

    def _storagepath(self, data:str):
        assert type(data) == str, "type mismatch error"
        self.__storagepath = data

    def _timestamps(self, data:TimeStamps):
        assert type(data) == TimeStamps, "type mismatch error"
        self.__timestamps = data

    def _status(self, data:Status):
        assert type(data) == Status, "type mismatch error"
        self.__status = data

    def from_json(self, data:dict):
        assert type(data) == dict, "type mismatch error"
        #fill fields from input json

    def to_json(self):
        #return json for this object
        pass
