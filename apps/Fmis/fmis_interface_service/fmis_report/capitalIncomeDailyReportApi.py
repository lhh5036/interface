# -*- coding:utf-8 -*-
#!/usr/bin/python3

'''
@File: capitalIncomeDailyReportApi.py
@time:2021/9/04
@Author:majiaqin 170479
@Desc:财务报表-资金收入日报表接口
'''

from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.Das.das_interface_service.dasSystem_interface_param import DasApiInputParam
from apps.Das.das_interface_service.publicCommonUrlSevice import PublicCommonUrlServiceClass
from apps.Das.logger import MyLog
import requests
import json

# 实例化日志类
logger = MyLog("CapitalIncomeDailyReportApi").getlog()

