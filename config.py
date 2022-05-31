'''
@File: settings.py
@time:2021/9/10
@Author:quanliu
@Desc:配置文件
'''

class BaseConfig():
    DEBUG = False
    TESTING = False

class DevelopementConfig(BaseConfig):
    ENV = "development"
    DEBUG = True
    LOG_LEVEL = False
    JSON_AS_ASCII = True
    # 为session加密的key
    # secret_key设置成os.urandom(24)的话，它的值就会变化，而一旦发生变化，
    # 原来的cookie中的token就不能被新的secret_key验证，于是cookie就失效了，相应的session存的内容也就没了，所以会再次提示用户登录。因此以后secret_key最好设置成一个固定的字符串！
    SECRET_KEY = "3422sfsdfsdw4523gdgdsfs"


class ProductionConfig(BaseConfig):
    ENV = "production"
    TESTING = True
