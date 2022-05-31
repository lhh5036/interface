'''
@File: config.py
@time:2021/9/10
@Author:quanliu
@Desc:配置文件
'''
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig():
    DEBUG = False
    TESTING = False
    # SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "data.sqlite")
    # 数据库配置
    HOST_NAME = "192.168.3.180"
    PORT = "3306"
    DATABASE = "data_warehouse"
    USERNAME = "root"
    PASSWORD = "root"
    DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,
                                                                                            password=PASSWORD,
                                                                                            host=HOST_NAME, port=PORT,
                                                                                            db=DATABASE)
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_POOL_TIMEOUT = 20 # 连接超时时间
    SQLALCHEMY_MAX_OVERFLOW = 20 # 最大连接数
    SQLALCHEMY_TRACK_MODIFICATIONS = False # 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
    SQLALCHEMY_ECHO = True # 显示原始SQL语句

    @staticmethod
    def init_app(app):
        pass

# 开发环境
class DevelopmentConfig(BaseConfig):
    DEBUG = True
    LOG_LEVEL = True
    JSON_AS_ASCII = True
    # 为session加密的key
    # secret_key设置成os.urandom(24)的话，它的值就会变化，而一旦发生变化，
    # 原来的cookie中的token就不能被新的secret_key验证，于是cookie就失效了，相应的session存的内容也就没了，所以会再次提示用户登录。因此以后secret_key最好设置成一个固定的字符串！
    SECRET_KEY = "3422sfsdfsdw4523gdgdsfs"
    # 可以绑定多个数据库（db.create_all(bind=['test_db'])）
    # SQLALCHEMY_BINDS = {
    #     "test_db":"mysql+pymysql://root:root@192.168.3.180:3306/data_warehouse?charset=utf8"
    # }

# 测试环境
class TestingConfig(BaseConfig):
    TESTING = True
    LOG_LEVEL = True

class ProductionConfig(BaseConfig):
    DEBUG = False
    LOG_LEVEL = False


config = {
    'default': DevelopmentConfig,
    'production':ProductionConfig
}