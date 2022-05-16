# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: assert_utils
@time:2021/10/7
@Author:majiaqin 170479
@Desc:全局断言工具类,供各系统的assert_file调用
'''

import unittest
import requests
import json
import pprint

from deepdiff import DeepDiff, DeepSearch
from apps.logger import MyLog
from apps.utils.mySql_database_util import Mysql_handleOperator
from apps.AllSystemData.FmisSystem.fmis_common_settting import Fmis_Common_Setting
from apps.utils.currency_utils import Json_Get

# 实例化日志类
logger = MyLog("AssertUtils").getlog()

class Assert_Api(unittest.TestCase):
    '''获取返回数据供所有方法调用'''
    # 初始化父类
    def __init__(self):
        super().__init__()

    '''断言返回数据状态码'''
    def assert_statucode(self, response_code):
        self.response_code = response_code
        try:
            self.assertEqual(200, self.response_code)
            print(self.assertEqual(200, self.response_code))
            logger.info("Assert statu_code ---> success!")
            return "True"
        except AssertionError:
            logger.error("Assert statu_code ---> fail!")
            logger.error("接口报错，statu_code：{0}".format(self.response_code))
            return "False"

    '''断言接口是否成功连接'''
    def assert_connect(self, response_code, response_msg):
        self.response_code = response_code
        self.response_msg = response_msg
        try:
            self.assertIn("connectionRefused", self.response_msg)
            self.assertIn("success", self.response_msg)
            self.assertIn("errorMsg", self.response_msg)
            logger.info("Api have response data!")
            try:
                self.assertEqual(False, self.response_msg["connectionRefused"])
                self.assertEqual(True, self.response_msg["success"])
                self.assertEqual(None, self.response_msg["errorMsg"])
                logger.info("Api connect success!")
                return "True"
            except AssertionError:
                logger.error("Api connect fail!")
                msg = "接口连接失败,connectionRefused的值为{0} \n success的值为{1} \n\
errorMsg的的值为{2}".format(self.response_msg["connectionRefused"],
                        self.response_msg["success"],
                        self.response_msg["errorMsg"])
                logger.error(msg)
                return "False"
        except AssertionError:
            logger.error("Api response fail!")
            logger.error("接口报错，statu_code：{0}".format(self.response_code))
            return "False"

    '''断言接口返回数据条目数是否正确'''
    def assert_total(self, response_msg, sql):
        self.response_msg = response_msg
        # 查询数据条目数的sql
        self.sql = sql
        message = Json_Get(self.response_msg).json_get("total")
        if message == "True":
            logger.info("Api response data have total!")
            sql_total = Mysql_handleOperator(Fmis_Common_Setting.fmis_mysql).data_sql("select", self.sql)[0][0]
            try:
                self.assertEqual(sql_total, Json_Get(self.response_msg).json_value("total"))
                logger.info(" The number of returned api data is correct!")
                return "True"
            except AssertionError:
                logger.error("Return api data total error")
                return "False"
        else:
            logger.error("Api response data not have total!")
            return "False"

    '''
    断言返回数据是否正确
    (method_type为deepsearch校验json中的某个对象
    为deepdiff校验整个json)
    respon_data为返回数据的处理，需要处理为与check_data格式一致
    check_data为数据库/其他数据源解析的数据
    use_regexp当=True时可用正则表达式
    当=False则不可用正则表达式
    strict_checking当=True检查要匹配的对象的类型,比如'1234'!=1234
    当=False则忽略匹配对象的类型,比如'1234'=1234
    case_sensitive当=True区分大小写
    当=False则忽略大小写
    ignore_string_case当=True则可以不区分String大小写 
    当=False则属于大小写敏感
    '''
    @classmethod
    def assert_data(cls, respon_data, check_data,
                    method_type='deepsearch',
                    use_regexp=True,
                    strict_checking=False,
                    case_sensitive=True,
                    ignore_string_case=False):
        if method_type == 'deepsearch':
            if type(check_data) == list:
                assert_list = []
                for dat in check_data:
                    assert_msg = DeepSearch(respon_data, dat,
                                            use_regexp=use_regexp,
                                            strict_checking=strict_checking,
                                            case_sensitive=case_sensitive)
                    msg_dat = cls().deep_search_assert(assert_msg)
                    assert_list.append(msg_dat)
                if 'False' in assert_list:
                    return 'False'
                else:
                    return 'True'
            elif type(check_data) == dict:
                assert_list = []
                for dat in check_data.keys():
                    assert_msg = DeepSearch(respon_data, check_data[dat],
                                            use_regexp=use_regexp,
                                            strict_checking=strict_checking,
                                            case_sensitive=case_sensitive)
                    msg_dat = cls().deep_search_assert(assert_msg)
                    assert_list.append(msg_dat)
                if 'False' in assert_list:
                    return 'False'
                else:
                    return 'True'

        elif method_type == 'deepdiff':
            assert_msg = DeepDiff(respon_data, check_data,
                                  view='text',
                                  ignore_string_case=ignore_string_case)
            if len(assert_msg) == 0:
                logger.info("Api response data is true")
                return "True"
            else:
                logger.error("Api response data is false")
                return "False"

    def deep_search_assert(self, assert_msg):
        self.assert_msg = assert_msg
        try:
            if len(assert_msg['matched_values']) > 0:
                logger.info("Api response data is true")
                return "True"
            elif len(assert_msg['matched_values']) == 0:
                logger.error("Api response data is false")
                return "False"
        except KeyError:
            logger.error("Api response data is false")
            return "False"

if __name__ == '__main__':
    def getRDPEmployees():
        url = 'http://192.168.3.165:8018/fmis/wishPlatformRefund/selectWishRefundDetail'
        header = {'Content-Type': 'application/json',
                  'Authorization': '5df26666b185fbf0b3437482125d340e'}
        form = {"model": {"syncTime": "2021-09",
                          "accounts": ["Bit by bit"],
                          "sellers": [], "dataSource": 2,
                          "ids": []}, "current": 1, "size": 100}

        r = requests.post(url, headers=header, data=json.dumps(form))
        return r
    response = getRDPEmployees()
    pprint.pprint(response.json())
    # s = Assert_Api(response).assert_data(1)
    # print(s)
    pass