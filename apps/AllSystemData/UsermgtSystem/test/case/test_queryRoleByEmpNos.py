# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test_queryRoleByEmpNos
@time:2022/5/19
@Author:majiaqin 170479
@Desc:queryRoleByEmpNos接口测试用例
'''

import unittest
import random
from loggerUtils import MyLog
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgt_api_ware.queryRoleByEmpNos import queryRoleByEmpNosApi
from apps.AllSystemData.UsermgtSystem.test.moduleFile.test_queryRoleByEmpNos_data import Get_Params
from apps.utils.assert_new_utils import new_assert_utils
# 实例化日志类
logger = MyLog("Test_queryRoleByEmpNosApi").getlog()
class Test_QueryRoleByEmpNos(unittest.TestCase):
    '''获取入参数据'''
    def get_params(self):
        self.num = random.randint(0, 40)
        params_list = [i for i in Get_Params().get_employeeNo()[self.num:40]]
        return params_list

    '''获取返回数据中的roleId'''
    def get_roleId(self, resp_json):
        self.resp_json = resp_json
        roleId_list = [i['roleId'] for i in resp_json['result']]
        return roleId_list

    @new_assert_utils
    def testCase01(self):
        params = self.get_params()
        logger.info('获取入参:{0}'.format(params))
        '''返回数据list'''
        resp_list = [queryRoleByEmpNosApi(params)[0], self.get_roleId(queryRoleByEmpNosApi(params)[1])]
        '''期望数据list'''
        expect_list = [200, Get_Params().get_roleId(tuple(params))]
        logger.info('返回数据list: {0}'.format(resp_list))
        logger.info('期望数据list: {0}'.format(expect_list))
        return resp_list, expect_list

if __name__ == '__main__':
    unittest.main(verbosity=2)