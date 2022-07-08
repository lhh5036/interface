# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test_getMenuCodes_data
@time:2022/6/29
@Author:majiaqin 170479
@Desc:getMenuCodes用例实际出参和期望出参拼接
'''
import pprint
from loggerUtils import MyLog
from apps.AllSystemData.UsermgtSystem.usermgt_common_setting import Usermgt_Common_Setting
from apps.utils.mySql_database_util import get_data, convert_list

# 实例化日志类
logger = MyLog("Test_GetMenuCodes_Data").getlog()
class Test_GetMenuCodes_Data():
    def __init__(self, paramMap, resp_list):
        self.paramMap = paramMap
        self.resp_list = resp_list
        logger.info(self.paramMap)
        logger.info(self.resp_list)

    '''获取出参数据'''
    def get_json(self):
        self.resp_json = self.resp_list[1]
        json_dict = {'menu_code': list(set(self.resp_json['result']))}
        return json_dict

    '''获取期望数据'''
    @convert_list
    @get_data(Usermgt_Common_Setting.usermgt_mysql)
    def expect_json(self):
        sql = "SELECT DISTINCT t.menu_code \
FROM rs_role_menu t \
LEFT JOIN role r \
ON r.id = t.role_id \
LEFT JOIN menu_permission mp \
ON mp.code = t.menu_code \
LEFT JOIN rs_employee_role rer \
ON rer.role_id = r.id \
LEFT JOIN employee e \
ON e.employee_id = rer.employee_id \
WHERE r.status = '1' \
AND mp.status = '1' \
AND e.employee_no = '{0}';".format(self.paramMap)
        return sql

    '''拼接实际出参code，实际出参和期望结果'''
    def expect_data(self):
        expect_json = {'menu_code': self.expect_json()}
        return [self.resp_list[0], self.get_json(), expect_json]

if __name__ == '__main__':
    pass