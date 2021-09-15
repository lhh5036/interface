'''
@time:
'''
from flask import Flask

from apps.Das import das_view
from apps.Fmis import fmis_view
from apps.config import DevelopementConfig, ProductionConfig

config = {
    "dev": DevelopementConfig,
    "prop": ProductionConfig,
}

def create_app(config_name):
    """项目的初始化函数"""
    app = Flask(__name__)
    # 设置配置类
    Config = config[config_name]

    # 加载配置
    app.config.from_object(Config)
    app.config['JSON_AS_ASCII'] = False

    # 在Flask对象中注册蓝图模块中的蓝图对象 das_view 中的 das_api
    app.register_blueprint(das_view.das_api)
    # 在Flask对象中注册蓝图模块中的蓝图对象 fmis_view 中的 fmis_api
    app.register_blueprint(fmis_view.fmis_api)

    return app