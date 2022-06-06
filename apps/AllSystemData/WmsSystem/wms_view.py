'''
@File: wms_view.py
@time:2022/1/18
@Author:quanliu 181324
@Desc:仓库系统接口用例调用入口
'''
from BeautifulReport import BeautifulReport as bf
from flask import Blueprint,render_template # 导入 Flask 中的蓝图 Blueprint 模块
import os
import unittest
import time
from pathlib import Path

from apps.AllSystemData.updateInterResult import insterOrUpdateData
from apps.utils.date_operate_util import DateUtils
from urllib.parse import urlparse

wms_api = Blueprint("wms_api",__name__) # 实例化一个蓝图(Blueprint)对象
wms_garder_path = os.path.dirname(os.path.realpath(__file__)) + "\\test\\case\\" # 获取物流系统测试用例文件路径
wms_report_path = os.path.dirname(os.path.realpath(__file__)) + "\\report" # 测试物流系统报告路径

# 为创建的蓝图添加路由配置
@wms_api.route('/allTestCase/execute')
def run_tmsTestcaseExecute():
    # 文件的路径
    discover = unittest.defaultTestLoader.discover(wms_garder_path, pattern='test_*.py', top_level_dir=os.getcwd())
    # 获取当前时间
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    # html报告文件路径
    report_abspath = os.path.join(wms_report_path,"result_wms_"+now+".html")

    # 删除昨天的报告
    p = Path(wms_report_path)
    delete_date = DateUtils().getTheDate(-1, "%Y-%m-%d")
    for file in p.rglob("result_wms_" + delete_date + "*" + ".html"):
        # 判断是否为文件，只删除文件
        if os.path.isfile(file):
            os.remove(file)

    filename = "result_wms_"+now + ".html"
    runner = bf(discover) # 实例化BeautifulReport模块
    runner.report(filename=filename,description='仓库系统-接口自动化报告',report_dir=wms_report_path)# bf默认为.html结尾
    # 远程连接192.168.3.10服务器(需要先设置免密ssh-copy-id ip)
    os.popen('ssh 192.168.3.10 "rm -rf /data/interfaceAutoTest_file/result_wms_*"') # 远程连接,删除远程192.168.3.10上面原来的报告
    os.popen('scp -r /home/InterfaceAutoTest/apps/AllSystemData/WmsSystem/report/{0} \
                 root@192.168.3.10:/data/interfaceAutoTest_file/'.format(filename)) # 远程传入最新的报告
    download_file_url = "http://192.168.3.10:81/interfaceAutoTest_file/{0}".format(filename)
    wms_url = urlparse(download_file_url).geturl()
    msg = "仓库系统测试报告地址:{0}".format(wms_url)
    # DingHelp(test_url,msg,["13923832556"]).dinghelp() # 推送钉钉消息
    # 存在则更新，不存在则插入
    insterOrUpdateData("wms", "仓库系统", runner.testsRun, runner.success_count, runner.failure_count, wms_url)
    return render_template("system_report.html",
                           wms_report_url=wms_url,
                           urlname='wms')