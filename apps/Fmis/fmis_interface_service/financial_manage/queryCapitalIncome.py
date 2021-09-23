# -*- coding:utf-8 -*-
#!/usr/bin/python3

'''
@File: query_capital_income.py
@time:2021/9/22
@Author:majiaqin 170479
@Desc:财务报表-查询资金收入日报表列表数据接口
'''

from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Das.das_interface_service.dasSystem_interface_param import DasApiInputParam
from apps.Das.das_interface_service.publicCommonUrlSevice import PublicCommonUrlServiceClass
from apps.logger import MyLog
import requests
import json

# 实例化日志类
logger = MyLog("QueryCapitalIncome").getlog()

# 查询资金收入日报表列表数据接口
class QueryCapitalIncome():
    def __init__(self, url, header, formData):
        self.url = url
        self.header = header
        self.formData = formData

    def querycapitalincome(self):
        logger.info("querycapitalincome ---->start!")
        pass