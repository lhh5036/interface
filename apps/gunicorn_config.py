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

# 监听内网端口5000
bind = '192.168.3.180:5000'

# 启动的进程数
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gunicorn.workers.ggevent.GeventWorker'

# 如果应用的代码有比那栋，work将会自动重启，适用于开发环境
reload = True

debug = True