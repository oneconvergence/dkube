import sys
import os

path = os.path.dirname(__file__)
path = '{}/internal'.format(path)
if path not in sys.path:
    sys.path.append(path)

from .api import *
from .rsrcs  import *
