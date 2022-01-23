import multiprocessing
import os

development = True if os.environ.get("FLASK_ENV") == "development" else False

timeout = 10
bind = "0.0.0.0:8000"
loglevel = "debug"
workers = 1 if development else multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"
worker_connections = 2000

max_requests = 100000
max_requests_jitter = 10000
