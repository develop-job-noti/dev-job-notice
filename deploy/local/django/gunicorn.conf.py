import multiprocessing

bind = "0.0.0.0:8000"

workers = multiprocessing.cpu_count() * 2 + 1

timeout = 120

loglevel = "info"

accesslog = "log/gunicorn-access.log"
errorlog = "log/gunicorn-error.log"
