'''
@File: das_common_header.py
@time:2021/8/5
@Author:quanliu 181324
@Desc:数据分析系统通过调用登录模块获取token
'''
from apps.Das.das_interface_service.das_login import DasystemLogin

# 拼接接口请求头信息
class DasCommonHeader():

    def getDasCommonHeader(self,method,employeeNo):

        # 调用登录操作，获取当前登录人token
        token = DasystemLogin().dasLogin(method,employeeNo)
        # 拼接token得到接口请求头数据
        header = {"Content-Type":"application/json","Authorization":token}

        return header
