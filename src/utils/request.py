# -*- coding: utf-8 -*-

import requests
import json


class Request:

    HOST = '165.227.89.229'

    PORT = '8080'

    @classmethod
    def get_base_url(cls):
        return "http://%s:%s" % (Request.HOST, Request.PORT)

    @classmethod
    def execute_get_request(cls, path, authorization=""):
        headers = {
            'cache-control': "no-cache"
        }

        if len(authorization) > 0:
            headers['Authorization'] = "Bearer %s" % authorization

        url = "%s/%s" % (Request.get_base_url(), path)

        response = requests.get(url, headers=headers)

        data = response.text

        assert (200 == response.status_code)

        return json.loads(data)

    @classmethod
    def execute_post_request(cls, path, body, authorization=""):
        headers = {
            'cache-control': "no-cache",
            'content-type': 'application/json'
        }

        if len(authorization) > 0:
            headers['Authorization'] = "Bearer %s" % authorization

        url = "%s/%s" % (Request.get_base_url(), path)

        response = requests.post(url, json=body, headers=headers)

        data = response.text

        assert (response.status_code in [200, 201])

        return json.loads(data)

    @classmethod
    def execute_put_request(cls, path, body, authorization=""):
        headers = {
            'cache-control': "no-cache",
            'content-type': 'application/json'
        }

        if len(authorization) > 0:
            headers['Authorization'] = "Bearer %s" % authorization

        url = "%s/%s" % (Request.get_base_url(), path)

        response = requests.request('PUT', url, json=body, headers=headers)

        data = response.text

        assert (200 == response.status_code)

        return json.loads(data)
