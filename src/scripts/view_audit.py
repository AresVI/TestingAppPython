# -*- coding: utf-8 -*-
import os
import random
import threading
import time

from src.entities.session import Session
from src.entities.traceability_audit import TraceabilityAudit


class ViewAudit(object):
    @classmethod
    def get_information(cls, loop_count, sleep_time):
        login_token = Session.login_with_auditor()
        for _ in range(loop_count):
            time.sleep(sleep_time)
            start_time = time.time()
            traceability_audit_id = random.randint(7, 1491)
            TraceabilityAudit.get_one_traceability_audit(traceability_audit_id, authorization=login_token)
            consuming_time = time.time() - start_time
            file = open("./viewAudit.csv", "a")
            file.write("{}\n".format(consuming_time))
            file.close()
            print("--- Tiempo empleado %s ---" % consuming_time)

    @classmethod
    def run(cls, count_threads=200, loop_count=20, time_sleep=0):

        threads = []

        try:
            os.remove("./viewAudit.csv")
        except Exception as _:
            print("")

        for i in range(count_threads):
            single_thread = threading.Thread(target=ViewAudit.get_information, args=[loop_count, time_sleep])
            threads.append(single_thread)
            single_thread.start()
            single_thread.join()

        file = open("./viewAudit.csv", "r")

        return file.read()
