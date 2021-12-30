'''
@File: config.py
@time:2021/9/10
@Author:quanliu
@Desc:配置文件
'''

class Config(object):
    DEBUG = False
    TESTING = False

class DevelopementConfig(Config):
    DEBUG = False


class ProductionConfig(Config):
    TESTING = True