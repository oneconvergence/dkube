"""

.. module:: DKubeAPI
   :synopsis: Helper class which provides high level methods for user to integrate at workflow level.

.. moduleauthor:: Ahmed Khan <github.com/mak-454>


"""

import json
import os
import time
from logging.config import valid_ident

import pandas as pd
import urllib3
from dkube.sdk.internal.api_base import *
from dkube.sdk.internal.dkube_api.models.conditions import \
    Conditions as TriggerCondition
from dkube.sdk.internal.dkube_api.rest import ApiException
from dkube.sdk.internal.files_base import *
from dkube.sdk.rsrcs import *
from dkube.sdk.rsrcs.featureset import DkubeFeatureSet, DKubeFeatureSetUtils
from dkube.sdk.rsrcs.modelmonitor import DatasetClass
from dkube.sdk.rsrcs.project import DkubeProject
from packaging import version as pversion

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class DkubeApi(ApiBase, FilesBase):

    """

    This class encapsules all the high level dkube workflow functions.::

        from dkube.sdk import *
        dapi = DkubeApi()

    *Inputs*

        URL
            FQDN endpoint at which DKube platform is deployed::

                http://dkube-controller-master.dkube.cluster.local:5000

                https://dkube.ai:32222

            .. note:: If not provided then the value is picked from *DKUBE_ACCESS_URL* env variable. If not found then http://dkube-controller-master.dkube.cluster.local:5000 is used assuming the access is internal to the DKube cluster


        token
            Access token for the APIs, without which DKube will return 40x codes

            .. note:: If not provided then the value is picked from *DKUBE_ACCESS_TOKEN* env variable. ASSERTs if env is not defined.


        common_tags
            Tags which need to applied all the resources created using this API object


        req_timeout
            Timeout for all the requests which are issued using this API object


        req_retries
            Number of retries per request

    """

    def __init__(
        self, URL=None, token=None, common_tags=[], req_timeout=None, req_retries=None
    ):

        self.url = URL
        if self.url is None:
            self.url = os.getenv(
                "DKUBE_ACCESS_URL",
                "http://dkube-controller-master.dkube.svc.cluster.local:5000",
            )
            self.files_url = os.getenv(
                "DKUBE_ACCESS_URL",
                "http://dkube-downloader.dkube.svc.cluster.local:9401",
            )
        else:
            self.files_url = self.url

        self.token = token
        if self.token == None:
            self.token = os.getenv("DKUBE_ACCESS_TOKEN", None)
            assert (
                self.token == None
            ), "TOKEN must be specified either by passing argument or by setting DKUBE_ACCESS_TOKEN env variable"

        ApiBase.__init__(self, self.url, self.token, common_tags)
        FilesBase.__init__(self, self.files_url, self.token)

        self.dkubeinfo = super().dkubeinfo()

    def set_active_project(self, project_id):
        """
        Set active project. Any resources created using this API instance will belong to the given project.

        *Available in DKube Release: 2.2*

        *Inputs*

            project_id
                ID of the project. pass None to unset.
        """
        self.common_tags = [
            tag for tag in self.common_tags if not tag.startswith("project:")
        ]
        if project_id:
            self.common_tags.append("project:" + str(project_id))

    def validate_token(self):
        """
        Method which can be used to validate the token.
        Returns the JWT Claims. Which contains the role assigned to the user.


        """

        return super().validate_token()

    def launch_jupyter_ide(self, ide: DkubeIDE, wait_for_completion=True):
        """
        Method to launch a Jupyter IDE on DKube platform. Two kinds of IDE are supported,
        Jupyter Notebook & RStudio.
        Raises Exception in case of errors.


        *Inputs*

            ide
                Instance of :bash:`dkube.sdk.rsrcs.DkubeIDE` class.
                Please see the :bash:`Resources` section for details on this class.


            wait_for_completion
                When set to :bash:`True` this method will wait for job to complete after submission.
                IDE is declared complete if it is one of the :bash:`running/failed/error` state

        """

        assert (
            type(ide) == DkubeIDE
        ), "Invalid type for run, value must be instance of rsrcs:DkubeIDE class"
        super().launch_jupyter_ide(ide)
        while wait_for_completion:
            status = super().get_ide("notebook", ide.user, ide.name, fields="status")
            state, reason = status["state"], status["reason"]
            if state.lower() in ["running", "failed", "error"]:
                print(
                    "IDE {} - completed with state {} and reason {}".format(
                        ide.name, state, reason
                    )
                )
                break
            else:
                print(
                    "IDE {} - waiting for completion, current state {}".format(
                        ide.name, state
                    )
                )
                time.sleep(self.wait_interval)

    def launch_rstudio_ide(self, ide: DkubeIDE, wait_for_completion=True):
        """
        Method to launch a Rstudio IDE on DKube platform. Two kinds of IDE are supported,
        Jupyter Notebook & RStudio.
        Raises Exception in case of errors.


        *Inputs*

            ide
                Instance of :bash:`dkube.sdk.rsrcs.DkubeIDE` class.
                Please see the :bash:`Resources` section for details on this class.


            wait_for_completion
                When set to :bash:`True` this method will wait for job to complete after submission.
                IDE is declared complete if it is one of the :bash:`running/failed/error` state

        """

        assert (
            type(ide) == DkubeIDE
        ), "Invalid type for run, value must be instance of rsrcs:DkubeIDE class"
        super().launch_rstudio_ide(ide)
        while wait_for_completion:
            status = super().get_ide("notebook", ide.user, ide.name, fields="status")
            state, reason = status["state"], status["reason"]
            if state.lower() in ["running", "failed", "error"]:
                print(
                    "IDE {} - completed with state {} and reason {}".format(
                        ide.name, state, reason
                    )
                )
                break
            else:
                print(
                    "IDE {} - waiting for completion, current state {}".format(
                        ide.name, state
                    )
                )
                time.sleep(self.wait_interval)

    def list_ides(self, user, shared=False, filters="*"):
        """
        Method to list all the IDEs of a user.
        Raises exception on any connection errors.

        *Inputs*

            user
                User whose IDE instances must be fetched.
                In case of if token is of different user, then the token should have permission to fetch the
                training runs of the :bash:`user` in the input. They should be in same DKube group.

            filters
                Only :bash:`*` is supported now.

                User will able to filter runs based on state or duration

        """

        return super().list_ides("notebook", user, shared)

    def delete_ide(self, user, name, wait_for_completion=True):
        """
        Method to delete an IDE.
        Raises exception if token is of different user or if IDE with name doesnt exist or on any connection errors.

        *Inputs*

            user
                The token must belong to this user. As IDE instance of different user cannot be deleted.

            name
                Name of the IDE which needs to be deleted.

            wait_for_completion
                When set to :bash:`True` this method will wait for ide to get deleted.

        """
        data = super().get_ide("notebook", user, name, fields="*")
        uuid = data["job"]["parameters"]["generated"]["uuid"]
        ret = super().delete_ide("notebook", user, name)
        if wait_for_completion:
            self._wait_for_rundelete_completion(uuid, "notebook", name)
        return ret

    def create_training_run(self, run: DkubeTraining, wait_for_completion=True):
        """
        Method to create a training run on DKube.
        Raises Exception in case of errors.


        *Inputs*

            run
                Instance of :bash:`dkube.sdk.rsrcs.Training` class.
                Please see the :bash:`Resources` section for details on this class.


            wait_for_completion
                When set to :bash:`True` this method will wait for job to complete after submission.
                Job is declared complete if it is one of the :bash:`complete/failed/error` state

        """

        assert (
            type(run) == DkubeTraining
        ), "Invalid type for run, value must be instance of rsrcs:DkubeTraining class"
        valid_fw = False
        fw_opts = ["custom"]
        if run.executor_dkube_framework.choice == "custom":
            valid_fw = True
        else:
            fws = self.get_training_capabilities()
            for fw in fws:
                for v in fw["versions"]:
                    if (
                        run.executor_dkube_framework.choice == fw["name"]
                        and run.dkube_framework_details.version == v["name"]
                    ):
                        valid_fw = True
                        break
                    else:
                        name = fw["name"] + "_" + v["name"]
                        fw_opts.append(name)
                if valid_fw == True:
                    break

        assert valid_fw == True, (
            "Invalid choice for framework, select oneof(" + str(fw_opts) + ")"
        )

        super().update_tags(run.training_def)
        super().create_run(run)
        while wait_for_completion:
            status = {}
            try:
                status = super().get_run(
                    "training", run.user, run.name, fields="status"
                )
            except ValueError as ve:
                ve_without_num = "".join(i for i in str(ve) if not i.isdigit())
                if "Invalid value for `state` (Waiting for  gpu(s))" in ve_without_num:
                    num = "".join(i for i in str(ve) if i.isdigit())
                    status["state"] = "Waiting for {} gpu(s)".format(num)
                    status["reason"] = ""
                else:
                    raise ve
            state, reason = status["state"], status["reason"]
            if state.lower() in ["complete", "failed", "error", "stopped", "created"]:
                print(
                    "run {} - completed with state {} and reason {}".format(
                        run.name, state, reason
                    )
                )
                break
            else:
                print(
                    "run {} - waiting for completion, current state {}".format(
                        run.name, state
                    )
                )
                time.sleep(self.wait_interval)

    def get_training_run(self, user, name):
        """
        Method to fetch the training run with given name for the given user.
        Raises exception in case of run is not found or any other connection errors.

        *Inputs*

            user
                User whose training run has to be fetched.
                In case of if token is of different user, then the token should have permission to fetch the
                training run of the :bash:`user` in the input. They should be in same DKube group.

            name
                Name of the training run to be fetched

        """

        return super().get_run("training", user, name)

    def list_training_runs(self, user, shared=False, filters="*"):
        """
        Method to list all the training runs of a user.
        Raises exception on any connection errors.

        *Inputs*

            user
                User whose training runs must be fetched.
                In case of if token is of different user, then the token should have permission to fetch the
                training runs of the :bash:`user` in the input. They should be in same DKube group.

            filters
                Only :bash:`*` is supported now.

                User will able to filter runs based on state or duration

        """

        return super().list_runs("training", user, shared)

    def delete_training_run(self, user, name, wait_for_completion=True):
        """
        Method to delete a run.
        Raises exception if token is of different user or if training run with name doesnt exist or on any connection errors.

        *Inputs*

            user
                The token must belong to this user. As run of different user cannot be deleted.

            name
                Name of the run which needs to be deleted.

            wait_for_completion
                When set to :bash:`True` this method will wait for training run to get deleted.

        """
        data = super().get_run("training", user, name, fields="*")
        uuid = data["job"]["parameters"]["generated"]["uuid"]
        ret = super().delete_run("training", user, name)
        if wait_for_completion:
            self._wait_for_rundelete_completion(uuid, "training", name)
        return ret

    def create_preprocessing_run(
        self, run: DkubePreprocessing, wait_for_completion=True
    ):
        """
        Method to create a preprocessing run on DKube.
        Raises Exception in case of errors.


        *Inputs*

            run
                Instance of :bash:`dkube.sdk.rsrcs.Preprocessing` class.
                Please see the :bash:`Resources` section for details on this class.


            wait_for_completion
                When set to :bash:`True` this method will wait for job to complete after submission.
                Job is declared complete if it is one of the :bash:`complete/failed/error` state

        """

        assert (
            type(run) == DkubePreprocessing
        ), "Invalid type for run, value must be instance of rsrcs:DkubePreprocessing class"
        super().update_tags(run.pp_def)
        super().create_run(run)
        while wait_for_completion:
            status = {}
            try:
                status = super().get_run(
                    "preprocessing", run.user, run.name, fields="status"
                )
            except ValueError as ve:
                ve_without_num = "".join(i for i in str(ve) if not i.isdigit())
                if "Invalid value for `state` (Waiting for  gpu(s))" in ve_without_num:
                    num = "".join(i for i in str(ve) if i.isdigit())
                    status["state"] = "Waiting for {} gpu(s)".format(num)
                    status["reason"] = ""
                else:
                    raise ve
            state, reason = status["state"], status["reason"]
            if state.lower() in ["complete", "failed", "error", "stopped"]:
                print(
                    "run {} - completed with state {} and reason {}".format(
                        run.name, state, reason
                    )
                )
                break
            else:
                print(
                    "run {} - waiting for completion, current state {}".format(
                        run.name, state
                    )
                )
                time.sleep(self.wait_interval)

    def get_preprocessing_run(self, user, name):
        """
        Method to fetch the preprocessing run with given name for the given user.
        Raises exception in case of run is not found or any other connection errors.

        *Inputs*

            user
                User whose preprocessing run has to be fetched.
                In case of if token is of different user, then the token should have permission to fetch the
                preprocessing run of the :bash:`user` in the input. They should be in same DKube group.

            name
                Name of the training run to be fetched

        """

        return super().get_run("preprocessing", user, name)

    def list_preprocessing_runs(self, user, shared=False, filters="*"):
        """
        Method to list all the preprocessing runs of a user.
        Raises exception on any connection errors.

        *Inputs*

            user
                User whose preprocessing runs must be fetched.
                In case of if token is of different user, then the token should have permission to fetch the
                preprocessing runs of the :bash:`user` in the input. They should be in same DKube group.

            filters
                Only :bash:`*` is supported now.

                User will able to filter runs based on state or duration

        """

        return super().list_runs("preprocessing", user, shared)

    def delete_preprocessing_run(self, user, name, wait_for_completion=True):
        """
        Method to delete a run.
        Raises exception if token is of different user or if preprocessing run with name doesnt exist or on any connection errors.

        *Inputs*

            user
                The token must belong to this user. As run of different user cannot be deleted.

            name
                Name of the run which needs to be deleted.

            wait_for_completion
                When set to :bash:`True` this method will wait for preprocess run to get deleted.

        """
        data = super().get_run("preprocessing", user, name, fields="*")
        uuid = data["job"]["parameters"]["generated"]["uuid"]
        ret = super().delete_run("preprocessing", user, name)
        if wait_for_completion:
            self._wait_for_rundelete_completion(uuid, "preprocessing", name)
        return ret

    def update_inference(self, run: DkubeServing, wait_for_completion=True):
        """
        Method to update a test inference/deployment in DKube.
        Raises Exception in case of errors.


        *Inputs*

            run
                Instance of :bash:`dkube.sdk.rsrcs.serving` class.
                Please see the :bash:`Resources` section for details on this class.

                Picks defaults for predictor, transformer configs from the existing inference deployment.
                If version is not specified then deployment is updated to latest version.

            wait_for_completion
                When set to :bash:`True` this method will wait for job to complete after submission.
                Job is declared complete if it is one of the :bash:`complete/failed/error` state

        """

        inference = super().get_run("inference", run.user, run.name)
        inference = inference["job"]["parameters"]["inference"]

        if run.predictor.image == None:
            run.update_serving_image(
                None,
                inference["serving_image"]["image"]["path"],
                inference["serving_image"]["image"]["username"],
                inference["serving_image"]["image"]["password"],
            )

        if run.serving_def.model == None:
            run.serving_def.model = inference["model"]

        if run.serving_def.version == None:
            run.serving_def.version = inference["version"]

        if inference["transformer"] == True and run.serving_def.transformer == False:
            run.update_transformer_image(
                inference["transformer_image"]["image"]["path"],
                inference["transformer_image"]["image"]["username"],
                inference["transformer_image"]["image"]["password"],
            )

            run.set_transformer(True, script=inference["transformer_code"])
            run.update_transformer_code(
                inference["transformer_project"], inference["transformer_commit_id"]
            )
        elif inference["transformer"] == False and run.serving_def.transformer == True:
            li = self.get_model_lineage(
                run.serving_def.owner, run.serving_def.model, run.serving_def.version
            )

            if run.transformer.image == None:
                ti = li["run"]["parameters"]["generated"]["training_image"]["image"]
                run.update_transformer_image(ti["path"], ti["username"], ti["password"])

            if run.serving_def.transformer_project == None:
                code = li["run"]["parameters"]["training"]["datums"]["workspace"][
                    "data"
                ]
                name = code["name"].split(":")[1]
                run.update_transformer_code(name, code["version"])

        if run.serving_def.min_replicas == 0:
            run.serving_def.min_replicas = inference["min_replicas"]

        if run.serving_def.max_concurrent_requests == 0:
            run.serving_def.max_concurrent_requests = inference["max_concurrent_requests"]

        if run.serving_def.enable_logs is None:
            run.serving_def.max_concurrent_requests = inference["enable_logs"]

        if run.serving_def.deploy:
            run.serving_def.deploy = inference["deploy"]
        else:
            run.serving_def.deploy = None

        super().update_inference(run)

        while wait_for_completion:
            status = super().get_run("inference", run.user, run.name, fields="status")
            state, reason = status["state"], status["reason"]
            if state.lower() in ["complete", "failed", "error", "running", "stopped"]:
                print(
                    "run {} - completed with state {} and reason {}".format(
                        run.name, state, reason
                    )
                )
                break
            else:
                print(
                    "run {} - waiting for completion, current state {}".format(
                        run.name, state
                    )
                )
                time.sleep(self.wait_interval)

    def create_test_inference(self, run: DkubeServing, wait_for_completion=True):
        """
        Method to create a test inference on DKube.
        Raises Exception in case of errors.


        *Inputs*

            run
                Instance of :bash:`dkube.sdk.rsrcs.serving` class.
                Please see the :bash:`Resources` section for details on this class.

                If serving image is not updated in :bash:`run:DkubeServing` argument then,
                - If training used supported standard framework, dkube will pick approp serving image
                - If training used custom image, dkube will try to use the same image for serving

                If transformer image is not updated in :bash:`run:DkubeServing` then,
                - Dkube will use same image as training image

                If transformer code is not updated in :bash:`run:DkubeServing` then,
                - Dkube will use the code used for training


            wait_for_completion
                When set to :bash:`True` this method will wait for job to complete after submission.
                Job is declared complete if it is one of the :bash:`complete/failed/error` state

        """

        assert (
            type(run) == DkubeServing
        ), "Invalid type for run, value must be instance of rsrcs:DkubeServing class"

        # Fetch training run details and fill in information for serving
        if (
            run.predictor.image == None
            or (run.serving_def.transformer == True and run.transformer.image == None)
            or (
                run.serving_def.transformer == True
                and run.serving_def.transformer_project == None
            )
        ):

            if run.serving_def.version == None:
                v = self.get_model_latest_version(
                    run.serving_def.owner, run.serving_def.model
                )
                run.serving_def.version = v["uuid"]

            li = self.get_model_lineage(
                run.serving_def.owner, run.serving_def.model, run.serving_def.version
            )

            if li == None or li["run"] == None:
                li = None

            if li == None and run.predictor.image == None:
                raise Exception("Lineage is nil, predictor image must be provided.")

            if li != None and run.predictor.image == None:
                si = li["run"]["parameters"]["generated"]["serving_image"]["image"]
                run.update_serving_image(
                    None, si["path"], si["username"], si["password"]
                )

            if (
                li != None
                and run.serving_def.transformer == True
                and run.transformer.image == None
            ):
                ti = li["run"]["parameters"]["generated"]["training_image"]["image"]
                run.update_transformer_image(ti["path"], ti["username"], ti["password"])

            if (
                li != None
                and run.serving_def.transformer == True
                and run.serving_def.transformer_project == None
            ):
                code = li["run"]["parameters"]["training"]["datums"]["workspace"][
                    "data"
                ]
                name = code["name"].split(":")[1]
                run.update_transformer_code(name, code["version"])
        # Don't allow prod deploy using this API, if MODEL_CATALOG_ENABLED=true
        if (
            run.serving_def.deploy == True
            and super().is_model_catalog_enabled() == True
        ):
            run.serving_def.deploy = None

        super().create_run(run)
        while wait_for_completion:
            status = super().get_run("inference", run.user, run.name, fields="status")
            state, reason = status["state"], status["reason"]
            if state.lower() in ["complete", "failed", "error", "running", "stopped"]:
                print(
                    "run {} - completed with state {} and reason {}".format(
                        run.name, state, reason
                    )
                )
                break
            else:
                print(
                    "run {} - waiting for completion, current state {}".format(
                        run.name, state
                    )
                )
                time.sleep(self.wait_interval)

    def get_test_inference(self, user, name):
        """
        Method to fetch the test inference with given name for the given user.
        Raises exception in case of run is not found or any other connection errors.

        *Inputs*

            user
                User whose test inference has to be fetched.
                In case of if token is of different user, then the token should have permission to fetch the
                serving run of the :bash:`user` in the input. They should be in same DKube group.

            name
                Name of the serving run to be fetched

        """

        return super().get_run("inference", user, name)

    def list_test_inferences(self, user, shared=False, filters="*"):
        """
        Method to list all the training inferences of a user.
        Raises exception on any connection errors.

        *Inputs*

            user
                User whose test inferences must be fetched.
                In case of if token is of different user, then the token should have permission to fetch the
                serving runs of the :bash:`user` in the input. They should be in same DKube group.

            filters
                Only :bash:`*` is supported now.

                User will able to filter runs based on state or duration

        """

        return super().list_runs("inference", user, shared)

    def delete_test_inference(self, user, name, wait_for_completion=True):
        """
        Method to delete a test inference.
        Raises exception if token is of different user or if serving run with name doesnt exist or on any connection errors.

        *Inputs*

            user
                The token must belong to this user. As run of different user cannot be deleted.

            name
                Name of the run which needs to be deleted.

            wait_for_completion
                When set to :bash:`True` this method will wait for inference to get deleted.

        """
        data = super().get_run("inference", user, name, fields="*")
        uuid = data["job"]["parameters"]["generated"]["uuid"]
        ret = super().delete_run("inference", user, name)
        if wait_for_completion:
            self._wait_for_rundelete_completion(uuid, "inference", name)
        return ret

    def create_code(self, code: DkubeCode, wait_for_completion=True):
        """
        Method to create a code repo on DKube.
        Raises Exception in case of errors.


        *Inputs*

            code
                Instance of :bash:`dkube.sdk.rsrcs.code` class.
                Please see the :bash:`Resources` section for details on this class.


            wait_for_completion
                When set to :bash:`True` this method will wait for code resource to get into one of the complete state.
                code is declared complete if it is one of the :bash:`complete/failed/error` state

        """

        assert (
            type(code) == DkubeCode
        ), "Invalid type for run, value must be instance of rsrcs:DkubeCode class"
        super().create_repo(code)
        while wait_for_completion:
            status = super().get_repo("program", code.user, code.name, fields="status")
            state, reason = status["state"], status["reason"]
            if state.lower() in ["ready", "failed", "error"]:
                print(
                    "code {} - completed with state {} and reason {}".format(
                        code.name, state, reason
                    )
                )
                break
            else:
                print(
                    "code {} - waiting for completion, current state {}".format(
                        code.name, state
                    )
                )
                time.sleep(self.wait_interval)

    def get_code(self, user, name):
        """
        Method to fetch the code repo with given name for the given user.
        Raises exception in case of code is not found or any other connection errors.

        *Inputs*

            user
                User whose code has to be fetched.
                In case of if token is of different user, then the token should have permission to fetch the
                code of the :bash:`user` in the input. They should be in same DKube group.

            name
                Name of the code repo to be fetched

        """

        return super().get_repo("program", user, name)

    def list_code(self, user, shared=False, filters="*"):
        """
        Method to list all the code repos of a user.
        Raises exception on any connection errors.

        *Inputs*

            user
                User whose projects must be fetched.
                In case of if token is of different user, then the token should have permission to fetch the
                projects of the :bash:`user` in the input. They should be in same DKube group.

            filters
                Only :bash:`*` is supported now.

                User will able to filter projects based on state or the source

        """

        return super().list_repos("program", user, shared)

    def delete_code(self, user, name, force=False):
        """
        Method to delete a code repo.
        Raises exception if token is of different user or if code with name doesnt exist or on any connection errors.

        *Inputs*

            user
                The token must belong to this user. As code of different user cannot be deleted.

            name
                Name of the code which needs to be deleted.

        """

        super().delete_repo("program", user, name, force=force)

    ################### Feature Store ############################
    def create_featureset(self, featureset: DkubeFeatureSet, wait_for_completion=True):
        """
        Method to create a featureset on DKube.

        *Available in DKube Release: 2.2*

        *Inputs*

            featureset
                Instance of :bash:`dkube.sdk.rsrcs.featureSet` class.
                Please see the :bash:`Resources` section for details on this class.

            wait_for_completion
                When set to :bash:`True` this method will wait for featureset resource to be ready or created
                with v1 version in :bash:`sync` state

        *Outputs*

            A dictionary object with response status

        """
        assert (
            type(featureset) == DkubeFeatureSet
        ), "Invalid type for run, value must be instance of rsrcs:DkubeFeatureset class"
        response = super().create_featureset(featureset)
        if response["code"] == 200 and featureset.featurespec_path is not None:
            spec_response = super().featureset_upload_featurespec(
                featureset.featureset.name, featureset.featurespec_path
            )
            if spec_response["code"] != 200:
                self.delete_featureset(featureset.featureset.name)
                return spec_response
        while wait_for_completion:
            versions = super().get_featureset_versions(featureset.featureset.name)
            if versions is None:
                print("create_featureset: waiting for featureset to be setup")
                time.sleep(self.wait_interval)
                continue

            version_status = DKubeFeatureSetUtils().get_version_status(versions, "v1")
            if version_status.lower() == "synced":
                break
            print("create_featureset: waiting for featureset to be setup")
            time.sleep(self.wait_interval)

        return response

    def delete_featuresets(self, featureset_list):
        """
        Method to delete a list of featuresets on DKube.
        Raises Exception in case of errors.

        *Available in DKube Release: 2.2*

        *Inputs*

            featureset_list
                list of featureset names
                example: ["mnist-fs", "titanic-fs"]

        *Outputs*

            A dictionary object  with response status with the list of deleted featureset names

        """
        assert (
            featureset_list
            and isinstance(featureset_list, list)
            and all(isinstance(featureset, str) for featureset in featureset_list)
        ), "Invalid parameter, value must be a list of featureset names"
        return super().delete_featureset(featureset_list)

    def delete_featureset(self, name):
        """
        Method to delete a a featureset.

        *Available in DKube Release: 2.2*

        *Inputs*

            name
                featureset name to be deleted.
                example: "mnist-fs"

        *Outputs*

            A dictionary object with response status and the deleted featureset name

        """
        assert name and isinstance(
            name, str
        ), "Invalid parameter, value must be a featureset name"
        return super().delete_featureset([name])

    def commit_featureset(self, **kwargs):
        """
        Method to commit sticky featuresets.

        featureset should be in ready state. It will be in created state if no featurespec is uploaded.
        If the featureset is in created state, the following will happen.

            a) If metadata is passed, it will be uploaded as featurespec
            b) If no metadata is passed, it derives from df and uploads it.

        If the featureset is in ready state, the following will happen.

            a) metadata if passed any will be ignored
            b) featurespec will be downloaded for the specifed featureset and df is validated for conformance.

        If name is specified, it derives the path for committing the features.

        If path is also specified, it doesn't derive the path. It uses the specified path. However, path should a mount path into dkube store.

        If df is not specified, it assumes the df is already written to the featureset path. Features can be written to featureset mount path using DkubeFeatureSet.write_features

        *Available in DKube Release: 2.2*

        *Inputs*

            name
                featureset name or None
                example: name='fset'

            df
                Dataframe with features to be written
                None or empty df are invalid
                type: pandas.DataFrame

            metadata
                optional yaml object with name, description and schema fields or None
                example:metadata=[{'name':age, 'description:'', 'schema':int64}]

            path
                Mount path where featureset is mounted or None
                example: path='/opt/dkube/fset'

        *Outputs*

            Dictionary with response status

        """

        name = kwargs.get("name", None)
        df = kwargs.get("df", None)
        metadata = kwargs.get("metadata", None)
        path = kwargs.get("path", None)
        merge = kwargs.get("merge", "True")
        dftype = kwargs.get("dftype", "Py")

        if not df is None:
            assert not df.empty, "df should not be empty"
        else:
            # Todo: Handle commit for featuresets mounted as k8s volumes
            assert name or path, "name or path should be specified"

        featurespec = None
        existing_spec = []

        if name is not None:
            featurespec, valid = super().get_featurespec(name)
            assert valid, "featureset not found"
            if featurespec:
                existing_spec = featurespec
        if merge is False:
            existing_spec = []
        if (dftype == "Py") and (
            (len(existing_spec) != len(df.keys()))
            and (name is not None)
            and (df is not None)
        ):
            if not metadata:
                metadata = DKubeFeatureSetUtils().compute_features_metadata(
                    df, existing_spec
                )
            assert metadata, "The specified featureset is invalid"
            self.upload_featurespec(featureset=name, filepath=None, metadata=metadata)
            featurespec = metadata

        if (dftype == "Py") and (featurespec is not None) and (df is not None):
            isdf_valid = DKubeFeatureSetUtils().validate_features(df, featurespec)
            assert isdf_valid, "DataFrame validation failed"

        return super().commit_featureset(name, df, path, dftype)

    def read_featureset(self, **kwargs):
        """
        Method to read a featureset version.
        If name is specified, path is derived. If featureset is not mounted, a copy is made to user's homedir
        If path is specified, it should be a mounted path

        *Available in DKube Release: 2.2*

        *Inputs*

            name
                featureset to be read
                example: name='fset' or None

            version
                version to be read.
                If no version specified, latest version is assumed
                example: version='v2' or None

            path
                path where featureset is mounted.
                path='/opt/dkube/fset' or None

        *Outputs*

            Dataframe object

        """
        name = kwargs.get("name", None)
        version = kwargs.get("version", None)
        path = kwargs.get("path", None)
        dftype = kwargs.get("dftype", "Py")

        assert (version == None) or isinstance(version, str), "version must be a string"

        return super().read_featureset(name, version, path, dftype)

    def list_featuresets(self, query=None):
        """
        Method to list featuresets based on query string.
        Raises Exception in case of errors.

        *Available in DKube Release: 2.2*

        *Inputs*

            query
                A query string that is compatible with Bleve search format

        *Outputs*

            A dictionary object  with response status and the list of featuresets

        """
        return super().list_featureset(query)

    def upload_featurespec(self, featureset=None, filepath=None, metadata=None):
        """
        Method to upload feature specification file.

        *Available in DKube Release: 2.2*

        *Inputs*

            featureset
                The name of featureset

            filepath
                Filepath for the feature specification metadata yaml file

            metadata
                feature specification in yaml object.

            One of filepath or metadata should be specified.

        *Outputs*

            A dictionary object with response status

        """
        assert featureset and isinstance(featureset, str), "featureset must be string"
        assert bool(filepath) ^ bool(
            metadata
        ), "One of filepath and metadata should be specified"
        return super().featureset_upload_featurespec(featureset, filepath, metadata)

    def get_featureset(self, featureset=None):
        """
        Method to retrieve details of a featureset

        *Available in DKube Release: 2.2*

        *Inputs*

            featureset

                The name of featureset

        *Outputs*

            A dictionary object with response status, featureset metadata and feature versions

        """
        return super().get_featureset(featureset)

    def get_featurespec(self, featureset=None):
        """
        Method to retrieve feature specification method.

        *Available in DKube Release: 2.2*

        *Inputs*

            featureset

                The name of featureset

        *Outputs*

            A dictionary object with response status and feature specification metadata

        """
        return super().get_featurespec(featureset)

    ###############################################################

    def create_dataset(self, dataset: DkubeDataset, wait_for_completion=True):
        """
        Method to create a dataset on DKube.
        Raises Exception in case of errors.


        *Inputs*

            dataset
                Instance of :bash:`dkube.sdk.rsrcs.dataset` class.
                Please see the :bash:`Resources` section for details on this class.


            wait_for_completion
                When set to :bash:`True` this method will wait for dataset resource to get into one of the complete state.
                dataset is declared complete if it is one of the :bash:`complete/failed/error` state

        """
        assert (
            type(dataset) == DkubeDataset
        ), "Invalid type for run, value must be instance of rsrcs:DkubeDataset class"
        super().create_repo(dataset)
        if dataset.datum.remote == True:
            wait_for_completion = False
        while wait_for_completion:
            status = super().get_repo(
                "dataset", dataset.user, dataset.name, fields="status"
            )
            state, reason = status["state"], status["reason"]
            if state.lower() in ["ready", "failed", "error"]:
                print(
                    "dataset {} - completed with state {} and reason {}".format(
                        dataset.name, state, reason
                    )
                )
                break
            else:
                print(
                    "dataset {} - waiting for completion, current state {}".format(
                        dataset.name, state
                    )
                )
                time.sleep(self.wait_interval)

    def get_dataset(self, user, name):
        """
        Method to fetch the dataset with given name for the given user.
        Raises exception in case of dataset is not found or any other connection errors.

        *Inputs*

            user
                User whose dataset has to be fetched.
                In case of if token is of different user, then the token should have permission to fetch the
                dataset of the :bash:`user` in the input. They should be in same DKube group.

            name
                Name of the dataset to be fetched

        """

        return super().get_repo("dataset", user, name)

    def list_datasets(self, user, shared=False, filters="*"):
        """
        Method to list all the datasets of a user.
        Raises exception on any connection errors.

        *Inputs*

            user
                User whose datasets must be fetched.
                In case of if token is of different user, then the token should have permission to fetch the
                datasets of the :bash:`user` in the input. They should be in same DKube group.

            filters
                Only :bash:`*` is supported now.

                User will able to filter datasets based on state or the source

        """

        return super().list_repos("dataset", user, shared)

    def delete_dataset(self, user, name, force=False):
        """
        Method to delete a dataset.
        Raises exception if token is of different user or if dataset with name doesnt exist or on any connection errors.

        *Inputs*

            user
                The token must belong to this user. As dataset of different user cannot be deleted.

            name
                Name of the dataset which needs to be deleted.

        """

        super().delete_repo("dataset", user, name, force=force)

    def create_model(self, model: DkubeModel, wait_for_completion=True):
        """
        Method to create a model on DKube.
        Raises Exception in case of errors.


        *Inputs*

            model
                Instance of :bash:`dkube.sdk.rsrcs.model` class.
                Please see the :bash:`Resources` section for details on this class.


            wait_for_completion
                When set to :bash:`True` this method will wait for model resource to get into one of the complete state.
                model is declared complete if it is one of the :bash:`complete/failed/error` state

        """

        assert (
            type(model) == DkubeModel
        ), "Invalid type for run, value must be instance of rsrcs:DkubeModel class"
        super().create_repo(model)
        while wait_for_completion:
            status = super().get_repo("model", model.user, model.name, fields="status")
            state, reason = status["state"], status["reason"]
            if state.lower() in ["ready", "failed", "error"]:
                print(
                    "model {} - completed with state {} and reason {}".format(
                        model.name, state, reason
                    )
                )
                break
            else:
                print(
                    "model {} - waiting for completion, current state {}".format(
                        model.name, state
                    )
                )
                time.sleep(self.wait_interval)

    def get_model(self, user, name, publish_details=False):
        """
        Method to fetch the model with given name for the given user.
        Raises exception in case of model is not found or any other connection errors.

        *Inputs*

            user
                User whose model has to be fetched.
                In case of if token is of different user, then the token should have permission to fetch the
                model of the :bash:`user` in the input. They should be in same DKube group.

            name
                Name of the model to be fetched

        """

        dkubever = self.dkubeinfo["version"]
        if (
            pversion.parse(dkubever) < pversion.parse("2.3.0.0")
        ) or publish_details == False:
            return super().get_repo("model", user, name)
        else:
            modelObj = super().get_repo("model", user, name)
            versions = modelObj["versions"]
            for v in versions:
                if v["version"]["model"]["stage"] == "PUBLISHED":
                    publish = super().get_model_catalog(user, name)
                    modelObj["publish_details"] = publish
                    return modelObj
            return modelObj

    def list_models(self, user, shared=False, published=False, filters="*"):
        """
        Method to list all the models of a user.
        Raises exception on any connection errors.

        *Inputs*

            user
                User whose models must be fetched.
                In case of if token is of different user, then the token should have permission to fetch the
                models of the :bash:`user` in the input. They should be in same DKube group.

            filters
                Only :bash:`*` is supported now.

                User will able to filter models based on state or the source
            published
                If Published is true, it will return all published models

        """

        if published == True:
            return super().list_published_models(user)
        return super().list_repos("model", user, shared)

    def delete_model(self, user, name, force=False):
        """
        Method to delete a model.
        Raises exception if token is of different user or if model with name doesnt exist or on any connection errors.

        *Inputs*

            user
                The token must belong to this user. As model of different user cannot be deleted.

            name
                Name of the model which needs to be deleted.

        """

        super().delete_repo("model", user, name, force=force)

    def trigger_runs_bycode(self, code, user):
        """
        Method to trigger all the runs in dkube which uses the mentioned code.

        *Inputs*

            code
                Name of the code.

            user
                Owner of the code. All runs of this user will be retriggered.

        """

        condition = TriggerCondition(match="code", name=code, user=user)
        return super().trigger_runs(condition)

    def trigger_runs_bydataset(self, dataset, user):
        """
        Method to trigger all the runs in dkube which uses the mentioned dataset in input.

        *Inputs*

            dataset
                Name of the dataset.

            user
                Owner of the dataset. All runs of this user will be retriggered.

        """
        condition = TriggerCondition(match="dataset", name=dataset, user=user)
        return super().trigger_runs(condition)

    def trigger_runs_bymodel(self, model, user):
        """
        Method to trigger all the runs in dkube which uses the mentioned model in input.

        *Inputs*

            model
                Name of the model.

            user
                Owner of the model. All runs of this user will be retriggered.

        """

        condition = TriggerCondition(match="model", name=model, user=user)
        return super().trigger_runs(condition)

    def get_model_lineage(self, user, name, version):
        """
        Method to get lineage of a model version.

        *Inputs*

            name
                Name of the model

            version
                Version of the model

            user
                Owner of the model.
        """

        return super().get_datum_lineage("model", user, name, version)

    def get_dataset_lineage(self, user, name, version):
        """
        Method to get lineage of a dataset version.

        *Inputs*

            name
                Name of the dataset

            version
                Version of the dataset

            user
                Owner of the dataset.
        """

        return super().get_datum_lineage("dataset", user, name, version)

    def get_training_run_lineage(self, user, name):
        """
        Method to get lineage of a training run.

        *Inputs*

            name
                Name of the run

            user
                owner of the run

        """

        # Get the training run info
        run = self.get_training_run(user, name)
        runid = run["job"]["parameters"]["generated"]["uuid"]
        return super().get_run_lineage("training", user, runid)

    def get_preprocessing_run_lineage(self, user, name):
        """
        Method to get lineage of a preprocessing run.

        *Inputs*

            name
                Name of the run

            user
                owner of the run

        """

        # Get the preprocessing run info
        run = get_preprocessing_run(user, name)
        runid = run["job"]["parameters"]["generated"]["uuid"]
        return super().get_run_lineage("preprocessing", user, runid)

    def get_model_versions(self, user, name):
        """
        Method to get the versions of model.
        Versions are returned in ascending order.

        *Inputs*

            name
                Name of the model

            user
                owner of the model

        """

        model = self.get_model(user, name)
        return model["versions"]

    def get_model_latest_version(self, user, name):
        """
        Method to get the latest version of the given model.

        *Inputs*

            name
                Name of the model

            user
                owner of the model

        """

        versions = self.get_model_versions(user, name)
        return versions[0]["version"]

    def get_model_version(self, user, name, version):
        """
        Method to get details of a version of the given model.
        Raises `NotFoundException` if the version is not found

        *Inputs*

            name
                Name of the model

            version
                Version of the model

            user
                owner of the model
        """
        versions = self.get_model_versions(user, name)
        for v in versions:
            if v["version"]["uuid"] == version:
                return v["version"]

        raise Exception("{}/{}/{} not found".format(user, name, version))

    def get_dataset_versions(self, user, name):
        """
        Method to get the versions of dataset.
        Versions are returned in ascending order.

        *Inputs*

            name
                Name of the dataset

            user
                owner of the dataset

        """

        dataset = self.get_dataset(user, name)
        return dataset["versions"]

    def get_dataset_latest_version(self, user, name):
        """
        Method to get the latest version of the given dataset.

        *Inputs*

            name
                Name of the dataset

            user
                owner of the dataset

        """

        versions = self.get_dataset_versions(user, name)
        return versions[0]["version"]

    def get_dataset_version(self, user, name, version):
        """
        Method to get details of a version of the given dataset.
        Raises `NotFoundException` if the version is not found

        *Inputs*

            name
                Name of the dataset

            version
                Version of the dataset

            user
                owner of the dataset
        """
        versions = self.get_dataset_versions(user, name)
        for v in versions:
            if v["version"]["uuid"] == version:
                return v["version"]

        raise Exception("{}/{}/{} not found".format(user, name, version))

    def get_datascience_capabilities(self):
        """
        Method to get the datascience capabilities of the platform.
        Returns the supported frameworks, versions and the corresponding container image details.

        """
        return super().get_datascience_capability()

    def get_notebook_capabilities(self):
        """
        Method to get the notebook capabilities of the platform.
        Returns the supported frameworks, versions and the image details.

        """
        caps = self.get_datascience_capabilities()
        return caps["nb_ide"]["frameworks"]

    def get_r_capabilities(self):
        """
        Method to get the R language capabilities of the platform.
        Returns the supported frameworks, versions and the image details.

        """
        caps = self.get_datascience_capabilities()
        return caps["r_ide"]["frameworks"]

    def get_training_capabilities(self):
        """
        Method to get the training capabilities of the platform.
        Returns the supported frameworks, versions and the image details.

        """
        caps = self.get_datascience_capabilities()
        return caps["training"]["frameworks"]

    def get_serving_capabilities(self):
        """
        Method to get the serving capabilities of the platform.
        Returns the supported frameworks, versions and the image details.

        """
        caps = self.get_datascience_capabilities()
        return caps["serving"]["frameworks"]

    def list_frameworks(self):
        fw_opts = ["custom"]
        fws = self.get_training_capabilities()
        for fw in fws:
            for v in fw["versions"]:
                name = fw["name"] + "_" + v["name"]
                fw_opts.append(name)
        return json.dumps(fw_opts)

    def release_model(self, user, model, version=None, wait_for_completion=True):
        """
        Method to release a model to model catalog.
        Raises Exception in case of errors.

        *Available in DKube Release: 2.2*

        *Inputs*

            model
                Name with model.

            version
                Version of the model to be released.
                If not passed then latest version is released automatically.

            user
                Owner of the model.

            wait_for_completion
                When set to :bash:`True` this method will wait for publish to finish.
                Publishing is complete if stage of the mode is changed to :bash:`published/failed/error`

        """

        if version == None:
            version = self.get_model_latest_version(user, model)
            version = version["uuid"]

        super().release_model(user, model, version)

        while wait_for_completion:
            v = self.get_model_version(user, model, version)
            stage = v["model"]["stage"]
            reason = v["model"]["reason"]
            if stage.lower() in ["released", "failed", "error"]:
                print(
                    "release {}/{} - completed with state {} and reason {}".format(
                        model, version, stage, reason
                    )
                )
                break
            else:
                print(
                    "release {}/{} - waiting for completion, current state {}".format(
                        model, version, stage
                    )
                )
                time.sleep(self.wait_interval)

    def publish_model(
        self, name, description, details: DkubeServing, wait_for_completion=True
    ):
        """
        Method to publish a model to model catalog.
        Raises Exception in case of errors.

        *Available in DKube Release: 2.2*

        *Inputs*

            name
                Name with which the model must be published in the model catalog.

            description
                Human readable text for the model being published

            details
                Instance of :bash:`dkube.sdk.rsrcs.serving` class.
                Please see the :bash:`Resources` section for details on this class.

                If serving image is not updated in :bash:`run:DkubeServing` argument then,
                - If training used supported standard framework, dkube will pick approp serving image
                - If training used custom image, dkube will try to use the same image for serving

                If transformer image is not updated in :bash:`run:DkubeServing` then,
                - Dkube will use same image as training image

                If transformer code is not updated in :bash:`run:DkubeServing` then,
                - Dkube will use the code used for training


            wait_for_completion
                When set to :bash:`True` this method will wait for publish to finish.
                Publishing is complete if stage of the mode is changed to :bash:`published/failed/error`

        """

        run = details
        user, model, version = (
            run.serving_def.owner,
            run.serving_def.model,
            run.serving_def.version,
        )
        # Fetch training run details and fill in information for serving
        if (
            run.predictor.image == None
            or (run.serving_def.transformer == True and run.transformer.image == None)
            or (
                run.serving_def.transformer == True
                and run.serving_def.transformer_project == None
            )
        ):

            if run.serving_def.version == None:
                v = self.get_model_latest_version(
                    run.serving_def.owner, run.serving_def.model
                )
                run.serving_def.version = v["uuid"]

            li = self.get_model_lineage(
                run.serving_def.owner, run.serving_def.model, run.serving_def.version
            )
            if run.predictor.image == None:
                si = li["run"]["parameters"]["generated"]["serving_image"]["image"]
                run.update_serving_image(
                    None, si["path"], si["username"], si["password"]
                )

            if run.serving_def.transformer == True and run.transformer.image == None:
                ti = li["run"]["parameters"]["generated"]["training_image"]["image"]
                run.update_transformer_image(ti["path"], ti["username"], ti["password"])

            if (
                run.serving_def.transformer == True
                and run.serving_def.transformer_project == None
            ):
                code = li["run"]["parameters"]["training"]["datums"]["workspace"][
                    "data"
                ]
                cname = code["name"].split(":")[1]
                run.update_transformer_code(cname, code["version"])

        data = {"name": name, "description": description, "serving": run.serving_def}
        super().publish_model(user, model, version, data)

        while wait_for_completion:
            v = self.get_model_version(user, model, version)
            stage = v["model"]["stage"]
            reason = v["model"]["reason"]
            if stage.lower() in ["published", "failed", "error"]:
                print(
                    "publish {}/{} - completed with state {} and reason {}".format(
                        model, version, stage, reason
                    )
                )
                break
            else:
                print(
                    "publish {}/{} - waiting for completion, current state {}".format(
                        model, version, stage
                    )
                )
                time.sleep(self.wait_interval)

    def create_model_deployment(
        self,
        user,
        name,
        model,
        version,
        description=None,
        stage_or_deploy="stage",
        min_replicas=0,
        max_concurrent_requests=0,
        wait_for_completion=True,
    ):
        """
        Method to create a serving deployment for a model in the model catalog.
        Raises Exception in case of errors.


        *Inputs*

            user
                Name of the user creating the deployment

            name
                Name of the deployment. Must be unique

            description
                User readable description of the deployment

            model
                Name of the model to be deployed

            version
                Version of the model to be deployed

                            stage_or_deploy
                                    Default set to :bash: `stage` which means to stage the model deployment for testing before
                                    deploying it for production.
                                    Change to :bash: `deploy` to deploy the model in production

            min_replicas
                Minimum number of replicas that each Revision should have.
                If not prvided, uses value set in platform config map.

            max_concurrent_requests
                Soft limit that specifies the maximum number of requests an inf pod can process at a time.
                If not prvided, uses value set in platform config map.

            wait_for_completion
                When set to :bash:`True` this method will wait for job to complete after submission.
                Job is declared complete if it is one of the :bash:`complete/failed/error` state

        """

        assert stage_or_deploy in [
            "stage",
            "deploy",
        ], "Invalid value for stage_or_deploy parameter."

        run = DkubeServing(user, name=name, description=description)
        run.update_serving_model(model, version=version)
        run.update_autoscaling_config(min_replicas, max_concurrent_requests)

        dkubever = self.dkubeinfo["version"]
        if pversion.parse(dkubever) < pversion.parse("2.3.0.0"):
            mcitem = self.get_modelcatalog_item(
                user, modelcatalog=model, version=version
            )
            run.update_serving_image(
                image_url=mcitem["serving"]["images"]["serving"]["image"]["path"]
            )
        else:
            mcitem = super().get_model_catalog(user, model)
            versions = mcitem["versions"]
            for v in versions:
                if v["version"] == version:
                    serving_image = v["serving"]["images"]["serving"]["image"]["path"]
            run.update_serving_image(image_url=serving_image)

        if stage_or_deploy == "stage":
            super().stage_model(run)
        if stage_or_deploy == "deploy":
            super().deploy_model(run)

        while wait_for_completion:
            status = super().get_run("inference", run.user, run.name, fields="status")
            state, reason = status["state"], status["reason"]
            if state.lower() in ["complete", "failed", "error", "running"]:
                print(
                    "run {} - completed with state {} and reason {}".format(
                        run.name, state, reason
                    )
                )
                break
            else:
                print(
                    "run {} - waiting for completion, current state {}".format(
                        run.name, state
                    )
                )
                time.sleep(self.wait_interval)

    def delete_model_deployment(self, user, name, wait_for_completion=True):
        """
        Method to delete a model deployment.
        Raises exception if token is of different user or if serving run with name doesnt exist or on any connection errors.

        *Inputs*

            user
                The token must belong to this user. As run of different user cannot be deleted.

            name
                Name of the run which needs to be deleted.

            wait_for_completion
                When set to :bash:`True` this method will wait for deployment to get deleted.

        """
        data = super().get_run("inference", user, name, fields="*")
        uuid = data["job"]["parameters"]["generated"]["uuid"]
        ret = super().delete_run("inference", user, name)
        if wait_for_completion:
            self._wait_for_rundelete_completion(uuid, "inference", name)
        return ret

    def list_model_deployments(self, user, shared=False, filters="*"):
        """
        Method to list all the model deployments.
        Raises exception on any connection errors.

        *Inputs*

            user
                Name of the user.

            filters
                Only :bash:`*` is supported now.

                User will able to filter runs based on state or duration

        """

        deps = []
        resp = super().list_runs("inference", user, shared)
        for item in resp:
            for inf in item["jobs"]:
                deploy = inf["parameters"]["inference"]["deploy"]
                # MAK - BUG - there is no way today from backend response to separate the test-inferences
                # vs serving deployments. So appending all.
                deps.append(inf)
        return deps

    def modelcatalog(self, user):
        """
        Method to fetch the model catalog from DKube.
        Model catalog is list of models published by datascientists and are
        ready for staging or deployment on a production cluster.
        The user must have permission to fetch the model catalog.

        *Available in DKube Release: 2.2*

        *Inputs*

            user
                Name of the user.
        """
        return super().modelcatalog(user)

    def get_modelcatalog_item(self, user, modelcatalog=None, model=None, version=None):
        """
        Method to get an item from modelcatalog
        Raises exception on any connection errors.

        *Available in DKube Release: 2.2*

        *Inputs*

            user
                Name of the user.

            modelcatalog
                Model catalog name

            model
                Name of the model catalog

            version
                Version of the model

        """
        if modelcatalog is None and model is None:
            return "either model catalog name or model name should be provided"
        if version is None:
            return "Model Version must be provided"
        if modelcatalog:
            mc = self.modelcatalog(user)
            for item in mc:
                if item["name"] == modelcatalog:
                    for iversion in item["versions"]:
                        if iversion["model"]["version"] == version:
                            return iversion

            raise Exception("{}.{} not found in model catalog".format(model, version))
        else:
            mc = self.modelcatalog(user)
            for item in mc:
                if item["model"]["name"] == model:
                    for iversion in item["versions"]:
                        if iversion["model"]["version"] == version:
                            return iversion

            raise Exception("{}.{} not found in model catalog".format(model, version))

    def delete_modelcatalog_item(
        self, user, modelcatalog=None, model=None, version=None
    ):
        """
        Method to delete an item from modelcatalog
        Raises exception on any connection errors.

        *Available in DKube Release: 2.2*

        *Inputs*

            user
                Name of the user.

            modelcatalog
                Model catalog name

            model
                Name of the model catalog

            version
                Version of the model

        """
        if modelcatalog is None and model is None:
            return "either model catalog name or model name should be provided"
        if version is None:
            return "Model Version must be provided"
        if modelcatalog:
            response = self._api.delete_model_catalog_item(user, modelcatalog, version)
            return response
        else:
            mc = self.modelcatalog(user)
            for item in mc:
                if item["model"]["name"] == model:
                    modelcatalog = item["name"]
                    response = self._api.delete_model_catalog_item(
                        user, modelcatalog, version
                    )
                    return response
            raise Exception("{}.{} not found in model catalog".format(model, version))

    def list_projects(self):
        """
        Return list of DKube projects.

        *Available in DKube Release: 2.2*
        """
        response = self._api.get_all_projects().to_dict()
        assert response["response"]["code"] == 200, response["response"]["message"]
        return response["data"]

    def create_project(self, project: DkubeProject):
        """Creates DKube Project.

        *Available in DKube Release: 2.2*

        *Inputs*

            project
                instance of :bash:`dkube.sdk.rsrcs.DkubeProject` class.
        """
        assert (
            type(project) == DkubeProject
        ), "Invalid type for project, value must be instance of rsrcs:DkubeProject class"
        response = self._api.create_project(project).to_dict()
        assert response["response"]["code"] == 200, response["response"]["message"]
        return response["data"]

    def update_project(self, project_id, project: DkubeProject):
        """Update project details.

        *Available in DKube Release: 2.2*
        Note: details and evail_details fields are base64 encoded.

        *Inputs*

            project_id
                id of the project

            project
                instance of :bash:`dkube.sdk.rsrcs.DkubeProject` class.
        """
        assert (
            type(project) == DkubeProject
        ), "Invalid type for project, value must be instance of rsrcs:DkubeProject class"
        project.id = project_id
        response = self._api.update_one_project(
            project_id=project.id, data=project
        ).to_dict()
        assert response["code"] == 200, response["message"]

    def get_project_id(self, name):
        """ "Get project id from project name.

        *Available in DKube Release: 2.2*

        *Inputs*

            name
                name of the project
        """
        response = self._api.get_all_projects().to_dict()
        assert response["response"]["code"] == 200, response["response"]["message"]
        for project in response["data"]:
            if project["name"] == name:
                return project["id"]
        return None

    def get_project(self, project_id):
        """Get project details.

        *Available in DKube Release: 2.2*

        *Inputs*

            project_id
                id of the project
        """
        response = self._api.get_one_project(project_id).to_dict()
        assert response["response"]["code"] == 200, response["response"]["message"]
        return response["data"]

    def get_leaderboard(self, project_id):
        """Get project's leaderboard details.

        *Available in DKube Release: 2.2*

        *Inputs*

            project_id
                id of the project
        """
        response = self._api.get_all_project_submissions(project_id).to_dict()
        assert response["response"]["code"] == 200, response["response"]["message"]
        return response["data"]

    def delete_project(self, project_id):
        """Delete project. This only deletes the project and not the associated resources.

        *Available in DKube Release: 2.2*

        *Inputs*

            project_id
                id of the project
        """
        project_ids = {"project_ids": [project_id]}
        response = self._api.projects_delete_list(project_ids).to_dict()
        assert response["code"] == 200, response["message"]

    def upload_model(
        self, user, name, filepath, extract=False, wait_for_completion=True
    ):
        """Upload model. This creates a model and uploads the file residing in your local workstation.
        Supported formats are tar, gz, tar.gz, tgz, zip, csv and txt.

        *Available in DKube Release: 2.2*

        *Inputs*

            user
                name of user under which model is to be created in dkube.

            name
                name of model to be created in dkube.

            filepath
                path of the file to be uploaded

            extract
                if extract is set to True, the file will be extracted after upload.

            wait_for_completion
                When set to :bash:`True` this method will wait for model resource to get into one of the complete state.
                model is declared complete if it is one of the :bash:`complete/failed/error` state
        """
        upl_resp = super().upload_model(user, name, filepath, extract=extract)
        while wait_for_completion:
            status = super().get_repo("model", user, name, fields="status")
            state, reason = status["state"], status["reason"]
            if state.lower() in ["ready", "failed", "error"]:
                print(
                    "model {} - completed with state {} and reason {}".format(
                        name, state, reason
                    )
                )
                break
            else:
                print(
                    "model {} - waiting for completion, current state {}".format(
                        name, state
                    )
                )
                time.sleep(self.wait_interval)

    def download_dataset(self, path, user, name, version=None):
        """This method is to download a version of dataset.
        Downloaded content will be copied in the specified path.

        *Inputs*

            path
                Target path where the dataset must be downloaded.

            user
                name of user who owns the dataset.

            name
                name of dataset.

            version
                version of the dataset.

        """

        if version == None:
            version = self.get_dataset_latest_version(user, name)
            version = version["uuid"]

        super().download_dataset(path, user, name, version)

    def download_model(self, path, user, name, version=None):
        """This method is to download a version of model.
        Downloaded content will be copied in the specified path.

        *Inputs*

            path
                Target path where the dataset must be downloaded.

            user
                name of user who owns the dataset.

            name
                name of dataset.

            version
                version of the dataset.

        """
        if version == None:
            version = self.get_model_latest_version(user, name)
            version = version["uuid"]

        super().download_model(path, user, name, version)

    def _wait_for_rundelete_completion(self, uuid, _class, name):

        dkubever = self.dkubeinfo["version"]
        # MAK - ideally the target version should be 2.2.7.0 and it should
        # be sufficient to check for older release(s), but there is an internal patch to enable
        # automation suite which returns release version as 2.2.1.13
        if pversion.parse(dkubever) < pversion.parse("2.2.1.13"):
            # Older release - waiting for deletion to complete not supported
            return

        try:  # MAK - try block can be removed, once 2.2.7.0 is released
            while True:
                data = super().get_run_byuuid(uuid)
                state = data["parameters"]["generated"]["status"]["sub_state"]
                if state == None:  # MAK - check can be removed once 2.2.7.0 is released
                    # Older release - ignore the error
                    break
                if state.lower() == "deleting":
                    print(
                        "{} {} - waiting for deletion, current state {}".format(
                            _class, name, state
                        )
                    )
                    time.sleep(self.wait_interval)
                elif state.lower() == "deleted":
                    print("{} {} - deleted successfully".format(_class, name))
                    break
        except ApiException as ae:
            if ae.status == 404:
                # Older release - ignore the error
                print(
                    "ignoring 404 - fetching deleted jobs failed, older release of dkube"
                )
            else:
                raise ae

    def list_inference_endpoints(self):
        """
        Method to list all the inferences in the dkube cluster.
        Raises exception on any connection errors.
        """

        return super().list_inference_endpoints()

    def list_cicd_images(self, repo=None):
        """
            Method to list all the CICD images + Any images manually added in DKube.

        *Inputs*

            repo
                Git repo URL. If provided, only returns images generated for that repo
        """
        response = self._api.get_all_cicd_images().to_dict()
        assert response["response"]["code"] == 200, response["response"]["message"]
        if repo is None:
            return response["data"]

        images = []

        for entry in response["data"]:
            if "repo" in entry["image"] and entry["image"]["repo"] == repo:
                images.append(entry)
        return images

    def get_smtp_artifact(self):
        """
        Method to get the smtp artifact

        *Available in DKube Release: 3.0*
        """
        return super().get_smtp_artifact()

    def update_smtp_artifact(
        self,
        full_name=None,
        sender_email=None,
        smtp_password=None,
        smtp_port=None,
        smtp_server=None,
        smtp_tls_port=None,
        enabled=True,
    ):
        """
        Method to update the smtp artifact"

        * Available in Dkube Release: 3.0*
        """
        data = {
            "full_name": full_name,
            "sender_email": sender_email,
            "smtp_password": smtp_password,
            "smtp_port": smtp_port,
            "smtp_server": smtp_server,
            "smtp_tls_port": smtp_tls_port,
            "enabled": enabled,
        }
        return super().update_smtp_artifact(data)

    ### Model monitor apis ##########

    def modelmonitor_create(
        self, modelmonitor: DkubeModelmonitor, wait_for_completion=True
    ):
        """
        Method to create Model Monitor on Dkube

        *Available in DKube Release: 3.0*

        *Inputs*

            id
              id of the deployment
            modelmonitor
                    Instance of :bash:`dkube.sdk.rsrcs.modelmonitor.DkubeModelmonitor class.
                    Please see the :bash:`Resources` section for details on this class.

            wait_for_completion
                    When set to :bash:`True` this method will wait for modelmonitor resource to get into one of the complete state.
                    modelmonitor is declared complete if it is one of the :bash:`init/ready/error` state

        *Outputs*
                modelmonitor ID
        """
        assert (
            type(modelmonitor) == DkubeModelmonitor
        ), "Invalid type for model monitor, value must be instance of rsrcs:DkubeModelmonitor class"
        response = super().create_model_monitor(modelmonitor)
        while wait_for_completion:
            mm_config = super().get_modelmonitor_configuration(response["uuid"])
            state = mm_config["status"]["state"]
            if state.lower() in ["init", "ready", "error", "incomplete","pending"]:
                print(
                    "ModelMonitor {} - is in state {} and reason {}".format(
                        modelmonitor.modelmonitor.name,
                        state,
                        mm_config["status"]["message"],
                    )
                )
                break
            else:
                print(
                    "ModelMonitor {} - waiting for completion, current state {}".format(
                        modelmonitor.modelmonitor.name, state
                    )
                )
                time.sleep(self.wait_interval)
        assert response["code"] == 200, response["message"]
        return response["uuid"]

    def modelmonitor_list(self, **kwargs):
        """
        Method to list the modelmonitors.

        *Available in DKube Release: 3.0*

        *Inputs*

            tags
                string

            page
                integer

            archived
                boolean, when archived=True, list the archived modelmonitors

        *Outputs*
            A list containing the modelmonitors
        """
        tags = kwargs.get("tags")
        page = kwargs.get("page")
        archived = kwargs.get("archived", False)
        query_params = {}
        if tags:
            query_params["tags"] = tags
        if page:
            query_params["page"] = page
        if archived:
            query_params["archived"] = archived
        return super().list_modelmonitor(query_params)

    def modelmonitor_get_id(self, name):
        """
        Method to get the id  of a model monitor.

        *Available in DKube Release: 3.0*

        *Inputs*

            name
                Name of the modelmonitor

        *Outputs*
            An uuid of the modelmonitor
        """
        response = super().get_modelmonitor_id(name).to_dict()["data"]
        if response != None:
            return response.get(name)
        else:
            return None

    def modelmonitor_get_alertid(self, id, alert_name):
        """
        Method to get the alert id  of a modelmonitor.

        *Available in DKube Release: 3.0*

        *Inputs*

            id
                Modelmonitor Id
            alert_name
                Name of the alert

        *Outputs*
            an id of the alert

        """
        response = super().get_modelmonitor_alerts(id)
        for alert in response:
            if alert["name"] == alert_name:
                return alert["id"]
        return None

    def modelmonitor_get(self, id):
        """
        Method to get the modelmonitor.

        *Available in DKube Release: 3.0*

        *Inputs*

            id
                Modelmonitor Id

        *Outputs*
            A dictionary containing the configuration of the modelmonitor
        """

        return super().get_modelmonitor_configuration(id)

    def modelmonitor_get_alerts(self, id):
        """
        Method to get the alerts of the modelmonitor.

        *Available in DKube Release: 3.0*

        *Inputs*

            id
                Modelmonitor Id

        *Outputs*

            a list of dictionaries containing individual alerts information

        """
        return super().get_modelmonitor_alerts(id)

    def modelmonitors_delete(self, ids=[]):
        """
        Method to delete the multiple modelmonitors.

        *Available in DKube Release: 3.0*

        *Inputs*

            ids
                List of modelmonitor Ids to be deleted. Example: ["cd123","345fg"]

        *Outputs*

            A dictionary object with response status

        """
        return super().delete_modelmonitors(ids)

    def modelmonitor_delete(self, id):
        """
        Method to delete the single modelmonitor.

        *Available in DKube Release: 3.0*

        *Inputs*

            id
                Modelmonitor Id

        *Outputs*

            A dictionary object with response status

        """
        return super().delete_modelmonitors([id])

    def modelmonitor_get_metricstemplate(self):
        """
        Method to get the metrics supported for the modelmonitor.

        *Available in DKube Release: 3.0*

        Outputs*
                a list of dictionaries containing metrics template for Regression and Classification

        """
        return super().get_modelmonitor_template()

    def modelmonitor_delete_alert(self, id, alert_id):
        """
        Method to delete the alerts in the modelmonitor

        *Available in DKube Release: 3.0*

        *Inputs*

            id
                Modelmonitor Id
            alert_id
                Id of a modelmonitor alert
        """
        delete_alertsid_list = []
        delete_alertsid_list.append(alert_id)
        return super().delete_modelmonitor_alert(id, delete_alertsid_list)

    def modelmonitor_add_alert(self, id, alert_data):
        """
        Method to add the alerts in the modelmonitor

        *Available in DKube Release: 3.0*

        *Inputs*
            id
                Modelmonitor Id

            alert_data
                Instance of :bash:`dkube.sdk.rsrcs.modelmonitor.DkubeModelmonitoralert` class.
                Please see the :bash:`Resources` section for details on this class.


        Outputs*
            a dictionary object with response status

        """
        mm = self.modelmonitor_get(id)
        if (mm["input_data_type"] == "image") and (alert_data._class == "feature_drift"):
            if len(alert_data.conditions) > 1:
                raise ValueError("Data Drift alert for image data type connot have more than one conditions")
            alert_data.conditions[0]["feature"] = "image"
            alert_data.conditions[0]["metric"] = None    
            alert_data.conditions[0]["op"] = "<"

        alert_dict = json.loads(alert_data.to_JSON())
        alert_class = alert_dict["_class"]
        for each_condition in alert_dict["conditions"]:
            
            if each_condition["state"] is None:
                if each_condition["op"] is None:
                    raise ValueError(f"operator is none for condition {each_condition}")
                if (alert_class == "feature_drift") and (each_condition["op"] not in ("<", "<=")):
                    raise ValueError("feature drift can only have op operator.lt or operator.le")
        alert_dict["class"] = alert_dict.pop("_class")
        response = super().modelmonitor_addalert(id, {"data": [alert_dict]})
        return response

    def modelmonitor_update_alert(self, id, alert, alert_id):
        """
        Method to update the modelmonitor alert

        *Available in DKube Release: 3.0*

        *Inputs*

            id
                Modelmonitor Id

            data
                Instance of :bash:`dkube.sdk.rsrcs.modelmonitor.DkubeModelmonitoralert` class.
                Please see the :bash:`Resources` section for details on this class.

            alert_id
                ID of the alert you want to update in the modelmonitor

        Outputs*
            a dictionary object with response status

        """
        current_alert = None
        alert_class = None
        alert_attr = lambda alert_class: "feature" if alert_class == "feature_drift" else "metric"
        if alert_id is None:
            raise ValueError("alert_id is recieved as None")
        existing_alerts = self.modelmonitor_get_alerts(id)
        for each_alert in existing_alerts:
            if each_alert["id"] == alert_id:
                current_alert = each_alert
                alert_class = each_alert["_class"]
        alert_key = alert_attr(alert_class)
        alert_dict = json.loads(alert.to_JSON())
        for each_condition in alert_dict['conditions']:
            cond_existing = False
            for each_current_condition in current_alert["conditions"]:
                if each_current_condition[alert_key] == each_condition[alert_key]:
                    cond_existing = True
                    if len(each_condition) == 2: # delete condition will only have two items
                        current_alert["conditions"].remove(each_current_condition)
                        continue
                    if each_condition["threshold"]:
                        each_current_condition["threshold"] = each_condition["threshold"]
                    if each_condition["state"]:
                        each_current_condition["state"] = each_condition["state"]
                    if each_condition["op"]:
                        each_current_condition["op"] = each_condition["op"]
            if not cond_existing:
                current_alert["conditions"].append(each_condition)
        
        alert_dict["conditions"] = current_alert["conditions"]
        if not alert_dict["enabled"]:
            alert_dict["enabled"] = current_alert["enabled"]
        if not alert_dict["alert_action"].get("emails"):
            alert_dict["emails"] = current_alert["alert_action"]
        alert_dict["class"] = alert_dict.pop("_class")
        return super().update_modelmonitor_alert(id, alert_id, alert_dict)

    def modelmonitor_archive(self, id):
        """
        Method to archive the modelmonitor

        *Available in DKube Release: 3.0*

        *Inputs*
            id
                Modelmonitor Id

        Outputs*
            a dictionary object with response status
        """
        return super().modelmonitor_archive(id, archive=True)

    def modelmonitor_unarchive(self, id):
        """
        Method to unarchive the modelmonitor

        *Available in DKube Release: 3.0*

        *Inputs*
            id
                Modelmonitor Id

        Outputs*
            a dictionary object with response status
        """
        return super().modelmonitor_archive(id, archive=False)

    def modelmonitor_start(self, id, wait_for_completion=True):
        """
        Method to start the modelmonitor

        *Available in DKube Release: 3.0*

        *Inputs*
            id
                Modelmonitor Id
            wait_for_completion
                When set to :bash:`True` this method will wait for modelmonitor resource to get into one of the complete state.
                modelmonitor is declared complete if it is one of the :bash:`init/ready/error` state , when it reaches ready state, it starts the modelmonitor

        Outputs*
            a dictionary object with response status

        """
        response = super().modelmonitor_state(id, "start")
        while wait_for_completion:
            mm_state = self.modelmonitor_get(id=id)["status"]["state"]
            if mm_state.lower() in ["init", "active", "error"]:
                break
            else:
                print("ModelMonitor {} - is in {} state".format(id, mm_state))
                time.sleep(self.wait_interval)
        return response

    def modelmonitor_stop(self, id):
        """
        Method to stop the modelmonitor

        *Available in DKube Release: 3.0*

        *Inputs*
            id
                Modelmonitor Id

        Outputs*
            a dictionary object with response status

        """
        return super().modelmonitor_state(id, "stop")

    def modelmonitor_update(
        self, config: DkubeModelmonitor, wait_for_completion=True
    ):
        """
        Method to update the modelmonitor

        *Available in DKube Release: 3.0*

        *Inputs*

            id
                Modelmonitor Id

            config
                Instance of :bash:`dkube.sdk.rsrcs.modelmonitor.DkubeModelmonitor` class.
                Please see the :bash:`Resources` section for details on this class to check
                what can be updated.


        Outputs*
            a dictionary object with response status
        """
        config_dict = config.__dict__["modelmonitor"].__dict__
        config_dict = {k.replace("_", "", 1): v for k, v in config_dict.items()}
        id = config_dict["id"]
        rem_list = [
            "updated_at",
            "id",
            "alerts",
            "created_at",
            "pipeline_component",
            "status",
            "owner",
            "name",
            "discriminator",
        ]
        [config_dict.pop(key) for key in rem_list]
        for k in list(config_dict.keys()):
            if config_dict[k] == None or config_dict[k] == [] or config_dict[k] == {}:
                del config_dict[k]

        if "datasources" in config_dict:
            for i in config_dict["datasources"]:
                if (
                    config_dict["datasources"][i]["name"]
                    == self.modelmonitor_get(id)["datasources"][i]["name"]
                ):
                    config_dict["datasources"][i]["id"] = self.modelmonitor_get(id)[
                        "datasources"
                    ][i]["id"]

        response = super().update_modelmonitor_config(id, config_dict)
        while wait_for_completion:
            mm_state = self.modelmonitor_get(id=id)["status"]["state"]
            if mm_state.lower() in ["init", "error", "ready", "incomplete", "pending"]:
                break
            else:
                print("ModelMonitor {} - is in {} state".format(id, mm_state))
                time.sleep(self.wait_interval)
        return response

    def modelmonitor_update_schema(
        self,
        id,
        label,
        selected=False,
        schema_class=None,
        schema_type=None,
    ):
        """
        Method to update the schema in the modelmonitor

        *Available in DKube Release: 3.0*

        *Inputs*

            id
                Modelmonitor Id
            label
                feature in the schema to be updated
            selected
                boolean (True or False), by default True
            schema_class
                class of the schema (Categorical,Continuous)
            schema_type
                type of schema (Input Feature, PredictionOutput, Rowid, Timestamp)

        Outputs*
            a dictionary object with response status
        """

        if not label:
            raise ValueError("Specify a valid column label")
        if (not schema_class) and (not schema_type):
            raise ValueError("Specify either schema_class, or schema_type")
        found = False
        config = self.modelmonitor_get(id=id)
        try:
            for feature in config["schema"]["features"]:
                if feature["label"] == label:
                    if schema_class:
                        feature["_class"] = schema_class
                    if schema_type:
                        feature["type"] = schema_type
                    if selected is not None:
                        feature["selected"] = selected
                    found = True
            if not found:
                print("specified label is not in the derived schema")
                return None
            for d in config["schema"]["features"]:
                d["class"] = d.pop("_class")
            mm = DkubeModelmonitor(deployemnt_id=id)
            mm.__dict__["modelmonitor"].__dict__["_schema"] = config["schema"]
            return self.modelmonitor_update(mm)
        except TypeError:
            print("Schema is Null")
            return

    def modelmonitor_schema_to_df(
        self,
        id,
    ):
        """
        Method to get schema of the modelmonitor as dataframe

        *Available in DKube Release: 3.0*

        *Inputs*

            id
                Modelmonitor Id
            
        Outputs*
            a dataframe object of schema
        """
        try:
            config = self.modelmonitor_get(id=id)
            if config["input_data_type"] != "tabular":
                raise (f"Schema is not available for {config['input_data_type']} data type")
            schema = config["schema"].get("features")
            if schema == None:
                return None
            existing_schema = pd.DataFrame(schema)
            existing_schema = existing_schema.rename({"_class":"class"}, axis='columns')
        except TypeError:
            print("Schema is Null")
            return
        return existing_schema

    def modelmonitor_update_schema_from_df(
        self,
        id,
        schema_df: pd.DataFrame
    ):
        """
        Method to get schema of the modelmonitor as dataframe

        *Available in DKube Release: 3.0*

        *Inputs*

            id
                Modelmonitor Id
            schema_df
                Pandas DataFrame having schema

        Outputs*
            a dictionary object with response status
        """
        try:
            existing_schema = self.modelmonitor_schema_to_df(id)
            existing_schema.set_index('label', inplace=True)
            existing_schema.update(schema_df.set_index('label'))
            existing_schema = existing_schema.reset_index()
            new_schema = json.loads(existing_schema.to_json(orient="records"))
            mm = DkubeModelmonitor(deployemnt_id=id)
            mm.__dict__["modelmonitor"].__dict__["_schema"] = {"features": new_schema}
            return self.modelmonitor_update(mm)
        except TypeError:
            print("Schema is Null")
            return

    ### operator api's ####

    def configure_clusters(self, data):
        """
        Method to configure clusters in dkube

        *Available in DKube Release: 3.x"

        *Inputs*

            data
               Instance of :bash:`dkube.sdk.rsrcs.operator.DkubeCluster` class.
                Please see the :bash:`Resources` section for details on this class.

        Outputs*
            a dictionary object with response status
        """
        clusters_info = []
        clusters_info.append(data)
        clusters_dict = {}
        clusters_dict["clusters"] = clusters_info
        response = super().configure_clusters(clusters_dict)
        return response

    def get_clusters(self):
        """
        Method to get the clusters in dkube

        *Available in DKube Release: 3.x"

        Outputs*
            returns the dictionary with response and data containing all the configured clusters
        """
        response = super().get_clusters()
        return response

    def get_cluster_details(self, clustername):
        """
        Method to get the cluster details in dkube

        *Available in DKube Release: 3.x"

        Outputs*
            returns the details of the cluster
        """
        response = super().get_cluster_details(clustername)
        return response

    def delete_cluster(self, clustername):
        """
        Method to delete the clusters in dkube

        *Available in DKube Release: 3.x"

        Outputs*
            a dictionary object with response status
        """
        response = super().delete_cluster(clustername)
        return response

    def update_cluster_configuration(self, clustername, data):
        """
        Method to update the cluster configuration in dkube

        *Available in DKube Release: 3.x"

        Outputs*
             a dictionary object with response status
        """
        data = {k.replace("_", "", 1): v for k, v in data.__dict__.items()}
        data = {k: v for k, v in data.items() if v is not None}
        data["class"] = data.pop("Cluster__class")
        response = super().update_cluster_configuration(clustername, data)
        return response

    ### Deployment Api's ###

    def list_deployments(self, **kwargs):
        """
        Return list of DKube deployments.

        *Available in DKube Release: 3.3.x*
        """
        shared = kwargs.get("shared")
        tags = kwargs.get("tags")
        page = kwargs.get("page")
        archived = kwargs.get("archived", False)
        query_params = {}
        if shared:
            query_params["shared"] = shared
        if tags:
            query_params["tags"] = tags
        if page:
            query_params["page"] = page
        if archived:
            query_params["archived"] = archived
        response = self._api.list_deployments().to_dict()
        return response["data"]

    def get_deployment_id(
        self, name=None, clustername=None, variant=None, namespace=None
    ):
        """
        Method to get the id  of a deployment.

        *Available in DKube Release: 3.3.x*

        *Inputs*

          name
            Name of the deployment
          clustername
            Name of the cluster
          variant
            variant of the cluster, if cluster type is sagemaker it's mandatory
          namespace
            namespace for the cluster, if cluster type is dkube, it's mandatory

        *Outputs*
          An uuid of the deployment
        """
        if clustername == None:
            for deployment in self.list_deployments():
                if deployment["name"] == name:
                    return deployment["id"]
        else:
            if clustername:
                cluster_kind = self.get_cluster_details(clustername)["data"]["cluster"][
                    "kind"
                ]
                if cluster_kind == "sagemaker" and variant == None:
                    print("Please provide the variant for the AWS cluster first")
                elif cluster_kind == "dkube-remote" and namespace == None:
                    print(
                        "Please provide the namespace for the dkube-remote cluster first"
                    )
                else:
                    for deployment in self.list_deployments():
                        if (
                            deployment["imported_deployment"]["cluster"]["name"]
                            == clustername
                        ):
                            return deployment["id"]

    def get_deployment(self, id=None):
        """
        Method to get the deployment based on the id

        *Available in DKube Release: 3.3.x*

        *Inputs*
         id
          id of the deployment

        Outputs*
          a dictionary object with response and data containing that deployment details
        """
        response = self._api.get_deployment(id)
        return response

    def import_deployment(
        self,
        name=None,
        description=None,
        tags=None,
        cluster=None,
        deployment_url=None,
        model_reference=None,
        namespace=None,
        variant=None,
    ):
        """
         Method to import the deployment

        *Available in DKube Release: 3.3.x*

        *Inputs*
         name of the deployment
         description of the deployment
         tags is a list of tags
         cluster is cluster name
         deployment_url is url of the deployment
         model_reference,
         if cluster is Dkube, namespace is compulsory field
         if cluster is Sagemaker, variant is compulsory field

        *Outputs*
          a dictionary object with response status
        """
        data = {}
        data["name"] = name
        if cluster:
            data["cluster"] = cluster
            cluster_type = self.get_cluster_details(cluster)["data"]["cluster"]["kind"]
            if cluster_type == "dkube-remote":
                data["namespace"] = namespace
            if cluster_type == "sagemaker":
                data["variant"] = variant
        if description:
            data["description"] = description
        if tags:
            data["tags"] = tags
        if deployment_url:
            data["deployment_url"] = deployment_url
        if model_reference:
            data["model_reference"] = model_reference
        response = self._api.import_new_deployment(data)
        response = response.to_dict()
        assert response["code"] == 200, response["message"]
        return response["uuid"]

    def update_deployment(
        self,
        id=None,
        description=None,
        tags=None,
        cluster=None,
        deployment_url=None,
        model_reference=None,
        namespace=None,
        variant=None,
    ):
        """
        Method to update the imported deployment

        *Available in DKube Release: 3.3.x*

        *Inputs*
          id of the deployment
          description of the deployment
          tags is a list of tags
          cluster is cluster name
          deployment_url is url of the deployment
          model_reference,
          namespace and variant

        Outputs*
          a dictionary object with response status
        """
        data = {}
        if description:
            data["description"] = description
        if tags:
            data["tags"] = tags
        if cluster:
            data["cluster"] = cluster
        if deployment_url:
            data["deployment_url"] = deployment_url
        if model_reference:
            data["model_reference"] = model_reference
        if namespace:
            data["namespace"] = namespace
        if variant:
            data["variant"] = variant
        response = self._api.update_deployment(id, data)
        return response

    def delete_deployments(self, ids=[]):
        """
        Method to delete the multiple deployments.
        *Available in DKube Release: 3.3.x*
        *Inputs*
          ids
            List of deployment Ids to be deleted. Example: ["cd123","345fg"]
        *Outputs*
           A dictionary object with response status
        """
        response = self._api.delete_deployments({"deployment_ids": ids})
        return response

    def delete_deployment(self, id=None):
        """
        Method to delete deployment.
        *Available in DKube Release: 3.3.x*
        *Inputs*
          id
            id of the deployment to be deleted
        *Outputs*
            A dictionary object with response status
        """
        response = self._api.delete_deployments({"deployment_ids": [id]})
        return response

    def archive_deployment(self, id=None):
        """
        Method to archive the deployment

        *Available in DKube Release: 3.3.x*

        *Inputs*
            id
            deployment Id to be archived

        Outputs*
            a dictionary object with response status
        """
        response = self._api.archive_deployments(
            data={"deployment_ids": [id]}, archive="true"
        )
        return response

    def archive_deployments(self, ids=[]):
        """
        Method to archive multiple deployments

        *Available in DKube Release: 3.3.x*

        *Inputs*
            ids
            List of deployment Ids to be archived. Example: ["cd123","345fg"]

        Outputs*
            a dictionary object with response status
        """
        response = self._api.archive_deployments(
            data={"deployment_ids": ids}, archive="true"
        )
        return response

    def unarchive_deployment(self, id=None):
        """
        Method to unarchive the deployment

        *Available in DKube Release: 3.3.x*

        *Inputs*
            id
            deployment Id to be archived

        Outputs*
            a dictionary object with response status
        """
        response = self._api.archive_deployments(
            data={"deployment_ids": [id]}, archive="false"
        )
        return response

    def unarchive_deployments(self, ids=[]):
        """
        Method to unarchive the deployments

        *Available in DKube Release: 3.3.x*

        *Inputs*
            id
            List of deployment Ids to be unarchived. Example: ["cd123","345fg"]

        Outputs*
            a dictionary object with response status
        """
        response = self._api.archive_deployments(
            data={"deployment_ids": ids}, archive="false"
        )
        return response

    def get_cloudevents_logstore_creds(self):
        """
        Method to get the credentials for cloudevents logs bucket.
        Raises exception on any connection errors.

        Outputs*
            a dictionary object with response status

        """
        response = super().get_cloudevents_logstore_creds()
        if response["response"]["code"] == 200:
            return response["data"]
        else:
            raise ValueError(response["response"]["message"])

