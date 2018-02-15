# -*- coding: utf-8 -*-

import argparse
import time
import random
import threading

from src.entities.company import Company
from src.entities.session import Session
from src.entities.traceability_audit import TraceabilityAudit
from src.utils.request import Request


class CreateAudit(object):

    @classmethod
    def get_company_contact_person(cls, company_id, authorization=""):
        return Request.execute_get_request("api/company/%s/company-contact-people?pagination=false" % company_id, authorization=authorization)

    @classmethod
    def create_random_company_contact_person(cls, company_id, authorization=""):
        return Request.execute_post_request("api/company/%d/company-contact-people" % company_id, {
            'companyId': company_id,
            'first_name': "Javier Hernán",
            'last_name': "Caballero Garcia",
            'email':  "caballerojavier13@gmail.com",
            'telephone': "2634200463",
            'job_possition': "Jefe"
        }, authorization=authorization)

    @classmethod
    def get_all_process(cls, authorization=""):
        return Request.execute_get_request('api/audit-processes?pagination=false', authorization=authorization)

    @classmethod
    def create_traceability_audit(cls, loop_count, sleep_time, company):

        login_token = Session.login_with_auditor()

        for index_loop in range(loop_count):

            time.sleep(sleep_time)
            start_time = time.time()

            print(" - Auditoría número %s ha sido creada correctamente" % str(index_loop + 1))

            login_token = Session.login_with_administrative()

            if company:
                random_company = Company.get_company(str(args.company[0]), authorization=login_token)

            else:
                companies = Company.get_all_companies(authorization=login_token)

                random_company = random.choice(companies)

            company_id = random_company['id']

            company_name = random_company['name'].encode('utf-8')

            company_contact_people = CreateAudit.get_company_contact_person(company_id, authorization=login_token)

            if len(company_contact_people) > 0:
                company_contact_person_id = random.choice(company_contact_people)['id']
            else:
                company_contact_person_id = CreateAudit.create_random_company_contact_person(company_id, authorization=login_token)['id']

            all_audit_processes = CreateAudit.get_all_process(authorization=login_token)

            body_traceability_audit = {
                'auditProcesses': all_audit_processes,
                'company': random_company,
                'companyId': company_id,
                'companyContactPersonId': company_contact_person_id,
                'name': "Auditoría %s" % company_name
            }

            traceability_audit = TraceabilityAudit.create_traceability_audit(body_traceability_audit, authorization=login_token)

            traceability_audit_id = traceability_audit['id']

            login_token = Session.login_with_auditor()

            TraceabilityAudit.start_traceability_audit(traceability_audit_id, authorization=login_token)

            TraceabilityAudit.simulate_audit(traceability_audit_id, authorization=login_token)

            TraceabilityAudit.finish_traceability_audit(traceability_audit_id, authorization=login_token)

            print("Auditoría finalizada")

            consuming_time = time.time() - start_time
            file = open("./listAudit.csv", "a")
            file.write("{}\n".format(consuming_time))
            file.close()
            print("--- Tiempo empleado %s ---" % consuming_time)

    @classmethod
    def run(cls, count_threads=200, loop_count=20, time_sleep=0, company=None):

        threads = []

        try:
            os.remove("./listAudit.csv")
        except Exception as _:
            print("")

        for i in range(count_threads):
            single_thread = threading.Thread(target=CreateAudit.create_traceability_audit, args=[loop_count, time_sleep, company])
            threads.append(single_thread)
            single_thread.start()
