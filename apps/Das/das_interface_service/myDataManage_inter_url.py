'''
@File: myDataManage_inter_url.py
@time:2021/8/5
@Author:quanliu 181324
@Desc:数据管理页面接口地址
'''
from apps.Common_Config.interface_common_info import InterfaceCommonInfo


class MyDataManageInterUrl:

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

    # 我的数据-SMT查询接口
    querySmtListing_url = InterfaceCommonInfo.common_url + "/das/smt/AccountProductInfo/querySmtPageList"

    # 我的数据-SMT释放产品接口
    smt_releaseProduct_url = InterfaceCommonInfo.common_url + "/das/smt/AccountProductInfo/releaseProduct"

    # 我的数据-SMT关联系统SKU接口
    smt_associateSySku_url = InterfaceCommonInfo.common_url + "/das/smt/AccountProductInfo/associatedSystemSku"