'''
@File: publicCommonParamService.py
@time:2021/8/31
@Author:quanliu
@Desc:存放数据分析系统param方法
'''
from apps.DasSystem.das_interface_service.dasSystem_interface_param import DasApiInputParam


class PublicCommonParamServiceClass():
    # 根据类型获取每种类型的入参地址
    def getApiInputParam(self,platform,searchType):
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
    elif searchType == "amazon_queryListing":# 我的数据amazon查询
        otherTypeListing03 = DasApiInputParam.amazon_ProductInfo03
        otherTypeListing02 = DasApiInputParam.amazon_ProductInfo02
        otherTypeListing01 = DasApiInputParam.amazon_ProductInfo01
    elif searchType == "amazon_unavailableListing": # 数据采集amazon死贴查询
        otherTypeListing03 = DasApiInputParam.amazon_unavailableListing03
        otherTypeListing02 = DasApiInputParam.amazon_unavailableListing02
        otherTypeListing01 = DasApiInputParam.amazon_unavailableListing01
    elif searchType == "amazon_customizeMarkListing": # 任务中心-自定义采集amazon查询
        otherTypeListing03 = DasApiInputParam.customizeMarkListing03
        otherTypeListing02 = DasApiInputParam.customizeMarkListing02
        otherTypeListing01 = DasApiInputParam.customizeMarkListing01
    elif searchType == "amazon_classificateMonitor":# 任务中心-分类监控Amazon查询
        otherTypeListing03 = DasApiInputParam.classificateMonitorListing03
        otherTypeListing02 = DasApiInputParam.classificateMonitorListing02
        otherTypeListing01 = DasApiInputParam.classificateMonitorListing01
    elif searchType == "amazon_keyWordsMonitor":# 任务中心-关键词监控amazon查询
        otherTypeListing03 = DasApiInputParam.keyWordsMonitorListing03
        otherTypeListing02 = DasApiInputParam.keyWordsMonitorListing02
        otherTypeListing01 = DasApiInputParam.keyWordsMonitorListing01
    elif searchType == "amazon_shopMonitor":# 任务中心-店铺监控amazon查询
        otherTypeListing03 = DasApiInputParam.shopMonitorListing03
        otherTypeListing02 = DasApiInputParam.shopMonitorListing02
        otherTypeListing01 = DasApiInputParam.shopMonitorListing01
    elif searchType == "amazon_listCategoryMonitor":# 任务中心-分类监控-Aamzon获取分类
        otherTypeListing03 = ""
        otherTypeListing02 = DasApiInputParam.amazon_newCategory02
        otherTypeListing01 = DasApiInputParam.amazon_newCategory01
    return otherTypeListing03, otherTypeListing02, otherTypeListing01

# 获取SMT平台入参
def getSmtApiInputParam(searchType):
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
    elif searchType == "smt_queryListing":  # 我的数据SMT查询
        otherTypeListing03 = DasApiInputParam.smt_ProductInfo03
        otherTypeListing02 = DasApiInputParam.smt_ProductInfo02
        otherTypeListing01 = DasApiInputParam.smt_ProductInfo01
    elif searchType == "smt_customizeMarkListing": # 任务中心-自定义采集smt查询
        otherTypeListing03 = DasApiInputParam.customizeMarkListing03
        otherTypeListing02 = DasApiInputParam.customizeMarkListing02
        otherTypeListing01 = DasApiInputParam.customizeMarkListing01
    elif searchType == "smt_classificateMonitor":# 任务中心-分类监控SMT查询
        otherTypeListing03 = DasApiInputParam.classificateMonitorListing03
        otherTypeListing02 = DasApiInputParam.classificateMonitorListing02
        otherTypeListing01 = DasApiInputParam.classificateMonitorListing01
    elif searchType == "smt_keyWordsMonitor":# 任务中心-关键词监控SMT查询
        otherTypeListing03 = DasApiInputParam.keyWordsMonitorListing03
        otherTypeListing02 = DasApiInputParam.keyWordsMonitorListing02
        otherTypeListing01 = DasApiInputParam.keyWordsMonitorListing01
    elif searchType == "smt_shopMonitor":# 任务中心-店铺监控SMT查询
        otherTypeListing03 = DasApiInputParam.shopMonitorListing03
        otherTypeListing02 = DasApiInputParam.shopMonitorListing02
        otherTypeListing01 = DasApiInputParam.shopMonitorListing01
    elif searchType == "smt_listCategoryMonitor":# 任务中心-分类监控-SMT获取分类
        otherTypeListing03 = ""
        otherTypeListing02 = DasApiInputParam.smt_newCategory02
        otherTypeListing01 = DasApiInputParam.smt_newCategory01
    return otherTypeListing03, otherTypeListing02, otherTypeListing01

# 获取1688平台入参
def getAliApiInputParam(searchType):
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
    elif searchType == "ali_queryListing": # 我的数据1688查询接口
        otherTypeListing03 = DasApiInputParam.ali_productInfo03
        otherTypeListing02 = DasApiInputParam.ali_productInfo02
        otherTypeListing01 = DasApiInputParam.ali_productInfo01
    elif searchType == "ali_customizeMarkListing": # 任务中心-自定义采集1688查询
        otherTypeListing03 = DasApiInputParam.customizeMarkListing03
        otherTypeListing02 = DasApiInputParam.customizeMarkListing02
        otherTypeListing01 = DasApiInputParam.customizeMarkListing01
    elif searchType == "ali_keyWordsMonitor":# 任务中心-关键词监控1688查询
        otherTypeListing03 = DasApiInputParam.keyWordsMonitorListing03
        otherTypeListing02 = DasApiInputParam.keyWordsMonitorListing02
        otherTypeListing01 = DasApiInputParam.keyWordsMonitorListing01
    elif searchType == "ali_shopMonitor":# 任务中心-店铺监控1688查询
        otherTypeListing03 = DasApiInputParam.shopMonitorListing03
        otherTypeListing02 = DasApiInputParam.shopMonitorListing02
        otherTypeListing01 = DasApiInputParam.shopMonitorListing01
    return otherTypeListing03, otherTypeListing02, otherTypeListing01

# 获取ebay平台入参
def getEbayApiInputParam(searchType):
    otherTypeListing03 = ""
    otherTypeListing02 = ""
    otherTypeListing01 = ""
    if searchType == "followMark_query": # 自定义采集-ebay页面查询
        otherTypeListing03 = DasApiInputParam.ebay_followMarkListing03
        otherTypeListing02 = DasApiInputParam.ebay_followMarkListing02
        otherTypeListing01 = DasApiInputParam.ebay_followMarkListing01
    elif searchType == "categoryMark_query": # 数据采集-ebay页面查询
        otherTypeListing03 = DasApiInputParam.ebay_categoryMarkListing03
        otherTypeListing02 = DasApiInputParam.ebay_categoryMarkListing02
        otherTypeListing01 = DasApiInputParam.ebay_categoryMarkListing01
    elif searchType == "ebay_queryListing": # 我的数据ebay查询
        otherTypeListing03 = DasApiInputParam.ebay_productInfo03
        otherTypeListing02 = DasApiInputParam.ebay_productInfo02
        otherTypeListing01 = DasApiInputParam.ebay_productInfo02

    return otherTypeListing03, otherTypeListing02, otherTypeListing01

# 获取shopee平台入参
def getShopeeApiInputParam(searchType):
    otherTypeListing03 = ""
    otherTypeListing02 = ""
    otherTypeListing01 = ""
    if searchType == "customizeMark_query": # 自定义采集-shopee
        otherTypeListing03 = DasApiInputParam.shopee_customizeMarkListing03
        otherTypeListing02 = DasApiInputParam.shopee_customizeMarkListing02
        otherTypeListing01 = DasApiInputParam.shopee_customizeMarkListing01
    elif searchType == "shopMark_query": # 关注店铺数据
        otherTypeListing03 = DasApiInputParam.shopee_shopMarkListing03
        otherTypeListing02 = DasApiInputParam.shopee_shopMarkListing02
        otherTypeListing01 = DasApiInputParam.shopee_shopMarkListing01
    elif searchType == "attentionCategoryMark_query": # 关注分类数据
        otherTypeListing03 = DasApiInputParam.shopee_attentionCategoryMarkListing03
        otherTypeListing02 = DasApiInputParam.shopee_attentionCategoryMarkListing02
        otherTypeListing01 = DasApiInputParam.shopee_attentionCategoryMarkListing01
    elif searchType == "keywordMark_query": # 关注关键词数据
        otherTypeListing03 = DasApiInputParam.shopee_keywordMarkListing03
        otherTypeListing02 = DasApiInputParam.shopee_keywordMarkListing02
        otherTypeListing01 = DasApiInputParam.shopee_keywordMarkListing01
    elif searchType == "shopee_queryListing":  # 我的数据shopee查询
        otherTypeListing03 = DasApiInputParam.shopee_productInfo03
        otherTypeListing02 = DasApiInputParam.shopee_productInfo02
        otherTypeListing01 = DasApiInputParam.shopee_productInfo01
    elif searchType == "shopee_classificateMonitor":# 任务中心-分类监控shopee查询
        otherTypeListing03 = DasApiInputParam.classificateMonitorListing03
        otherTypeListing02 = DasApiInputParam.classificateMonitorListing02
        otherTypeListing01 = DasApiInputParam.classificateMonitorListing01
    elif searchType == "shopee_keyWordsMonitor":# 任务中心-关键词监控shopee查询
        otherTypeListing03 = DasApiInputParam.keyWordsMonitorListing03
        otherTypeListing02 = DasApiInputParam.keyWordsMonitorListing02
        otherTypeListing01 = DasApiInputParam.keyWordsMonitorListing01
    elif searchType == "shopee_shopMonitor":# 任务中心-店铺监控shopee查询
        otherTypeListing03 = DasApiInputParam.shopMonitorListing03
        otherTypeListing02 = DasApiInputParam.shopMonitorListing02
        otherTypeListing01 = DasApiInputParam.shopMonitorListing01
    elif searchType == "shopee_listCategoryMonitor":# 任务中心-分类监控-shopee获取分类
        otherTypeListing03 = ""
        otherTypeListing02 = DasApiInputParam.shopee_newCategory02
        otherTypeListing01 = DasApiInputParam.shopee_newCategory01
    return otherTypeListing03, otherTypeListing02, otherTypeListing01

