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

    def __init__(self, user, name=generate("featureset"), tags=None):
        self.datum = DatumModel(name=None, tags=None, _class='featureset',
                                dvs=None, source='dvs', url=None, remote=False, gitaccess=self.gitaccess,
                                s3access=self.s3access, nfsaccess=self.nfsaccess, gcsaccess=self.gcsaccess)

        self.update_basic(user, name, tags)

    def update_basic(self, user, name, tags):
        tags = list_of_strs(tags)

        self.user = user
        self.name = name

        self.datum.name = name
        self.datum.tags = tags

    def update_dataset_source(self, source=FEATURE_SOURCES[0]):
        """
            Method to update the source for this dataset.
            It should be one of the choice mentioned in DATASET_SOURCES
            Default value is **git**
        """
        self.datum.source = source
