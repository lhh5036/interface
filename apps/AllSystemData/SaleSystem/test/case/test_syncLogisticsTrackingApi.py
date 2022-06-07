'''
@File: test_syncLogisticsTrackingApi.py
@time:2022/6/7
@Author:quanliu 181324
@Desc:同步追踪号
'''
from apps.AllSystemData.SaleSystem.sale_api.platSystemOrder.syncLogisticsTrackingApi import syncLogisticsTrackingFunc
import unittest
import ddt
import os
from apps.AllSystemData.SaleSystem.sale_common_setting import Sale_Common_Setting
from apps.utils.mySql_database_util import controlDatebase


# 参数化
saleChannelList = ["Amazon","SMT"]
# 获取当前文件所在目录的上一级目录
upPath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# 系统订单查询
@ddt.ddt
class Test_syncLogisticsTrackingApi(unittest.TestCase):

    # 获取各个平台的追踪号
    @controlDatebase(Sale_Common_Setting.sale_mysql)
    def getPlatLogisticsTracking(self):
        select_sql_list = []
        for saleChannel in saleChannelList:
            # 查询每个平台符合同步追踪号的单
            select_tracking_sql = "select sale_channel,yst from customer_order where order_status = '2' " \
                              "and yst is not NULL and exception_status = '15'and order_type is NULL and logistics_status = 0 " \
                              "and sale_channel = '{0}' order by created_date desc LIMIT 1".format(saleChannel)
            select_sql_list.append(select_tracking_sql)
        return select_sql_list

    @ddt.data(*saleChannelList)
    def testCase01(self,saleChannelStr):
        '''系统订单同步追踪号-{0}'''.format(saleChannelStr)
        result_list = self.getPlatLogisticsTracking()
        if len(result_list) <= 0:
            return
        orderYstList = []
        for one_result in result_list:
            saleChannel = one_result[0][0] # 渠道
            orderYst = one_result[0][1] # YST追踪号
            orderYstList.append(orderYst)
            responseResult01 = syncLogisticsTrackingFunc(saleChannel,orderYstList)
            print(responseResult01)

if __name__ == '__main__':
    unittest.main(verbosity=2)