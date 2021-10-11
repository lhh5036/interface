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

from apps.utils.assert_utils import Assert_Api

class Fmis_Unit_Assert():
    def __init__(self, response):
        self.response = response

    def fmis_unit_assert(self, sql=None):
        self.sql = sql
        if self.sql == None:
            Assert_Api(self.response).assert_statucode()
            Assert_Api(self.response).assert_connect()
            return None
        else:
            Assert_Api(self.response).assert_statucode()
            Assert_Api(self.response).assert_connect()
            Assert_Api(self.response).assert_total(self.sql)
            return None

if __name__ == '__main__':
    def getRDPEmployees():
        url = 'http://192.168.3.165:8018/fmis/wishPlatformRefund/selectWishRefundDetail'
        header = {'Content-Type': 'application/json',
                  'Authorization': '5df26666b185fbf0b3437482125d340e'}
        form = {"model":{"syncTime":"2021-09","accounts":["Bit by bit"],"sellers":[],"dataSource":2,"ids":[]},"current":1,"size":100}

        r = requests.post(url, headers=header, data=json.dumps(form))
        return r
    response = getRDPEmployees()
    Fmis_Unit_Assert(response).fmis_unit_assert()