# -*- coding: utf-8 -*-
from src.utils.request import Request


class Company(object):

    @classmethod
    def get_all_companies(cls, authorization=""):
        return Request.execute_get_request('api/companies?pagination=false', authorization=authorization)

    @classmethod
    def get_company(cls, company_id, authorization=""):
        return Request.execute_get_request("api/companies/%s" % company_id, authorization=authorization)