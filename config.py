'''
@File: config.py
@time:2021/9/10
@Author:quanliu
@Desc:配置文件
'''
import logging

class Config(object):
    DEBUG = False
    TESTING = False

class DevelopementConfig(Config):
    DEBUG = True
    LOG_LEVEL = logging.DEBUG
    host = "192.168.3.180" # 测试环境
    port = "3306"
    username = "root"
    password = "root"
    databasename = "data_warehouse"

    # 设置数据库的连接
    DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{databasename}?charset=utf8mb4" \
        .format(username=username, password=password, host=host, port=port, databasename=databasename)
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False # 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
    SQLALCHEMY_POOL_TIMEOUT = 20 # 连接超时时间
    SQLALCHEMY_POOL_SIZE = 5 # 数据库池的大小，默认为5

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    TESTING = True
    LOG_LEVEL = logging.ERROR
    host = "192.168.3.180"
    port = "3306"
    username = "root"
    password = "root"
    databasename = "data_warehouse"

    # 设置数据库的连接
    DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{databasename}?charset=utf8mb4" \
        .format(username=username, password=password, host=host, port=port, databasename=databasename)
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_TIMEOUT = 20