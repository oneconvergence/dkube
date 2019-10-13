from ._environ import *
from ._defaults import *

import os

self = globals()['_defaults']

def _env(key, val):
    os.environ[key.lstrip('_')] = val
    return key

envs = [_env(var, getattr(self, var)) for var in getattr(self, '__vars__')]
