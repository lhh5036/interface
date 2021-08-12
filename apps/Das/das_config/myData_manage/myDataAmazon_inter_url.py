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