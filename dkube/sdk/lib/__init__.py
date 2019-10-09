from .rest import *
from .minio import *

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
