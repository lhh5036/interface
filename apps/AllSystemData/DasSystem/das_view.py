'''
@File:das_view.py
@time:2021/9/10
@Author:quanliu 181324
@Desc:数据分析系统接口用例调用入口
'''
import HTMLTestRunner
from BeautifulReport import BeautifulReport as bf
from bs4 import BeautifulSoup
from flask import Blueprint,render_template,redirect # 导入 Flask 中的蓝图 Blueprint 模块
import os
import unittest
from unittestreport import TestRunner
import time
import requests
from pathlib import Path
from apps.Common_Config.Ding_Webhook import WebHook
from apps.utils.Ding_Robot import DingHelp
from apps.utils.date_operate_util import DateUtils
from selenium import webdriver
import json
from urllib.parse import urlparse

test_url = WebHook.test_url
das_api = Blueprint("das_api",__name__) # 实例化一个蓝图(Blueprint)对象

das_garder_path = os.path.dirname(os.path.realpath(__file__)) + "/test/case/" # 获取数据分析测试用例文件路径
das_report_path = os.path.dirname(os.path.realpath(__file__)) + "/report" # 测试数据分析报告路径

# 为创建的蓝图添加路由配置
@das_api.route('/allTestCase/execute')
def run_dasTestcaseExecute():
    # 文件的路径
    discover = unittest.defaultTestLoader.discover(das_garder_path, pattern='test_*.py', top_level_dir=os.getcwd())
    # 获取当前时间
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    # html报告文件路径
    report_abspath = os.path.join(das_report_path,"result_das_"+now+".html")

    # 删除昨天的报告
    p = Path(das_report_path)
    delete_date = DateUtils().getTheDate(-1, "%Y-%m-%d")
    for file in p.rglob("result_das_" + delete_date + "*" + ".html"):
        # 判断是否为文件，只删除文件
        if os.path.isfile(file):
            os.remove(file)

    # 方法一打开文件，将报告写入
    # fp = open(report_abspath,"wb")
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='数据分析系统-接口自动化报告,测试结果如下:',description='用例执行情况:')
    # runner.run(discover)
    # fp.close()
    # 方法二
    # filename = "result_"+now
    # runner = bf(discover) # 实例化BeautifulReport模块
    # runner.report(filename=filename,description='数据分析系统-接口自动化报告',report_dir=das_report_path)
    # 添加浏览器驱动
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    # driver.get(report_abspath)
    # return "数据分析测试用例执行完成!"
    # 方法三
    # runner = TestRunner(discover)
    # runner.run() # 执行用例
    # # 发送钉钉通知，可以得到执行用例成功个数、失败个数、总数
    # runner.dingtalk_notice(url=test_url)
    # return "数据分析测试用例执行完成!"
    # 方法四--推送钉钉报告连接
    filename = "result_das_"+now
    runner = bf(discover) # 实例化BeautifulReport模块
    runner.report(filename=filename,description='数据分析系统-接口自动化报告',report_dir=das_report_path)
    # 远程连接192.168.3.10服务器(需要先设置免密ssh-copy-id ip)
    os.popen('ssh 192.168.3.10 "rm -rf /data/interfaceAutoTest_file/result_das_*"') # 远程连接,删除远程192.168.3.10上面原来的报告
    os.popen('scp -r /home/InterfaceAutoTest/apps/AllSystemData/DasSystem/report/{0}.html \
                 root@192.168.3.10:/data/interfaceAutoTest_file/'.format(filename)) # 远程传入最新的报告
    download_file_url = "http://192.168.3.10:81/interfaceAutoTest_file/{0}.html".format(filename)
    das_url = urlparse(download_file_url).geturl()
    msg = "数据分析测试报告地址:{0}".format(das_url)
    # DingHelp(test_url,msg,["13923832556"]).dinghelp() # 推送钉钉消息
    return render_template("system_report.html",das_report_url=das_url)
