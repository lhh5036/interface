'''
@time:
'''
from flask import Flask
# 导入此前写好的蓝图模块
from apps.AllSystemData.DasSystem import das_view
from apps.AllSystemData.FmisSystem import fmis_view
from apps.AllSystemData.PmsSystem import pms_view
from apps.AllSystemData.ProductSystem import product_view
from apps.AllSystemData.SaleSystem import sale_view
from apps.AllSystemData.TmsSystem import tms_view
from apps.AllSystemData.UsermgtSystem import usermgt_view
from apps.AllSystemData.WmsSystem import wms_view
from logger import setup_log
from config import config
from dbExat import db
from schedulerExat import schedule
from datetime import timedelta


def create_app(config_name):
    """项目的初始化函数"""
    app = Flask(__name__, template_folder='templates',
                static_folder='static')
    # 加载配置
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    # 初始化db
    db.init_app(app)
    # 初始化定时器
    schedule.init_app(app)
    schedule.start()

    app.logger.addHandler(setup_log(config[config_name])) # 日志绑定app
    app.permanent_session_lifetime = timedelta(days=1551)   # session的生存时间——测试时设置
    # 在Flask对象中注册蓝图模块中的蓝图对象 das_view 中的 das_api
    app.register_blueprint(das_view.das_api,url_prefix="/interfaceTest/das/")
    # 在Flask对象中注册蓝图模块中的蓝图对象 fmis_view 中的 fmis_api
    app.register_blueprint(fmis_view.fmis_api, url_prefix="/interfaceTest/fmis/")
    # 在Flask对象中注册蓝图模块中的蓝图对象 usermgt_view 中的 usermgt_api
    app.register_blueprint(usermgt_view.usermgt_api,url_prefix="/interfaceTest/usermgt/")
    # 订单系统
    app.register_blueprint(sale_view.sale_api, url_prefix="/interfaceTest/sale/")
    # 物流系统
    app.register_blueprint(tms_view.tms_api, url_prefix="/interfaceTest/tms/")
    # 产品系统
    app.register_blueprint(product_view.product_api, url_prefix="/interfaceTest/product/")
    # 采购系统
    app.register_blueprint(pms_view.pms_api,url_prefix="/interfaceTest/pms/")
    # 仓库系统
    app.register_blueprint(wms_view.wms_api,url_prefix="/interfaceTest/wms/")
    return app
