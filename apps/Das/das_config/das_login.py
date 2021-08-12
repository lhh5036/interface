'''
@File: das_login.py
@time:2021/8/5
@Author:quanliu 181324
@Desc:数据分析系统登录操作
'''

import requests
import json
import logging
from apps.Common_Config.interface_common_info import InterfaceCommonInfo

class DasystemLogin():
    def dasLogin(self):
        # 登录地址
        login_url = InterfaceCommonInfo.common_url_test + "/usermgt-n/login"
        # 登录请求头
        login_header = {"Content-Type":"application/json"}
        # 登录入参
        login_body = {"args":'{"employeeNo":"181324","password":"MTIzNDU2YWJj"}',"time":"1275786281258","signature":"a5b59c739465863df334cb2ea929781e"}

        resp = requests.post(url=login_url,headers = login_header,data= json.dumps(login_body))
        if resp.json()["success"] == True :
            # 新系统数据分析-token
            newAccessToken = resp.json()["result"]["accessToken"]
            # 旧系统数据分析-token
            #oldAccessToken = resp.json()["result"]["oldAccessToken"]
            return newAccessToken
        else:
            logging.error("该员工不存在!")

