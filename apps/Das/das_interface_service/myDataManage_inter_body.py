'''
@File: myDataManage_inter_body.py
@time:2021/8/5
@Author:quanliu 181324
@Desc:数据管理页面接口请求入参
'''

class MyDataManageInterParam:

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

    # 参数配置-取消开发备注保存接口入参
    paramConfig_param = {"args":"{args}"}
    paramConfig_select = '{"notesInfoList":[{notesInfoList}],"id":"datasystem-1234567895201314"}'

    # 参数配置-取消开发备注查询接口入参
    paramConfigQuery = {"args": "{\"id\":\"datasystem-1234567895201314\"}"}