# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File:  saleSystem_interface_url.py(请求URL)  saleSystem_interface_param.py(入参)
salePlatformOrderQueryApi.py(入参拼接)   test_salePlatformOrderQueryApi.py(设置断言)
@time:2022/7/4
@Author:lu 10338
@Desc: 销售系统-平台订单查询接口
'''
import json
from apps.AllSystemData.SaleSystem.sale_api.saleSystem_interface_param import SaleApiInputParam
from apps.AllSystemData.SaleSystem.sale_api.saleSystem_interface_url import SaleApiUrl
from apps.Common_Config.operate_api_data import api_assemble_new, Common_TokenHeader
from loggerUtils import MyLog


logger = MyLog("salePlatformOrderApi").getlog()
@api_assemble_new(api_header=Common_TokenHeader().token_header('new', '10338'))
def salePlatformOrderApi(orderStatus):
    logger.info("salePlatformOrderApi ---->start!")
    url = SaleApiUrl.aliexpressOrderQuery_url
    param01 = SaleApiInputParam.smtQueryStatus_param01
    param02 = SaleApiInputParam.smtQueryStatus_param02
    param03 = SaleApiInputParam.smtQueryStatus_param03
    param03["orderStatus"] = orderStatus
    param02["search"] = param03
    param01["args"] = json.dumps(param02)
    reqParam = param01
    return url, reqParam

if __name__ == '__main__':
    print(salePlatformOrderApi("WAIT_SELLER_SEND_GOODS"))
    # print(salePlatformOrderApi("WAIT_SELLER_SEND_GOODS"))
    # print(salePlatformOrderApi({"accountNumber":"szhesitong1902@163.com"}))