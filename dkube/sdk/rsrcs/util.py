import json
import os
import random
import string
import sys

generate = lambda hint: "{}-{}".format(hint, ''.join(random.sample(string.ascii_letters + string.digits, 6)))


def list_of_strs(x):
    if x:
        if type(x) == list:
            # make sure each element is of type str
            x = [str(y) for y in x]
        else:
            x = [str(x)]
    return x


def get_configuration(configuration=None):
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


def write_tabular_distributions(schema, train_data, predict_data=None):
    mm_home = os.getenv('MM_HOME')
    filepath = os.path.join(mm_home, "distributions/training-data")
    all_subdirs = [os.path.join(filepath, d) for d in os.listdir(filepath)
                if os.path.isdir(os.path.join(filepath, d))]
    latest_distribution_dir = max(all_subdirs, key=os.path.getctime)
    latest_distribution_file = os.path.join(latest_distribution_dir,
                                            "train_data_distribution.json")
    with open(latest_distribution_file) as fp:
        meta_data = json.load(fp)
    import matplotlib.pyplot as plt
    import seaborn as sns
    distribution = {}
    graphs = dict()
    selected_features, prediction_col_name = get_selected_features()
    cat_idx = [idx for idx in range(len(selected_features))
                if meta_data[selected_features[idx]]["class"] == "categorical"]
    cont_col_idx = 0
    all_columns = selected_features + [prediction_col_name]
    for f_idx in range(len(all_columns)):
        sns.set_style("darkgrid")
        feature_name = all_columns[f_idx]
        distribution[feature_name] = {}
        if f_idx in cat_idx:
            train_value_counts = meta_data[feature_name]["bins"]
            predict_value_counts = predict_data[feature_name].astype(int).value_counts().to_dict()
            cat_df = create_cat_bin_df(train_value_counts, predict_value_counts)
            fig, ax = plt.subplots()
            cat_df.plot(use_index=True, kind='bar', y=["Train data", "Predict data"],
                ax=ax, color=["seagreen","darkorange"],)
            ax.get_yaxis().set_visible(False)
            graphs[feature_name] = plt_to_base64(plt)
            distribution[feature_name]["description"] = predict_data[feature_name].astype(int).astype("string").describe().astype(int).to_dict()
        else:
            x_ref = train_data[feature_name].values
            p_ref = predict_data[feature_name].values
            ax=sns.kdeplot(x_ref, color="seagreen", shade=True, label="Train data")
            ax=sns.kdeplot(p_ref, color="darkorange", shade=True, label="Predict data")
            plt.ylabel(feature_name)
            plt.legend()
            graphs[feature_name] = plt_to_base64(plt)
            distribution[feature_name]["description"] = predict_data[feature_name].describe().to_dict()
        plt.clf();plt.cla()
    
    filepath = os.path.join(mm_home, "distributions/live-data",
                            str(int(self.run_start_time.timestamp())))
    os.makedirs(filepath, exist_ok=True)
    with open(os.path.join(filepath, "live_data_distribution.json"), 'w') as fp:
        json.dump(distribution, fp, indent=4)
    ## Writing predict data graphs
    for each_graph_key in graphs:
        graph_file_data = {"graph": graphs[each_graph_key]}
        with open(os.path.join(filepath, f"{each_graph_key}.json"), 'w') as fp:
            json.dump(graph_file_data, fp, indent=4)
