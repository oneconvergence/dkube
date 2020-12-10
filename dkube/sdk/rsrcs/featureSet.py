from __future__ import print_function

import os
import sys
import time
from pprint import pprint

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from dkube.sdk.internal import dkube_api
from dkube.sdk.internal.dkube_api.models.feature_set_input_def import \
    FeatureSetInputDef
from dkube.sdk.internal.dkube_api.rest import ApiException

from .util import *


class DkubeFeatureSet(object):

    """

        This class defines the DKube featureset with helper functions to set properties of dataset.::

            from dkube.sdk import *
             = DkubeDataset("oneconv", name="")

            Where first argument is the user of this dataset. User should be a valid onboarded user in dkube.

        List of valid feature store sources in DKube.

        :bash:`dvs` :- To create an empty repository which can be used in future runs.
    """

    def __init__(self, name=generate("featureset"), tags=None, description=None, path=None, config_file="/opt/dkube/conf/conf.json"):
        self.featureset = FeatureSetInputDef(
            name=None, tags=None, description=None)

        self.update_basic(name, description, tags, config_file)
        self.update_featurespec_file(path)
        self.update_features_path()

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
        self.featurespec_path = path

    def update_features_path(self, path=None):
        self.features_path = path

    def read(self, filename='featureset.parquet'):
        df_empty = pd.DataFrame({'A': []})
        if self.features_path is None:
            return {"data": df_empty, "status": -1, "error": "Path of featureset not found"}
        try:
            table = pq.read_table(os.path.join(self.features_path, filename))
            feature_df = table.to_pandas()
            return {"data": feature_df, "status": 0, "error": None}
        except Exception as e:
            return {"data": df_empty, "status": -1, "error": e}

    def write(self, dataframe, filename='featureset.parquet'):
        if self.features_path is None:
            return {"status": -1, "error": "Featureet doesn't exist"}
        try:
            table = pa.Table.from_pandas(dataframe)
            pq.write_table(table, os.path.join(self.features_path, filename))
            return {"status": 0, "error": None}
        except Exception as e:
            return {"status": -1, "error": e}

    def validate(self, dataframe=None, featureset_name=None):
        authToken = os.getenv('DKUBE_USER_ACCESS_TOKEN')
        d_api = api.DkubeApi(token=authToken)
        res = d_api.get_featurespec(featureset=featureset_name)
        f_spec = res.data
        if f_spec == None:
            status = "Featurespec is found."
            return {"status": status}
        fspec_dic = {}
        fspec_keys = []
        for each_spec in f_spec:
            fspec_dic[str(each_spec.name)] = str(each_spec.schema)
            fspec_keys.append(str(each_spec.name))

        schema = [str(sma) for sma in dataframe.dtypes.to_list()]
        df_keys = [str(k) for k in dataframe.keys()]
        df_spec = {}
        for i in range(len(df_keys)):
            df_spec[df_keys[i]] = schema[i]

        status = "success"

        if len(fspec_keys) != len(df_keys):
            status = "No. of columns in dataframe and featurespec are not equal"
            return {"status": status}
        for each_key in df_keys:
            if each_key not in fspec_keys:
                status = f"Column name {each_key} not found in featurespec"
                break
            if df_spec[each_key] != fspec_dic[each_key]:
                status = f"Datatype not matched for column {each_key}"
                break
        return {"status": status}
