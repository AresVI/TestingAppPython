# -*- coding: utf-8 -*-
import random

from src.utils.request import Request


class TraceabilityAudit:
    
    @classmethod
    def create_traceability_audit(cls, traceability_audit, authorization=""):
        return Request.execute_post_request('api/traceability-audits', traceability_audit, authorization=authorization)

    @classmethod
    def get_traceability_audit(cls, traceability_audit_id, authorization=""):
        return Request.execute_get_request("api/traceability-audits/%s" % traceability_audit_id,
                                           authorization=authorization)

    @classmethod
    def start_traceability_audit(cls, traceability_audit_id, authorization=""):
        return Request.execute_put_request("api/traceability-audits/%s/start" % traceability_audit_id, {},
                                           authorization=authorization)

    @classmethod
    def finish_traceability_audit(cls, traceability_audit_id, authorization=""):
        return Request.execute_put_request("api/traceability-audits/%s/finish" % traceability_audit_id, {},
                                           authorization=authorization)

    @classmethod
    def review_audit_task_recommendation(cls, audit_task_recommendation, authorization=""):
        return Request.execute_put_request("api/audit-task-recommendations", audit_task_recommendation,
                                           authorization=authorization)

    @classmethod
    def review_audit_process_recommendation(cls, audit_process_recommendation, authorization=""):
        return Request.execute_put_request("api/audit-process-recommendations", audit_process_recommendation,
                                           authorization=authorization)

    @classmethod
    def review_audit_recommendation(cls, recommendation, authorization=""):
        return Request.execute_put_request("api/recommendations", recommendation, authorization=authorization)

    @classmethod
    def simulate_audit(cls, traceability_audit_id, authorization=""):
        traceability_audit = TraceabilityAudit.get_traceability_audit(traceability_audit_id, authorization=authorization)

        audit_process_recommendation_set = traceability_audit.get('recommendationSet')[0].get(
            'auditProcessRecommendationSet')

        for i in range(len(audit_process_recommendation_set)):

            audit_task_recommendation_set = audit_process_recommendation_set[i].get('auditTaskRecommendationSet')

            for j in range(len(audit_task_recommendation_set)):

                category_attr_recommendation_set = audit_task_recommendation_set[j].get('categoryAttrRecommendationSet')

                for k in range(len(category_attr_recommendation_set)):

                    attribute_recommendation_set = category_attr_recommendation_set[k].get('attributeRecommendationSet')

                    for l in range(len(attribute_recommendation_set)):
                        attribute_recommendation_set[l]['implemented'] = random.randint(0, 9) > 2

                TraceabilityAudit.review_audit_task_recommendation(
                    audit_task_recommendation_set[j], authorization=authorization
                )

            TraceabilityAudit.review_audit_process_recommendation(
                audit_process_recommendation_set[i], authorization=authorization
            )

        traceability_audit.get('recommendationSet')[0]['levelComputerization'] = random.randint(1, 5)

        TraceabilityAudit.review_audit_recommendation(
            traceability_audit.get('recommendationSet')[0], authorization=authorization
        )
