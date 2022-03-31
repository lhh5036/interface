'''
@File: testReportComConfig.py
@time:2022/3/31
@Author:quanliu 181324
@Desc:
'''

class TestReportComConfig():

    host = "192.168.3.10" # 安装nginx的服务器地址
    # 测试报告nginx服务器文件夹地址
    report_server_url = "/data/interfaceAutoTest_file/"
    # 数据分析测试报告nginx服务器上面存放的地址
    report_das_server_url = "/data/interfaceAutoTest_file/result_das_*"
    # 数据分析服务器上面的地址（测试报告存放地址）
    das_server_url ="/home/InterfaceAutoTest/apps/DasSystem/report"



    # 最终生成的报告页面上查看地址
    report_url = "http://192.168.3.10:81/interfaceAutoTest_file"