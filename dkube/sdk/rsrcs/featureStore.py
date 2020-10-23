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
            return {"data":df_empty ,"status": -1, "error": "Featureset doesn't exist"}
        try:
            table = pq.read_table(os.path.join(path,'example.parquet'))
            feature_df = table.to_pandas()
            return {"data":feature_df ,"status": 0, "error": None}
        except Exception as e:
            return {"data":df_empty ,"status": -1, "error": e}

    def write(self, dataframe, featureset, path = None):
        if path == None:
            with open(self.CONFIG_FILE) as json_file:
                fsconfig = json.load(json_file)
            featuresets = fsconfig["outputs"]["featuresets"]
            for each_feature in featuresets:
                if each_feature["name"] == featureset:
                    path = each_feature["location"]
        if path == None:
            return {"status": -1, "error": "Featureset doesn't exist"}
        try:
            table = pa.Table.from_pandas(dataframe)
            pq.write_table(table, os.path.join(path,'example.parquet'))
            return {"status": 0, "error": None}
        except Exception as e:
            return {"status": -1, "error": e}