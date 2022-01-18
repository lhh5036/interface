'''
@File: sale_publicCommonParamService.py
@time:2022/1/18
@Author:
@Desc:
'''
from apps.SaleSystem.sale_interface_service.saleSystem_interface_param import SaleApiInputParam


class SalePublicCommonParamServiceClass():
    # 根据类型获取每种类型的入参地址
    def getApiInputParam(self, platform, searchType):
        if platform == "Amazon":
            return getAmazonApiInputParam(searchType)
        elif platform == "SMT":
            return getSmtApiInputParam(searchType)
        elif platform == "Ali":
            return getAliApiInputParam(searchType)
        elif platform == "Ebay":
            return getEbayApiInputParam(searchType)
        elif platform == "Shopee":
            return getShopeeApiInputParam(searchType)
        else:
            return ""

# 获取Amazon平台入参
def getAmazonApiInputParam(searchType):
    otherTypeListing03 = ""
    otherTypeListing02 = ""
    otherTypeListing01 = ""
    if searchType == "listCustomerOrder":  # 系统订单查询页面
        otherTypeListing03 = SaleApiInputParam.systemOrder_query_param03
        otherTypeListing02 = SaleApiInputParam.systemOrder_query_param02
        otherTypeListing01 = SaleApiInputParam.systemOrder_query_param01
    else:
        pass

    return otherTypeListing03,otherTypeListing02,otherTypeListing01


def getSmtApiInputParam(searchType):
    otherTypeListing03 = ""
    otherTypeListing02 = ""
    otherTypeListing01 = ""
    if searchType == "listCustomerOrder":  # 系统订单查询页面
        otherTypeListing03 = SaleApiInputParam.systemOrder_query_param03
        otherTypeListing02 = SaleApiInputParam.systemOrder_query_param02
        otherTypeListing01 = SaleApiInputParam.systemOrder_query_param01
    else:
        pass

    return otherTypeListing03, otherTypeListing02, otherTypeListing01

def getAliApiInputParam(searchType):
    pass
def getEbayApiInputParam(searchType):
    pass
def getShopeeApiInputParam(searchType):
    pass