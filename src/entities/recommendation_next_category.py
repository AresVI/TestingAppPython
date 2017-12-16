# -*- coding: utf-8 -*-
from src.utils.request import Request


class RecommendationNextCategory(object):

    @classmethod
    def get_recommendation(cls, company_id, authorization=""):
        return Request.execute_get_request(
            "api/recommendation-next-category/%s" % company_id,
            authorization=authorization
        )
