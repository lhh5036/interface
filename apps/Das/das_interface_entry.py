'''
@File: das_interface_entry.py
@time:2021/8/19
@Author:quanliu 181324
@Desc:数据分析系统接口调用入口
'''

from flask import Flask,render_template
import os
import unittest

app = Flask(__name__)

garder_path = os.path.dirname(os.path.realpath(__file__)) + "\\test\\case\\" # 获取测试用例文件路径

# 接口调用入口
@app.route("/dasInterfaceEntry")
def dasInterfaceEntry():
    return render_template('das_entry.html')

# 数据分析所有用例执行入口
@app.route('/das/allTestCase/execute')
def run_dasTestcaseExecute():
    # 文件的路径
    discover = unittest.defaultTestLoader.discover(garder_path,pattern='test_*.py')
    runner = unittest.TextTestRunner()
    runner.run(discover) # 调用数据分析系统所有用例
    # 返回执行结果



if __name__ == '__main__':
    app.run(debug=True)