'''
@File:fmis_view.py
@time:2021/9/24
@Author:majiaqin 170479
@Desc:财务系统接口用例调用入口
'''

import os
import unittest
import time
import HTMLTestRunner
from flask import Blueprint
from pathlib import Path

from apps.utils.date_operate_util import DateUtils

# 实例化一个蓝图(Blueprint)对象
fmis_api = Blueprint("fmis_api", __name__)

# 获取财务系统测试用例文件路径
fmis_garder_path = os.path.dirname(os.path.realpath(__file__)) + "/test/case/"

# 获取财务系统测试报告路径
fmis_report_path = os.path.dirname(os.path.realpath(__file__)) + "/report"

# 财务系统所有用例执行入口
@fmis_api.route("/fmis/allTestCase/execute")
def run_fmisTestcaseExecute():
    # 执行用例的文件路径
    discover = unittest.defaultTestLoader.discover(fmis_garder_path, pattern='test_*.py', top_level_dir=os.getcwd())
    # 获取当前时间
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    # html报告文件路径
    report_abspath = os.path.join(fmis_report_path, "result_" + now + ".html")
    # 删除昨天的报告
    p = Path(fmis_report_path)
    delete_date = DateUtils().getTheDate(-1, "%Y-%m-%d")
    for file in p.rglob("result_" + delete_date + "*" + ".html"):
        # 判断是否为文件，只删除文件
        if os.path.isfile(file):
            os.remove(file)

    # 打开文件并写入报告
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="财务系统-接口自动化报告,测试结果如下:",
                                           description="用例执行情况:")
    runner.run(discover)
    fp.close()

    return "财务系统用例执行完成!"


if __name__ == '__main__':
    s = run_fmisTestcaseExecute()
    print(s)