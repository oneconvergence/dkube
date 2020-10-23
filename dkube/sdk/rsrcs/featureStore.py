import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import os, json

class FeatureStore(object):

    def __init__(self, config_file = "/opt/dkube/fs/config.json"):
        self.CONFIG_FILE = config_file

    def list_fs(self):
        fs = []
        try:
            with open(self.CONFIG_FILE) as json_file:
                fsconfig = json.load(json_file)
            featuresets = fsconfig["inputs"]["featuresets"]
            for each_feature in featuresets:
                fs.append([each_feature["name"], each_feature["location"]])
            return fs
        except Exception as e:
            return e

    def read(self, featureset, path = None):
        df_empty = pd.DataFrame({'A' : []})
        if path == None:
            with open(self.CONFIG_FILE) as json_file:
                fsconfig = json.load(json_file)
            featuresets = fsconfig["inputs"]["featuresets"]
            for each_feature in featuresets:
                if each_feature["name"] == featureset:
                    path = each_feature["location"]
        if path == None:
            fs = list_fs()
            msg = "feature " + str(featureset) + "doesn't exist, avaiable featuresets are "
            fs_list = ", ".join(fs)
            return msg + fs_list
        try:
            table = pq.read_table(os.path.join(path,'example.parquet'))
            feature_df = table.to_pandas()
            return feature_df, 'none'
        except Exception as e:
            return df_empty, e

    def write(self, dataframe, featureset, path = None):
        if path == None:
            with open(self.CONFIG_FILE) as json_file:
                fsconfig = json.load(json_file)
            featuresets = fsconfig["outputs"]["featuresets"]
            for each_feature in featuresets:
                if each_feature["name"] == featureset:
                    path = each_feature["location"]
        if path == None:
            fs = list_fs()
            msg = "feature " + str(featureset) + "doesn't exist, avaiable featuresets are "
            fs_list = ", ".join(fs)
            return msg + fs_list
        try:
            table = pa.Table.from_pandas(dataframe)
            pq.write_table(table, os.path.join(path,'example.parquet'))
            return 'Data Written'
        except Exception as e:
            return e