'''
@File: logger.py
@time:2021/8/4
@Author:quanliu 181324
@Desc:log日志封装
'''
import time
import logging.handlers
import os

def setup_log(config):
    # 当前文件的根路径
    garder_path = os.path.dirname(os.path.realpath(__file__))
    log_time = time.strftime("%Y-%m-%d")
    log_path = garder_path + "/apps/logs/"
    log_name = log_path + "{0}.log".format(log_time)
    '''配置日志'''
    # 设置日志的记录等级
    logging.basicConfig(level=config.LOG_LEVEL)
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = logging.handlers.RotatingFileHandler(log_name, maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s]%(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    return file_log_handler
#
# class MyLog():
#     def __init__(self,logger_name):
#
#         # 创建一个logger
#         self.logger = logging.getLogger(logger_name)
#         self.logger.setLevel(logging.DEBUG)
#
#         # 当前文件的根路径
#         garder_path = os.path.dirname(os.path.realpath(__file__))
#         # 创建一个handler，用于写入日志文件
#         self.log_time = time.strftime("%Y-%m-%d")
#         self.log_path = garder_path + "\\apps\\logs\\"
#         self.log_name = self.log_path+"{0}.log".format(self.log_time)
#
#         fh = logging.handlers.TimedRotatingFileHandler(self.log_name, 'D', 1, 10)
#         fh.setLevel(logging.INFO)
#
#         # 再创建一个handler，用于输出到控制台
#         ch = logging.StreamHandler()
#         ch.setLevel(logging.DEBUG) # 需要写入的日志级别
#
#         # 定义handler的输出格式
#         formatter = logging.Formatter('[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s]%(message)s')
#         fh.setFormatter(formatter)
#         ch.setFormatter(formatter)
#
#         # 给logger添加handler
#         self.logger.addHandler(fh)
#         self.logger.addHandler(ch)
#
#
#         # 关闭打开的文件
#         fh.close()
#         ch.close()
#
#     def getlog(self): # 定义一个函数，回调logger实例
#         return self.logger
