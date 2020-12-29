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

        This class defines the DKube featureset with helper functions to set properties of featureset.::

            from dkube.sdk import *
             mnist = DkubeFeatureSet(name="mnist-fs")

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
            Method to update the filepath for feature specification metadata

            *Inputs*

                path
                    A valid filepath. The file should be an YAML file describing a 'Name', 'Description', 'Schema' for each feature.

        """
        self.featurespec_path = path

    def upload_featurespec(self):
        pass

    def update_features_path(self, path=None):
        """
            Method to update the directory path for features data

            *Inputs*

                path
                    A valid directory path. This folder is typically where the featureset is mounted by DKube. The folder contains features saved in Apache Parquet file format. 

        """
        self.features_path = path

    def read(self, filename='featureset.parquet'):
        """
            Method to read features 

            *Inputs*

                filename
                    This is optional. It defaults to featureset.parquet. The features are read from features_path/filename into a Panda's Dataframe object.

            *Outputs*  
                A dictionaly with the following elements

                    "data" : Dataframe with features

                    "status" : 0 for success, -1 for failure

                    "error" : None or human readable text in the case of failures

        """
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
        """
            Method to write features 

            *Inputs*

                dataframe
                    Panda's dataframe object with features data. This should confirm to the feature specification metadata.

                filename
                    This is optional. It defaults to featureset.parquet. The features in 'dataframe' are written to features_path/filename.

            *Outputs*  
                A dictionaly with the following elements

                    "status" : 0 for success, -1 for failure

                    "error" : None or human readable text in the case of failures

        """
        if self.features_path is None:
            return {"status": -1, "error": "Featureset doesn't exist"}
        try:
            table = pa.Table.from_pandas(dataframe)
            pq.write_table(table, os.path.join(self.features_path, filename))
            return {"status": 0, "error": None}
        except Exception as e:
            return {"status": -1, "error": e}

    def validate(self, dataframe=None):
        """
            Method to validate features data against features specification metadata 

            *Inputs*

                dataframe
                    Panda's dataframe object with features data. This should confirm to the feature specification metadata.

            *Outputs*  
                A dictionaly with the following elements

                    "status" : 0 for success, -1 for failure

                    "error" : None or human readable text in the case of failures

        """
        # Get featurespec from DKube
        authToken = os.getenv('DKUBE_USER_ACCESS_TOKEN')
        d_api = api.DkubeApi(token=authToken)
        res = d_api.get_featurespec(featureset=self.featureset.name)
        f_spec = res.data
        if f_spec == None:
            return {"status": -1, "error": "Featurespec is not found"}

        # Parse featurespec.
        # - Create a list of feature names
        # - Create a map of feature name and schema
        fspec_dic = {}
        fspec_keys = []
        for each_spec in f_spec:
            fspec_dic[str(each_spec.name)] = str(each_spec.schema)
            fspec_keys.append(str(each_spec.name))

        # Get the feature names and schema from the dataframe
        schema = [str(sma) for sma in dataframe.dtypes.to_list()]
        df_keys = [str(k) for k in dataframe.keys()]
        df_spec = {}
        for i in range(len(df_keys)):
            df_spec[df_keys[i]] = schema[i]

        # Validations
        # - The number of features should be the same
        # - The feature names should be the same
        # - The feature schema should be the same.

        if len(fspec_keys) != len(df_keys):
            return {"status": -1, "error": "No. of columns in dataframe and featurespec are not equal"}
        for each_key in df_keys:
            if each_key not in fspec_keys:
                return {"status": -1, "error": "Column name {} not found in featurespec".format(each_key)}
            if df_spec[each_key] != fspec_dic[each_key]:
                return {"status": -1, "error": "Datatype not matched for column {}".format(each_key)}

        return {"status": 0, "error": None}
