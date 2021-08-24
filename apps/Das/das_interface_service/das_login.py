'''
@File: das_login.py
@time:2021/8/5
@Author:quanliu 181324
@Desc:数据分析系统登录操作
'''

import requests
import json
from apps.Common_Config.interface_common_info import InterfaceCommonInfo

class DasystemLogin():
    def dasLogin(self,method,employeeNo):# method:new/old employeeNo:用户工号
        # 登录请求头
        login_header = {"Content-Type":"application/json"}
        # 登录入参
        userInfo = {"employeeNo": "{0}".format(employeeNo), "password": "MTIzNDU2YWJj"}
        login_body = {"args": '{0}'.format(userInfo), "time": "1275786281258", "signature": "a5b59c739465863df334cb2ea929781e"}

        if method == 'new':
            login_url = InterfaceCommonInfo.common_url + "/usermgt-n/login"
            resp = requests.post(url=login_url,headers=login_header,data=json.dumps(login_body))
            try:
                results = resp.json()["result"]['accessToken']
                return results
            except KeyError:
                return "员工账号不存在或密码错误"
        elif method == 'old':
            login_url = InterfaceCommonInfo.common_url + "/usermgt/login"
            resp = requests.post(url=login_url,headers=login_header,data=json.dumps(login_body))
            try:
                results = resp.json()["result"]['accessToken']
                return results
            except KeyError:
                return "员工账号不存在或密码错误"
