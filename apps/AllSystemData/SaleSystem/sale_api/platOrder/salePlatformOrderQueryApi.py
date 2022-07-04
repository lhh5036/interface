# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File:
@time:2022/7/4
@Author:lu 10338
@Desc: 销售系统-平台订单查询接口
'''
from apps.AllSystemData.SaleSystem.sale_api.saleSystem_interface_param import SaleApiInputParam
from apps.AllSystemData.SaleSystem.sale_api.saleSystem_interface_url import SaleApiUrl
from apps.Common_Config.operate_api_data import api_assemble_new, Splicing_Params

@api_assemble_new()
def salePlatformOrderApi(paramMap=None):
    url = SaleApiUrl.aliexpressOrderQuery_url
    param01 = SaleApiInputParam.smtQueryStatus_param01
    param02 = SaleApiInputParam.smtQueryStatus_param01
    param03 = SaleApiInputParam.smtQueryStatus_param01
    paramList = []
    paramList.append(param01)
    paramList.append(param02)
    paramList.append(param03)
    requestJson = Splicing_Params(paramList,paramMap).splicing_params() # 拼接接口参数的方法
    return url,requestJson

if __name__ == '__main__':
    print(salePlatformOrderApi({"orderStatus":"WAIT_SELLER_SEND_GOODS"}))
    print(salePlatformOrderApi({"accountNumber":"szhesitong1902@163.com"}))