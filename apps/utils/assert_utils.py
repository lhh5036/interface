# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: assert_utils
@time:2021/10/7
@Author:majiaqin 170479
@Desc:全局断言工具类,供各系统的assert_file调用
'''

import assertpy
import unittest
import pytest
import requests
import json
import pprint

from apps.logger import MyLog
from apps.utils.mySql_database_util import Mysql_handleOperator
from apps.Fmis.fmis_common_settting import Fmis_Common_Setting
from apps.utils.currency_utils import Json_Get

# 实例化日志类
logger = MyLog("AssertUtils").getlog()

class Assert_Api(unittest.TestCase):
    '''获取返回数据供所有方法调用'''
    # 初始化父类
    def __init__(self, response):
        super().__init__()
        self.response = response

    '''断言返回数据状态码'''
    def assert_statucode(self):
        try:
            self.assertEqual(200, self.response.status_code)
            print(self.assertEqual(200, self.response.status_code))
            logger.info("Assert statu_code ---> success!")
            return "True"
        except AssertionError:
            logger.error("Assert statu_code ---> fail!")
            logger.error("接口报错，statu_code：{0}".format(self.response.status_code))
            return "False"

    '''断言接口是否成功连接'''
    def assert_connect(self):
        try:
            self.assertIn("connectionRefused", self.response.json())
            self.assertIn("success", self.response.json())
            self.assertIn("errorMsg", self.response.json())
            logger.info("Api have response data!")
            try:
                self.assertEqual(False, self.response.json()["connectionRefused"])
                self.assertEqual(True, self.response.json()["success"])
                self.assertEqual(None, self.response.json()["errorMsg"])
                logger.info("Api connect success!")
                return "True"
            except AssertionError:
                logger.error("Api connect fail!")
                msg = "接口连接失败,connectionRefused的值为{0} \n success的值为{1} \n\
errorMsg的的值为{2}".format(self.response.json()["connectionRefused"],
                        self.response.json()["success"],
                        self.response.json["errorMsg"])
                logger.error(msg)
                return "False"
        except AssertionError:
            logger.error("Api response fail!")
            logger.error("接口报错，statu_code：{0}".format(self.response.status_code))
            return "False"

    '''断言接口返回数据条目数是否正确'''
    def assert_total(self, sql):
        # 查询数据条目数的sql
        self.sql = sql
        message = Json_Get(self.response.json()).json_get("total")
        if message == "True":
            logger.info("Api response data have total!")
            sql_total = Mysql_handleOperator(Fmis_Common_Setting.fmis_mysql).data_sql("select", self.sql)[0][0]
            try:
                self.assertEqual(sql_total, Json_Get(self.response.json()).json_value("total"))
                logger.info(" The number of returned api data is correct!")
                return "True"
            except AssertionError:
                logger.error("Return api data total error")
                return "False"
        else:
            logger.error("Api response data not have total!")
            return "False"


if __name__ == '__main__':
    def getRDPEmployees():
        url = 'http://192.168.3.165:8018/fmis/wishPlatformRefund/selectWishRefundDetail'
        header = {'Content-Type': 'application/json',
                  'Authorization': '5df26666b185fbf0b3437482125d340e'}
        form = {"model":{"syncTime":"2021-09","accounts":["Bit by bit"],"sellers":[],"dataSource":2,"ids":[]},"current":1,"size":100}

        r = requests.post(url, headers=header, data=json.dumps(form))
        return r
    response = getRDPEmployees()
    # pprint.pprint(response.json())
    s = Assert_Api(response).assert_total(1)
    print(s)
    pass