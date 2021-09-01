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
    def getApiInputParam(self,platform,searchType):
        if platform == "Amazon":
            return self.getAmazonApiInputParam(searchType)
        elif platform == "Smt":
            return self.getSmtApiInputParam(searchType)
        elif platform == "Ali":
            return self.getAliApiInputParam(searchType)
        elif platform == "Ebay":
            return self.getEbayApiInputParam(searchType)
        elif platform == "Shopee":
            return self.getShopeeApiInputParam(searchType)
        else:
            return ""

    # 获取Amazon平台入参
    def getAmazonApiInputParam(self,searchType):
        otherTypeListing03 = ""
        otherTypeListing02 = ""
        otherTypeListing01 = ""
        if searchType == "bestsellerMark_query":  # bestseller页面
            otherTypeListing03 = DasApiInputParam.amazon_bestsellersListing03
            otherTypeListing02 = DasApiInputParam.amazon_bestsellersListing02
            otherTypeListing01 = DasApiInputParam.amazon_bestsellersListing01
        elif searchType == "newReleasesMark_query":  # newReleases页面
            otherTypeListing03 = DasApiInputParam.amazon_NewReleaseListing03
            otherTypeListing02 = DasApiInputParam.amazon_NewReleaseListing02
            otherTypeListing01 = DasApiInputParam.amazon_NewReleaseListing01
        elif searchType == "moverShakerMark_query":  # moversShakers页面
            otherTypeListing03 = DasApiInputParam.amazon_MoversShakersListing03
            otherTypeListing02 = DasApiInputParam.amazon_MoversShakersListing02
            otherTypeListing01 = DasApiInputParam.amazon_MoversShakersListing01
        elif searchType == "mostWishMark_query":  # MostWishedFor页面
            otherTypeListing03 = DasApiInputParam.amazon_MostWishedForListing03
            otherTypeListing02 = DasApiInputParam.amazon_MostWishedForListing02
            otherTypeListing01 = DasApiInputParam.amazon_MostWishedForListing01
        elif searchType == "giftIdeasMark_query":  # Giftldeas页面
            otherTypeListing03 = DasApiInputParam.amazon_GiftldeasListing03
            otherTypeListing02 = DasApiInputParam.amazon_GiftldeasListing02
            otherTypeListing01 = DasApiInputParam.amazon_GiftldeasListing01
        elif searchType == "shopMark_query":  # 关注店铺数据页面
            otherTypeListing03 = DasApiInputParam.amazon_attentStoreListing03
            otherTypeListing02 = DasApiInputParam.amazon_attentStoreListing02
            otherTypeListing01 = DasApiInputParam.amazon_attentStoreListing01
        elif searchType == "categoryMark_query":  # 关注分类数据页面
            otherTypeListing03 = DasApiInputParam.amazon_categoryListing03
            otherTypeListing02 = DasApiInputParam.amazon_categoryListing02
            otherTypeListing01 = DasApiInputParam.amazon_categoryListing01
        elif searchType == "keywordMark_query":  # 关注关键词数据页面
            otherTypeListing03 = DasApiInputParam.amazon_keywordsListing03
            otherTypeListing02 = DasApiInputParam.amazon_keywordsListing02
            otherTypeListing01 = DasApiInputParam.amazon_keywordsListing01
        elif searchType == "jungleScoutKeywordMark_query":  # JungleScout关键词数据页面
            otherTypeListing03 = DasApiInputParam.amazon_jungleScoutListing03
            otherTypeListing02 = DasApiInputParam.amazon_jungleScoutListing02
            otherTypeListing01 = DasApiInputParam.amazon_jungleScoutListing01
        return otherTypeListing03, otherTypeListing02, otherTypeListing01

    # 获取SMT平台入参
    def getSmtApiInputParam(self,searchType):
        otherTypeListing03 = ""
        otherTypeListing02 = ""
        otherTypeListing01 = ""
        if searchType == "categoryMark_query":# 数据采集-SMTorder大于100查询页面
            otherTypeListing03 = DasApiInputParam.smt_categoryMarkListing03
            otherTypeListing02 = DasApiInputParam.smt_categoryMarkListing02
            otherTypeListing01 = DasApiInputParam.smt_categoryMarkListing01
        elif searchType == "bestsellerMark_query":# 数据采集-SMTtopselling查询页面
            otherTypeListing03 = DasApiInputParam.smt_bestsellerMarkListing03
            otherTypeListing02 = DasApiInputParam.smt_bestsellerMarkListing02
            otherTypeListing01 = DasApiInputParam.smt_bestsellerMarkListing01
        elif searchType == "shopMark_query":# 数据采集SMT关注店铺数据查询页面
            otherTypeListing03 = DasApiInputParam.smt_shopMarkListing03
            otherTypeListing02 = DasApiInputParam.smt_shopMarkListing02
            otherTypeListing01 = DasApiInputParam.smt_shopMarkListing01
        elif searchType == "attentionCategoryMark_query":# 数据采集SMT关注分类数据查询页面
            otherTypeListing03 = DasApiInputParam.smt_attentionCategoryMarkListing03
            otherTypeListing02 = DasApiInputParam.smt_attentionCategoryMarkListing02
            otherTypeListing01 = DasApiInputParam.smt_attentionCategoryMarkListing01
        elif searchType == "keywordMark_query":# 数据采集SMT关注关键词数据查询页面
            otherTypeListing03 = DasApiInputParam.smt_keywordMarkListing03
            otherTypeListing02 = DasApiInputParam.smt_keywordMarkListing02
            otherTypeListing01 = DasApiInputParam.smt_keywordMarkListing01
        return otherTypeListing03, otherTypeListing02, otherTypeListing01

    # 获取1688平台入参
    def getAliApiInputParam(self, searchType):
        otherTypeListing03 = ""
        otherTypeListing02 = ""
        otherTypeListing01 = ""
        if searchType == "categoryMark_query":  # 数据采集-1688分类数据页面查询
            otherTypeListing03 = DasApiInputParam.ali_categoryMarkListing03
            otherTypeListing02 = DasApiInputParam.ali_categoryMarkListing02
            otherTypeListing01 = DasApiInputParam.ali_categoryMarkListing01
        elif searchType == "shopMark_query":# 数据采集-1688关注店铺数据页面查询
            otherTypeListing03 = DasApiInputParam.ali_shopMarkListing03
            otherTypeListing02 = DasApiInputParam.ali_shopMarkListing02
            otherTypeListing01 = DasApiInputParam.ali_shopMarkListing01
        elif searchType == "attentionCategoryMark_query":# 数据采集-1688关注分类数据页面查询
            otherTypeListing03 = DasApiInputParam.ali_attentionCategoryMarkListing03
            otherTypeListing02 = DasApiInputParam.ali_attentionCategoryMarkListing02
            otherTypeListing01 = DasApiInputParam.ali_attentionCategoryMarkListing01
        elif searchType == "keywordMark_query":# 数据采集-1688关注关键词数据页面查询
            otherTypeListing03 = DasApiInputParam.ali_keywordMarkListing03
            otherTypeListing02 = DasApiInputParam.ali_keywordMarkListing02
            otherTypeListing01 = DasApiInputParam.ali_keywordMarkListing01
        elif searchType == "shopTopOneMark_query":# 数据采集-1688镇店之宝页面查询
            otherTypeListing03 = DasApiInputParam.ali_shopMarkListing03
            otherTypeListing02 = DasApiInputParam.ali_shopMarkListing02
            otherTypeListing01 = DasApiInputParam.ali_shopMarkListing01
        return otherTypeListing03, otherTypeListing02, otherTypeListing01

    # 获取ebay平台入参
    def getEbayApiInputParam(self,searchType):
        otherTypeListing03 = ""
        otherTypeListing02 = ""
        otherTypeListing01 = ""
        if searchType == "": # 自定义采集-ebay页面查询
            otherTypeListing03 = DasApiInputParam.ebay_followMarkListing03
            otherTypeListing02 = DasApiInputParam.ebay_followMarkListing02
            otherTypeListing01 = DasApiInputParam.ebay_followMarkListing01
        elif searchType == "": # 数据采集-ebay页面查询
            otherTypeListing03 = DasApiInputParam.ebay_categoryMarkListing03
            otherTypeListing02 = DasApiInputParam.ebay_categoryMarkListing02
            otherTypeListing01 = DasApiInputParam.ebay_categoryMarkListing01
        return otherTypeListing03, otherTypeListing02, otherTypeListing01

    # 获取shopee平台入参
    def getShopeeApiInputParam(self,searchType):
        otherTypeListing03 = ""
        otherTypeListing02 = ""
        otherTypeListing01 = ""
        return otherTypeListing03, otherTypeListing02, otherTypeListing01

    # 获取请求地址
    def getApiUrl(self,platform,searchType):
        if platform == "Amazon":
            return self.getAmazonApiUrl(searchType)
        elif platform == "Smt":
            return self.getSmtApiUrl(searchType)
        elif platform == "Ali":
            return self.getAliApiUrl(searchType)
        elif platform == "Ebay":
            return self.getEbayApiUrl(searchType)
        elif platform == "Shopee":
            return self.getShopeeApiUrl(searchType)
        else:
            return ""

    # 获取Amazon平台的url
    def getAmazonApiUrl(self,searchType):
        url = ""
        if searchType == "bestsellerMark_query":  # bestseller查询页面
            url = DasApiUrl.amazon_dataSampleListing_url
        elif searchType == "newReleasesMark_query":  # newReleases查询页面
            url = DasApiUrl.amazon_dataSampleListing_url
        elif searchType == "moverShakerMark_query":  # moversShakers查询页面
            url = DasApiUrl.amazon_dataSampleListing_url
        elif searchType == "mostWishMark_query":  # MostWishedFor查询页面
            url = DasApiUrl.amazon_dataSampleListing_url
        elif searchType == "giftIdeasMark_query":  # Giftldeas查询页面
            url = DasApiUrl.amazon_dataSampleListing_url
        elif searchType == "shopMark_query":  # 关注店铺数据查询页面
            url = DasApiUrl.amazon_attentStoreListing_url
        elif searchType == "categoryMark_query":  # 关注分类数据查询页面
            url = DasApiUrl.amazon_attentStoreListing_url
        elif searchType == "keywordMark_query":  # 关注关键词数据查询页面
            url = DasApiUrl.amazon_attentStoreListing_url
        elif searchType == "jungleScoutKeywordMark_query":  # JungleScout关键词数据查询页面
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
        elif searchType == "categoryMark_query": # 数据采集-SMTorder大于100查询页面
            url = DasApiUrl.smt_dataSampleListing_url
        elif searchType == "bestsellerMark_query": # 数据采集-SMTtopselling查询页面
            url = DasApiUrl.smt_dataSampleListing_url
        elif searchType == "shopMark_query": # 数据采集SMT关注店铺数据查询页面
            url = DasApiUrl.smt_dataSampleListing_url
        elif searchType == "attentionCategoryMark_query": # 数据采集SMT关注分类数据查询页面
            url = DasApiUrl.smt_dataSampleListing_url
        elif searchType == "keywordMark_query": # 数据采集SMT关注关键词数据查询页面
            url = DasApiUrl.smt_dataSampleListing_url
        return url
    # 获取1688平台的URL
    def getAliApiUrl(self,searchType):
        url = ""
        if searchType == "ali_claimProduct": # 1688认领产品接口
            url = DasApiUrl.ali_claimProduct_url
        elif searchType == "categoryMark_query": # 数据采集-1688分类数据页面查询
            url = DasApiUrl.ali_dataSampleListing_url
        elif searchType == "shopMark_query":# 数据采集-1688关注店铺数据页面查询
            url = DasApiUrl.ali_dataSampleListing_url
        elif searchType == "attentionCategoryMark_query":# 数据采集-1688关注分类数据页面查询
            url = DasApiUrl.ali_dataSampleListing_url
        elif searchType == "keywordMark_query":# 数据采集-1688关注关键词数据页面查询
            url = DasApiUrl.ali_dataSampleListing_url
        elif searchType == "shopTopOneMark_query":# 数据采集-1688镇店之宝页面查询
            url = DasApiUrl.ali_dataSampleListing_url
        return url

    # 获取ebay平台的URL
    def getEbayApiUrl(self,searchType):
        url = ""
        if searchType == "ebay_claimProduct":  # ebay认领产品接口
            url = DasApiUrl.ebay_claimProduct_url
        elif searchType == "": # 自定义采集-ebay页面查询
            url = DasApiUrl.ebay_dataSampleListing_url
        elif searchType == "": # 数据采集-ebay页面查询
            url = DasApiUrl.ebay_dataSampleListing_url
        return url
    # 获取shopee平台URL
    def getShopeeApiUrl(self,searchType):
        url = ""
        if searchType == "shopee_claimProduct":  # shopee认领产品接口
            url = DasApiUrl.shopee_claimProduct_url
        return url

    # 判断哪个页面的数据需要对入参进行判空
    def needJudgeEmpty(self,platform,searchType):
        if platform == "Amazon":
            return self.amazonNeedJudgeEmpty(searchType)
        elif platform == "Smt":
            return self.smtNeedJudgeEmpty(searchType)
        elif platform == "Ali":
            return self.aliNeedJudgeEmpty(searchType)
        elif platform == "Ebay":
            return self.ebayNeedJudgeEmpty(searchType)
        elif platform == "Shopee":
            return self.shopeeNeedJudgeEmpty(searchType)
        else:
            return ""

    # 判断Amazon平台哪些页面需要对入参判空
    def amazonNeedJudgeEmpty(self,searchType):
        if searchType == "bestsellerMark_query":
            return True
        elif searchType == "newReleasesMark_query":
            return True
        elif searchType == "moverShakerMark_query":
            return True
        elif searchType == "mostWishMark_query":
            return True
        elif searchType == "giftIdeasMark_query":
            return True
        else:
            return False

    # 判断SMT平台哪些页面需要对入参判空
    def smtNeedJudgeEmpty(self,searchType):
        pass

    # 判断1688平台哪些页面需要对入参判空
    def aliNeedJudgeEmpty(self,searchType):
        pass

    # 判断ebay平台哪些页面需要对入参判空
    def ebayNeedJudgeEmpty(self,searchType):
        pass

    # 判断shopee平台哪些页面需要对入参判空
    def shopeeNeedJudgeEmpty(self,searchType):
        pass