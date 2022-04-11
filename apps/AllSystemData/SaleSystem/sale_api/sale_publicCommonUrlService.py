'''
@File: sale_publicCommonUrlService.py
@time:2022/1/18
@Author:quanliu 181324
@Desc:接口处理
'''


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
            return getEbayApiUrl(searchType)
        elif platform == "Shopee":
            return getShopeeApiUrl()
        else:
            return ""

def getAmazonApiUrl(searchType):
    amazon_url = ""

    return amazon_url


def getSmtApiUrl(searchType):
    smt_url = ""

    return smt_url



def getAliApiUrl():
    pass
def getEbayApiUrl(searchType):
    ebay_url = ""

    return ebay_url
def getShopeeApiUrl():
    pass
