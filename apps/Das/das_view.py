'''
@File:das_view.py
@time:2021/9/10
@Author:quanliu 181324
@Desc:数据分析系统接口用例调用入口
'''
import HTMLTestRunner
from flask import Blueprint
import os
import unittest
import time
from pathlib import Path

from apps.utils.date_operate_util import DateUtils

das_api = Blueprint("das_api",__name__) # 实例化一个蓝图(Blueprint)对象

das_garder_path = os.path.dirname(os.path.realpath(__file__)) + "/test/case/" # 获取数据分析测试用例文件路径
das_report_path = os.path.dirname(os.path.realpath(__file__)) + "/report" # 测试数据分析报告路径

# 数据分析所有用例执行入口
@das_api.route('/das/allTestCase/execute')
def run_dasTestcaseExecute():
    # 文件的路径
    discover = unittest.defaultTestLoader.discover(das_garder_path, pattern='test_*.py', top_level_dir=os.getcwd())
    # 获取当前时间
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    # html报告文件路径
    report_abspath = os.path.join(das_report_path,"result_"+now+".html")

    # 删除昨天的报告
    p = Path(das_report_path)
    delete_date = DateUtils().getTheDate(-1, "%Y-%m-%d")
    for file in p.rglob("result_" + delete_date + "*" + ".html"):
        # 判断是否为文件，只删除文件
        if os.path.isfile(file):
            os.remove(file)

    # 打开文件，将报告写入
    fp = open(report_abspath,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='数据分析系统-接口自动化报告,测试结果如下:',description='用例执行情况:')
    runner.run(discover)
    fp.close()
    return "报告:{0}".format(report_abspath)

if __name__ == '__main__':
    s = run_dasTestcaseExecute()
    print(s)