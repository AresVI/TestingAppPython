# -*- coding: utf-8 -*-
import random
import threading
import time
import csv

from src.entities.session import Session
from src.entities.traceability_audit import TraceabilityAudit

"""
Realizar 200 consultas concurrentes de auditorías realizadas con el usuario ‘Auditor / Auditor Interno’ al sistema
para simular una carga baja. Repetir las pruebas 10 veces con intervalos de 15 segundos entre cada prueba.
"""


def get_information():
    login_token = Session.login_with_auditor()
    loop_count = 20
    for _ in range(loop_count):
        start_time = time.time()
        traceability_audit_id = random.randint(1, 61673)
        TraceabilityAudit.get_traceability_audit(traceability_audit_id, authorization=login_token)
        consuming_time = time.time() - start_time

        file = open("/home/jcaballero/viewAudit.csv", "a")
        file.write("{}\n".format(consuming_time))
        file.close()
        print("--- Tiempo empleado %s ---" % consuming_time)

count_threads = 1000000
threads = []

for i in range(count_threads):
    single_thread = threading.Thread(target=get_information)
    threads.append(single_thread)
    single_thread.start()
