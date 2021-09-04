# -*- coding:utf-8 -*-
#!/usr/bin/python3

'''
@File: fmisSystem_interface_url.py
@time:2021/9/4
@Author:majiaqin 170479
@Desc:财务系统接口地址
'''
from apps.Common_Config.interface_common_info import InterfaceCommonInfo

class FmisApiUrl:
    '''财务管理-财务报表'''
    # 资金收入日报表&资金支出日报表&资金余额日报表&资金对比日报表-查询&添加&删除接口
    fmis_fundReport_query_url = InterfaceCommonInfo.common_url + "/fmis/fundReport"

    '''财务管理-第三方收款-Payoneer收款'''
    # 查询接口
    fmis_payoneer_query_url = InterfaceCommonInfo.common_url + "/fmis/thirdPartyAccount"
    # 刷新接口
    fmis_payoneer_refresh_url = InterfaceCommonInfo.common_url + "/fmis/thirdPartyAccountBalance/refresh/balance"
    # 查询汇总数据接口
    fmis_payoneer_total_url = InterfaceCommonInfo.common_url + "/fmis/thirdPartyAccountBalance/balance/query"
    # 跳转交易明细接口
    fmis_payoneer_detail_url = InterfaceCommonInfo.common_url + "/fmis/transactionDetail/email/list"
    # 查询交易明细接口
    fmis_payoneer_querydetail_url = InterfaceCommonInfo.common_url + "/fmis/transactionDetail/searchTransactionDetail"
    # 同步交易明细接口
    fmis_payoneer_synchronous_url = InterfaceCommonInfo.common_url + "/fmis/transactionDetail/synchronous/transaction"

    '''财务管理-第三方收款-pingpong收款'''
    # 账号管理-查询接口
    fmis_pingpong_queryaccount_url = InterfaceCommonInfo.common_url + "/fmis/pingPong"
    # 账号管理-查询币种汇总余额接口
    fmis_pingpong_querydetail_url = InterfaceCommonInfo.common_url + "/fmis/pingPong/balance/query"
    # 账号管理-同步店铺接口
    fmis_pingpong_batchSyncAccount_url = InterfaceCommonInfo.common_url + "/fmis/pingPong/batchSyncAccount"
    # 账号管理-同步余额接口
    fmis_pingpong_batchSyncBalance_url = InterfaceCommonInfo.common_url + "/fmis/pingPong/batchSyncBalance"

    # 账单明细-查询接口
    fmis_pingpong_querytransfer_url = InterfaceCommonInfo.common_url + "/fmis/transfer"
    # 账单明细-同步账单明细接口
    fmis_pingpong_batchSyncDetail_url = InterfaceCommonInfo.common_url + "/fmis/transfer/batchSyncDetail"

    # 系统店铺账号映射-查询接口
    fmis_pingpong_systemShopMapping_query_url = InterfaceCommonInfo.common_url + "/fmis/systemShopMapping/list"
    # 系统店铺账号映射-批量删除接口
    fmis_pingpong_systemShopMapping_delete_url = InterfaceCommonInfo.common_url + "/fmis/systemShopMapping/delete"
    # 系统店铺账号映射-获取店铺名称接口
    fmis_pingpong_systemShopMapping_getAccountNameList_url = InterfaceCommonInfo.common_url + "/fmis/systemShopMapping/getAccountNameList"

    # 账号申请-查询接口
    fmis_pingpong_AccountApply_url = InterfaceCommonInfo.common_url + "/fmis/pingPongAccountApply/selectPingPongApplyNewAccount"
    # 账号申请-获取申请人接口
    fmis_pingpong_getApplicant_url = InterfaceCommonInfo.common_url + "/fmis/pingPongAccountApply/selectApplicant"
    # 账号申请-获取申请部门接口
    fmis_pingpong_getApplyDepartment_url = InterfaceCommonInfo.common_url + "/fmis/pingPongAccountApply/selectApplyDepartment"
    # 账号申请-根据平台关联店铺接口
    fmis_pingpong_platform_url = InterfaceCommonInfo.common_url + "/fmis/pingPongAccountApply/selectRelateStore/platform"
    # 账号申请-增加申请接口
    fmis_pingpong_addApply_url = InterfaceCommonInfo.common_url + "fmis/pingPongAccountApply/pingPongApplyNewAccount"

    '''财务管理-第三方收款-平台对账流程'''
    # 平台对账-获取收款方式接口
    fmis_platformCheck_getAllPayType_url = InterfaceCommonInfo.common_url + "/fmis/platformCheckDifferenceData/getAllPayType"
    # 平台对账-获取销售平台接口
    fmis_platformCheck_getSalesPlatform_url = InterfaceCommonInfo.common_url + "/fmis/platformCheckDifferenceData/getSalesPlatform"
    # 平台对账-获取店铺接口&lazada平台账单-获取店铺接口
    fmis_platformCheck_getAllSaleAccount_url = InterfaceCommonInfo.common_url + "/fmis/platformCheckDifferenceData/getAllSaleAccount"
    # 平台对账-查询差异数据接口
    fmis_platformCheck_querydiff_url = InterfaceCommonInfo.common_url + "/fmis/platformCheckDifferenceData/list"
    # 平台对账-查询已匹配数据接口
    fmis_platformCheck_querymatch_url = InterfaceCommonInfo.common_url + "/fmis/platformCheckMatchData/list"

    # lazada平台账单-查询接口
    fmis_lazadaFinancePayout_query_url = InterfaceCommonInfo.common_url + "/fmis/lazadaFinancePayout/list"

    '''财务管理-第三方收款-连连收款'''
    # 账号管理-获取店铺状态接口&获取连连账号接口&获取持有人名称接口&获取币种汇总金额接口&获取账号数据接口&查询接口
    fmis_lianlian_url = InterfaceCommonInfo.common_url + "/fmis/lianLian"
    # 账号管理-获取平台店铺接口
    fmis_lianlian_platformAccount_url = InterfaceCommonInfo.common_url + "/fmis/accountBindPlatform/query/platformAccount"
    # 账号管理-同步接口
    fmis_lianlian_syncAccount_url = InterfaceCommonInfo.common_url + "/fmis/lianLian/syncAccount"
    # 账号管理-申请境外卡接口
    fmis_lianlian_applyCard_url = InterfaceCommonInfo.common_url + "/fmis/lianLian/applyCard"

    # 交易明细-获取平台数据&获取交易状态数据&获取币种数据&查询交易明细数据
    fmis_lianLianEntryDetail_url = InterfaceCommonInfo.common_url + "/fmis/lianLianEntryDetail"
    # 交易明细-同步交易明细
    fmis_lianLianEntryDetail_syncEntryDetail_url = InterfaceCommonInfo.common_url + "/fmis/lianLianEntryDetail/syncEntryDetail"

    '''财务管理-第三方收款-Paypal'''
    # Paypal余额-获取Paypal账号接口
    fmis_paypal_getAllPayPalAccount_url = InterfaceCommonInfo.common_url + "/fmis/paypalSyncAccountBalance/getAllPayPalAccount"
    # Paypal余额-查询接口
    fmis_paypal_query_url = InterfaceCommonInfo.common_url + "/fmis/paypalSyncAccountBalance/getList"
    # Paypal余额-同步余额接口
    fmis_paypal_sychAllAccountBalance_url = InterfaceCommonInfo.common_url + "/fmis/paypalSyncAccountBalance/sychAllAccountBalance"

    # Paypal账户信息管理-获取Paypal账号接口
    fmis_newPaypalAccount_getAllPayPalAccount_url = InterfaceCommonInfo.common_url + "/fmis/newPaypalAccount/getPaypalAccountList"
    # Paypal账户信息管理-查询接口
    fmis_newPaypalAccount_query_url = InterfaceCommonInfo.common_url + "/fmis/newPaypalAccount/getNewPaypalAccountList"
    # Paypal账户信息管理-添加&保存账号接口
    fmis_newPaypalAccount_addAccount_url = InterfaceCommonInfo.common_url + "/fmis/newPaypalAccount/addPaypalAccount"

    '''财务管理-财务审核'''
    # 库存报废审核-获取审核状态接口&库存外界审核-获取审核状态接口
    fmis_whLendAudit_getAllStatus_url = InterfaceCommonInfo.common_url + "/fmis/whLendAudit/getAllStatus"
    # 库存报废审核-查询接口
    fmis_whScrap_query_url = InterfaceCommonInfo.common_url + "/fmis/whScrap/list"
    # 库存报废审核-通过接口
    fmis_whScrap_pass_url = InterfaceCommonInfo.common_url + "/fmis/whScrap/change/3/67"
    # 库存报废审核-驳回接口
    fmis_whScrap_reject_url = InterfaceCommonInfo.common_url + "/fmis/whScrap/change/6/67"

    # 库存外界审核-查询接口
    fmis_whLendAudit_query_url = InterfaceCommonInfo.common_url + "/fmis/whLendAudit/list"
    # 库存外界审核-通过接口
    fmis_whLendAudit_pass_url = InterfaceCommonInfo.common_url + "/fmis/whLendAudit/change/3/67"
    # 库存外界审核-驳回接口
    fmis_whLendAudit_reject_url = InterfaceCommonInfo.common_url + "/fmis/whLendAudit/change/6/67"

    # 外借核销-查询接口
    fmis_whVerification_query_url = InterfaceCommonInfo.common_url + "/fmis/whVerification/getVerificationInfoByPage"

    # 供应商资料审核-获取处理状态接口
    fmis_vendorVerifyRecord_getAllStatus_url = InterfaceCommonInfo.common_url + "/fmis/vendorVerifyRecord/getAllStatus"
    # 供应商资料审核-获取创建人接口
    fmis_vendorVerifyRecord_getUserByDeptName_url = InterfaceCommonInfo.common_url + "/fmis/vendorVerifyRecord/getUserByDeptName"
    # 供应商资料审核-查询接口
    fmis_vendorVerifyRecord_query_url = InterfaceCommonInfo.common_url + "/fmis/vendorVerifyRecord/getVerifyVendorInfo"
    # 供应商资料审核-通过&驳回接口
    fmis_vendorVerifyRecord_verifyVendorInfo_url = InterfaceCommonInfo.common_url + "/fmis/vendorVerifyRecord/verifyVendorInfo"

    '''财务管理-付款管理'''
    # 付款单-获取物流商接口&预付帐户-预付帐户管理-获取物流商接口&预付帐户-账户明细-获取物流商接口
    fmis_oaccount_selectOAccountList_url = InterfaceCommonInfo.common_url + "/fmis/oaccount/selectOAccountList"
    # 付款单-查询接口
    fmis_paymentRecord_query_url = InterfaceCommonInfo.common_url + "/fmis/paymentRecord/page"
    # 付款单-支付接口
    fmis_paymentRecord_updateById_url = InterfaceCommonInfo.common_url + "/fmis/paymentRecord/updateById"
    # 付款单-详情接口
    fmis_paymentRecord_getById_url = InterfaceCommonInfo.common_url + "/fmis/paymentRecord/getById/73"

    # 预付帐户-预付帐户管理-查询接口
    fmis_oaccount_selectOAccount_url = InterfaceCommonInfo.common_url + "/fmis/oaccount/selectOAccount"
    # 预付帐户-预付帐户管理-余额变更接口
    fmis_oaccount_updateAccountBalance_url = InterfaceCommonInfo.common_url + "/fmis/oaccount/updateAccountBalance"

    # 预付帐户-账户明细-查询接口
    fmis_oaccountPaymentDetails_selectPaymentDetail_url = InterfaceCommonInfo.common_url + "/fmis/oaccountPaymentDetails/selectPaymentDetail"

    '''绩效管理-绩效管理'''
    # Amazon员工绩效

if __name__ == '__main__':
    pass