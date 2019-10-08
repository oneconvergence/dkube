import os
import validators

class Environment(object):
    def __init__(self, ip:str='127.0.0.1', user:str='', token:str=''):
        assert validators.ipv4(ip) == True, "type mismatch for ip field should be IPV4 address"
        assert type(user) == str, "type mismatch error, username must be string"
        assert type(token) == str, "type mismatch error, token must be string"

        self.ip     = ip
        self.user   = user
        self.token  = token

    @property
    def internal(self):
        self.type       = "internal"
        self.endpoint   = os.getenv("S3_ENDPOINT")
        self.key        = os.getenv("DKUBE_STORE_ACCESS_KEY")
        self.secret     = os.getenv("DKUBE_STORE_ACCESS_SECRET")
        self.bucket     = os.getenv("DKUBE_STORE_BUCKET")
        self.user       = os.getenv('USERNAME')
        self.token      = os.getenv("ACCESS_TOKEN")
        self.url        = "http://dkube-d3api.dkube:5000"
        return self

    @property
    def external(self):
        self.type       = "external"
        self.endpoint   = "{}:32222".format(self.ip)
        self.key        = os.getenv("DKUBE_STORE_ACCESS_KEY")
        self.secret     = os.getenv("DKUBE_STORE_ACCESS_SECRET")
        self.bucket     = os.getenv("DKUBE_STORE_BUCKET")
        self.url        = "https://{}:32222".format(self.ip)

        return self
