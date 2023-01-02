import json
import os

from .metrics import DKubeMetrics


def get_configuration():
    config_file = os.getenv('MM_CONFIG_FILE')
    if os.path.exists(config_file):
        with open(config_file) as f:
            configuration = json.load(f)
    else:
        raise FileNotFoundError("Configuration not found")
    return configuration


def infer_tabular_schema(train_df):
    timestamp_possibilities = ["time", "timestamp", "date"]
    prediction_output_possibilities = ["target", "label", "prediction", "output"]
    schema = {"schema": {"features": list()}}
    features = train_df.columns.to_list()
    df_types = train_df.dtypes.to_dict()
    # Checking if column is categorical or continuous
    likely_cat = {}
    # if no of unique values in column is leaa than 10 than categorical
    for var in train_df.columns:
        likely_cat[var] = train_df[var].nunique() <= 10
    import pandas as pd
    from pandas.api.types import is_numeric_dtype
    for each_col in features:
        col_schema = {}
        if (likely_cat[each_col] is False) and (is_numeric_dtype(train_df[each_col])):
            col_schema["class"] = "continuous"
        else:
            col_schema["class"] = "categorical"
        col_schema["class"] = col_schema["class"]
        col_schema["label"] = each_col
        if (("datetime" in df_types[each_col].name)
        or any(each_possibility in each_col for each_possibility in timestamp_possibilities)
        ):
            col_schema["type"] = "timestamp"
        elif any(each_possibility in each_col for each_possibility in prediction_output_possibilities):
            col_schema["type"] = "prediction_output"
        # if no of unique values are equal to no of samles then predicting column as row_id
        elif train_df[each_col].nunique() == train_df.shape[0]:
            col_schema["type"] = "row_id"
        else:
            col_schema["type"] = "input_feature"
        col_schema["selected"] = False
        schema["schema"]["features"].append(col_schema)
    return pd.DataFrame(schema["schema"]["features"])


def baseline_from_schema(train_df, schema_df):
    features = train_df.columns.to_list()
    selected_features = list()
    prediction_output = None
    schema = json.loads(schema_df.to_json(orient="records"))
    for each_feature in schema:
        if each_feature["type"] == "input_feature" and each_feature.get("selected", False) is True:
            selected_features.append(each_feature)
        elif each_feature["type"] == "prediction_output":
            prediction_output = each_feature
    if prediction_output:
        selected_features.append(prediction_output)
    else:
        raise ValueError("Prediction output not found in schema")
    baseline = {}
    from pandas.api.types import is_numeric_dtype
    for each_feature in selected_features:
        col_baseline = {}
        feature_name = each_feature["label"]
        if feature_name not in features:
            msg = f"{feature_name} Not found in training data"
            raise ValueError(msg)
        if each_feature["class"] == "continuous":
            if is_numeric_dtype(train_df[feature_name]):
                col_baseline["class"] = "continuous"
                col_baseline["numerical"] = True
                col_baseline["description"] = train_df[feature_name].describe().to_dict()
            else:
                msg = f"{feature_name} is defined continious, but values are not in int/float"
                raise ValueError(msg)
        elif each_feature["class"] == "categorical":
            col_baseline["class"] = "categorical"
            col_baseline["bins"] = train_df[feature_name].astype(int).value_counts().to_dict()
            col_baseline["description"] = train_df[feature_name].astype(int).astype("string").describe().astype(int).to_dict()
        baseline[feature_name] = col_baseline
    return baseline
