# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test_listNextEmployeeByDeptId
@time:2022/5/10
@Author:majiaqin 170479
@Desc:listNextEmployeeByDeptId接口测试用例
'''

import unittest
import random
from ddt import ddt, data, unpack
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgtSystem_interface_url import UsermgtApiUrl
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgt_api_ware.listNextEmployeeByDeptId import ListNextEmployeeByDeptIdApi
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgtSystem_interface_param import UsermgtApiInputParam
from apps.Common_Config.operate_api_data import splicing_params_new, api_assemble
from apps.AllSystemData.UsermgtSystem.assert_usermgt.assert_file import usermgt_unit_assert
from apps.logger import MyLog
# 实例化日志类
logger = MyLog("ListNextEmployeeByDeptIdApi").getlog()


class Test_ListNextEmployeeByDeptId(unittest.TestCase):
    @usermgt_unit_assert()
    @api_assemble(UsermgtApiUrl.listNextEmployeeByDeptId_url)
    @splicing_params_new()
    def testCase(self):
        '''查看该组织架构id的下级员工'''
        deptid_list = ListNextEmployeeByDeptIdApi().splicing_params_list()
        deptid = deptid_list[random.randint(0, len(deptid_list) - 1)]
        logger.info("listNextEmployeeByDeptId ---->start! {0}".format(deptid))
        lis = []
        lis.append([UsermgtApiInputParam.listNextEmployeeByDeptId_param01])
        lis.append({"args": deptid})
        return lis

if __name__ == '__main__':
    # print(Test_ListNextEmployeeByDeptId().testCase())
    unittest.main()