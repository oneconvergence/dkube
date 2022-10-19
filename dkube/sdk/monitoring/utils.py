import base64
import json
import os
import sys
import time


def get_run_end_boundary(self, klass="drift_monitoring"):
    run_end_time = int(time.time())
    # run_frequency in min
    run_freq = self.configuration[klass]["frequency"] * 60
    return run_end_time - (run_end_time % run_freq)


def get_run_start_boundary(self, timezone):
    import datetime
    if self.timezone == "utc":
        basetime = datetime.utcnow()
    else:
        basetime = datetime.now()
    # rounding off time to the mm frequency
    run_begin_time = int(basetime.timestamp())
    run_freq = self.mm_frequency * 60
    run_begin_time = run_begin_time - (run_begin_time % run_freq)
    run_start_time = datetime.fromtimestamp(run_begin_time)
    return run_start_time


def plt_to_base64(plt):
    import base64
    import io
    my_stringIObytes = io.BytesIO()
    plt.savefig(my_stringIObytes, format='png')
    my_stringIObytes.seek(0)
    my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    return my_base64_jpgData.decode('utf-8')


def create_cat_bin_df(t_value_counts, p_value_counts):
    import pandas as pd
    x = list()
    y = list()
    t_value_counts = {str(key): value for key, value in t_value_counts.items()}
    p_value_counts = {str(key): value for key, value in p_value_counts.items()}
    all_keys = set().union(*[t_value_counts, p_value_counts])
    for each_key in all_keys:
        x.append(t_value_counts.get(each_key))
        y.append(p_value_counts.get(each_key))
    counts_df = pd.DataFrame({"Train data": pd.Series(x),
                           "Predict data": pd.Series(y)})
    counts_df["Train data"] = (counts_df["Train data"]/counts_df["Train data"].sum())*100
    counts_df["Predict data"] = (counts_df["Predict data"]/counts_df["Predict data"].sum())*100
    return counts_df


def get_configuration():
    config_file = os.getenv('MM_CONFIG_FILE')
    if (configuration is not None):
        configuration = json.loads(configuration)
    elif config_file and os.path.isfile(config_file):
        with open(config_file) as f:
            configuration = json.load(f)
    else:
        sys.exit("Configuration not found")
    return configuration


def get_selected_features():
    configuration = get_configuration()
    schema = configuration["schema"]
    selected_features = list()
    prediction_col_name = None
    for each_feature in schema["features"]:
        if each_feature["type"] == "input_feature":
            if each_feature.get("selected", False) is True:
                selected_features.append(each_feature["label"])
        if each_feature["type"] == "prediction_output":
            prediction_col_name = each_feature["label"]
    return selected_features, prediction_col_name


def write_tabular_distributions(train_df, predict_df=None):
    """
        Method to write tabular data distributions
        *Inputs*
            train_df
                Training dataframe
            predict_df
                Predict/live data dataframe, if it's not passed then
                function will save train data distributions only.

    """
    mm_home = os.getenv('MM_HOME')
    filepath = os.path.join(mm_home, "distributions/training-data")
    all_subdirs = [os.path.join(filepath, d) for d in os.listdir(filepath)
                if os.path.isdir(os.path.join(filepath, d))]
    latest_distribution_dir = max(all_subdirs, key=os.path.getctime)
    latest_distribution_file = os.path.join(latest_distribution_dir,
                                            "train_df_distribution.json")
    with open(latest_distribution_file) as fp:
        meta_data = json.load(fp)
    import matplotlib.pyplot as plt
    import seaborn as sns
    distribution = {}
    graphs = dict()
    selected_features, prediction_col_name = get_selected_features()
    cat_idx = [idx for idx in range(len(selected_features))
                if meta_data[selected_features[idx]]["class"] == "categorical"]
    all_columns = selected_features + [prediction_col_name]
    for f_idx in range(len(all_columns)):
        sns.set_style("darkgrid")
        feature_name = all_columns[f_idx]
        distribution[feature_name] = {}
        if f_idx in cat_idx:
            train_value_counts = meta_data[feature_name]["bins"]
            fig, ax = plt.subplots()
            if predict_df:
                predict_value_counts = predict_df[feature_name].astype(int).value_counts().to_dict()
                cat_df = create_cat_bin_df(train_value_counts, predict_value_counts)
                cat_df.plot(use_index=True, kind='bar', y=["Train data", "Predict data"],
                    ax=ax, color=["seagreen", "darkorange"],)
            else:
                train_value_counts = (train_value_counts/train_value_counts.sum())*100
                cat_df = pd.DataFrame({"Train data":train_value_counts})
                cat_df.plot(use_index=True, kind='bar', y="Train data", ax=ax, color="seagreen")
                ax.get_yaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
            graphs[feature_name] = plt_to_base64(plt)
            distribution[feature_name]["description"] = predict_df[feature_name].astype(int).astype("string").describe().astype(int).to_dict()
        else:
            x_ref = train_df[feature_name].values
            ax=sns.kdeplot(x_ref, color="seagreen", shade=True, label="Train data")
            if predict_df:
                p_ref = predict_df[feature_name].values
                ax=sns.kdeplot(p_ref, color="darkorange", shade=True, label="Predict data")
            plt.ylabel(feature_name)
            plt.legend()
            graphs[feature_name] = plt_to_base64(plt)
            distribution[feature_name]["description"] = predict_df[feature_name].describe().to_dict()
        plt.clf();plt.cla()
    config = get_configuration()
    run_start_time = get_run_start_boundary(config["envs"].get("data_timezone", "utc"))
    if predict_df:
        filepath = os.path.join(mm_home, "distributions/live-data",
                                str(int(run_start_time.timestamp())))
        os.makedirs(filepath, exist_ok=True)
        with open(os.path.join(filepath, "live_data_distribution.json"), 'w') as fp:
            json.dump(distribution, fp, indent=4)
    else:
        filepath = os.path.join(mm_home, "distributions/training-data", str(int(time.time())))
        os.makedirs(filepath, exist_ok=True)
        with open(os.path.join(filepath, "train_data_distribution.json"), 'w') as fp:
            json.dump(distribution, fp, indent=4)
    # Writing predict data graphs
    for each_graph_key in graphs:
        graph_file_data = {"graph": graphs[each_graph_key]}
        with open(os.path.join(filepath, f"{each_graph_key}.json"), 'w') as fp:
            json.dump(graph_file_data, fp, indent=4)


def infer_tabular_schema(train_df):
    configuration = get_configuration()
    timestamp_possibilities = ["time", "timestamp", "date"]
    prediction_output_possibilities = ["target", "label", "prediction", "output"]
    valid_feature_types = ["input_feature", "prediction_output", "timestamp", "row_id"]
    schema = {"schema": {"features": list()}}
    features = train_df.columns.to_list()
    df_types = train_df.dtypes.to_dict()
    is_most_null = train_df.columns[train_df.isnull().mean() > 0.8]
    null_values_percent = (train_df.isnull().sum() * 100 / len(train_df)).to_dict()
    ## Checking for null values
    if schema["features"]:
        all_existing_features = configuration["schema"].get("features", list())
        existing_features = list()
        for each_existing_feature in all_existing_features:
            if each_existing_feature["type"] in valid_feature_types:
                existing_features.append(each_existing_feature)
    else:
        existing_features = list()
    ## Checking if column is categorical or continuous
    likely_cat = {}
    for var in train_df.columns:
        likely_cat[var] = train_df[var].nunique() <= 10
    ## if no of unique values in column is leaa than 10 than categorical
    from pandas.api.types import is_numeric_dtype, is_string_dtype
    for each_col in features:
        col_schema = {}
        # importing column schema also retaining the column order
        colmun_imported = False
        for each_feature in existing_features:
            if each_feature["label"] == each_col:
                col_schema = each_feature
                if (each_feature["type"].lower() == "continuous"
                    and
                    (is_numeric_dtype(train_df[each_col]))
                ):
                    col_schema["mean"] = train_df[each_col].mean()
                    col_schema["std"] = train_df[each_col].std()
                else:
                    col_schema[each_col] = train_df[each_col].value_counts().index[0]
                col_schema["null_values"] = null_values_percent[each_col]
                schema["schema"]["features"].append(col_schema)
                colmun_imported = True
                break
        if colmun_imported:
            continue

        if (likely_cat[each_col] is False) and (is_numeric_dtype(train_df[each_col])):
            if each_col in is_most_null:
                col_schema["class"] = "null"
            else:
                col_schema["class"] = "continuous"
            col_schema["mean"] = train_df[each_col].mean()
            col_schema["std"] = train_df[each_col].std()
        else:
            col_schema["class"] = "categorical"
            col_schema[each_col] = train_df[each_col].value_counts().index[0]
        # schema
        col_schema["class"] = col_schema["class"]
        col_schema["label"] = each_col
        # if no of unique values are equal to no of samles then predicting column as row_id
        if (("datetime" in df_types[each_col].name)
        or any(each_possibility in each_col for each_possibility in timestamp_possibilities)
        ):
            col_schema["type"] = "timestamp"
        elif any(each_possibility in each_col for each_possibility in prediction_output_possibilities):
            col_schema["type"] = "prediction_output"
        elif train_df[each_col].nunique() == train_df.shape[0]:
            col_schema["type"] = "row_id"
        else:
            col_schema["type"] = "input_feature"
        col_schema["selected"] = False
        col_schema["null_values"] = null_values_percent[each_col]
        schema["schema"]["features"].append(col_schema)
        return schema


def compute_svd(image_data):
    import cv2
    import dask.array as da
    import numpy as np
    image_data_shape = image_data.shape
    # discarding numper of samples dimention.
    image_shape = image_data_shape[1:3]
    if ((len(image_data_shape) != 3)
        and
    (image_data_shape[-1] != 1)):
        return "image data is not grayscaled to compute SVD", None
    flatten_image_data = image_data.reshape(image_data.shape[0], image_data.shape[1]*image_data.shape[2])
    flatten_image_data = flatten_image_data.transpose()
    flatten_image_data = np.float32(flatten_image_data)
    dask_image_array = da.from_array(flatten_image_data)
    nb = dask_image_array.numblocks
    if nb[0] > 1 and nb[1] > 1:
        U, _, _ = np.linalg.svd(flatten_image_data, full_matrices=False)
    else:
        U, _ , _ = da.linalg.svd(dask_image_array)
    eigen_images = U.transpose()
    svd_representation = eigen_images[0]
    if "dask" in str(type(svd_representation)):
        svd_representation = np.array(svd_representation)
    else:
        pass
    svd_representation = svd_representation.reshape(image_shape)
    # Normalizing pixels from 0-1 to 0-255 to fix black images. 
    norm_image = cv2.normalize(svd_representation, None, alpha= 0, beta= 255, 
                                    norm_type= cv2.NORM_MINMAX, dtype= cv2.CV_32F)
    norm_image = norm_image.astype(np.uint8)
    svd_hist = cv2.calcHist([norm_image], [0], None, [256], [0, 256])
    # converting to heatmap
    norm_image = cv2.applyColorMap(norm_image, cv2.COLORMAP_HOT)
    status , buffer = cv2.imencode('.png', norm_image)
    if status is True:
        image_string = base64.b64encode(buffer)
        return None, image_string.decode('utf-8'), svd_hist
    else:
        return "eigen image cannot be converted to base64", None, None
