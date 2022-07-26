'''
@File: saleSystem_interface_param.py
@time:2022/1/18
@Author:quanliu 181324
@Desc:订单系统接口入参
'''

class SaleApiInputParam:
    true = True
    null = None
    false = False
    # 系统订单接口入参
    systemOrder_query_param01 = {"args": "{0}", "method": "listCustomerOrder"}
    systemOrder_query_param02 = {"search": {0}, "offset": 0, "limit": 200}
    systemOrder_query_param03 = {"salesSubsectorLeaderSet":[],"salesTeamLeaderSet":[],"salesmanSet":[],"salesJuniorSupervisorSet":[],"saleChannel":"","history":"false","orderStatus":"0","withoutProfitInfo":0}

    # 生成系统订单（lazada平台）
    lazadaGenerateSysOrder_param01 = [{"saleChannelOrderId": {0}, "accountNumber": {1}}]

    # 生成系统订单（其他平台）
    otherGenerateSysOrder_param01 = {"args":"{0}","method":"generateCustomerOrder"}
    otherGenerateSysOrder_param02 = {"saleChannel": "{saleChannel}", "saleChannelOrderId": "{saleChannelOrderId}"}

    # 同步追踪号
    syncLogisticsTracking_param01 = {"args": "{0}", "method": "syncLogisticsTracking"}
    syncLogisticsTracking_param02 = ["{0}"]

    # SMT平台查询订单界面——查询订单状态：等待您发货
    smtQueryStatus_param01 = {"args":"{0}","method":"listAliexpressOrder"}
    smtQueryStatus_param02 = {"search":{0},"pageReqired":"true" ,"limit":200 ,"offset":0,"sort":"gmt_create","order":"desc"}
    smtQueryStatus_param03 = {"orderAmountStart":"null","orderAmountEnd":"null"}

    # SMT平台查询订单——查询订单状态+销售账号：xxx + 等待您发货
    smtAccountNumber_param01 = {"args":"{0}","method":"listAliexpressOrder"}
    smtAccountNumber_param02 = {"search":{0},"pageReqired":"true","limit":200,"offset":0,"sort":"gmt_create","order":"desc"}
    smtAccountNumber_param03 = {"accountNumber":"{accountNumber}","orderStatus":"{orderStatus}","orderAmountStart":"null","orderAmountEnd":"null"}

    # 查询资费国家
    tariffCountry_param01 = {"args": "", "method": "getCountry"}
    tariffCountry_param02 = {"search": {0}, "limit": 20, "offset": 0, "pageReqired": true, "sort": "id", "order": "desc"}
    tariffCountry_param03 = {"name": "chineseName", "inputText": ""}

    # 查询黑名单买家
    blackedBuyer_param01 = {"args": "", "method": "getBlackedBuyerList"}
    blackedBuyer_param02 = {"search": {0}, "offset": 0, "limit": 10}
    blackedBuyer_param03 = {"saleChannel": "", "accountNumber": "", "customerName": "",
                            "blackedType": "", "recipientName": ""}

    # # SMT平台查询订单——查询平台订单号
    # smtPlatformOrder_param01 = {"args":"{0}","method": "listAliexpressOrder"}
    # smtPlatformOrder_param02 = {"search":{0},"pageReqired": "true", "limit": 200,"offset": 0,"sort":"gmt_create","order":"desc"}
    # smtPlatformOrder_param03 = {"orderId":"{orderId}","orderAmountStart": "null","orderAmountEnd":"null"}
    #
    # # SMT平台查询订单——查询产品ID
    # smtProductId_param01 = {"args":"{0}","method": "listAliexpressOrder"}
    # smtProductId_param02 = {"search":{0},"pageReqired": "true", "limit": 200,"offset": 0,"sort":"gmt_create","order":"desc"}
    # smtProductId_param03 = {"orderAmountStart": "null","orderAmountEnd":"null","ProductId":"{ProductId}"}
    #
    # # SMT平台查询订单——查询商品编码
    # smtSkuCode_param01 = {"args":"{0}","method": "listAliexpressOrder"}
    # smtSkuCode_param02 = {"search":{0},"pageReqired": "true", "limit": 200,"offset": 0,"sort":"gmt_create","order":"desc"}
    # smtSkuCode_param03 = {"orderAmountStart": "null","orderAmountEnd":"null","skuCode":"{skuCode}"}
    #
    # # SMT平台查询订单——查询平台追踪号
    # smtLogisticsNo_param01 = {"args":"{0}","method": "listAliexpressOrder"}
    # smtLogisticsNo_param02 = {"search":{0},"pageReqired": "true", "limit": 200,"offset": 0,"sort":"gmt_create","order":"desc"}
    # smtLogisticsNo_param03 = {"orderAmountStart": "null","orderAmountEnd":"null","logisticsNo":"{logisticsNo}"}
    #
    # # SMT平台查询订单——查询系统追踪号
    # smtSystemLogisticsTrackingNumber_param01 = {"args":"{0}","method": "listAliexpressOrder"}
    # smtSystemLogisticsTrackingNumber_param02 = {"search":{0},"pageReqired": "true", "limit": 200,"offset": 0,"sort":"gmt_create","order":"desc"}
    # smtSystemLogisticsTrackingNumber_param03 = {"orderAmountStart": "null","orderAmountEnd":"null","systemLogisticsTrackingNumber":"{systemLogisticsTrackingNumber}"}
    #
    # # SMT平台查询订单——查询下单时间
    # smtOrderTimeStart_param01 = {"args":"{0}","method": "listAliexpressOrder"}
    # smtOrderTimeStart_param02 = {"search":{0},"pageReqired": "true", "limit": 200,"offset": 0,"sort":"gmt_create","order":"desc"}
    # smtOrderTimeStart_param03 = {"orderTimeStart":"2022-07-01 00:00:00","orderTimeEnd":"2022-07-04 23:59:59","orderAmountStart": "null","orderAmountEnd":"null"}
