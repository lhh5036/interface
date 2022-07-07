# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File:  ①saleSystem_interface_url.py(请求URL)  ②saleSystem_interface_param.py(入参)
③salePlatformOrderQueryApi.py(入参拼接)   ④test_salePlatformOrderQueryApi.py(设置断言)
@time:2022/7/4
@Author:lu 10338
@Desc: 销售系统-平台订单查询接口
'''
import json
import copy
from apps.AllSystemData.SaleSystem.sale_api.saleSystem_interface_param import SaleApiInputParam
from apps.AllSystemData.SaleSystem.sale_api.saleSystem_interface_url import SaleApiUrl
from apps.Common_Config.operate_api_data import api_assemble_new, Common_TokenHeader
from loggerUtils import MyLog

logger = MyLog("salePlatformOrderApi").getlog()
@api_assemble_new(api_header=Common_TokenHeader().token_header('new', '031'))
def salePlatformOrderApi(field,orderStatus):
    logger.info("salePlatformOrderApi ---->start!")
    url = SaleApiUrl.aliexpressOrderQuery_url
    param01 = SaleApiInputParam.smtQueryStatus_param01
    param02 = SaleApiInputParam.smtQueryStatus_param02
    param03 = copy.deepcopy(SaleApiInputParam.smtQueryStatus_param03) # 深复制：该变量及其内所有可变对象重新分配地址。修改任意值，原变量都不会发生改变
    # param03 = SaleApiInputParam.smtQueryStatus_param03  # 不会初始化param03对象
    param03[field] = orderStatus
    param02["search"] = param03
    param01["args"] = json.dumps(param02)
    return url, param01

if __name__ == '__main__':
    print(salePlatformOrderApi("accountNumber", "szhesitong1902@163.com"))
    print(salePlatformOrderApi("orderStatus","WAIT_SELLER_SEND_GOODS"))
    print(salePlatformOrderApi("orderId", "8151578618327041"))
    # print(salePlatformOrderApi("WAIT_SELLER_SEND_GOODS"))
