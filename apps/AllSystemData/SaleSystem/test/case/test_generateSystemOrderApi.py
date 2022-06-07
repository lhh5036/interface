'''
@File: test_generateSystemOrderApi.py
@time:2022/6/7
@Author:quanliu 181324
@Desc:生成系统订单
'''
from apps.AllSystemData.SaleSystem.sale_api.platSystemOrder.generateSystemOrderApi import generateSystemOrderApi
import unittest
import ddt
from apps.AllSystemData.SaleSystem.sale_common_setting import Sale_Common_Setting
from apps.utils.mySql_database_util import controlDatebase

platformList = ["Amazon","SMT","Ebay","Wish","Joom","Shopee","Lazada","Shopify","NewEgg","Walmart","Allegro","Mercadolibre","Cdiscount","Fruugo","B2W","Fanno","Coupang","Ozon"]
# 平台的SQL
select_sql_dict ={
    "Amazon":"select amazon_order_id,id FROM amazon_order where is_push_complete = b'0' and order_status = 'Unshipped' order by purchase_date desc LIMIT 1;",
    "SMT":"select order_id,id FROM aliexpress_order where is_push_complete = b'0' and order_status = 'WAIT_SELLER_SEND_GOODS' order by gmt_create desc LIMIT 1;",
    "Ebay":"select order_id,id FROM ebay_order where is_push_complete = b'0' and custom_order_status = 'WaitShipment' order by create_time desc LIMIT 1;",
    "Wish":"select order_id,id FROM wish_order where is_push_complete = b'0' and order_status = 'APPROVED' order by order_time desc LIMIT 1;",
    "Joom":"select order_id,id FROM joom_order where is_push_complete = b'0' and order_status = 'APPROVED' order by order_time desc LIMIT 1;",
    "Shopee":"select order_id,id FROM shopee_order where is_push_complete = b'0' and order_status = 'READY_TO_SHIP' order by create_time desc LIMIT 1;",
    "Lazada":"select lo.order_id,lo.account_Number,lo.id from lazada_order lo left join lazada_order_item loi on lo.id = loi.lazada_order_id where lo.statuses = 'pending'and lo.is_pushed = b'0' and loi.status = 'pending' order by lo.created_at desc LIMIT 1;",
    "Shopify":"select order_id,id,order_number from shopify_order where is_push_complete = b'0' and order_status = 'Open' order by create_time desc LIMIT 1;",
    "NewEgg":"select order_number,id from newegg_order where is_push_complete = b'0' and order_status = 0 order by order_date desc LIMIT 1;",
    "Walmart":"select purchase_order_id,id from walmart_order where is_push_complete = b'0' and status = 'Created' order by order_date desc LIMIT 1;",
    "Allegro":"select order_id,id from allegro_order where is_push_complete = b'0' and status = 'READY_FOR_PROCESSING'and fulfillment_satus = 'NEW' order by payment_finishedAt desc LIMIT 1;",
    "Mercadolibre":"select order_id,id from mercadolibre_order where is_push_complete = b'0' and status = 'paid' order by date_created desc LIMIT 1;",
    "Cdiscount":"select id,order_number from cdiscount_order where is_push_complete = b'0' and status = 'Completed' and order_state = 'WaitingForShipmentAcceptation' order by creation_date desc LIMIT 1;",
    "Fruugo":"select id,order_id from fruugo_order where is_push_complete = b'0'  and order_status = 'PENDING' order by order_date desc LIMIT 1;",
    "B2W":"select id,order_id from b2w_order where  is_push_complete = b'0' and order_status = 'APPROVED' order by imported_at desc LIMIT 1;",
    "Fanno":"select id,order_id from fanno_order where  is_push_complete = b'0' and order_status = '111' order by create_time desc LIMIT 1;",
    "Coupang":"select order_id,id from coupang_order where  is_push_complete = b'0' and status = 'ACCEPT' order by ordered_at desc LIMIT 1;",
    "Microsoft":"",
    "Ozon":"select id,order_id from ozon_order where  is_push_complete = b'0' and status = 'awaiting_packaging' order by created_date desc LIMIT 1;",
    "JDwalmart":""
}

# 系统订单查询
@ddt.ddt
class Test_generateSystemOrderApi(unittest.TestCase):
    # 获取每个平台的查询sql
    @controlDatebase(Sale_Common_Setting.sale_mysql)
    def getPlatformSql(self,platform):
        resultInfo = select_sql_dict[platform]
        return resultInfo

    @ddt.data(*platformList)
    def testCase01(self,saleChannelStr):
        '''生成系统订单-{0}'''.format(saleChannelStr)
        result_data = self.getPlatformSql(saleChannelStr)
        if len(result_data) <= 0:
            return "平台:{0},没有需要生成系统订单的平台订单数据".format(saleChannelStr)
        saleChannelOrderId = result_data[0][0] # 平台订单ID
        accountNumber = result_data[0][1] # 账号
        responseResult01 = generateSystemOrderApi(saleChannelStr,saleChannelOrderId,accountNumber)
        print(responseResult01)

if __name__ == '__main__':
    unittest.main(verbosity=2)