# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test_newListOrgStructAndEmployeeVO
@time:2022/5/18
@Author:majiaqin 170479
@Desc:newListOrgStructAndEmployeeVO接口测试用例
'''

import unittest
import random
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgtSystem_interface_url import UsermgtApiUrl
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgt_api_ware.newListOrgStructAndEmployeeVO import NewListOrgStructAndEmployeeVOApi
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgtSystem_interface_param import UsermgtApiInputParam
from apps.Common_Config.operate_api_data import splicing_params_new, api_assemble
from apps.AllSystemData.UsermgtSystem.assert_usermgt.assert_file import usermgt_unit_assert
from loggerUtils import MyLog
# 实例化日志类
logger = MyLog("ListOrgStructAndEmployeeVOApi").getlog()

class Test_newListOrgStructAndEmployeeVO():
    @usermgt_unit_assert()
    @api_assemble(UsermgtApiUrl.listNextEmployeeByDeptId_url)
    @splicing_params_new()
    def testCase(self):
        '''根据平台和工号获取级联获取员工信息'''
        params_list = NewListOrgStructAndEmployeeVOApi().splicing_params_list()
        params = params_list[random.randint(0, len(params_list)-1)]
        lis = []
        lis.append([UsermgtApiInputParam.newListOrgStructAndEmployeeVO_param01])
        lis.append({"orgName": params[0], "employeeNo": params[1]})
        logger.info(lis[1])
        return lis
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
    pass