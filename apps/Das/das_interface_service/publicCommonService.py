'''
@File: publicCommonService.py
@time:2021/8/31
@Author:quanliu
@Desc:存放数据分析系统公共方法
'''
from apps.Das.das_interface_service.dasSystem_interface_param import DasApiInputParam
from apps.Das.das_interface_service.dasSystem_interface_url import DasApiUrl


class PublicCommonServiceClass():
    # 根据类型获取每种类型的入参地址
    def getApiInputParam(self,searchType):
        otherTypeListing03 = ""
        otherTypeListing02 = ""
        otherTypeListing01 = ""
        if searchType == "bestsellerMark":  # bestseller页面
            otherTypeListing03 = DasApiInputParam.amazon_bestsellersListing03
            otherTypeListing02 = DasApiInputParam.amazon_bestsellersListing02
            otherTypeListing01 = DasApiInputParam.amazon_bestsellersListing01
        elif searchType == "newReleasesMark":  # newReleases页面
            otherTypeListing03 = DasApiInputParam.amazon_NewReleaseListing03
            otherTypeListing02 = DasApiInputParam.amazon_NewReleaseListing02
            otherTypeListing01 = DasApiInputParam.amazon_NewReleaseListing01
        elif searchType == "moverShakerMark":  # moversShakers页面
            otherTypeListing03 = DasApiInputParam.amazon_MoversShakersListing03
            otherTypeListing02 = DasApiInputParam.amazon_MoversShakersListing02
            otherTypeListing01 = DasApiInputParam.amazon_MoversShakersListing01
        elif searchType == "mostWishMark":  # MostWishedFor页面
            otherTypeListing03 = DasApiInputParam.amazon_MostWishedForListing03
            otherTypeListing02 = DasApiInputParam.amazon_MostWishedForListing02
            otherTypeListing01 = DasApiInputParam.amazon_MostWishedForListing01
        elif searchType == "giftIdeasMark":  # Giftldeas页面
            otherTypeListing03 = DasApiInputParam.amazon_GiftldeasListing03
            otherTypeListing02 = DasApiInputParam.amazon_GiftldeasListing02
            otherTypeListing01 = DasApiInputParam.amazon_GiftldeasListing01
        elif searchType == "shopMark":  # 关注店铺数据页面
            otherTypeListing03 = DasApiInputParam.amazon_attentStoreListing03
            otherTypeListing02 = DasApiInputParam.amazon_attentStoreListing02
            otherTypeListing01 = DasApiInputParam.amazon_attentStoreListing01
        elif searchType == "categoryMark":  # 关注分类数据页面
            otherTypeListing03 = DasApiInputParam.amazon_categoryListing03
            otherTypeListing02 = DasApiInputParam.amazon_categoryListing02
            otherTypeListing01 = DasApiInputParam.amazon_categoryListing01
        elif searchType == "keywordMark":  # 关注关键词数据页面
            otherTypeListing03 = DasApiInputParam.amazon_keywordsListing03
            otherTypeListing02 = DasApiInputParam.amazon_keywordsListing02
            otherTypeListing01 = DasApiInputParam.amazon_keywordsListing01
        elif searchType == "jungleScoutKeywordMark":  # JungleScout关键词数据页面
            otherTypeListing03 = DasApiInputParam.amazon_jungleScoutListing03
            otherTypeListing02 = DasApiInputParam.amazon_jungleScoutListing02
            otherTypeListing01 = DasApiInputParam.amazon_jungleScoutListing01
        return otherTypeListing03, otherTypeListing02, otherTypeListing01

    # 获取请求地址
    def getApiUrl(self,platform,searchType):
        if platform == "Amazon":
            return self.getAmazonApiUrl(searchType)
        elif platform == "SMT":
            return self.getSmtApiUrl(searchType)
        elif platform == "ali":
            return self.getAliApiUrl(searchType)
        elif platform == "ebay":
            return self.getEbayApiUrl(searchType)
        elif platform == "shopee":
            return self.getShopeeApiUrl(searchType)
        else:
            return ""



    # 获取Amazon平台的url
    def getAmazonApiUrl(self,searchType):
        url = ""
        if searchType == "bestsellerMark_query":  # bestseller查询页面
            url = DasApiUrl.amazon_dataSampleListing_url
        elif searchType == "newReleasesMark":  # newReleases查询页面
            url = DasApiUrl.amazon_dataSampleListing_url
        elif searchType == "moverShakerMark":  # moversShakers查询页面
            url = DasApiUrl.amazon_dataSampleListing_url
        elif searchType == "mostWishMark":  # MostWishedFor查询页面
            url = DasApiUrl.amazon_dataSampleListing_url
        elif searchType == "giftIdeasMark":  # Giftldeas查询页面
            url = DasApiUrl.amazon_dataSampleListing_url
        elif searchType == "shopMark":  # 关注店铺数据查询页面
            url = DasApiUrl.amazon_attentStoreListing_url
        elif searchType == "categoryMark":  # 关注分类数据查询页面
            url = DasApiUrl.amazon_attentStoreListing_url
        elif searchType == "keywordMark":  # 关注关键词数据查询页面
            url = DasApiUrl.amazon_attentStoreListing_url
        elif searchType == "jungleScoutKeywordMark":  # JungleScout关键词数据查询页面
            url = DasApiUrl.amazon_attentStoreListing_url
        elif searchType == "amazon_associateSystemSku": # Amazon关联系统SKU
            url = DasApiUrl.amazon_associateSySku_url
        elif searchType == "amazon_cancelDevelopment": # Amazon取消开发
            url = DasApiUrl.amazon_cancelDevelopment_url
        elif searchType == "amazon_releaseProduct": # Amazon释放产品
            url = DasApiUrl.amazon_releaseProduct_url
        elif searchType == "bestseller_allocation": # Amazon-bestsellers分配接口
            url = DasApiUrl.amazon_allocationProduct_url
        elif searchType == "amazon_checkProductByRank": # Amazon判断产品是否认领接口
            url = DasApiUrl.amazon_checkProductByRank_url
        elif searchType == "amazon_claimProduct": # Amazon认领产品接口
            url = DasApiUrl.amazon_claimProduct_url
        elif searchType == "amazon_deleteProduct": # Amazon删除产品接口
            url = DasApiUrl.amazon_deleteProduct_url
        elif searchType == "amazon_disableProduct": # Amazon禁用产品接口
            url = DasApiUrl.amazon_disableProduct_url
        elif searchType == "amazon_enableProduct": # Amazon启用产品接口
            url = DasApiUrl.amazon_enableProduct_url
        return url

    # 获取SMT平台的url
    def getSmtApiUrl(self,searchType):
        url = ""
        if searchType == "smt_associateSystemSku":  # SMT关联系统SKU
            url = DasApiUrl.smt_associateSySku_url
        elif searchType == "smt_infringementAudits": # SMT侵权审核接口
            url = DasApiUrl.smt_infringementAudit_url
        elif searchType == "smt_checkProductByRank": # SMT判断产品是否认领接口
            url = DasApiUrl.smt_checkProductByRank_url
        elif searchType == "smt_claimProduct" : # SMT认领产品接口
            url = DasApiUrl.smt_claimProduct_url
        return url
    # 获取1688平台的URL
    def getAliApiUrl(self,searchType):
        url = ""
        if searchType == "ali_claimProduct": # 1688认领产品接口
            url = DasApiUrl.ali_claimProduct_url
        return url

    # 获取ebay平台的URL
    def getEbayApiUrl(self,searchType):
        url = ""
        if searchType == "ebay_claimProduct":  # ebay认领产品接口
            url = DasApiUrl.ebay_claimProduct_url
        return url
    # 获取shopee平台URL
    def getShopeeApiUrl(self,searchType):
        url = ""
        if searchType == "shopee_claimProduct":  # shopee认领产品接口
            url = DasApiUrl.shopee_claimProduct_url
        return url

    # 判断哪个页面的数据需要对入参进行判空
    def needJudgeEmpty(searchType):
        if searchType == "bestsellerMark":
            return True
        elif searchType == "newReleasesMark":
            return True
        elif searchType == "moverShakerMark":
            return True
        elif searchType == "mostWishMark":
            return True
        elif searchType == "giftIdeasMark":
            return True
        else:
            return False