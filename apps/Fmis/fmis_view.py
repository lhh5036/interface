'''
@File:das_view.py
@time:2021/9/10
@Author:quanliu 181324
@Desc:财务系统接口用例调用入口
'''

from flask import Blueprint
import os
import unittest
import time
import HTMLTestRunner

fmis_api = Blueprint("fmis_api",__name__) # 实例化一个蓝图(Blueprint)对象

das_garder_path = os.path.dirname(os.path.realpath(__file__)) + "\\test\\case\\" # 获取财务系统测试用例文件路径
das_report_path = os.path.dirname(os.path.realpath(__file__)) + "\\report" # 测试财务系统报告路径

# 财务系统所有用例执行入口
@fmis_api.route('/fmis/allTestCase/execute')
def run_fmisTestcaseExecute():

    return "财务系统用例执行完成!"
