# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test_listTeamLeaderByEmployeeNo
@time:2022/5/18
@Author:majiaqin 170479
@Desc:listTeamLeaderByEmployeeNo接口测试用例
'''

import unittest
import random
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgtSystem_interface_url import UsermgtApiUrl
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgt_api_ware.listTeamLeaderByEmployeeNo import ListTeamLeaderByEmployeeNoApi
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgtSystem_interface_param import UsermgtApiInputParam
from apps.Common_Config.operate_api_data import splicing_params_new, api_assemble
from apps.AllSystemData.UsermgtSystem.assert_usermgt.assert_file import usermgt_unit_assert
from logger import MyLog
# 实例化日志类
logger = MyLog("ListTeamLeaderByEmployeeNoApi").getlog()

class Test_listTeamLeaderByEmployeeNo(unittest.TestCase):
    @usermgt_unit_assert()
    @api_assemble(UsermgtApiUrl.listTeamLeaderByEmployeeNo_url)
    @splicing_params_new()
    def testCase(self):
        '''判断员工是否为负责人,返回相关员工信息'''
        params_list = ListTeamLeaderByEmployeeNoApi().splicing_params_list()
        params = params_list[random.randint(0, len(params_list)-1)]
        lis = []
        lis.append([UsermgtApiInputParam.listTeamLeaderByEmployeeNo_param02,
                    UsermgtApiInputParam.listTeamLeaderByEmployeeNo_param01])
        lis.append({"employeeNo": params[0],
                    "servicePlatform": params[1]})
        logger.info(lis[1])
        return lis

if __name__ == '__main__':
    unittest.main(verbosity=2)
    pass