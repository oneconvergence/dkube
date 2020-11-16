from __future__ import print_function

import sys
import time
from pprint import pprint

from dkube.sdk.internal import dkube_api
from dkube.sdk.internal.dkube_api.models.feature_set_input_def import \
    FeatureSetInputDef
from dkube.sdk.internal.dkube_api.rest import ApiException

from .util import *


class DkubeFeatureSet(object):

    """

        This class defines the DKube featureset with helper functions to set properties of dataset.::

            from dkube.sdk import *
            mnist = DkubeDataset("oneconv", name="mnist")

            Where first argument is the user of this dataset. User should be a valid onboarded user in dkube.

        List of valid feature store sources in DKube.

        :bash:`dvs` :- To create an empty repository which can be used in future runs.
    """

    def __init__(self, name=generate("featureset"), tags=None, description=None, path=None, config_file="/opt/dkube/conf/conf.json"):
        self.featureset = FeatureSetInputDef(
            name=None, tags=None, description=None)

        self.update_basic(name, description, tags, config_file)
        self.update_featurespec_file(path)

    def update_basic(self, name, description, tags, config_file):
        if name is not None:
            self.featureset.name = name
        if description is not None:
            self.featureset.description = description
        if tags is not None:
            self.featureset.tags = tags
        self.CONFIG_FILE = config_file

    def update_featurespec_file(self, path=None):
        """
            Method to update features specification metadata
        """
        if path is None and self.CONFIG_FILE is None:
            self.featurespec_path = path
            return
        if path is None:
            with open(self.CONFIG_FILE) as json_file:
                fsconfig = json.load(json_file)
            featuresets = fsconfig["inputs"]["featuresets"]
            for each_feature in featuresets:
                if each_feature["name"] == self.featureset.name:
                    path = each_feature["location"]
                    break
        self.featurespec_path = path
