# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File:
@time:2022/7/4
@Author:lu 10338
@Desc: 销售系统-平台订单查询接口
'''
import unittest
import ddt
from apps.AllSystemData.SaleSystem.sale_common_setting import Sale_Common_Setting
from apps.utils.mySql_database_util import controlDatebase
from apps.AllSystemData.SaleSystem.sale_api.platOrder.salePlatformOrderQueryApi import salePlatformOrderApi

@ddt.ddt
class Test_salePlatformOrderQueryApi(unittest.TestCase):
    @controlDatebase(Sale_Common_Setting.sale_mysql)
    def getSMTPlatformOrderCountNumer(self):
        # 预期达到的结果
        expected_resultsCode = 200
        expected_resultsValue = "select count(id) from aliexpress_order where order_status = 'WAIT_SELLER_SEND_GOODS';"

        # api返回json结果提取
        api_retest = salePlatformOrderApi("WAIT_SELLER_SEND_GOODS")
        api_reCode = api_retest[0]
        api_reJsonValue = api_retest[1]["total"]

        api_test = [api_reCode,api_reJsonValue] # 接口返回的code码以及对应字段的值
        expected_test = [expected_resultsCode,expected_resultsValue] # 预期返回200以及数据库查询到的数据
        print(api_test,expected_test)
        return api_test,expected_test

if __name__ == '__main__':
    unittest.main(verbosity=2)



