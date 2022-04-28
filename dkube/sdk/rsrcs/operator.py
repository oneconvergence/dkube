import json
from enum import Enum
from pprint import pprint

from dkube.sdk.internal.dkube_api.api import dkube_operator_exclusive_api
from dkube.sdk.internal.dkube_api.models.cluster import Cluster
from dkube.sdk.internal.dkube_api.models.cluster_access_keys_def import \
    ClusterAccessKeysDef

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
        self.cluster = Cluster(name=None, kind=None, _class=None, url=None, ca=None, version=None, auth_type=None, jwt_token_type=None, jwt_token=None,
                               jwt_signing_key=None, cluster_user=None, access_keys=None, tags=None, description=None, plugin=None)

        self.update_basic(name, description, tags)

    def update_basic(self, name, description, tags):
        """
        Method to update the attributes specified at creation. Description and tags can be updated. tags is a list of string values.
        """
        tags = list_of_strs(tags)

        self.cluster.name = name
        self.cluster.description = description
        self.cluster.tags = tags

        return self

    def update_kind(self, kind: ClusterKind = None):
        """
        Method to update the kind of the cluster
        """
        self.cluster.kind = kind

    def update_url(self, url=None):
        """
        Method to update the url of the cluster
        """
        self.cluster.url = url

    def update_class(self, cluster_class: ClusterClass = None):
        """
        Method to update the class of the cluster
        """
        self.cluster._class = cluster_class

    def update_ca(self, ca=None):
        """
        Method to update the ca for the cluster
        """
        self.cluster.ca = ca

    def update_version(self, version=None):
        """
        Method to update the version
        """
        self.cluster.version = version

    def update_authtype(self, auth_type: AuthType = None):
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

    def update_cluster_user(self, cluster_user=None):
        """
        Method to update the cluster user
        """
        self.cluster.cluster_user = cluster_user

    def update_plugin(self, plugin=None):
        """
        Method to update the plugin
        """
        self.cluster.plugin = plugin

    def update_access_keys(self, access_key=None, secret_key=None):
        """
        Method to update the access keys
        """
        self.cluster.access_keys = ClusterAccessKeysDef(
            access_key=access_key, secret_key=secret_key)
        
    def update_region(self, region=None):
        """
        Method to update the region
        """
        self.cluster.access_keys.region = region
