#__all__ = ['_environ', 'Environment']

from ._environ import *

import os

os.environ["DKUBE_STORE_ACCESS_KEY"] = "dkube"
os.environ["DKUBE_STORE_ACCESS_SECRET"] = "l06dands19s"
os.environ["DKUBE_STORE_BUCKET"] = "dkube"
