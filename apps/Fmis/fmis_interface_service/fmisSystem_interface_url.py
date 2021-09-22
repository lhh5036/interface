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
    fundReport_query_url = InterfaceCommonInfo.common_url + "/fmis/fundReport"

    '''财务管理-第三方收款-Payoneer收款'''
    # 查询接口
    payoneer_query_url = InterfaceCommonInfo.common_url + "/fmis/thirdPartyAccount"
    # 刷新接口
    payoneer_refresh_url = InterfaceCommonInfo.common_url + "/fmis/thirdPartyAccountBalance/refresh/balance"
    # 查询汇总数据接口
    payoneer_total_url = InterfaceCommonInfo.common_url + "/fmis/thirdPartyAccountBalance/balance/query"
    # 跳转交易明细接口
    payoneer_detail_url = InterfaceCommonInfo.common_url + "/fmis/transactionDetail/email/list"
    # 查询交易明细接口
    payoneer_querydetail_url = InterfaceCommonInfo.common_url + "/fmis/transactionDetail/searchTransactionDetail"
    # 同步交易明细接口
    payoneer_synchronous_url = InterfaceCommonInfo.common_url + "/fmis/transactionDetail/synchronous/transaction"

    '''财务管理-第三方收款-pingpong收款'''
    # 账号管理-查询接口
    pingpong_queryaccount_url = InterfaceCommonInfo.common_url + "/fmis/pingPong"
    # 账号管理-查询币种汇总余额接口
    pingpong_querydetail_url = InterfaceCommonInfo.common_url + "/fmis/pingPong/balance/query"
    # 账号管理-同步店铺接口
    pingpong_batchSyncAccount_url = InterfaceCommonInfo.common_url + "/fmis/pingPong/batchSyncAccount"
    # 账号管理-同步余额接口
    pingpong_batchSyncBalance_url = InterfaceCommonInfo.common_url + "/fmis/pingPong/batchSyncBalance"

    # 账单明细-查询接口
    pingpong_querytransfer_url = InterfaceCommonInfo.common_url + "/fmis/transfer"
    # 账单明细-同步账单明细接口
    pingpong_batchSyncDetail_url = InterfaceCommonInfo.common_url + "/fmis/transfer/batchSyncDetail"

    # 系统店铺账号映射-查询接口
    pingpong_systemShopMapping_query_url = InterfaceCommonInfo.common_url + "/fmis/systemShopMapping/list"
    # 系统店铺账号映射-批量删除接口
    pingpong_systemShopMapping_delete_url = InterfaceCommonInfo.common_url + "/fmis/systemShopMapping/delete"
    # 系统店铺账号映射-获取店铺名称接口
    pingpong_systemShopMapping_getAccountNameList_url = InterfaceCommonInfo.common_url + "/fmis/systemShopMapping/getAccountNameList"

    # 账号申请-查询接口
    pingpong_AccountApply_url = InterfaceCommonInfo.common_url + "/fmis/pingPongAccountApply/selectPingPongApplyNewAccount"
    # 账号申请-获取申请人接口
    pingpong_getApplicant_url = InterfaceCommonInfo.common_url + "/fmis/pingPongAccountApply/selectApplicant"
    # 账号申请-获取申请部门接口
    pingpong_getApplyDepartment_url = InterfaceCommonInfo.common_url + "/fmis/pingPongAccountApply/selectApplyDepartment"
    # 账号申请-根据平台关联店铺接口
    pingpong_platform_url = InterfaceCommonInfo.common_url + "/fmis/pingPongAccountApply/selectRelateStore/platform"
    # 账号申请-增加申请接口
    pingpong_addApply_url = InterfaceCommonInfo.common_url + "fmis/pingPongAccountApply/pingPongApplyNewAccount"

    '''财务管理-第三方收款-平台对账流程'''
    # 平台对账-获取收款方式接口
    platformCheck_getAllPayType_url = InterfaceCommonInfo.common_url + "/fmis/platformCheckDifferenceData/getAllPayType"
    # 平台对账-获取销售平台接口
    platformCheck_getSalesPlatform_url = InterfaceCommonInfo.common_url + "/fmis/platformCheckDifferenceData/getSalesPlatform"
    # 平台对账-获取店铺接口&lazada平台账单-获取店铺接口
    platformCheck_getAllSaleAccount_url = InterfaceCommonInfo.common_url + "/fmis/platformCheckDifferenceData/getAllSaleAccount"
    # 平台对账-查询差异数据接口
    platformCheck_querydiff_url = InterfaceCommonInfo.common_url + "/fmis/platformCheckDifferenceData/list"
    # 平台对账-查询已匹配数据接口
    platformCheck_querymatch_url = InterfaceCommonInfo.common_url + "/fmis/platformCheckMatchData/list"

    # lazada平台账单-查询接口
    lazadaFinancePayout_query_url = InterfaceCommonInfo.common_url + "/fmis/lazadaFinancePayout/list"

    '''财务管理-第三方收款-连连收款'''
    # 账号管理-获取店铺状态接口&获取连连账号接口&获取持有人名称接口&获取币种汇总金额接口&获取账号数据接口&查询接口
    lianlian_url = InterfaceCommonInfo.common_url + "/fmis/lianLian"
    # 账号管理-获取平台店铺接口
    lianlian_platformAccount_url = InterfaceCommonInfo.common_url + "/fmis/accountBindPlatform/query/platformAccount"
    # 账号管理-同步接口
    lianlian_syncAccount_url = InterfaceCommonInfo.common_url + "/fmis/lianLian/syncAccount"
    # 账号管理-申请境外卡接口
    lianlian_applyCard_url = InterfaceCommonInfo.common_url + "/fmis/lianLian/applyCard"

    # 交易明细-获取平台数据&获取交易状态数据&获取币种数据&查询交易明细数据
    lianLianEntryDetail_url = InterfaceCommonInfo.common_url + "/fmis/lianLianEntryDetail"
    # 交易明细-同步交易明细
    lianLianEntryDetail_syncEntryDetail_url = InterfaceCommonInfo.common_url + "/fmis/lianLianEntryDetail/syncEntryDetail"

    '''财务管理-第三方收款-Paypal'''
    # Paypal余额-获取Paypal账号接口
    paypal_getAllPayPalAccount_url = InterfaceCommonInfo.common_url + "/fmis/paypalSyncAccountBalance/getAllPayPalAccount"
    # Paypal余额-查询接口
    paypal_query_url = InterfaceCommonInfo.common_url + "/fmis/paypalSyncAccountBalance/getList"
    # Paypal余额-同步余额接口
    paypal_sychAllAccountBalance_url = InterfaceCommonInfo.common_url + "/fmis/paypalSyncAccountBalance/sychAllAccountBalance"

    # Paypal账户信息管理-获取Paypal账号接口
    newPaypalAccount_getAllPayPalAccount_url = InterfaceCommonInfo.common_url + "/fmis/newPaypalAccount/getPaypalAccountList"
    # Paypal账户信息管理-查询接口
    newPaypalAccount_query_url = InterfaceCommonInfo.common_url + "/fmis/newPaypalAccount/getNewPaypalAccountList"
    # Paypal账户信息管理-添加&保存账号接口
    newPaypalAccount_addAccount_url = InterfaceCommonInfo.common_url + "/fmis/newPaypalAccount/addPaypalAccount"

    '''财务管理-财务审核'''
    # 库存报废审核-获取审核状态接口&库存外界审核-获取审核状态接口
    whLendAudit_getAllStatus_url = InterfaceCommonInfo.common_url + "/fmis/whLendAudit/getAllStatus"
    # 库存报废审核-查询接口
    whScrap_query_url = InterfaceCommonInfo.common_url + "/fmis/whScrap/list"
    # 库存报废审核-通过接口
    whScrap_pass_url = InterfaceCommonInfo.common_url + "/fmis/whScrap/change/3/67"
    # 库存报废审核-驳回接口
    whScrap_reject_url = InterfaceCommonInfo.common_url + "/fmis/whScrap/change/6/67"

    # 库存外界审核-查询接口
    whLendAudit_query_url = InterfaceCommonInfo.common_url + "/fmis/whLendAudit/list"
    # 库存外界审核-通过接口
    whLendAudit_pass_url = InterfaceCommonInfo.common_url + "/fmis/whLendAudit/change/3/67"
    # 库存外界审核-驳回接口
    whLendAudit_reject_url = InterfaceCommonInfo.common_url + "/fmis/whLendAudit/change/6/67"

    # 外借核销-查询接口
    whVerification_query_url = InterfaceCommonInfo.common_url + "/fmis/whVerification/getVerificationInfoByPage"

    # 供应商资料审核-获取处理状态接口
    vendorVerifyRecord_getAllStatus_url = InterfaceCommonInfo.common_url + "/fmis/vendorVerifyRecord/getAllStatus"
    # 供应商资料审核-获取创建人接口
    vendorVerifyRecord_getUserByDeptName_url = InterfaceCommonInfo.common_url + "/fmis/vendorVerifyRecord/getUserByDeptName"
    # 供应商资料审核-查询接口
    vendorVerifyRecord_query_url = InterfaceCommonInfo.common_url + "/fmis/vendorVerifyRecord/getVerifyVendorInfo"
    # 供应商资料审核-通过&驳回接口
    vendorVerifyRecord_verifyVendorInfo_url = InterfaceCommonInfo.common_url + "/fmis/vendorVerifyRecord/verifyVendorInfo"

    '''财务管理-付款管理'''
    # 付款单-获取物流商接口&预付帐户-预付帐户管理-获取物流商接口&预付帐户-账户明细-获取物流商接口
    oaccount_selectOAccountList_url = InterfaceCommonInfo.common_url + "/fmis/oaccount/selectOAccountList"
    # 付款单-查询接口
    paymentRecord_query_url = InterfaceCommonInfo.common_url + "/fmis/paymentRecord/page"
    # 付款单-支付接口
    paymentRecord_updateById_url = InterfaceCommonInfo.common_url + "/fmis/paymentRecord/updateById"
    # 付款单-详情接口
    paymentRecord_getById_url = InterfaceCommonInfo.common_url + "/fmis/paymentRecord/getById/73"

    # 预付帐户-预付帐户管理-查询接口
    oaccount_selectOAccount_url = InterfaceCommonInfo.common_url + "/fmis/oaccount/selectOAccount"
    # 预付帐户-预付帐户管理-余额变更接口
    oaccount_updateAccountBalance_url = InterfaceCommonInfo.common_url + "/fmis/oaccount/updateAccountBalance"

    # 预付帐户-账户明细-查询接口
    oaccountPaymentDetails_selectPaymentDetail_url = InterfaceCommonInfo.common_url + "/fmis/oaccountPaymentDetails/selectPaymentDetail"

    '''绩效管理'''
    # Amazon员工绩效-获取公司&部别&组别数据接口&获取列表数据接口
    amazonStaffPerformance_url = InterfaceCommonInfo.common_url + "fmis/amazonStaffPerformance"

    # Amazon&SMT&eBay&wish&joom&shopee&lazada绩效明细&部门绩效汇总-获取表头&平台&部门&组织架构&组长&组员&列表信息接口
    departmentPerformance_url = InterfaceCommonInfo.common_url + "fmis/departmentPerformance"

    # 产品开发新品转化绩效-获取产品开发信息&获取列表数据接口
    transformPerformance_url = InterfaceCommonInfo.common_url + "fmis/transformPerformance"

    '''交易数据'''
    # 销售结汇明细-获取列表数据接口
    settlementExchange_url = InterfaceCommonInfo.common_url + "fmis/settlementExchange"

    '''交易数据-平台账单'''
    # 平台账单-SMT-账单数据&退款详情&支付宝报告-获取账号接口
    smtPlatformBill_getSmtSellerAccount_url = InterfaceCommonInfo.common_url + "fmis/smtPlatformBill/getSmtSellerAccount"
    # 平台账单-SMT-账单数据-获取销售接口
    smtPlatformBill_selectSmtSellers_url = InterfaceCommonInfo.common_url + "fmis/smtPlatformBill/selectSmtSellers"
    # 平台账单-SMT-账单数据-获取列表数据接口
    smtPlatformBill_getSmtPlatFormBill_url = InterfaceCommonInfo.common_url + "fmis/smtPlatformBill/getSmtPlatFormBill"

    # 平台账单-SMT-退款详情-获取列表数据接口
    smtRefundInfoDetail_getSmtRefundInfoDetail_url = InterfaceCommonInfo.common_url + "fmis/smtRefundInfoDetail/getSmtRefundInfoDetail"

    # 平台账单-SMT-支付宝报告-获取下载链接接口
    fileStore_export_smt_alipay_file_url = InterfaceCommonInfo.common_url + "fmis/fileStore/selectFileListByType/export_smt_alipay_file"
    # 平台账单-SMT-支付宝报告-获取列表数据接口
    smtAlipayReport_getSmtAlipayReport_url = InterfaceCommonInfo.common_url + "fmis/smtAlipayReport/getSmtAlipayReport"

    # 平台账单-WISH-账单数据&交易退款汇总-获取账号接口
    wishPlatformBill_selectWishAccounts_url = InterfaceCommonInfo.common_url + "fmis/wishPlatformBill/selectWishAccounts"
    # 平台账单-WISH-账单数据&交易退款汇总-获取销售接口
    wishPlatformBill_selectSellers_url = InterfaceCommonInfo.common_url + "fmis/wishPlatformBill/selectSellers"
    # 平台账单-WISH-账单数据-获取列表数据接口
    wishPlatformBill_selectWishPlatformBill_url = InterfaceCommonInfo.common_url + "fmis/wishPlatformBill/selectWishPlatformBill"

    # 平台账单-WISH-交易退款汇总-获取列表数据接口
    wishPlatformRefund_selectWishRefundDetail_url = InterfaceCommonInfo.common_url + "fmis/wishPlatformRefund/selectWishRefundDetail"

    '''成本管理'''
    # 在途明细表-获取列表数据接口
    cost_list_url = InterfaceCommonInfo.common_url + "fmis/cost/list"
    # 在途明细表-获取汇总数据接口
    cost_sum_url = InterfaceCommonInfo.common_url + "fmis/cost/sum"

    '''系统设置'''
    # 加班提成比例配置&阶梯底薪配置-获取部门&创建人&列表数据接口
    newRatioSetting_url = InterfaceCommonInfo.common_url + "fmis/newRatioSetting"

    # 阶梯底薪配置-获取公司&列表数据接口
    salarySetting_url = InterfaceCommonInfo.common_url + "fmis/salarySetting"

    # 产品开发转化目标配置-获取创建人接口
    newProductTarget_getCreateList_url = InterfaceCommonInfo.common_url + "fmis/tranParam/newProductTarget/getCreateList"
    # 产品开发转化目标配置-获取新品目标值列表数据接口
    tranParam_newProductTarget_list_url = InterfaceCommonInfo.common_url + "/fmis/tranParam/newProductTarget/list"
    # 产品开发转化目标配置-获取高价值目标值列表数据接口
    tranParam_highValueTarget_list_url = InterfaceCommonInfo.common_url + "fmis/tranParam/highValueTarget/list"
    # 产品开发转化目标配置-获取操作日志列表数据接口
    tranParam_targetLog_list_url = InterfaceCommonInfo.common_url + "fmis/tranParam/targetLog/list"

if __name__ == '__main__':
    pass