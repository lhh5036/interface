'''
@File: publicCommonUrlSevice.py
@time:2021/9/1
@Author:quanliu
@Desc:存放数据分析系统url方法
'''
from apps.Das.das_interface_service.dasSystem_interface_url import DasApiUrl


class PublicCommonUrlServiceClass():
    # 获取请求地址
    def getApiUrl(self, platform, searchType):
        if platform == "Amazon":
            return getAmazonApiUrl(searchType)
        elif platform == "SMT":
            return getSmtApiUrl(searchType)
        elif platform == "Ali":
            return getAliApiUrl(searchType)
        elif platform == "Ebay":
            return getEbayApiUrl(searchType)
        elif platform == "Shopee":
            return getShopeeApiUrl(searchType)
        else:
            return ""

# 获取Amazon平台的url
def getAmazonApiUrl(searchType):
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
    elif searchType == "amazon_associateSystemSku":  # Amazon关联系统SKU
        url = DasApiUrl.amazon_associateSySku_url
    elif searchType == "amazon_cancelDevelopment":  # Amazon取消开发
        url = DasApiUrl.amazon_cancelDevelopment_url
    elif searchType == "amazon_releaseProduct":  # Amazon释放产品
        url = DasApiUrl.amazon_releaseProduct_url
    elif searchType == "amazon_allocationPerson":  # 数据采集Amazon获取分配人信息接口
        url = DasApiUrl.amazon_allocationPerson_url
    elif searchType == "amazon_allocation":  # 数据采集Amazon分配接口
        url = DasApiUrl.amazon_allocationProduct_url
    elif searchType == "amazon_checkProductByRank":  # 数据采集Amazon判断产品是否认领接口
        url = DasApiUrl.amazon_checkProductByRank_url
    elif searchType == "amazon_claimProduct":  # 数据采集Amazon认领产品接口
        url = DasApiUrl.amazon_claimProduct_url
    elif searchType == "amazon_deleteProduct":  # 数据采集Amazon删除产品接口
        url = DasApiUrl.amazon_deleteProduct_url
    elif searchType == "amazon_disableProduct":  # 数据采集Amazon禁用产品接口
        url = DasApiUrl.amazon_disableProduct_url
    elif searchType == "amazon_enableProduct":  # Amazon启用产品接口
        url = DasApiUrl.amazon_enableProduct_url
    elif searchType == "amazon_dataSample_associate":  # 数据采集Amazon关联系统SKU
        url = DasApiUrl.amazon_dataSample_associate_url
    elif searchType == "amazon_queryListing":  # 我的数据amazon查询
        url = DasApiUrl.amazon_queryListing_url
    elif searchType == "amazon_unavailableListing": # 数据采集amazon死贴查询
        url = DasApiUrl.amazon_unavailableListing_url
    elif searchType == "amazon_customizeMarkListing": # 任务中心-自定义采集Amazon查询
        url = DasApiUrl.amazon_customizeMarkListing_url
    elif searchType == "amazon_classificateMonitor":# 任务中心-分类监控Amazon查询
        url = DasApiUrl.classificateMonitor_url
    elif searchType == "amazon_keyWordsMonitor":# 任务中心-关键词监控Amazon查询
        url = DasApiUrl.keyWordsMonitor_url
    elif searchType == "amazon_shopMonitor":# 任务中心-店铺监控Amazon查询
        url = DasApiUrl.shopMonitor_url
    elif searchType == "amazon_listCategoryMonitor":# 任务中心-分类监控-Aamzon获取分类
        url = DasApiUrl.amazon_taskCenterNewCategory_url
    return url

# 获取SMT平台的url
def getSmtApiUrl(searchType):
    url = ""
    if searchType == "smt_associateSystemSku":  # SMT关联系统SKU
        url = DasApiUrl.smt_associateSySku_url
    elif searchType == "smt_cancelDevelopment":  # SMT取消开发
        url = DasApiUrl.smt_cancelDevelopment_url
    elif searchType == "smt_releaseProduct":  # SMT释放产品
        url = DasApiUrl.smt_releaseProduct_url
    elif searchType == "smt_infringementAudits":  # SMT侵权审核接口
        url = DasApiUrl.smt_infringementAudit_url
    elif searchType == "smt_checkProductByRank":  # SMT判断产品是否认领接口
        url = DasApiUrl.smt_checkProductByRank_url
    elif searchType == "smt_claimProduct":  # SMT认领产品接口
        url = DasApiUrl.smt_claimProduct_url
    elif searchType == "smt_deleteProduct":  # SMT删除产品
        url = DasApiUrl.smt_deleteProduct_url
    elif searchType == "smt_disableProduct":  # SMT禁用产品
        url = DasApiUrl.smt_disableProduct_url
    elif searchType == "smt_enableProduct":  # SMT启用产品
        url = DasApiUrl.smt_enableProduct_url
    elif searchType == "categoryMark_query":  # 数据采集-SMTorder大于100查询页面
        url = DasApiUrl.smt_dataSampleListing_url
    elif searchType == "bestsellerMark_query":  # 数据采集-SMTtopselling查询页面
        url = DasApiUrl.smt_dataSampleListing_url
    elif searchType == "shopMark_query":  # 数据采集SMT关注店铺数据查询页面
        url = DasApiUrl.smt_dataSampleListing_url
    elif searchType == "attentionCategoryMark_query":  # 数据采集SMT关注分类数据查询页面
        url = DasApiUrl.smt_dataSampleListing_url
    elif searchType == "keywordMark_query":  # 数据采集SMT关注关键词数据查询页面
        url = DasApiUrl.smt_dataSampleListing_url
    elif searchType == "smt_dataSample_associate":  # 数据采集SMT关联系统SKU
        url = DasApiUrl.smt_dataSample_associate_url
    elif searchType == "smt_allocationPerson":  # 数据采集SMT获取分配人信息接口
        url = DasApiUrl.smt_allocationPerson_url
    elif searchType == "smt_allocation":  # 数据采集SMT分配接口
        url = DasApiUrl.smt_allocationProduct_url
    elif searchType == "smt_queryListing":  # 我的数据SMT查询
        url = DasApiUrl.smt_queryListing_url
    elif searchType == "smt_customizeMarkListing": # 任务中心-自定义采集SMT查询
        url = DasApiUrl.smt_customizeMarkListing_url
    elif searchType == "smt_classificateMonitor":# 任务中心-分类监控SMT查询
        url = DasApiUrl.classificateMonitor_url
    elif searchType == "smt_keyWordsMonitor":# 任务中心-关键词监控SMT查询
        url = DasApiUrl.keyWordsMonitor_url
    elif searchType == "smt_shopMonitor":# 任务中心-店铺监控SMT查询
        url = DasApiUrl.shopMonitor_url
    elif searchType == "smt_listCategoryMonitor":# 任务中心-分类监控-SMT获取分类
        url = DasApiUrl.smt_checkProductByRank_url
    return url

# 获取1688平台的URL
def getAliApiUrl(searchType):
    url = ""
    if searchType == "ali_claimProduct":  # 1688认领产品接口
        url = DasApiUrl.ali_claimProduct_url
    elif searchType == "ali_checkProductByRank":  # 1688判断产品是否已经认领
        url = DasApiUrl.ali_checkProductByRank_url
    elif searchType == "categoryMark_query":  # 数据采集-1688分类数据页面查询
        url = DasApiUrl.ali_dataSampleListing_url
    elif searchType == "shopMark_query":  # 数据采集-1688关注店铺数据页面查询
        url = DasApiUrl.ali_dataSampleListing_url
    elif searchType == "attentionCategoryMark_query":  # 数据采集-1688关注分类数据页面查询
        url = DasApiUrl.ali_dataSampleListing_url
    elif searchType == "keywordMark_query":  # 数据采集-1688关注关键词数据页面查询
        url = DasApiUrl.ali_dataSampleListing_url
    elif searchType == "shopTopOneMark_query":  # 数据采集-1688镇店之宝页面查询
        url = DasApiUrl.ali_dataSampleListing_url
    elif searchType == "ali_disableProduct":  # 数据采集-1688禁用
        url = DasApiUrl.ali_disableProduct_url
    elif searchType == "ali_enableProduct":  # 数据采集-1688启用
        url = DasApiUrl.ali_enableProduct_url
    elif searchType == "ali_deleteProduct":  # 数据采集-1688删除
        url = DasApiUrl.ali_deleteProduct_url
    elif searchType == "ali_dataSample_associate":  # 数据采集-1688关联系统SKU
        url = DasApiUrl.ali_dataSample_associate_url
    elif searchType == "ali_allocationPerson":  # 数据采集-1688获取分配人信息接口
        url = DasApiUrl.ali_allocationPerson_url
    elif searchType == "ali_allocationProduct":  # 数据采集-1688分配接口
        url = DasApiUrl.ali_allocationProduct_url
    elif searchType == "ali_queryListing":  # 我的数据1688查询
        url = DasApiUrl.ali_queryListing_url
    elif searchType == "ali_customizeMarkListing": # 任务中心-自定义采集1688查询
        url = DasApiUrl.ali_customizeMarkListing_url
    elif searchType == "ali_keyWordsMonitor":# 任务中心-关键词监控1688查询
        url = DasApiUrl.keyWordsMonitor_url
    elif searchType == "ali_shopMonitor":# 任务中心-店铺监控1688查询
        url = DasApiUrl.shopMonitor_url
    return url

# 获取ebay平台的URL
def getEbayApiUrl(searchType):
    url = ""
    if searchType == "ebay_claimProduct":  # ebay认领产品接口
        url = DasApiUrl.ebay_claimProduct_url
    elif searchType == "followMark_query":  # 自定义采集-ebay页面查询
        url = DasApiUrl.ebay_dataSampleListing_url
    elif searchType == "categoryMark_query":  # 数据采集-ebay页面查询
        url = DasApiUrl.ebay_dataSampleListing_url
    elif searchType == "ebay_disableProduct":  # 数据采集-ebay禁用
        url = DasApiUrl.ebay_disableProduct_url
    elif searchType == "ebay_enableProduct":  # 数据采集-ebay启用
        url = DasApiUrl.ebay_enableProduct_url
    elif searchType == "ebay_deleteProduct":  # 数据采集-ebay删除
        url = DasApiUrl.ebay_deleteProduct_url
    elif searchType == "ebay_dataSample_associate":  # 数据采集-ebay关联系统SKU
        url = DasApiUrl.ebay_dataSample_associate_url
    elif searchType == "ebay_allocationPerson":  # 数据采集-ebay获取分配人接口
        url = DasApiUrl.ebay_allocationPerson_url
    elif searchType == "ebay_allocationProduct":  # 数据采集-ebay分配接口
        url = DasApiUrl.ebay_allocationProduct_url
    elif searchType == "ebay_queryListing":  # 我的数据ebay查询
        url = DasApiUrl.ebay_queryListing_url
    return url

# 获取shopee平台URL
def getShopeeApiUrl(searchType):
    url = ""
    if searchType == "shopee_claimProduct":  # shopee认领产品接口
        url = DasApiUrl.shopee_claimProduct_url
    elif searchType == "customizeMark_query":  # 自定义采集-shopee
        url = DasApiUrl.shopee_dataSampleListing_url
    elif searchType == "shopMark_query":  # 关注店铺数据
        url = DasApiUrl.shopee_dataSampleListing_url
    elif searchType == "attentionCategoryMark_query":  # 关注分类数据
        url = DasApiUrl.shopee_dataSampleListing_url
    elif searchType == "keywordMark_query":  # 关注关键词数据
        url = DasApiUrl.shopee_dataSampleListing_url
    elif searchType == "shopee_disableProduct":  # 数据采集-shopee禁用
        url = DasApiUrl.shopee_disableProduct_url
    elif searchType == "shopee_enableProduct":  # 数据采集-shopee启用
        url = DasApiUrl.shopee_enableProduct_url
    elif searchType == "shopee_deleteProduct":  # 数据采集-shopee删除
        url = DasApiUrl.shopee_deleteProduct_url
    elif searchType == "shopee_dataSample_associate":  # 数据采集-shopee关联系统SKU
        url = DasApiUrl.shopee_dataSample_associate_url
    elif searchType == "shopee_allocationPerson":  # 数据采集-shopee获取分配人接口
        url = DasApiUrl.shopee_allocationPerson_url
    elif searchType == "shopee_allocationProduct":  # 数据采集-shopee分配接口
        url = DasApiUrl.shopee_allocationProduct_url
    elif searchType == "shopee_queryListing":  # 我的数据shopee查询
        url = DasApiUrl.shopee_queryListing_url
    elif searchType == "shopee_classificateMonitor":# 任务中心-分类监控shopee查询
        url = DasApiUrl.classificateMonitor_url
    elif searchType == "shopee_keyWordsMonitor":# 任务中心-关键词监控Shopee查询
        url = DasApiUrl.keyWordsMonitor_url
    elif searchType == "shopee_shopMonitor":# 任务中心-店铺监控shopee查询
        url = DasApiUrl.shopMonitor_url
    elif searchType == "shopee_listCategoryMonitor":# 任务中心-分类监控-shopee获取分类
        url = DasApiUrl.shopee_checkProductByRank_url
    return url

if __name__ == '__main__':
    print(PublicCommonUrlServiceClass().getApiUrl('Shopee', 'shopee_shopMonitor'))
