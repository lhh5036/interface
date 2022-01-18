'''
@File: sale_publicCommonUrlService.py
@time:2022/1/18
@Author:quanliu 181324
@Desc:接口处理
'''
from apps.SaleSystem.sale_interface_service.saleSystem_interface_url import SaleApiUrl


class SalePublicCommonUrlServiceClass():
    # 获取请求地址
    def getApiUrl(self, platform,searchType):
        if platform == "Amazon":
            return getAmazonApiUrl(searchType)
        elif platform == "SMT":
            return getSmtApiUrl(searchType)
        elif platform == "Ali":
            return getAliApiUrl()
        elif platform == "Ebay":
            return getEbayApiUrl()
        elif platform == "Shopee":
            return getShopeeApiUrl()
        else:
            return ""

def getAmazonApiUrl(searchType):
    amazon_url = ""
    if searchType == "listCustomerOrder":
        amazon_url = SaleApiUrl.systemOrder_queryListing_url
    else:
        pass
    return amazon_url


def getSmtApiUrl(searchType):
    smt_url = ""
    if searchType == "listCustomerOrder":
        smt_url = SaleApiUrl.systemOrder_queryListing_url
    else:
        pass
    return smt_url



def getAliApiUrl():
    pass
def getEbayApiUrl():
    pass
def getShopeeApiUrl():
    pass