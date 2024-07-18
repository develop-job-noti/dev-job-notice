import multiprocessing

bind = "0.0.0.0:8000"

workers = multiprocessing.cpu_count() * 2 + 1

timeout = 120

loglevel = "info"

accesslog = "/var/log/aiapi/log/gunicorn-access.log"
errorlog = "/var/log/aiapi/log/gunicorn-error.log"
