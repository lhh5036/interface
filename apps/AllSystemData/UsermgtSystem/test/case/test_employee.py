# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test_employee
@time:2022/5/18
@Author:majiaqin 170479
@Desc:employee接口测试用例
'''
import unittest
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgtSystem_interface_url import UsermgtApiUrl
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgt_api_ware.employee import EmployeeApi
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgtSystem_interface_param import UsermgtApiInputParam
from apps.Common_Config.operate_api_data import splicing_params_new, api_assemble
from apps.AllSystemData.UsermgtSystem.assert_usermgt.assert_file import usermgt_unit_assert
from loggerUtils import MyLog
# 实例化日志类
logger = MyLog("EmployeeApi").getlog()

class Test_employee():
    @usermgt_unit_assert()
    @api_assemble(UsermgtApiUrl.employee_url)
    @splicing_params_new()
    def testCase(self):
        params = EmployeeApi().splicing_params_list()
        lis = []
        parmas01 = UsermgtApiInputParam.employee_params01
        parmas01['method'] = params[2]
        lis.append([UsermgtApiInputParam.employee_params02,
                    parmas01])
        lis.append({"employeeNo": params[0],
                    "menuCode": params[1]})
        return lis

if __name__ == '__main__':
    unittest.main(verbosity=2)
    pass