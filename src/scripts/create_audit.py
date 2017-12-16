# -*- coding: utf-8 -*-

import argparse
import datetime
import random
import threading

from src.entities.company import Company
from src.entities.session import Session
from src.entities.traceability_audit import TraceabilityAudit
from src.utils.request import Request

parser = argparse.ArgumentParser(description='Crear auditorías de trazabilidad')

parser.add_argument('--company', '-c', metavar='N', type=int, nargs='+',
                    help='Bodega a auditar. Por defecto es una bodega elegida aleatoriamente por loop.')

parser.add_argument('--loop', '-l', dest='count_loops', type=int, default=1,
                    help='Cantidad de ejecuciones. Por defecto es 1.')

parser.add_argument('--thread', '-t', dest='count_threads', type=int, default=1,
                    help='Cantidad de hilos paralelos por ejeecución. Por defecto es 1.')

args = parser.parse_args()


def get_company_contact_person(company_id, authorization=""):
    return Request.execute_get_request("api/company/%s/company-contact-people?pagination=false" % company_id, authorization=authorization)


def create_random_company_contact_person(company_id, authorization=""):
    return Request.execute_post_request("api/company/%d/company-contact-people" % company_id, {
        'companyId': company_id,
        'first_name': "Javier Hernán",
        'last_name': "Caballero Garcia",
        'email':  "caballerojavier13@gmail.com",
        'telephone': "2634200463",
        'job_possition': "Jefe"
    }, authorization=authorization)


def get_all_process(authorization=""):
    return Request.execute_get_request('api/audit-processes?pagination=false', authorization=authorization)


def make_all_the_work():

    for index_loop in range(0, args.count_loops):

        start_time = datetime.datetime.now()

        print(" - Auditoría número %s ha sido creada correctamente" % str(index_loop + 1))

        login_token = Session.login_with_administrative()

        if args.company:
            random_company = Company.get_company(str(args.company[0]), authorization=login_token)

        else:
            companies = Company.get_all_companies(authorization=login_token)

            random_company = random.choice(companies)

        company_id = random_company['id']

        company_name = random_company['name'].encode('utf-8')

        company_contact_people = get_company_contact_person(company_id, authorization=login_token)

        if len(company_contact_people) > 0:
            company_contact_person_id = random.choice(company_contact_people)['id']
        else:
            company_contact_person_id = create_random_company_contact_person(company_id, authorization=login_token)['id']

        all_audit_processes = get_all_process(authorization=login_token)

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

        print("--- Tiempo empleado %s ---" % (datetime.datetime.now() - start_time))


threads = []
for i in range(args.count_threads):
    single_thread = threading.Thread(target=make_all_the_work)
    threads.append(single_thread)
    single_thread.start()
