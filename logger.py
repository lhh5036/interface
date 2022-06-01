'''
@File: logger.py
@time:2021/8/4
@Author:quanliu 181324
@Desc:log日志封装
'''
import time
import logging.handlers
import os,multiprocessing
from logging.handlers import TimedRotatingFileHandler


class SafeLog(TimedRotatingFileHandler):
    """
    因为TimedRotatingFileHandler在多进程访问log文件时，切分log日志会报错文件被占用，所以修复这个问题
    """

    def __init__(self, *args, **kwargs):
        super(SafeLog, self).__init__(*args, **kwargs)
        self.suffix_time = ""
        self.origin_basename = self.baseFilename

    def shouldRollover(self, record):
        time_tuple = time.localtime()
        if self.suffix_time != time.strftime(self.suffix, time_tuple) or not os.path.exists(
                self.origin_basename + '.' + self.suffix_time):
            return 1
        else:
            return 0

    def doRollover(self):
        if self.stream:
            self.stream.close()
            self.stream = None

        current_time_tuple = time.localtime()
        self.suffix_time = time.strftime(self.suffix, current_time_tuple)
        self.baseFilename = self.origin_basename + '.' + self.suffix_time

        self.mode = 'a'

        with multiprocessing.Lock():
            if self.backupCount > 0:
                for s in self.getFilesToDelete():
                    os.remove(s)

        if not self.delay:
            self.stream = self._open()

    def getFilesToDelete(self):
        # 将源代码的 self.baseFilename 改为 self.origin_basename
        dir_name, base_name = os.path.split(self.origin_basename)
        file_names = os.listdir(dir_name)
        result = []
        prefix = base_name + "."
        p_len = len(prefix)
        for fileName in file_names:
            if fileName[:p_len] == prefix:
                suffix = fileName[p_len:]
                if self.extMatch.match(suffix):
                    result.append(os.path.join(dir_name, fileName))
        if len(result) < self.backupCount:
            result = []
        else:
            result.sort()
            result = result[:len(result) - self.backupCount]
        return result



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
    # filename：日志文件名
    # when：日志文件按什么维度切分。'S'-秒；'M'-分钟；'H'-小时；'D'-天；'W'-周
    #       这里需要注意，如果选择 D-天，那么这个不是严格意义上的'天'，而是从你
    #       项目启动开始，过了24小时，才会从新创建一个新的日志文件，
    #       如果项目重启，这个时间就会重置。所以这里选择'MIDNIGHT'-是指过了午夜
    #       12点，就会创建新的日志。
    # interval：是指等待多少个单位 when 的时间后，Logger会自动重建文件。
    # backupCount：是保留日志个数。默认的0是不会自动删除掉日志。
    file_log_handler = SafeLog(filename=log_name, interval=1, backupCount=10, when="D",encoding='UTF-8')
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s]%(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    return file_log_handler

class MyLog():
    def __init__(self,logger_name):

        # 创建一个logger
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)

        # 当前文件的根路径
        garder_path = os.path.dirname(os.path.realpath(__file__))
        # 创建一个handler，用于写入日志文件
        self.log_time = time.strftime("%Y-%m-%d")
        self.log_path = garder_path + "/apps/logs/"
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
