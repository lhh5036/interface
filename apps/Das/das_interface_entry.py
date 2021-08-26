'''
@File: das_interface_entry.py
@time:2021/8/19
@Author:quanliu 181324
@Desc:数据分析系统接口调用入口
'''

from flask import Flask,render_template
import os
import unittest
import time
import HTMLTestRunner

app = Flask(__name__)

garder_path = os.path.dirname(os.path.realpath(__file__)) + "\\test\\case\\" # 获取测试用例文件路径
report_path = os.path.dirname(os.path.realpath(__file__)) + "\\report" # 测试报告路径

# 接口调用入口
@app.route("/dasInterfaceEntry")
def dasInterfaceEntry():
    return render_template('das_entry.html')

# 数据分析所有用例执行入口
@app.route('/das/allTestCase/execute')
def run_dasTestcaseExecute():
    # 文件的路径
    discover = unittest.defaultTestLoader.discover(garder_path,pattern='test_*.py')
    # runner = unittest.TextTestRunner()
    # runner.run(discover) # 调用数据分析系统所有用例
    # 获取当前时间
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    # html报告文件路径
    report_abspath = os.path.join(report_path,"result_"+now+".html")

    # 打开文件，将报告写入
    fp = open(report_abspath,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='数据分析系统-接口自动化报告,测试结果如下:',description='用例执行情况:')
    runner.run(discover)
    fp.close()
    return "数据分析系统用例执行完成!"





if __name__ == '__main__':
    app.run(debug=True)