# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test_getEmployeeList
@time:2022/5/16
@Author:majiaqin 170479
@Desc:getEmployeeList接口测试用例
'''
import unittest
import random
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgtSystem_interface_url import UsermgtApiUrl
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgt_api_ware.getEmployeeList import GetEmployeeList
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgtSystem_interface_param import UsermgtApiInputParam
from apps.Common_Config.operate_api_data import splicing_params_new, api_assemble
from apps.AllSystemData.UsermgtSystem.assert_usermgt.assert_file import usermgt_unit_assert
from apps.logger import MyLog

# 实例化日志类
logger = MyLog("GetEmployeeListApi").getlog()

class Test_GetEmployeeList(unittest.TestCase):
    @usermgt_unit_assert()
    @api_assemble(UsermgtApiUrl.getEmployeeList_url)
    @splicing_params_new()
    def testCase(self):
        '''根据职位查询员工'''
        lis = []
        position_list = GetEmployeeList().splicing_params_list()
        position = position_list[random.randint(0, len(position_list)-1)]
        lis.append([UsermgtApiInputParam.getEmployeeList_param01])
        lis.append({"positionName": position})
        return lis

if __name__ == '__main__':
    unittest.main(verbosity=2)
    pass