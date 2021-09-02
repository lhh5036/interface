'''
@File: publicCommonJudgeEmptySevice.py
@time:2021/9/1
@Author:quanliu
@Desc:数据分析接口参数判空方法
'''
from apps.Common_Config.parseRequestDatas import parseRequestDatas

class PublicCommonJudgeEmptySevice():
    # 判断哪个页面的数据需要对入参进行判空
    def needJudgeEmpty(self, platform, searchType,kwargs):
        if platform == "Amazon":
            return amazonNeedJudgeEmpty(searchType,kwargs)
        elif platform == "SMT":
            return smtNeedJudgeEmpty(searchType,kwargs)
        elif platform == "Ali":
            return aliNeedJudgeEmpty(searchType,kwargs)
        elif platform == "Ebay":
            return ebayNeedJudgeEmpty(searchType,kwargs)
        elif platform == "Shopee":
            return shopeeNeedJudgeEmpty(searchType,kwargs)
        else:
            return ""

# 判断Amazon平台哪些页面需要对入参判空
def amazonNeedJudgeEmpty(searchType,kwargs):
    if searchType == "bestsellerMark_query": # 数据采集bestseller
        return needJudgeEmptyParam(["country"],kwargs)
    elif searchType == "newReleasesMark_query":# 数据采集newReleases
        return needJudgeEmptyParam(["country"],kwargs)
    elif searchType == "moverShakerMark_query":# 数据采集moversShakers
        return needJudgeEmptyParam(["country"],kwargs)
    elif searchType == "mostWishMark_query":# 数据采集mostWishedFor
        return needJudgeEmptyParam(["country"],kwargs)
    elif searchType == "giftIdeasMark_query":# 数据采集giftIdeas
        return needJudgeEmptyParam(["country"],kwargs)
    elif searchType == "amazon_customizeMarkListing":  # 任务中心-自定义采集Amazon查询
        return needJudgeEmptyParam(["saleChannel"], kwargs)
    elif searchType == "amazon_classificateMonitor":# 任务中心-分类监控Amazon查询
        return needJudgeEmptyParam(["saleChannel"], kwargs)
    elif searchType == "amazon_keyWordsMonitor":# 任务中心-关键词监控Amazon查询
        return needJudgeEmptyParam(["saleChannel"], kwargs)
    elif searchType == "amazon_shopMonitor":# 任务中心-店铺监控Amazon查询
        return needJudgeEmptyParam(["saleChannel"], kwargs)
    else:
        return False

# 判断SMT平台哪些页面需要对入参判空
def smtNeedJudgeEmpty(searchType,kwargs):
    if searchType == "smt_customizeMarkListing": # 任务中心-自定义采集SMT查询
        return needJudgeEmptyParam(["saleChannel","country"], kwargs)
    elif searchType == "smt_classificateMonitor":  # 任务中心-分类监控SMT查询
        return needJudgeEmptyParam(["saleChannel"], kwargs)
    elif searchType == "smt_keyWordsMonitor":# 任务中心-关键词监控SMT查询
        return needJudgeEmptyParam(["saleChannel"], kwargs)
    elif searchType == "smt_shopMonitor":# 任务中心-店铺监控SMT查询
        return needJudgeEmptyParam(["saleChannel"], kwargs)
    else:
        return False

# 判断1688平台哪些页面需要对入参判空
def aliNeedJudgeEmpty(searchType,kwargs):
    if searchType == "ali_customizeMarkListing": # 任务中心-自定义采集1688查询
        return needJudgeEmptyParam(["saleChannel","country"],kwargs)
    elif searchType == "ali_keyWordsMonitor":# 任务中心-关键词监控1688查询
        return needJudgeEmptyParam(["saleChannel"],kwargs)
    elif searchType == "ali_shopMonitor":# 任务中心-店铺监控1688查询
        return needJudgeEmptyParam(["saleChannel"], kwargs)
    else:
        return False

# 判断ebay平台哪些页面需要对入参判空
def ebayNeedJudgeEmpty(searchType,kwargs):
    pass

# 判断shopee平台哪些页面需要对入参判空
def shopeeNeedJudgeEmpty(searchType,kwargs):
    if searchType == "shopee_classificateMonitor":  # 任务中心-分类监控shopee查询
        return needJudgeEmptyParam(["saleChannel"], kwargs)
    elif searchType == "shopee_keyWordsMonitor":  # 任务中心-关键词监控Shopee查询
        return needJudgeEmptyParam(["saleChannel"], kwargs)
    elif searchType == "shopee_shopMonitor":  # 任务中心-店铺监控shopee查询
        return needJudgeEmptyParam(["saleChannel"], kwargs)
    else:
        return False

# 判断需要校验哪些入参key
def needJudgeEmptyParam(keyList,kwargs):
    notEmpty = False # 不需要判空
    for key in keyList:
        if parseRequestDatas(key,kwargs) == "": # 如果需要判空则True
            notEmpty = notEmpty | True
        else:
            notEmpty = notEmpty | False
    return notEmpty