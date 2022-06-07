'''
@File: test_systemOrderSelectApi.py
@time:2022/6/7
@Author:quanliu 181324
@Desc:系统订单查询接口用例
'''
from apps.AllSystemData.SaleSystem.sale_api.platSystemOrder.systemOrderSelectApi import systemOrderQueryFun
import unittest
import ddt
import os

# 参数化
saleChannelList = ["Amazon","SMT"]
# 获取当前文件所在目录的上一级目录
upPath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# 系统订单查询
@ddt.ddt
class Test_systemOrderSelectApi(unittest.TestCase):
    @ddt.data(*saleChannelList)
    def testCase01(self,saleChannelStr):
        '''系统订单查询用例-{0}'''.format(saleChannelStr)
        responseResult01 = systemOrderQueryFun(saleChannelStr)
        print(responseResult01)

if __name__ == '__main__':
    unittest.main(verbosity=2)