'''
@File: test_productSingleItemSelectApi.py
@time:2022/6/8
@Author:quanliu 181324
@Desc:管理单品查询用例
'''
import unittest
from apps.AllSystemData.ProductSystem.product_api.productDataCenter.productSingleItemSelectApi import \
    productSingleItemSelectApi


class Test_productSingleItemSelectApi(unittest.TestCase):

    def testCase01(self):
        '''管理单品查询用例-无参数'''
        responseResult01 = productSingleItemSelectApi({})
        print(responseResult01)

    def testCase02(self):
        '''管理单品查询用例-有参数'''
        responseResult02 = productSingleItemSelectApi({"itemStatus":[7009]})
        print(responseResult02)


if __name__ == '__main__':
    unittest.main()