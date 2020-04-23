import os
import validators
import enum

DEFAULT_CONNECTION_SCHEME = 'http'
DEFAULT_SERVICE_ACCESS_IP = 'dkube-d3api.dkube'
DEFAULT_SERVICE_ACCESS_PORT = 5000

SUPPORTED_SCHEMES = ['http', 'https']

class Connection(dict):
    def __init__(self):
        super().__init__()
        self.__defaults()

    def __defaults(self):
        self.update(scheme=DEFAULT_CONNECTION_SCHEME)
        self.update(host=DEFAULT_SERVICE_ACCESS_IP)
        self.update(port=DEFAULT_SERVICE_ACCESS_PORT)
        self.update(token='')

    @property
    def scheme(self):
        return self['scheme']

    @scheme.setter
    def scheme(self, value:str):
        assert value in SUPPORTED_SCHEMES, "Invalid value {} for scheme".format(value)
        self.update(scheme=value)

    @property
    def host(self):
        return self['host']

    @host.setter
    def host(self, value:str):
        assert validators.ipv4(value) or validators.domain(value), "type mismatch for ip field should be IPV4 address"
        self.update(host=value)

    @property
    def port(self):
        return self['port']

    @port.setter
    def port(self, value:int):
        assert type(value) == int, "type mismatch for value, should be integer"
        self.update(port=value)

    @property
    def token(self):
        return self['token']

    @token.setter
    def token(self, value:str):
        assert type(value) == str, "type mismatch for value, should be string"
        self.update(token=value)

    @property
    def endpoint(self):
        return '{}:{}'.format(self['host'], self['port'])

    @property
    def url(self):
        return '{}://{}'.format(self['scheme'], self.endpoint)
