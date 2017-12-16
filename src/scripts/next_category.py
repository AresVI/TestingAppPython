# -*- coding: utf-8 -*-
import os
import threading
import time

from src.entities.recommendation_next_category import RecommendationNextCategory
from src.entities.session import Session


class NextCategory(object):
    @classmethod
    def get_information(cls, loop_count, sleep_time):
        login_token = Session.login_with_auditor()
        for _ in range(loop_count):
            time.sleep(sleep_time)
            start_time = time.time()
            company_id = 5
            RecommendationNextCategory.get_recommendation(company_id, authorization=login_token)
            consuming_time = time.time() - start_time
            file = open("./NextCategory.csv", "a")
            file.write("{}\n".format(consuming_time))
            file.close()
            print("--- Tiempo empleado %s ---" % consuming_time)

    @classmethod
    def run(cls, count_threads=200, loop_count=20, time_sleep=0):

        threads = []

        try:
            os.remove("./NextCategory.csv")
        except Exception as _:
            print("")

        for i in range(count_threads):
            single_thread = threading.Thread(target=NextCategory.get_information, args=[loop_count, time_sleep])
            threads.append(single_thread)
            single_thread.start()
            single_thread.join()

        file = open("./NextCategory.csv", "r")

        return file.read()
