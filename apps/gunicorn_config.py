'''
@File: gunicorn_config.py
@time:2021/9/10
@Author:quanliu
@Desc:
'''


import gevent.monkey
# gevent的猴子魔法 变成非阻塞
gevent.monkey.patch_all()
import multiprocessing

"""
gunicorn的配置文件
"""


bind = '0.0.0.0:5000'

# 启动的进程数
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gunicorn.workers.ggevent.GeventWorker'