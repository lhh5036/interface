'''
@File: logger.py.py
@time:2021/8/4
@Author:quanliu 181324
@Desc:log日志封装
'''
import time
import logging.handlers
import os

class MyLog():
    def __init__(self,logger_name):

        # 创建一个logger
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)

        # 当前文件的根路径
        garder_path = os.path.dirname(os.path.realpath(__file__))
        # 创建一个handler，用于写入日志文件
        self.log_time = time.strftime("%Y-%m-%d")
        self.log_path = garder_path + "\\logs\\"
        self.log_name = self.log_path+"{0}.log".format(self.log_time)

        fh = logging.handlers.TimedRotatingFileHandler(self.log_name, 'D', 1, 10)
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG) # 需要写入的日志级别

        # 定义handler的输出格式
        formatter = logging.Formatter('[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s]%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)


        # 关闭打开的文件
        fh.close()
        ch.close()

    def getlog(self): # 定义一个函数，回调logger实例
        return self.logger
