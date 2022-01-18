'''
@File: sale_view.py
@time:2022/1/18
@Author:quanliu 181324
@Desc:订单系统接口用例调用入口
'''
from flask import Blueprint
import os


sale_api = Blueprint("sale_api",__name__) # 实例化一个蓝图(Blueprint)对象

sale_garder_path = os.path.dirname(os.path.realpath(__file__)) + "\\test\\case\\" # 获取订单系统测试用例文件路径
sale_report_path = os.path.dirname(os.path.realpath(__file__)) + "\\report" # 测试订单系统报告路径