"""

.. module:: DKubeAPIs for file upload and download
   :synopsis: Helper class which provides high level methods for user to integrate at workflow level.

.. moduleauthor:: Subrahmanyam Ongole <github.com/songole>


"""

from __future__ import print_function

import json
import os
from pprint import pprint

import requests
from dkube.sdk.internal.dkube_api.models.api_response import ApiResponse
from dkube.sdk.internal.dkube_api.rest import ApiException
from url_normalize import url_normalize


class FilesBase(object):

    def __init__(self, url=None, token=None):

        protocol = url.split(':')
        if protocol[0] == "https":
            self.url = f"{url}/dkube/v2/ext"
        else:
            assert protocol[0] == "http", "Invalid host"
            self.url = f"{url}/dkube/v2"

        self.token = token
        self.request_headers = {}
        self.request_headers['Authorization'] = f'Bearer {self.token}'

    def _upload_file(self, urlpath=None, filepath=None):

        try:
            fp = open(filepath)
        except BaseException:
            print(f"Specified filepath {filepath} is not valid")
            return response()
        ep = f'{self.url}{urlpath}'
        response = requests.post(
            ep,
            headers=self.request_headers,
            files={'upfile': fp},
            verify=False,
        )
        return response

    def featureset_upload_specfile(self, featureset=None, filepath=None) -> ApiResponse:
        """
        Method to upload features specification file on DKube.
        Raises Exception in case of errors.

        *Inputs*

            featureset
                FeatureSet name.

            filepath
                The full pathname of features specification file on your workstation

        """
        url = f"/ext/featuresets/" + featureset + "/featurespec/upload"
        assert (
            os.path.isfile(filepath) == True
        ), f"Specified file path {filepath} is invalid"
        resp = self._upload_file(url, filepath)
        resp_dict = json.loads(resp.text)
        api_response = ApiResponse(
            code=resp_dict['code'], message=resp_dict['message'])
        return api_response
