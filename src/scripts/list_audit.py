# -*- coding: utf-8 -*-
import os
import random
import threading
import time

from src.entities.session import Session
from src.entities.traceability_audit import TraceabilityAudit


class ListAudit(object):
    @classmethod
    def get_information(cls, loop_count, sleep_time):
        login_token = Session.login_with_auditor()
        for _ in range(loop_count):
            time.sleep(sleep_time)
            start_time = time.time()
            TraceabilityAudit.get_all_traceability_audit(authorization=login_token)
            consuming_time = time.time() - start_time
            file = open("./listAudit.csv", "a")
            file.write("{}\n".format(consuming_time))
            file.close()
            print("--- Tiempo empleado %s ---" % consuming_time)

    @classmethod
    def run(cls, count_threads=200, loop_count=20, time_sleep=0):

        threads = []

        try:
            os.remove("./listAudit.csv")
        except Exception as _:
            print("")

        for i in range(count_threads):
            single_thread = threading.Thread(target=ListAudit.get_information, args=[loop_count, time_sleep])
            threads.append(single_thread)
            single_thread.start()
            single_thread.join()

        file = open("./listAudit.csv", "r")

        return file.read()
