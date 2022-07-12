'''
@File: test_getEnrollDateBySkusApi.py
@time:2022/7/11
@Author:quanliu 181324
@Desc:查询最近七天的sku信息
'''

import unittest
from apps.AllSystemData.ProductSystem.product_api.provideSaleApi.getEnrollDateBySkusApi import getEnrollDateBySkusApi


class Test_getEnrollDateBySkusApi(unittest.TestCase):
    def testCase01(self):
        '''查询最近七天的sku信息'''
        responseResult01 = getEnrollDateBySkusApi()
        print(responseResult01)


if __name__ == '__main__':
    unittest.main()