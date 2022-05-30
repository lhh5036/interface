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
    DEBUG = True
    host = "192.168.3.180" # 测试环境
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


class ProductionConfig(Config):
    TESTING = True
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