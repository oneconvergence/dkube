
import json
import os
import os.path
import sys
import time
from datetime import datetime

import requests

url = "http://dkube-exporter.dkube:9401/modelmonitor/metrics"


class DKubeMetrics:
    def __init__(self, drift_type, id):
        if drift_type == "data-drift" or drift_type == "data_drift" :
            self.drift_type = "data_drift"
        elif drift_type == "performance-drift" or drift_type == "performance_drift":
            self.drift_type = "performance_drift"
        self.export_metrics = dict()
        self.export_metrics['metrics'] = list()
        self.update_timestamp()
        self.id = id

    def update_timestamp(self):
        self.export_metrics["timestamp"] = int(time.time())

    def add_metric(self, metric, value, labels):
        metric_obj = dict()
        metric_obj["label_values"] = labels
        metric_obj["metric_name"] = metric
        metric_obj["type"] = self.drift_type
        metric_obj["generated_value"] = value
        self.export_metrics["metrics"].append(metric_obj)
    
    def publish_metrics(self):
        self.export_metrics["id"] = self.id
        payload = json.dumps(self.export_metrics)
        headers = {
            "Authorization": "Bearer {}".format(os.getenv("DKUBE_USER_ACCESS_TOKEN")),
            "Content-Type": "application/json",
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        if response.status_code == 200:
            print("Metrics published")
        else:
            raise ValueError(response.reason)
