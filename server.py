from flask import Flask, request

from src.scripts.list_audit import ListAudit
from src.scripts.next_category import NextCategory
from src.scripts.validate_certificate import ValidateCertificate
from src.scripts.view_audit import ViewAudit

app = Flask(__name__)


@app.route('/list_audit/')
def list_audit():
    count_threads = request.args.get('count_threads', default=200, type=int)
    loop_count = request.args.get('loop_count', default=20, type=int)
    time_sleep = request.args.get('time_sleep', default=0, type=int)

    return ListAudit.run(count_threads, loop_count, time_sleep)


@app.route('/view_audit/')
def view_audit():
    count_threads = request.args.get('count_threads', default=200, type=int)
    loop_count = request.args.get('loop_count', default=20, type=int)
    time_sleep = request.args.get('time_sleep', default=0, type=int)

    return ViewAudit.run(count_threads, loop_count, time_sleep)


@app.route('/next_category/')
def next_category():
    count_threads = request.args.get('count_threads', default=200, type=int)
    loop_count = request.args.get('loop_count', default=20, type=int)
    time_sleep = request.args.get('time_sleep', default=0, type=int)

    return NextCategory.run(count_threads, loop_count, time_sleep)


@app.route('/validate_certificate/')
def validate_certificate():
    count_threads = request.args.get('count_threads', default=200, type=int)
    loop_count = request.args.get('loop_count', default=20, type=int)
    time_sleep = request.args.get('time_sleep', default=0, type=int)

    return ValidateCertificate.run(count_threads, loop_count, time_sleep)


if __name__ == '__main__':
    app.run()
