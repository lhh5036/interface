# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: assert_file
@time:2022/3/25
@Author:majiaqin 170479
@Desc:断言文件
'''

import requests
import json
import pprint

from apps.utils.assert_utils import Assert_Api

class Usermgt_Unit_Assert():
    def __init__(self, response):
        self.response = response

    def usermgt_unit_assert(self, sql=None):
        self.sql = sql
        l = []
        if self.sql == None:
            statucode = Assert_Api(self.response).assert_statucode()
            connect = Assert_Api(self.response).assert_connect()
            l.append(statucode)
            l.append(connect)
            if "False" in l:
                return "False"
            else:
                return "True"
        else:
            statucode = Assert_Api(self.response).assert_statucode()
            connect = Assert_Api(self.response).assert_connect()
            total = Assert_Api(self.response).assert_total(self.sql)
            l.append(statucode)
            l.append(connect)
            l.append(total)
            if "False" in l:
                return "False"
            else:
                return "True"

if __name__ == '__main__':
    pass