# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: usermgt_view
@time:2022/3/25
@Author:majiaqin 170479
@Desc:用户系统接口用例调用入口
'''

import os, unittest, time
from BeautifulReport import BeautifulReport as bf
from flask import Blueprint, render_template
from pathlib import Path
from selenium import webdriver
from urllib.parse import urlparse

from apps.utils.date_operate_util import DateUtils
from apps.Common_Config.interface_common_info import InterfaceCommonInfo

# 实例化一个蓝图(Blueprint)对象
usermgt_api = Blueprint("usermgt_api", __name__)

# 获取用户系统测试用例文件路径
usermgt_garder_path = os.path.dirname(os.path.realpath(__file__)) + "/test/case/"

# 获取用户系统测试报告路径
usermgt_report_path = os.path.dirname(os.path.realpath(__file__)) + "/report"

# 用户系统所有用例执行入口
@usermgt_api.route("/usermgt/allTestCase/execute")
def run_usermgtTTestcaseExecute():
    # 执行用例的文件路径
    discover = unittest.defaultTestLoader.discover(usermgt_garder_path, pattern='test_*.py',
                                                   top_level_dir=os.getcwd())
    # 获取当前时间
    now = DateUtils().getCurrentTimeFormate("%Y-%m-%d-%H_%M_%S")
    # html报告文件路径
    report_abspath = os.path.join(usermgt_report_path, 'result_'+now+'.html')
    # 删除昨天的报告
    p = Path(usermgt_report_path)
    delete_date = DateUtils().getTheDate(-1, "%Y-%m-%d")
    for file in p.rglob('result_'+delete_date+'*'+'.html'):
        # 判断是否为文件,只删除文件
        if os.path.isfile(file):
            os.remove(file)

    # 打开文件并写入报告
    filename = "result_usermgt_"+now
    runner = bf(discover)
    runner.report(filename=filename,
                  description='新用户系统-接口自动化报告',
                  report_dir=usermgt_report_path)
    # 远程连接192.168.3.10服务器(需要先设置免密ssh-copy-id ip)
    os.popen("ssh {0} 'rm -rf /data/interfaceAutoTest_file/result_usermgt_*'".format(InterfaceCommonInfo.server_ip))
    os.popen('scp -r /home/InterfaceAutoTest/apps/UsermgtSystem/report/{0}.html \
             root@{1}:/data/interfaceAutoTest_file/'.format(filename, InterfaceCommonInfo.server_ip))
    download_file_url = "http://{0}:81/interfaceAutoTest_file/{1}.html".format(InterfaceCommonInfo.server_ip,
                                                                               filename)
    usermgt_url = urlparse(download_file_url).geturl()
    msg = "新用户测试报告地址:{0}".format(usermgt_url)
    return render_template("system_report.html", usermgt_report_url=usermgt_url)

if __name__ == '__main__':
    pass