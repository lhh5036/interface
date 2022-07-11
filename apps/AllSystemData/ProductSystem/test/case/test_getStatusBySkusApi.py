'''
@File: test_getStatusBySkusApi.py
@time:2022/7/11
@Author:quanliu 181324
@Desc:查询多个货号对应状态
'''

import unittest
from apps.AllSystemData.ProductSystem.product_api.provideSaleApi.getStatusBySkusApi import getStatusBySkusApi
from apps.AllSystemData.ProductSystem.test.moduleFile.test_getStatusBySkus_data import getSkus


class Test_getStatusBySkusApi(unittest.TestCase):

    def testCase01(self):
        '''询多个货号对应状态'''
        # 获取多个货号
        skuList = getSkus()
        responseResult01 = getStatusBySkusApi(skuList)
        print(responseResult01)


    def testCase02(self):
        '''询多个货号对应状态(不传参数)'''
        # 获取多个货号
        skuList = []
        responseResult02 = getStatusBySkusApi(skuList)
        print(responseResult02)


if __name__ == '__main__':
    unittest.main()