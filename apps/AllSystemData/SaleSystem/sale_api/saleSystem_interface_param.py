'''
@File: saleSystem_interface_param.py
@time:2022/1/18
@Author:quanliu 181324
@Desc:订单系统接口入参
'''

class SaleApiInputParam:
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
    smtQueryStatus_param01 = {"args":"{0}","method" :"listAliexpressOrder"}
    smtQueryStatus_param02 = {"search":{0},"pageReqired" :"true" ,"limit" :200 ,"offset" :0 ,"sort" :"gmt_create","order" :"desc"}
    smtQueryStatus_param03 = {"orderStatus" :"{orderStatus}" ,"orderAmountStart" :"null" ,"orderAmountEnd" :"null"}

    # SMT平台查询订单——查询订单状态+销售账号：xxx + 等待您发货
    smtAccountNumber_param01 = {"args":"{0}","method":"listAliexpressOrder"}
    smtAccountNumber_param02 = {"search": {0},"pageReqired":"true" ,"limit":200 ,"offset":0 ,"sort":"gmt_create","order":"desc"}
    smtAccountNumber_param03 = {"accountNumber":"{accountNumber}" ,"orderStatus":"{orderStatus}","orderAmountStart":"null" ,"orderAmountEnd":"null"}

