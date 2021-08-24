from __future__ import print_function

import sys
import time
from pprint import pprint
from .util import *

from dkube.sdk.internal import dkube_api

from dkube.sdk.internal.dkube_api.models.modelmonitor_status_def import ModelmonitorStatusDef
from dkube.sdk.internal.dkube_api.models.modelmonitor_schema_feature import ModelmonitorSchemaFeature
from dkube.sdk.internal.dkube_api.models.modelmonitor_features_spec_def import ModelmonitorFeaturesSpecDef
from dkube.sdk.internal.dkube_api.models.modelmonitor_component_def import ModelmonitorComponentDef
from dkube.sdk.internal.dkube_api.models.modelmonitor_dataset_def import ModelmonitorDatasetDef
from dkube.sdk.internal.dkube_api.models.modelmonitor_alert_cond_def import ModelmonitorAlertCondDef
from dkube.sdk.internal.dkube_api.models.modelmonitor_alert_def import ModelmonitorAlertDef
from dkube.sdk.internal.dkube_api.models.modelmonitor_def import ModelmonitorDef


class DkubeModelMonitor(object):
    def __init__(self, user, name=generate("mm"), tags=None):

        self.status = ModelmonitorStatusDef(
            state=None,
            sub_state=None,
            message=None,
            code=None,
            success=False)
        self.features = ModelmonitorSchemaFeature(selected=None, label=None, _class=None, type=None)
        self.schema = ModelmonitorFeaturesSpecDef(features=self.features)
        self.pipeline_component = ModelmonitorComponentDef(
            run_id=None, status_info=None, status=None, type=None)

        self.datasets = ModelmonitorDatasetDef(id=None, _class=None, transformer_script=None, name=None, sql_query=None,
                                               s3_subpath=None, version=None, data_format=None, groundtruth_col=None,
                                               predict_col=None, created_at=None, updated_at=None)

        self.conditions = ModelmonitorAlertCondDef(
            id=None, feature=None, op=None, threshold=0.0)

        self.alerts = ModelmonitorAlertDef(
            id=None,
            _class='FeatureDrift',
            email=None,
            name=None,
            conditions=self.conditions)

        self.modelmonitor = ModelmonitorDef(
            id=None,
            status=self.status,
            schema=self.schema,
            pipeline_component=self.pipeline_component,
            owner=None,
            emails=None,
            name=None,
            description=None,
            tags=None,
            model=None,
            version=None,
            endpoint_url=None,
            model_type=None,
            model_framework=None,
            drift_detection_run_frequency_hrs=1,
            drift_detection_algorithm=None,
            performance_metrics_template=None,
            datasets=self.datasets,
            alerts=self.alerts)

        self.update_basic(user, name, description, tags)

    def update_basic(self, user, name, description, tags):
        """
            Method to update the attributes specified at creation. Description and tags can be updated. tags is a list of string values.
        """
        tags = list_of_strs(tags)

        self.user = user
        self.name = name
        self.description = description
