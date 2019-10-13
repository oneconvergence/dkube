import os
import validators
import enum

class EnvironmentType(enum.Enum):
    INTERNAL = "internal"
    EXTERNAL = "external"

class Environment(object):
    def __init__(self, ip:str='127.0.0.1', user:str='', token:str=''):
        assert validators.ipv4(ip) == True, "type mismatch for ip field should be IPV4 address"
        assert type(user) == str, "type mismatch error, username must be string"
        assert type(token) == str, "type mismatch error, token must be string"

        self.__ip     = ip
        self.__user   = user
        self.__token  = token

    @property
    def internal(self):
        self.type       = EnvironmentType.INTERNAL
        self.endpoint   = os.getenv('DKUBE_STORE_S3_ENDPOINT')
        self.key        = os.getenv('DKUBE_STORE_S3_ACCESS_KEY')
        self.secret     = os.getenv('DKUBE_STORE_S3_ACCESS_SECRET')
        self.bucket     = os.getenv('DKUBE_STORE_S3_BUCKET')
        self.user       = os.getenv('DKUBE_LOGIN_USERNAME')
        self.token      = os.getenv('DKUBE_ACCESS_TOKEN')
        self.url        = os.getenv('DKUBE_ACCESS_URL')
        return self

    @property
    def external(self):
        self.type       = EnvironmentType.EXTERNAL
        self.endpoint   = "{}:32222".format(self.__ip)
        self.key        = os.getenv('DKUBE_STORE_S3_ACCESS_KEY')
        self.secret     = os.getenv('DKUBE_STORE_S3_ACCESS_SECRET')
        self.bucket     = os.getenv('DKUBE_STORE_S3_BUCKET')
        self.url        = "https://{}:32222".format(self.__ip)
        self.user       = self.__user or os.getenv('DKUBE_LOGIN_USERNAME')
        self.token      = self.__token or os.getenv('DKUBE_ACCESS_TOKEN')
        return self
