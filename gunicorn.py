import multiprocessing

workers = multiprocessing.cpu_count() * 2
worker_class = 'gevent'
bind = '0.0.0.0:5100'