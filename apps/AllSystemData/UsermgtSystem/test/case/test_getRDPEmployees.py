# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test_getRDPEmployees
@time:2022/4/30
@Author:majiaqin 170479
@Desc:getRDPEmployees接口测试用例
'''
import random
import pprint
import unittest
from ddt import ddt, data, unpack
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgtSystem_interface_url import UsermgtApiUrl
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgt_api_ware.getRDPEmployees import GetRDPEmployeesApi
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgtSystem_interface_param import UsermgtApiInputParam
from apps.Common_Config.operate_api_data import splicing_params_new, api_assemble
from apps.AllSystemData.UsermgtSystem.assert_usermgt.assert_file import usermgt_unit_assert
from apps.logger import MyLog
# 实例化日志类
logger = MyLog("GetRDPEmployeesApi").getlog()

class Test_GetRDPEmployees(unittest.TestCase):
    '''查看账号在该页面下的数据权限接口用例'''
    @usermgt_unit_assert()
    @api_assemble(UsermgtApiUrl.getRDPEmployees_url)
    @splicing_params_new()
    def testCase(self):

        logger.info("getRDPEmployees ---->start!")
        lis =[]
        lis.append([UsermgtApiInputParam.getRDPEmployees_param01,
                    UsermgtApiInputParam.getRDPEmployees_param02])
        info_list = GetRDPEmployeesApi().splicing_params_list()
        info = info_list[random.randint(0, len(info_list)-1)]
        lis.append({'employeeNo': info[0],
                  'menuCode': info[1]})
        return lis

if __name__ == '__main__':
    unittest.main(verbosity=2)