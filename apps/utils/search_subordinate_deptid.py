# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: search_subordinate_deptid
@time:2022/6/23
@Author:majiaqin 170479
@Desc:递归查询组织架构id的全部下级id
'''
import pprint
from apps.AllSystemData.UsermgtSystem.usermgt_common_setting import Usermgt_Common_Setting
from apps.utils.mySql_database_util import get_data, convert_list
class Search_Subordinate_Deptid():
    def __init__(self, deptid_list):
        self.deptid_list = deptid_list

    @convert_list
    @get_data(Usermgt_Common_Setting.usermgt_mysql)
    def get_deptId(self, deptId):
        self.deptId = deptId
        sql = "SELECT id FROM org_struct \
WHERE parent_id = '{0}';".format(self.deptId)
        return sql

    def search_subordinate_deptid(self):
        for deptId in self.deptid_list:
            deptIdList = self.get_deptId(deptId)
            if len(deptIdList) > 0:
                self.deptid_list += deptIdList
                self.get_deptId(deptIdList)
            else:
                continue
        return list(set(self.deptid_list))


if __name__ == '__main__':
    pprint.pprint(Search_Subordinate_Deptid([143236066]).search_subordinate_deptid())
    pass