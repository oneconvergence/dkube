import urllib3
from urllib3.util.url import parse_url
from urllib3.util.url import Url

from minio import Minio

class DkubeProxy(urllib3.ProxyManager):
    def urlopen(self, method, url, redirect=True, **kw):
        murl = parse_url(url)
        if murl.path.startswith('/minio') == False:
            murl = Url(
                    scheme=murl.scheme,
                    auth=murl.auth,
                    host=murl.host,
                    port=murl.port,
                    path='/minio{}'.format(murl.path), #modified URL
                    query=murl.query,
                    fragment=murl.fragment
                    )
        return super(DkubeProxy, self).urlopen(method, str(murl), redirect=redirect, **kw)

def _proxy(endpoint, access_token):
    return DkubeProxy('https://{}'.format(endpoint),
            headers = {"Content-Type": "application/keyauth.api.v1+json", 
                "Authorization": "Bearer {}".format(access_token)},
            timeout=urllib3.Timeout.DEFAULT_TIMEOUT,
            cert_reqs='CERT_NONE',
            retries=urllib3.Retry(
                total=5,
                backoff_factor=0.2,
                status_forcelist=[500, 502, 503, 504]
                )
            )

def minio_client(endpoint, accesskey, secret, proxy=False, token=None):
    http_client = None
    secure = False
    if proxy == True:
        assert token != '', "token must be supplied for proxied conns"
        http_client = _proxy(endpoint, token)
        secure = True

    client = Minio(endpoint,
                   access_key=accesskey,
                   secret_key=secret,
                   secure=secure,
                   http_client = http_client)
    return client
