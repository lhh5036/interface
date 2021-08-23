'''
@File: myDataManage_inter_body.py
@time:2021/8/5
@Author:quanliu 181324
@Desc:数据管理页面接口请求入参
'''

class MyDataManageInterParam:

    # 我的数据-Amazon查询接口入参
    accountProductInfo_param = {"method":"listBaseListing","args":"{args}"}
    accountProductInfo_select = '{"search":{"baseListingType": "followMark", "country": "{country}", "departmentName": "{departmentName}", "keywords": "{keywords}",' \
                                '"asin": "{asin}", "menuCode": "9010702", "mainSku": "{mainSku}", "associatedSystemSku": "{associatedSystemSku}","skuMapStr": "{skuMapStr}", ' \
                                '"startPrice": "{startPrice}", "endPrice": "{endPrice}", "dataStatus": "{dataStatus}", "sellerName": "{sellerName}","fba": "{fba}", "isBrand": "{isBrand}", ' \
                                '"startFirstListOnTime": "{startFirstListOnTime}", "endFirstListOnTime": "{endFirstListOnTime}"},"limit":50,"offset":0,"sort":"claimTime","order":"DESC"}'


    # 我的数据-Amazon释放产品接口入参
    releaseProductInfo_param = {"method": "updateBaseListingByIds","args": "{args}"}
    releaseProductInfo_select = '{"ids":[{ids}],"dataStatus":0}'

    # 我的数据-Amazon关联系统SKU接口入参
    associateSySku_param = {"args":"{args}"}
    associateSySku_select = '{"ids":[{ids}],"systemSku":"{systemSku}"}'

    # 我的数据-Amazon低价接口入参
    productGenDijia_param = {"args":"{args}"}
    productGenDijia_select = '{"asinUrlStr":"{asinUrlStr}"}'

    # 我的数据-Amazon同款接口入参
    productGenTongkuan_param = {"args":"{args}"}
    productGenTongkuan_select = '{"asinUrlStr":"{asinUrlStr}"}'

    # 我的数据-SMT查询接口入参
    smtProductInfo_param = {"args":"{args}"}
    smtProductInfo_select = '{"search":{"baseListingType":"followMark","mainSku":"{mainSku}","associatedSystemSku":"{associatedSystemSku}","skuMapStr":"{skuMapStr}",' \
                            '"brand":"{brand}","keywords":"{keywords}","startPrice":"{startPrice}","endPrice":"{endPrice}","dataStatus":"{dataStatus}","infringementReviewer":"{infringementReviewer}",' \
                            '"menuCode":"9010703","country":"US","productId":"{productId}","endOrders":"{endOrders}","developmentStatus":"{developmentStatus}","startOrders":"{startOrders}","Reviews":"{Reviews}",' \
                            '"rating":"{rating}","merchantName":"{merchantName}","startCrawlTime":"{startCrawlTime}","endCrawlTime":"{endCrawlTime}","systemSku":"{systemSku}","distributor":"{distributor}",' \
                            '"startDistributionTime":"{startDistributionTime}","endDistributionTime":"{endDistributionTime}","startInfringementReviewTime":"{startInfringementReviewTime}","endInfringementReviewTime":"{endInfringementReviewTime}",' \
                            '"auditStatus":"{auditStatus}"},"limit":50,"offset":0,"sort":"claimTime","order":"DESC"}'
