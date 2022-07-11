'''
@File: test_getStatusBySkus_data.py
@time:2022/7/11
@Author:quanliu 181324
@Desc: 根据多个货号获取状态
'''
from apps.AllSystemData.ProductSystem.product_common_settting import Product_Common_Setting
from apps.utils.mySql_database_util import convert_list, get_data


# 获取多个货号
@convert_list
@get_data(Product_Common_Setting.product_mysql)
def getSkus():
    sql = "select son_sku from single_item where son_sku is not null  and son_sku !='' order by create_at desc limit 2"
    return sql


if __name__ == '__main__':
    print(getSkus())