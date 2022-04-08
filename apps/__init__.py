'''
@time:
'''
from flask import Flask
# 导入此前写好的蓝图模块
from apps.AllSystemData.DasSystem import das_view
from apps.AllSystemData.FmisSystem import fmis_view
from config import DevelopementConfig, ProductionConfig

config = {
    "dev": DevelopementConfig,
    "prop": ProductionConfig,
}

def create_app(config_name):
    """项目的初始化函数"""
    app = Flask(__name__,template_folder='templates',static_folder='static')
    # 设置配置类
    Config = config[config_name]

    # 加载配置
    app.config.from_object(Config)
    app.config['JSON_AS_ASCII'] = False
    # 为session加密的key
    app.config['SECRET_KEY'] = "3422sfsdfsdw4523gdgdsfs" # secret_key设置成os.urandom(24)的话，它的值就会变化，而一旦发生变化，
    # 原来的cookie中的token就不能被新的secret_key验证，于是cookie就失效了，相应的session存的内容也就没了，所以会再次提示用户登录。因此以后secret_key最好设置成一个固定的字符串！
    app.permanent_session_lifetime = 1551 # session的生存时间——测试时设置

    # 在Flask对象中注册蓝图模块中的蓝图对象 das_view 中的 das_api
    app.register_blueprint(das_view.das_api, url_prefix ="/interfaceTest/")
    # 在Flask对象中注册蓝图模块中的蓝图对象 fmis_view 中的 fmis_api
    app.register_blueprint(fmis_view.fmis_api)

    return app