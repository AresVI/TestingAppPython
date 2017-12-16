import os
import threading
import time

from src.entities.company import Company


class ValidateCertificate(object):

    @classmethod
    def get_information(cls, loop_count, sleep_time):
        for _ in range(loop_count):
            time.sleep(sleep_time)
            start_time = time.time()
            cuit = "30-70798511-5"
            Company.get_certificate(cuit)
            consuming_time = time.time() - start_time
            file = open("./validateCertificate.csv", "a")
            file.write("{}\n".format(consuming_time))
            file.close()
            print("--- Tiempo empleado %s ---" % consuming_time)

    @classmethod
    def run(cls, count_threads=200, loop_count=20, time_sleep=0):

        threads = []

        try:
            os.remove("./ValidateCertificate.csv")
        except Exception as _:
            print("")

        for i in range(count_threads):
            single_thread = threading.Thread(target=ValidateCertificate.get_information, args=[loop_count, time_sleep])
            threads.append(single_thread)
            single_thread.start()
