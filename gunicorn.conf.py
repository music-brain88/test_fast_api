#
# Gunicorn config file
#

# worker
worker_class = "uvicorn.workers.UvicornWorker"
workers = 9

# host
bind = "0.0.0.0"
timeout = 0

# log
accesslog = "-"
errorlog = "-"
loglevel = "info"
