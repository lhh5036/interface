'''
@File: sale_publicCommonParamService.py
@time:2022/1/18
@Author:
@Desc:
'''


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


    return otherTypeListing03,otherTypeListing02,otherTypeListing01


def getSmtApiInputParam(searchType):
    otherTypeListing03 = ""
    otherTypeListing02 = ""
    otherTypeListing01 = ""

    return otherTypeListing03, otherTypeListing02, otherTypeListing01

def getAliApiInputParam(searchType):
    pass



def getEbayApiInputParam(searchType):
    otherTypeListing03 = ""
    otherTypeListing02 = ""
    otherTypeListing01 = ""

    return otherTypeListing03, otherTypeListing02, otherTypeListing01



def getShopeeApiInputParam(searchType):
    pass