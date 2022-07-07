# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File:saleSystem_interface_url.py(请求URL) saleSystem_interface_param.py(入参)
 salePlatformOrderQueryApi.py(入参拼接) test_salePlatformOrderQueryApi.py(设置断言)
@time:2022/7/4
@Author:lu 10338
@Desc: 销售系统-平台订单查询接口
'''
import unittest
import ddt
from apps.AllSystemData.SaleSystem.sale_common_setting import Sale_Common_Setting
from apps.utils.mySql_database_util import Mysql_handleOperator
from apps.AllSystemData.SaleSystem.sale_api.platOrder.salePlatformOrderQueryApi import salePlatformOrderApi

@ddt.ddt
class Test_salePlatformOrderQueryApi(unittest.TestCase):
    def testCase01(self):
        # api返回json结果提取
        api_retest = salePlatformOrderApi("accountNumber", "13009005919@163.com")  # 查询店铺账号——13009005919@163.com SMT平台订单
        api_reCode = api_retest[0]
        api_reJsonValue = api_retest[1]["total"]

        # 预期达到的结果
        expected_resultsCode = 200
        sql = "select count(id) from aliexpress_order where account_number = '13009005919@163.com';"
        expected_resultsValue = Mysql_handleOperator(Sale_Common_Setting.sale_mysql).data_sql("select", sql)

        # 将预期结果和api结果返回——方便进行下一步比较
        api_test = [api_reCode, api_reJsonValue]  # 接口返回的code码以及‘total’字段的值
        expected_test = [expected_resultsCode, expected_resultsValue]  # 预期返回200以及数据库查询到的总计条数
        print("\napi返回结果：", api_test, "\n预期结果:", expected_test)
        return api_test, expected_test

    def testCase02(self):
        # api返回json结果提取
        api_retest = salePlatformOrderApi("orderStatus","WAIT_SELLER_SEND_GOODS") # 查询订单状态——等待您发货 SMT平台订单
        api_reCode = api_retest[0]
        api_reJsonValue = api_retest[1]["total"]

        # 预期达到的结果
        expected_resultsCode = 200
        sql = "select count(id) from aliexpress_order where order_status = 'WAIT_SELLER_SEND_GOODS';"
        expected_resultsValue = Mysql_handleOperator(Sale_Common_Setting.sale_mysql).data_sql("select", sql)

        # 将预期结果和api结果返回——方便进行下一步比较
        api_test = [api_reCode,api_reJsonValue] # 接口返回的code码以及‘total’字段的值
        expected_test = [expected_resultsCode,expected_resultsValue] # 预期返回200以及数据库查询到的总计条数
        print("\napi返回结果：",api_test,"\n预期结果:",expected_test)
        return api_test,expected_test

    def testCase03(self):
        # api返回json结果提取
        api_retest = salePlatformOrderApi("orderId", "5030256190081355")  # 查询平台单号——5030256190081355 SMT平台订单
        api_reCode = api_retest[0]
        api_reJsonValue = api_retest[1]["total"]

        # 预期达到的结果
        expected_resultsCode = 200
        sql = "select count(id) from aliexpress_order where order_id = '5030256190081355';"
        expected_resultsValue = Mysql_handleOperator(Sale_Common_Setting.sale_mysql).data_sql("select", sql)

        # 将预期结果和api结果返回——方便进行下一步比较
        api_test = [api_reCode, api_reJsonValue]  # 接口返回的code码以及‘total’字段的值
        expected_test = [expected_resultsCode, expected_resultsValue]  # 预期返回200以及数据库查询到的总计条数
        print("\napi返回结果：", api_test, "\n预期结果:", expected_test)
        return api_test, expected_test


if __name__ == '__main__':
    unittest.main(verbosity=2)



