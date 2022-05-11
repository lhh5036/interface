# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test_listNextEmployeeByDeptId
@time:2022/5/10
@Author:majiaqin 170479
@Desc:listNextEmployeeByDeptId接口测试用例
'''

import unittest
from ddt import ddt, data, unpack
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgtSystem_interface_url import UsermgtApiUrl
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgt_api_ware.listNextEmployeeByDeptId import ListNextEmployeeByDeptIdApi
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgtSystem_interface_param import UsermgtApiInputParam
from apps.Common_Config.operate_api_data import splicing_params_new, api_assemble
from apps.AllSystemData.UsermgtSystem.assert_usermgt.assert_file import usermgt_unit_assert
from apps.logger import MyLog
# 实例化日志类
logger = MyLog("ListNextEmployeeByDeptIdApi").getlog()

@ddt
class Test_ListNextEmployeeByDeptId(unittest.TestCase):
    @usermgt_unit_assert
    @api_assemble(UsermgtApiUrl.listEmployeeByDeptId_url)
    @splicing_params_new
    @data(*ListNextEmployeeByDeptIdApi().splicing_params_list())
    @unpack
    def testCase(self, deptid):
        logger.info("listNextEmployeeByDeptId ---->start!")
        lis = []
        lis.append([UsermgtApiInputParam.listNextEmployeeByDeptId_param01])
        lis.append({"args": deptid})
        return lis

if __name__ == '__main__':
    unittest.main(verbosity=2)