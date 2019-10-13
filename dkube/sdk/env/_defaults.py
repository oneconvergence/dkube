import os

_DKUBE_STORE_S3_ENDPOINT = os.getenv("DKUBE_STORE_S3_ENDPOINT", "minio-service.dkube:9000")
_DKUBE_STORE_S3_ACCESS_KEY = os.getenv("DKUBE_STORE_S3_ACCESS_KEY", "dkube")
_DKUBE_STORE_S3_ACCESS_SECRET = os.getenv("DKUBE_STORE_S3_ACCESS_SECRET", "l06dands19s")
_DKUBE_STORE_S3_BUCKET = os.getenv("DKUBE_STORE_S3_BUCKET", "dkube")
_DKUBE_LOGIN_USERNAME = os.getenv("DKUBE_LOGIN_USERNAME", os.getenv("USERNAME", ""))
_DKUBE_ACCESS_TOKEN = os.getenv("DKUBE_ACCESS_TOKEN", os.getenv("ACCESS_TOKEN", ""))
_DKUBE_ACCESS_URL = os.getenv("DKUBE_ACCESS_URL", "http://dkube-d3api.dkube:5000")

__vars__ = [
        "_DKUBE_STORE_S3_ENDPOINT", 
        "_DKUBE_STORE_S3_ACCESS_KEY", 
        "_DKUBE_STORE_S3_ACCESS_SECRET",
        "_DKUBE_STORE_S3_BUCKET",
        "_DKUBE_LOGIN_USERNAME",
        "_DKUBE_ACCESS_TOKEN",
        "_DKUBE_ACCESS_URL"
        ]
