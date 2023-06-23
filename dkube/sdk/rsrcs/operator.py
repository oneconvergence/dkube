import json
from enum import Enum
from pprint import pprint

from dkube.sdk.internal.dkube_api.api import dkube_operator_exclusive_api
from dkube.sdk.internal.dkube_api.models.cluster import Cluster
from dkube.sdk.internal.dkube_api.models.cluster_access_keys_def import \
    ClusterAccessKeysDef
from dkube.sdk.internal.dkube_api.models.dl_framework import DLFramework
from dkube.sdk.internal.dkube_api.models.dl_framework_model_versions import DLFrameworkModelVersions

from .util import *


class ClusterKind(Enum):
    """
    This Enum class defines the kind of the cluster that are suported in the Dkube.
    *Available in DKube Release: 3.0*
    """
    kubernetes = "kubernetes"
    slurmremote = "slurm-remote"
    sagemaker = "sagemaker"
    kserve = "kserve"
    custom = "custom"

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class ClusterClass(Enum):
    """
    This Enum class defines the class of the cluster that are suported in the Dkube.
    *Available in DKube Release: 3.0*
    """
    execution = "execution"
    monitoring = "monitoring"

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class AuthType(Enum):
    """
    This Enum class defines the authentication type of the cluster that are suported in the Dkube.
    *Available in DKube Release: 3.0*
    """

    jwt = "jwt"
    accesskeys = "access_keys"
    none = "none"

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class JwtTokenType(Enum):
    """
    This Enum class defines the token type of the jwt that are suported in the Dkube.
    *Available in DKube Release: 3.0*
    """

    signed = "signed"
    new = "new"

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class DkubeCluster(object):
    """
    This class defines the DKube cluster.
    *Available in DKube Release: 3.0*
    """

    def __init__(self, name=generate("dkube_cluster"), description="", tags=None):
        self.cluster = Cluster(name=None, tags=None, description=None, auth_type="none")

        self.update_basic(name, description, tags)

    def update_basic(self, name, description, tags):
        """
        Method to update the attributes specified at creation. 
        Description and tags can be updated. 
        tags is a list of string values.
        """
        
        tags = list_of_strs(tags)

        self.cluster.name = name
        self.cluster.description = description
        self.cluster.tags = tags

        return self

    def update_kind(self, kind: ClusterKind):
        """
        Method to update the kind of the cluster
        """
        self.cluster.kind = kind

    def update_url(self, url):
        """
        Method to update the url of the cluster
        """
        self.cluster.url = url

    def update_class(self, cluster_class: ClusterClass):
        """
        Method to update the class of the cluster
        """
        self.cluster._class = cluster_class

    def update_ca(self, ca):
        """
        Method to update the ca for the cluster
        """
        self.cluster.ca = ca

    def update_version(self, version):
        """
        Method to update the version
        """
        self.cluster.version = version

    def update_authtype(self, auth_type: AuthType):
        """
        Method to update the authentication type
        """
        self.cluster.auth_type = auth_type

    def update_jwt_details(self, jwt_token=None, jwt_signing_key=None, jwt_token_type: JwtTokenType = None):
        """
        Method to update the jwt details for the cluster
        """
        if jwt_token:
            self.cluster.jwt_token = jwt_token
        if jwt_signing_key:
            self.cluster.jwt_signing_key = jwt_signing_key
        if jwt_token_type:
            self.cluster.jwt_token_type = jwt_token_type

    def update_cluster_user(self, cluster_user):
        """
        Method to update the cluster user
        """
        self.cluster.cluster_user = cluster_user

    def update_plugin(self, plugin):
        """
        Method to update the plugin
        """
        self.cluster.plugin = plugin

    def update_access_keys(self, access_key, secret_key):
        """
        Method to update the access keys
        """
        self.cluster.access_keys = ClusterAccessKeysDef(
            access_key=access_key, secret_key=secret_key)
        
    def update_region(self, region):
        """
        Method to update the region
        """
        self.cluster.access_keys.region = region

    def update_host_port(self, host, port):
        self.cluster.host = host
        self.cluster.port = port

class DkubeDSFramework(object):
    def __init__(self, name=""):
        self.framework = DLFramework(name)
        self.versions = []

    def update_basic(self, name):
        self.framework.name = name

    def update_version(self, name, image, login_uname="", login_pswd="", capabilities=["training"]):
        private = False
        if login_uname != "" and login_pswd != "":
            private = True
            self.validate_image_hostname(image)
        fv = DLFrameworkModelVersions(name=name, image=image, private=private,
            username=login_uname, password=login_pswd, capabilities=capabilities)
        self.versions.append(fv)

    def validate_image_hostname(self, image):
        i = image.find("/")
        if i == -1 or not any([x in image[:i] for x in [".", ":"]]):
            e = "Image name {} is not prefixed with hostname. Hostname is required for private image. Hint: add docker.io as prefix in image name for dockerhub registry eg. docker.io/<path>:<tag>".format(image)
            raise Exception(e)
