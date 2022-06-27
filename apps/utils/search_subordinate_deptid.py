# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: search_subordinate_deptid
@time:2022/6/23
@Author:majiaqin 170479
@Desc:递归查询组织架构id
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

    @convert_list
    @get_data(Usermgt_Common_Setting.usermgt_mysql)
    def get_superdeptId(self, deptId):
        self.deptId = deptId
        sql = "SELECT parent_id FROM org_struct \
WHERE id = '{0}';".format(self.deptId)
        return sql

    '''递归查询组织架构id的全部下级id'''
    def search_subordinate_deptid(self):
        for deptId in self.deptid_list:
            deptIdList = self.get_deptId(deptId)
            if len(deptIdList) > 0:
                self.deptid_list += deptIdList
                self.get_deptId(deptIdList)
            else:
                continue
        dept_list = []
        for i in self.deptid_list:
            if i not in dept_list:
                dept_list.append(i)
        return dept_list

    '''递归查询组织架构id的全部上级id'''
    def search_subordinate_superdeptid(self):
        for deptId in self.deptid_list:
            deptIdList = self.get_superdeptId(deptId)
            if len(deptIdList) > 0:
                self.deptid_list += deptIdList
                self.get_superdeptId(deptIdList)
            else:
                continue
        return self.deptid_list


if __name__ == '__main__':
    pprint.pprint(Search_Subordinate_Deptid([143236066]).search_subordinate_deptid())
    pass