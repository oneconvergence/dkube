import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from numpy import random
import os

class FeatureStore(object):
    FEATURE_TYPE = ['dataframe', 'numpyarray']

    def read(dtype = 'dataframe', featureset, path):
        df_empty = pd.DataFrame({'A' : []})
        if dtype not in FeatureStore:
            err = 'data type not supported, supported types dataframe, numpyarray'
            return df_empty, err
        try:
            table = pq.read_table(os.path.join(path,'example.parquet'))
            feature_df = table.to_pandas()
            if dtype = 'dataframe':
                return feature_df, 'none'
            elif dtype = 'numpyarray':
                return featureset.to_numpy(), 'none'
        except Exception as e:
            return df_empty, e

    def write(dataframe, featureset, path):
        try:
            table = pa.Table.from_pandas(dataframe)
            pq.write_table(table, os.path.join(path,'example.parquet'))
            return 'Data Written'
        except Exception as e:
            return e