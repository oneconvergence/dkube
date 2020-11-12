from __future__ import print_function

import sys
import time
from pprint import pprint

from dkube.sdk.internal import dkube_api
from dkube.sdk.internal.dkube_api.models.datum_model import DatumModel
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

    def __init__(self, user, name=generate("featureset"), description=None, tags=None):
        self.update_basic(user, name, description, tags)

    def update_basic(self, name, description, tags):
        self._name = None
        self._description = None
        self._tags = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags

    def update_dataset_source(self, source=FEATURE_SOURCES[0]):
        """
            Method to update the source for this dataset.
            It should be one of the choice mentioned in DATASET_SOURCES
            Default value is **git**
        """
        self.datum.source = source
