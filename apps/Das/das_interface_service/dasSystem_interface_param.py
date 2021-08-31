'''
@File: dasSystem_interface_param.py
@time:2021/8/5
@Author:quanliu 181324
@Desc:数据管理页面接口请求入参
'''

class DasApiInputParam:

    # 我的数据-Amazon查询接口入参
    amazon_ProductInfo01 = {"method":"listBaseListing","args":"{args}"}
    amazon_ProductInfo02 = {"search":{0},"limit":50,"offset":0,"sort":"claimTime","order":"DESC"}
    amazon_ProductInfo03 = {"baseListingType":"followMark","country":"","departmentName":"","brand":"","keywords":"","asin":"","menuCode":"9010702","mainSku":"",
                            "associatedSystemSku":"","skuMapStr":"","startPrice":"","endPrice":"","dataStatus":"","sellerName":"","fba":"","isBrand":1,"startFirstListOnTime":"",
                            "endFirstListOnTime":"","developmentStatus":"","startDistributionTime":"","endDistributionTime":""}


    # 我的数据-释放产品接口入参
    releaseProductInfo_param = {"method": "updateBaseListingByIds","args": "{args}"}
    releaseProductInfo_select = '{"ids":[{ids}],"dataStatus":0}'

    # 我的数据-关联系统SKU接口入参
    associateSySku_param = {"args":"{args}"}
    associateSySku_select = '{"ids":[{ids}],"systemSku":"{systemSku}"}'

    # 我的数据-取消开发接口入参
    cancelDevelop_param = {"args":"{args}"}
    cancelDevelop_select = '{"ids":[{ids}],"cancelNotesInfo":"{cancelNotesInfo}"}'

    # 我的数据-低价接口入参
    productGenDijia_param = {"args":"{args}"}
    productGenDijia_select = '{"asinUrlStr":"{asinUrlStr}"}'

    # 我的数据-同款接口入参
    productGenTongkuan_param = {"args":"{args}"}
    productGenTongkuan_select = '{"asinUrlStr":"{asinUrlStr}"}'

    # 我的数据-SMT查询接口入参
    smt_ProductInfo01 = {"args":"{args}"}
    smt_ProductInfo02 = {"search":{0},"limit":50,"offset":0,"sort":"claimTime","order":"DESC"}
    smt_ProductInfo03 = {"baseListingType":"followMark","mainSku":"","associatedSystemSku":"","skuMapStr":"","brand":"","keywords":"","startPrice":"","endPrice":"","dataStatus":"",
                         "infringementReviewer":"","menuCode":"9010703","country":"US","productId":"","endOrders":"","developmentStatus":"","startOrders":"","Reviews":"","rating":"",
                         "merchantName":"","startCrawlTime":"","endCrawlTime":"","systemSku":"","distributor":"","startDistributionTime":"","endDistributionTime":"","startInfringementReviewTime":"",
                         "endInfringementReviewTime":"","auditStatus":""}

    # 我的数据-SMT侵权审核接口入参
    infringementReview_param = {"args":"{0}"}
    infringementReview_select = {"ids":{0},"infringementObj":"{1}","auditNotesInfo":"{2}","infringementTypeName":"{3}","salesProhibition":{4},"auditStatus":{5}}
    infringementReview_plat = {"plat":"{0}","sites":{1}} # 存放禁用平台和站点
    infringmentReview_site = {"site":{0},"isAuthority":0} # 存放禁用站点

    # 我的数据-SMT获取侵权审核人信息入参
    infringementAduitsPerson_param = {}

    # 我的数据-SMT分配侵权审核人入参
    smt_infringementReviewer01 = {"args": "{0}"}
    smt_infringementReviewer02 = {"ids":{0},"infringementReviewer":{1}}



    # 我的数据-1688查询接口入参
    ali_productInfo01 = {"method":"listBaseListing","args":"{args}"}
    ali_productInfo02 = {"search":{0},"limit":50,"offset":0,"sort":"claimTime","order":"DESC"}
    ali_productInfo03 = {"baseListingType":"followMark","brand":"","keywords":"","startPrice":"","endPrice":"","dataStatus":"","mainSku":"",
                                        "associatedSystemSku":"","skuMapStr":"","menuCode":"9010704","country":"CN","productId":"","endOrders":"","startOrders":"",
                                        "Reviews":"","rating":"","merchantName":"","startCrawlTime":"","endCrawlTime":"","startDistributionTime":"",
                                        "endDistributionTime":"","developmentStatus":""}


    # 我的数据-ebay查询接口入参
    ebay_productInfo01 = {"args":"{0}"}
    ebay_productInfo02 = {"search":{0},"sort":"claimTime","order":"DESC","offset":0,"limit":50}
    ebay_productInfo03 = {"mainSku":"","associatedSystemSku":"","skuMapStr":"","baseListingType":"followMark","menuCode":"9010705","merchantUserName":"","rating":"","startTotalSold":"",
                          "endTotalSold":"","productId":"","dataStatus":"","categoriesKw":"","title":"","startOnlineDate":"","endOnlineDate":"","count":"","startFirstListOnTime":"",
                          "endFirstListOnTime":"","developmentStatus":"","startDistributionTime":"","endDistributionTime":""}

    # 我的数据-shopee查询接口入参
    shopee_productInfo01 = {"args":"{0}"}
    shopee_productInfo02 = {"search":{0},"sort":"crawlTime","order":"DESC","offset":0,"limit":50}
    shopee_productInfo03 = {"associatedSystemSku":"","skuMapStr":"","baseListingType":"followMark","menuCode":"9010706","merchantUserName":"","rating":"","reviews":"","startTotalSold":"",
                            "endTotalSold":"","productId":"","dataStatus":"","categoriesKw":"","title":"","startOnlineDate":"","endOnlineDate":"","startClaimTime":"","endClaimTime":"","account":"",
                            "startOriginalPrice":"","endOriginalPrice":"","startDiscount":"","endDiscount":"","startPrice":"","endPrice":"","developmentStatus":"","startDistributionTime":"","endDistributionTime":"","systemSku":""}

    # 校验产品是否已经认领接口入参
    checkAccountProductByRank01 = {"args":"{0}"}
    checkAccountProductByRank02 = {"saleChannel": {0}, "baseIdList": {1}}

    # 数据采集-Amazon查询接口入参（数据采集bestsellers/NewRelease/MoversShakers/MostWishedFor/Giftldeas页面共用）
    amazon_dataSampleListing01 = {"args":"{0}"}
    amazon_dataSampleListing02 = {"search":{0},"offset":0,"limit":50,"sort":"crawlTime","order":"DESC"}
    amazon_dataSampleListing03 = {"baseListingType":"","menuCode":"","developmentClaim":"","salesTrialSale":"","startCrawlTime":"","endCrawlTime":"","country":"","asin":"","dataStatus":"","keywords":"","sellerName":"",
                                  "rating":"","nodes":"","brand":"","startFirstListOnTime":"","endFirstListOnTime":"","startPrice":"","endPrice":"","Reviews":""}

    # 数据采集-Amazon查询接口入参（关注店铺数据页面）
    amazon_attentStoreListing01 = {"method":"listBaseListing","args":"{0}"}
    amazon_attentStoreListing02 = {"search":{0},"limit":50,"offset":0,"sort":"crawlTime","order":"DESC"}
    amazon_attentStoreListing03 = {"baseListingType":"shopMark","developmentClaim":"","country":"","Reviews":"","rating":"","menuCode":"9010807","brand":"","startCrawlTime":"","endCrawlTime":"","isBrand":"","departmentName":"",
                                   "keywords":"","asin":"","startPrice":"","endPrice":"","dataStatus":"","sellerName":"","fba":"","startFirstListOnTime":"","endFirstListOnTime":""}
    # 数据采集-Amazon查询接口入参（关注分类数据页面）
    amazon_categoryListing01 = {"method":"listBaseListing","args":"{0}"}
    amazon_categoryListing02 = {"search":{0},"limit":50,"offset":0,"sort":"crawlTime","order":"DESC"}
    amazon_categoryListing03 = {"baseListingType":"categoryMark","nodes":"","salesTrialSale":"","developmentClaim":"","startCrawlTime":"","endCrawlTime":"","country":"","menuCode":"9010808","departmentName":"","brand":"",
                                "Reviews":"","rating":"","keywords":"","asin":"","startPrice":"","endPrice":"","dataStatus":"","sellerName":"","fba":"","isBrand":"","startFirstListOnTime":"","endFirstListOnTime":""}

    # 数据采集-Amazon查询接口入参（关注关键词数据页面）
    amazon_keywordsListing01 = {"method":"listBaseListing","args":"{0}"}
    amazon_keywordsListing02 = {"search":{0},"limit":50,"offset":0,"sort":"crawlTime","order":"DESC"}
    amazon_keywordsListing03 = {"baseListingType":"keywordMark","taskKeyword":"","Reviews":"","rating":"","searchKeywords":"","developmentClaim":"","menuCode":"9010809","country":"","departmentName":"","keywords":"",
                                "brand":"","isBrand":"","asin":"","startPrice":"","endPrice":"","sellerName":"","fba":"","startFirstListOnTime":"","endFirstListOnTime":"","startCrawlTime":"","endCrawlTime":""}

    # 数据采集-认领产品接口入参
    claimProduct01 = {"args":"{0}"}
    claimProduct02 = {"ids":{0}}

    # 数据采集-禁用接口入参
    disableProduct01 = {"args":"{0}"}
    disableProduct02 = {"ids":{0}}

    # 数据采集-启用接口入参
    enableProduct01 = {"args":"{0}"}
    enableProduct02 = {"ids":{0}}

    # 数据采集-删除接口入参
    deleteProduct01 = {"args":"{0}"}
    deleteProduct02 = {"ids":{0}}

    # 数据采集-分配接口入参
    allocationProduct01 = {"args":"{0}"}
    allocationProduct02 = {"ids":{0},"claimant":{1}}




    # 参数配置-取消开发备注保存接口入参
    paramConfig_param = {"args":"{args}"}
    paramConfig_select = '{"notesInfoList":[{notesInfoList}],"id":"datasystem-1234567895201314"}'

    # 参数配置-取消开发备注查询接口入参
    paramConfigQuery = {"args": "{\"id\":\"datasystem-1234567895201314\"}"}