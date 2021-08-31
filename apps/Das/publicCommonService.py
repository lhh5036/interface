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
    def getApiInputParam(searchType):
        otherTypeListing03 = ""
        otherTypeListing02 = ""
        otherTypeListing01 = ""
        url = ""
        if searchType == "bestsellerMark":  # bestseller页面
            otherTypeListing03 = DasApiInputParam.amazon_bestsellersListing03
            otherTypeListing02 = DasApiInputParam.amazon_bestsellersListing02
            otherTypeListing01 = DasApiInputParam.amazon_bestsellersListing01
            url = DasApiUrl.amazon_dataSampleListing_url
        elif searchType == "newReleasesMark":  # newReleases页面
            otherTypeListing03 = DasApiInputParam.amazon_NewReleaseListing03
            otherTypeListing02 = DasApiInputParam.amazon_NewReleaseListing02
            otherTypeListing01 = DasApiInputParam.amazon_NewReleaseListing01
            url = DasApiUrl.amazon_dataSampleListing_url
        elif searchType == "moverShakerMark":  # moversShakers页面
            otherTypeListing03 = DasApiInputParam.amazon_MoversShakersListing03
            otherTypeListing02 = DasApiInputParam.amazon_MoversShakersListing02
            otherTypeListing01 = DasApiInputParam.amazon_MoversShakersListing01
            url = DasApiUrl.amazon_dataSampleListing_url
        elif searchType == "mostWishMark":  # MostWishedFor页面
            otherTypeListing03 = DasApiInputParam.amazon_MostWishedForListing03
            otherTypeListing02 = DasApiInputParam.amazon_MostWishedForListing02
            otherTypeListing01 = DasApiInputParam.amazon_MostWishedForListing01
            url = DasApiUrl.amazon_dataSampleListing_url
        elif searchType == "giftIdeasMark":  # Giftldeas页面
            otherTypeListing03 = DasApiInputParam.amazon_GiftldeasListing03
            otherTypeListing02 = DasApiInputParam.amazon_GiftldeasListing02
            otherTypeListing01 = DasApiInputParam.amazon_GiftldeasListing01
            url = DasApiUrl.amazon_dataSampleListing_url
        elif searchType == "shopMark":  # 关注店铺数据页面
            otherTypeListing03 = DasApiInputParam.amazon_attentStoreListing03
            otherTypeListing02 = DasApiInputParam.amazon_attentStoreListing02
            otherTypeListing01 = DasApiInputParam.amazon_attentStoreListing01
            url = DasApiUrl.amazon_attentStoreListing_url
        elif searchType == "categoryMark":  # 关注分类数据页面
            otherTypeListing03 = DasApiInputParam.amazon_categoryListing03
            otherTypeListing02 = DasApiInputParam.amazon_categoryListing02
            otherTypeListing01 = DasApiInputParam.amazon_categoryListing01
            url = DasApiUrl.amazon_attentStoreListing_url
        elif searchType == "keywordMark":  # 关注关键词数据页面
            otherTypeListing03 = DasApiInputParam.amazon_keywordsListing03
            otherTypeListing02 = DasApiInputParam.amazon_keywordsListing02
            otherTypeListing01 = DasApiInputParam.amazon_keywordsListing01
            url = DasApiUrl.amazon_attentStoreListing_url
        elif searchType == "jungleScoutKeywordMark":  # JungleScout关键词数据页面
            otherTypeListing03 = DasApiInputParam.amazon_jungleScoutListing03
            otherTypeListing02 = DasApiInputParam.amazon_jungleScoutListing02
            otherTypeListing01 = DasApiInputParam.amazon_jungleScoutListing01
            url = DasApiUrl.amazon_attentStoreListing_url
        return otherTypeListing03, otherTypeListing02, otherTypeListing01, url

    # 判断哪个页面的数据需要对入参进行判空
    def needJudgeEmpty(searchType):
        if searchType=="bestsellerMark":
            return True
        elif searchType=="newReleasesMark":
            return True
        elif searchType=="moverShakerMark":
            return True
        elif searchType=="mostWishMark":
            return True
        elif searchType=="giftIdeasMark":
            return True
        else:
            return False