import enum
from .datum import *

class Version(object):
    def __init__(self):
        self.__name         = ''
        self.__index        = ''
        self.__user         = ''
        self.__datumname    = ''
        self.__datumtype    = ''
        self.__storagepath  = ''
        self.__syncstate    = ''
        self.__versionid    = ''
        self.__commitid     = ''

    @property
    def name(self):
        return self.__name

    @property
    def index(self):
        return self.__index

    @property
    def user(self):
        return self.__user

    @property
    def datumname(self):
        return self.__datumname

    @property
    def datumtype(self):
        return self.__datumtype

    @property
    def storagepath(self):
        return self.__storagepath

    @property
    def syncstate(self):
        return self.__syncstate

    @property
    def versionid(self):
        return self.__verisonid

    @property
    def commitid(self):
        return self.__commitid


    @name.setter
    def name(self, val:str):
        assert type(val) == str, "type mismatch error"
        self.__name = val

    @index.setter
    def index(self, val:int):
        assert type(val) == int, "type mismatch error"
        self.__index = val

    @user.setter
    def user(self, val:str):
        assert type(val) == str, "type mismatch error"
        self.__user = val

    @datumname.setter
    def datumname(self, val:str):
        assert type(val) == str, "type mismatch error"
        self.__datumname = val

    @datumtype.setter
    def datumtype(self, val:str):
        assert type(val) == str, "type mismatch error"
        self.__datumtype == val

    @storagepath.setter
    def storagepath(self, val:str):
        assert type(val) == str, "type mismatch error"
        self.__storagepath = val

    @syncstate.setter
    def syncstate(self, val:str):
        assert type(val) == str, "type mismatch error"
        self.__syncstate = val

    @versionid.setter
    def versionid(self, val:str):
        assert type(val) == str, "type mismatch error"
        self.__versionid = val

    @commitid.setter
    def commitid(self, val:str):
        assert type(val) == str, "type mismatch error"
        self.__commitid = val

    def to_json(self):
        return {
            'name': self.name,
            'index': self.index,
            'user': self.user,
            'datumname': self.datumname,
            'datumtype': self.datumtype,
            'storagepath': self.storagepath,
            'syncstate': self.syncstate,
            'versionid': self.versionid,
            'commitid': self.commitid
        }

    def from_json(self, data:dict):
        self.name = data['name']
        self.index = data['index']
        self.user = data['user']
        self.datumname = data.get('datumName', '')
        self.datumtype = data.get('datumType', '')
        self.storagepath = data.get('storagePath', '')
        self.syncstate = data.get('syncState', '')
        self.versionid = data['uuid']
        self.commitid = data.get('commitID', '')
        return self
