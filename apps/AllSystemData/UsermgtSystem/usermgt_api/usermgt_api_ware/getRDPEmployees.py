# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: getRDPEmployees
@time:2022/4/21
@Author:majiaqin 170479
@Desc:查看账号在该页面下的数据权限
'''
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgtSystem_interface_url import UsermgtApiUrl
from apps.Common_Config.operate_api_data import api_assemble
from apps.logger import MyLog

# 实例化日志类
logger = MyLog("GetRDPEmployeesApi").getlog()

class GetRDPEmployeesApi():
    def __init__(self, api_url):
        self.api_url = api_url
        pass

    @api_assemble(UsermgtApiUrl.getRDPEmployees_url)
    def getRDPEmployees(self, params):
        self.params = params
        logger.info("getRDPEmployees ---->start!")
        return self.params


if __name__ == '__main__':
    pass