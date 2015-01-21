import os

def num_cpus():
    if not hasattr(os, "sysconf"):
        raise RuntimeError("No sysconf detected.")
    return os.sysconf("SC_NPROCESSORS_ONLN")


preload = True
workers = num_cpus() * 2 + 1
bind = '127.0.0.1:8000'

# log files
accesslog = 'logs/gunicorn-access.log'
errorlog  = 'logs/gunicorn-error.log'
loglevel  = 'debug'
