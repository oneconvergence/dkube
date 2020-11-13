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

    """

    FEATURE_SOURCES = ["dvs", None]
    """
	List of valid feature store sources in DKube.

	:bash:`dvs` :- To create an empty repository which can be used in future runs.
    """

    def __init__(self, name=generate("featureset"), tags=None, description=None):
        self.featureset = FeatureSetInputDef(name=None, tags=None, description=None)

        self.update_basic(name, description, tags)

    def update_basic(self, name, description, tags):
    
        if name is not None:
            self.featureset.name = name
        if description is not None:
            self.featureset.description = description
        if tags is not None:
            self.featureset.tags = tags

    def update_featurespec_file(self, path=None):
        """
            Method to update features specification metadata
        """
        self.featurespec_path = path
