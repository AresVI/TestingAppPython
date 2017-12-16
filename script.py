from src.scripts.validate_certificate import ValidateCertificate

count_threads = 200
loop_count = 10
time_sleep = 15


ValidateCertificate.run(count_threads, loop_count, time_sleep)
