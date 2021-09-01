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

    # 数据采集-Amazon获取分配人接口
    amazon_allocationPerson_url = InterfaceCommonInfo.common_url + "/das/usermgtn/getAmazonUserListByJobNumber"

    # 数据采集-Amazon分配接口
    amazon_allocationProduct_url = InterfaceCommonInfo.common_url + "/das/amazonRankListing/allocationAmazonRankListing"

    # 数据采集-Amazon关联系统SKU接口
    amazon_dataSample_associate_url = InterfaceCommonInfo.common_url + "/das/amazonRankListing/associatedSystemSku"

    # 数据采集-SMT查询接口
    smt_dataSampleListing_url = InterfaceCommonInfo.common_url + "/das/smt/querySmtBaseListingPageList"

    # 数据采集-SMT认领产品接口
    smt_claimProduct_url = InterfaceCommonInfo.common_url + "/das/smt/claimSmtBaseListing"

    # 数据采集-SMT删除接口
    smt_deleteProduct_url = InterfaceCommonInfo.common_url + "/das/smt/deleteSmtBaseListing"

    # 数据采集-SMT禁用接口
    smt_disableProduct_url = InterfaceCommonInfo.common_url + "/das/smt/unenableSmtBaseListing"

    # 数据采集-SMT启用接口
    smt_enableProduct_url = InterfaceCommonInfo.common_url + "/das/smt/enableSmtBaseListing"

    # 数据采集-SMT关联系统SKU接口
    smt_dataSample_associate_url = InterfaceCommonInfo.common_url + "/das/smt/associatedSystemSku"

    # 数据采集-SMT获取分配人接口
    smt_allocationPerson_url = InterfaceCommonInfo.common_url + "/das/usermgtn/getUserListByJobNumber"

    # 数据采集-SMT分配接口
    smt_allocationProduct_url = InterfaceCommonInfo.common_url + "/das/smt/allocationSmtBaseListing"

    # 数据采集-1688查询接口
    ali_dataSampleListing_url = InterfaceCommonInfo.common_url + "/das/ali1688/queryAli1688PageList"

    # 数据采集-1688认领产品接口
    ali_claimProduct_url = InterfaceCommonInfo.common_url + "/das/ali1688/claimAli1688BaseListing"

    # 1688校验产品是否已经认领接口地址
    ali_checkProductByRank_url = InterfaceCommonInfo.common_url + "/das/account/checkAccountProductInfo"
    # 数据采集-1688禁用接口
    ali_disableProduct_url = InterfaceCommonInfo.common_url + "/das/ali1688/unenableAli1688BaseListing"
    # 数据采集-1688启用接口
    ali_enableProduct_url = InterfaceCommonInfo.common_url + "/das/ali1688/enableAli1688BaseListing"
    # 数据采集-1688删除接口
    ali_deleteProduct_url = InterfaceCommonInfo.common_url + "/das/ali1688/deleteAli1688BaseListing"
    # 数据采集-1688关联系统SKU
    ali_dataSample_associate_url = InterfaceCommonInfo.common_url + "/das/ali1688/associatedSystemSku"
    # 数据采集-1688获取分配人接口
    ali_allocationPerson_url = InterfaceCommonInfo.common_url + "/das/usermgtn/getAli1688UserListByJobNumber"
    # 数据采集-1688分配接口
    ali_allocationProduct_url = InterfaceCommonInfo.common_url + "das/ali1688/allocationAli1688BaseListing"


    # 数据采集-ebay查询接口
    ebay_dataSampleListing_url = InterfaceCommonInfo.common_url + "/das/ebay/queryEbayPageList"
    # 数据采集-ebay认领产品接口
    ebay_claimProduct_url = InterfaceCommonInfo.common_url + "/das/ebay/claimEbayBaseListing"
    # 数据采集-ebay禁用接口
    ebay_disableProduct_url = InterfaceCommonInfo.common_url + "/das/ebay/unenableEbayBaseListing"
    # 数据采集-ebay启用接口
    ebay_enableProduct_url = InterfaceCommonInfo.common_url + "/das/ebay/enableEbayBaseListing"
    # 数据采集-ebay删除接口
    ebay_deleteProduct_url = InterfaceCommonInfo.common_url + "/das/ebay/deleteEbayBaseListing"
    # 数据采集-ebay关联系统SKU
    ebay_dataSample_associate_url = InterfaceCommonInfo.common_url + "/das/ebay/associatedSystemSku"
    # 数据采集-ebay获取分配人接口
    ebay_allocationPerson_url = InterfaceCommonInfo.common_url + "/das/usermgtn/getEbayUserListByJobNumber"
    # 数据采集-ebay分配接口
    ebay_allocationProduct_url = InterfaceCommonInfo.common_url + "/das/ebay/allocationEbayBaseListing"


    # 数据采集-shopee查询接口
    shopee_dataSampleListing_url = InterfaceCommonInfo.common_url + "/das/shopee/queryShopeePageList"
    # 数据采集-shopee认领产品接口
    shopee_claimProduct_url = InterfaceCommonInfo.common_url + "/das/shopee/claimShopeeBaseListing"
    # 数据采集-shopee禁用接口
    shopee_disableProduct_url = InterfaceCommonInfo.common_url + "/das/shopee/unenableShopeeBaseListing"
    # 数据采集-shopee启用接口
    shopee_enableProduct_url = InterfaceCommonInfo.common_url + "/das/shopee/enableShopeeBaseListing"
    # 数据采集-shopee删除接口
    shopee_deleteProduct_url = InterfaceCommonInfo.common_url + "/das/shopee/deleteShopeeBaseListing"
    # 数据采集-shopee关联系统SKU
    shopee_dataSample_associate_url = InterfaceCommonInfo.common_url + "/das/shopee/associatedSystemSku"
    # 数据采集-shopee获取分配人接口
    shopee_allocationPerson_url = InterfaceCommonInfo.common_url + "/das/usermgtn/getShopeeUserListByJobNumber"
    # 数据采集-ebay分配接口
    shopee_allocationProduct_url = InterfaceCommonInfo.common_url + "/das/shopee/allocationShopeeBaseListing"




    # 参数配置-取消开发备注保存接口
    paramConfigSave_url = InterfaceCommonInfo.common_url + "/das/parameterConfiguration/updateCancelDevNotesInfo"

    # 参数配置-取消开发备注查询接口
    paramConfigSelect_url = InterfaceCommonInfo.common_url + "/das/parameterConfiguration/queryCancelDevNotesInfo"