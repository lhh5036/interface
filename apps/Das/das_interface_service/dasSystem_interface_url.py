'''
@File: dasSystem_interface_url.py
@time:2021/8/5
@Author:quanliu 181324
@Desc:数据管理页面接口地址
'''
from apps.Common_Config.interface_common_info import InterfaceCommonInfo


class DasApiUrl:

    # 我的数据-Amazon查询接口
    amazon_queryListing_url = InterfaceCommonInfo.common_url + "/das/amazon/AccountProductInfo"

    # 我的数据-Amazon释放产品接口
    amazon_releaseProduct_url = InterfaceCommonInfo.common_url + "/das/amazon/AccountProductInfo"

    # 我的数据-Amazon关联系统SKU接口
    amazon_associateSySku_url = InterfaceCommonInfo.common_url + "/das/amazon/AccountProductInfo/associatedSystemSku"

    # 我的数据-Amazon取消开发接口
    amazon_cancelDevelopment_url = InterfaceCommonInfo.common_url + "/das/amazon/AccountProductInfo/cancelDevelopment"

    # Amazon校验产品是否已经认领接口地址
    amazon_checkProductByRank_url = InterfaceCommonInfo.common_url + "/das/account/checkAmazonAccountProductByRank"

    # 我的数据-低价接口
    productGenDijia_url = InterfaceCommonInfo.common_url + "/das/ali/productGenDijia"

    # 我的数据-同款接口
    productGenTongkuan_url = InterfaceCommonInfo.common_url + "/das/ali/productGenTongkuan"

    # 我的数据-SMT查询接口
    smt_queryListing_url = InterfaceCommonInfo.common_url + "/das/smt/AccountProductInfo/querySmtPageList"

    # 我的数据-SMT释放产品接口
    smt_releaseProduct_url = InterfaceCommonInfo.common_url + "/das/smt/AccountProductInfo/releaseProduct"

    # 我的数据-SMT关联系统SKU接口
    smt_associateSySku_url = InterfaceCommonInfo.common_url + "/das/smt/AccountProductInfo/associatedSystemSku"

    # 我的数据-SMT取消开发接口
    smt_cancelDevelopment_url = InterfaceCommonInfo.common_url + "/das/smt/AccountProductInfo/cancelDevelopment"

    # 我的数据-SMT侵权审核接口
    smt_infringementAudit_url = InterfaceCommonInfo.common_url + "/das/smt/AccountProductInfo/infringementReview"

    # 我的数据-SMT获取侵权审核人信息
    smt_infringementAuditPerson_url = InterfaceCommonInfo.common_url + "/das/usermgtn/getSMTLeaderList"

    # 我的数据-SMT分配侵权审核人接口
    smt_infringementReviewer_url = InterfaceCommonInfo.common_url + "/das/smt/AccountProductInfo/allocationInfringementReviewer"

    # SMT校验产品是否已经认领接口地址
    smt_checkProductByRank_url = InterfaceCommonInfo.common_url + "/das/account/checkAccountProductInfo"

    # 我的数据-1688查询接口
    ali_queryListing_url = InterfaceCommonInfo.common_url + "/das/ali1688/AccountProductInfo"

    # 我的数据-1688释放产品接口
    ali_releaseProduct_url = InterfaceCommonInfo.common_url + "/das/ali1688/AccountProductInfo"

    # 我的数据-1688关联系统SKU接口
    ali_associateSySku_url = InterfaceCommonInfo.common_url + "/das/ali1688/AccountProductInfo/associatedSystemSku"

    # 我的数据-1688取消开发接口
    ali_cancelDevelopment_url = InterfaceCommonInfo.common_url + "/das/ali1688/AccountProductInfo/cancelDevelopment"

    # 我的数据-ebay查询接口
    ebay_queryListing_url = InterfaceCommonInfo.common_url + "/das/ebay/AccountProductInfo/queryEbayPageList"

    # 我的数据-ebay释放产品接口
    ebay_releaseProduct_url = InterfaceCommonInfo.common_url + "/das/ebay/AccountProductInfo/releaseProduct"

    # 我的数据-ebay关联系统SKU接口
    ebay_associateSySku_url = InterfaceCommonInfo.common_url + "/das/ebay/AccountProductInfo/associatedSystemSku"

    # 我的数据-ebay取消开发接口
    ebay_cancelDevelopment_url = InterfaceCommonInfo.common_url + "/das/ebay/AccountProductInfo/cancelDevelopment"

    # 我的数据-shopee查询接口
    shopee_queryListing_url = InterfaceCommonInfo.common_url + "/das/shopee/AccountProductInfo/queryShopeePageList"

    # 我的数据-shopee释放产品接口
    shopee_releaseProduct_url = InterfaceCommonInfo.common_url + "/das/shopee/AccountProductInfo/releaseProduct"

    # 我的数据-shopee关联系统SKU接口
    shopee_associateSySku_url = InterfaceCommonInfo.common_url + "/das/shopee/AccountProductInfo/associatedSystemSku"

    # 我的数据-shopee取消开发接口
    shopee_cancelDevelopment_url = InterfaceCommonInfo.common_url + "/das/shopee/AccountProductInfo/cancelDevelopment"

    # 数据采集-Amazon查询接口（bestsellers/NewRelease/MoversShakers/MostWishedFor/Giftldeas）
    amazon_dataSampleListing_url = InterfaceCommonInfo.common_url + "/das/amazonRankListing/queryAmazonRankListing"

    # 数据采集-Amazon关注店铺数据/关注分类数据查询接口
    amazon_attentStoreListing_url = InterfaceCommonInfo.common_url + "/das/amazon/baselisting"

    # 数据采集-Amazon认领产品接口
    amazon_claimProduct_url = InterfaceCommonInfo.common_url + "/das/amazonRankListing/claimAmazonRankListing"

    # 数据采集-Amazon禁用接口
    amazon_disableProduct_url = InterfaceCommonInfo.common_url + "/das/amazonRankListing/disableAmazonRankListing"

    # 数据采集-Amazon启用接口
    amazon_enableProduct_url = InterfaceCommonInfo.common_url + "/das/amazonRankListing/enableAmazonRankListing"

    # 数据采集-Amazon删除接口
    amazon_deleteProduct_url = InterfaceCommonInfo.common_url + "/das/amazonRankListing/deleteAmazonRankListing"

    # 数据采集-Amazon分配接口
    amazon_allocationProduct_url = InterfaceCommonInfo.common_url + "/das/amazonRankListing/allocationAmazonRankListing"

    # 数据采集-SMT查询接口
    smt_dataSampleListing_url = InterfaceCommonInfo.common_url + "/das/smt/querySmtBaseListingPageList"

    # 数据采集-SMT认领产品接口
    smt_claimProduct_url = InterfaceCommonInfo.common_url + "/das/smt/claimSmtBaseListing"

    # 数据采集-1688查询接口
    ali_dataSampleListing_url = InterfaceCommonInfo.common_url + "/das/ali1688/queryAli1688PageList"

    # 数据采集-1688认领产品接口
    ali_claimProduct_url = InterfaceCommonInfo.common_url + "/das/ali1688/claimAli1688BaseListing"

    # 数据采集-ebay认领产品接口
    ebay_claimProduct_url = InterfaceCommonInfo.common_url + "/das/ebay/claimEbayBaseListing"

    # 数据采集-shopee认领产品接口
    shopee_claimProduct_url = InterfaceCommonInfo.common_url + "/das/shopee/claimShopeeBaseListing"




    # 参数配置-取消开发备注保存接口
    paramConfigSave_url = InterfaceCommonInfo.common_url + "/das/parameterConfiguration/updateCancelDevNotesInfo"

    # 参数配置-取消开发备注查询接口
    paramConfigSelect_url = InterfaceCommonInfo.common_url + "/das/parameterConfiguration/queryCancelDevNotesInfo"