'''
@File: myDataAmazon_inter_body.py
@time:2021/8/5
@Author:quanliu 181324
@Desc:我的数据-Amazon页面接口请求入参
'''

class MyDataAmazonInterParam:

    # 我的数据-Amazon查询接口入参
    accountProductInfo_param = {"method":"listBaseListing","args":"{args}"}
    accountProductInfo_select = '{"search":{"baseListingType": "followMark", "country": "{country}", "departmentName": "{departmentName}", "keywords": "{keywords}",' \
                                '"asin": "{asin}", "menuCode": "9010702", "mainSku": "{mainSku}", "associatedSystemSku": "{associatedSystemSku}","skuMapStr": "{skuMapStr}", ' \
                                '"startPrice": "{startPrice}", "endPrice": "{endPrice}", "dataStatus": "{dataStatus}", "sellerName": "{sellerName}","fba": "{fba}", "isBrand": "1", ' \
                                '"startFirstListOnTime": "{startFirstListOnTime}", "endFirstListOnTime": "{endFirstListOnTime}"},"limit":50,"offset":0,"sort":"claimTime","order":"DESC"}'


    # 我的数据-Amazon释放产品接口入参
    releaseProductInfo_param = {"method": "updateBaseListingByIds","args": "{args}"}
    releaseProductInfo_select = '{"ids":[{ids}],"dataStatus":0}'


