'''
@time:
'''
from flask import Flask
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

    return app