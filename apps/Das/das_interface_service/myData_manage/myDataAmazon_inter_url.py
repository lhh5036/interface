'''
@File: myDataAmazon_inter_url.py
@time:2021/8/5
@Author:quanliu 181324
@Desc:我的数据-Amazon页面接口地址
'''
from apps.Common_Config.interface_common_info import InterfaceCommonInfo


class MyDataAmazonInterUrl:

    # 我的数据-Amazon查询接口
    queryAmazonRankListing_url = InterfaceCommonInfo.common_url + "/das/amazon/AccountProductInfo"

    # 我的数据-Amazon释放产品接口
    releaseProductInfo_url = InterfaceCommonInfo.common_url + "/das/amazon/AccountProductInfo"


    # 我的数据-Amazon关联系统SKU接口
    associateSySku_url = InterfaceCommonInfo.common_url + "/das/amazon/AccountProductInfo/associatedSystemSku"

    # 我的数据-Amazon低价接口
    productGenDijia_url = InterfaceCommonInfo.common_url + "/das/ali/productGenDijia"

    # 我的数据-Amazon同款接口
    productGenTongkuan_url = InterfaceCommonInfo.common_url + "/das/ali/productGenTongkuan"