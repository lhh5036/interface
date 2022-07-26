'''
@File:product_view.py
@time:2021/9/24
@Author:majiaqin 170479
@Desc:财务系统接口用例调用入口
'''

import os
import unittest
import time
import HTMLTestRunner
from BeautifulReport import BeautifulReport as bf
from flask import Blueprint
from flask import render_template
from pathlib import Path
from urllib.parse import urlparse

from apps.AllSystemData.updateInterResult import insterOrUpdateData
from apps.utils.date_operate_util import DateUtils
from apps.Common_Config.interface_common_info import InterfaceCommonInfo

# 实例化一个蓝图(Blueprint)对象
fmis_api = Blueprint("fmis_api", __name__)

# 获取财务系统测试用例文件路径
fmis_garder_path = os.path.dirname(os.path.realpath(__file__)) + "/test/case/"

# 获取财务系统测试报告路径
fmis_report_path = os.path.dirname(os.path.realpath(__file__)) + "/report"

# 财务系统所有用例执行入口
@fmis_api.route("/allTestCase/execute")
def run_fmisTestcaseExecute():
    # 执行用例的文件路径
    discover = unittest.defaultTestLoader.discover(fmis_garder_path, pattern='test_*.py', top_level_dir=os.getcwd())
    # 获取当前时间
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    # html报告文件路径
    report_abspath = os.path.join(fmis_report_path, "result_fmis_" + now + ".html")
    # 删除昨天的报告
    p = Path(fmis_report_path)
    delete_date = DateUtils().getTheDate(-1, "%Y-%m-%d")
    for file in p.rglob("result_fmis_" + delete_date + "*" + ".html"):
        # 判断是否为文件，只删除文件
        if os.path.isfile(file):
            os.remove(file)

    # 打开文件并写入报告
    filename = "result_fmis_" + now + ".html"
    runner = bf(discover)
    runner.report(filename=filename,
                  description='新用户系统-接口自动化报告',
                  report_dir=fmis_report_path)
    # 远程连接192.168.3.10服务器(需要先设置免密ssh-copy-id ip)
    os.popen("ssh {0} 'rm -rf /data/interfaceAutoTest_file/result_fmis_*'".format(InterfaceCommonInfo.server_ip))
    os.popen('scp -r /home/InterfaceAutoTest/apps/FmisSystem/report/{0} \
             root@{1}:/data/interfaceAutoTest_file/'.format(filename, InterfaceCommonInfo.server_ip))
    download_file_url = "http://{0}:81/interfaceAutoTest_file/{1}".format(InterfaceCommonInfo.server_ip,
                                                                          filename)
    fmis_url = urlparse(download_file_url).geturl()
    msg = "财务测试报告地址:{0}".format(fmis_url)

    # 存在则更新，不存在则插入
    insterOrUpdateData("fmis", "财务系统", runner.testsRun, runner.success_count, runner.failure_count, fmis_url)
    return render_template("system_report.html", fmis_report_url=fmis_url, urlname='fmis')


if __name__ == '__main__':
    s = run_fmisTestcaseExecute()
    print(s)