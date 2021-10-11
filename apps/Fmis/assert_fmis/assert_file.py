# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: assert_file
@time:2021/10/7
@Author:majiaqin 170479
@Desc:断言文件
'''

import unittest
import assertpy
import requests
import json
import pprint

from apps.utils.assert_utils import Assert_Api

class Fmis_Unit_Assert():
    def __init__(self, response):
        self.response = response

    def fmis_unit_assert(self, sql=None):
        self.sql = sql
        l = []
        if self.sql == None:
            statucode = Assert_Api(self.response).assert_statucode()
            connect = Assert_Api(self.response).assert_connect()
            l.append(statucode)
            l.append(connect)
            if "False" in l:
                return "False"
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
            return "True"

if __name__ == '__main__':
    def getRDPEmployees():
        url = 'http://192.168.3.162:80/usermgt-n/sys/roledatapermission/getRDPEmployees'
        header = {'Content-Type': 'application/json',
                  'Authorization': '5df26666b185fbf0b3437482125d340e'}
        form = {"args": "{'employeeNo':'170478','menuCode':'90010101'}"}

        r = requests.post(url, headers=header, data=json.dumps(form))
        return r
    response = getRDPEmployees()
    pprint.pprint(response.json())
    s = Fmis_Unit_Assert(response).fmis_unit_assert()
    print(s)