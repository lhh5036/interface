# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: blackedBuyerApi
@time:2022/7/19
@Author:majiaqin 170479
@Desc:查询黑名单买家
'''
import pprint
from apps.AllSystemData.SaleSystem.sale_api.saleSystem_interface_url import SaleApiUrl
from apps.AllSystemData.SaleSystem.sale_api.saleSystem_interface_param import SaleApiInputParam
from apps.Common_Config.operate_api_data import api_assemble_new, Splicing_Params

@api_assemble_new()
def blackedBuyerApi(paramMap=None):
    url = SaleApiUrl.blackedBuyer_url
    params_list = [SaleApiInputParam.blackedBuyer_param01,
                   SaleApiInputParam.blackedBuyer_param02,
                   SaleApiInputParam.blackedBuyer_param03]
    api_params = Splicing_Params(params_list, paramMap).splicing_params()
    return url, api_params

if __name__ == '__main__':
    pprint.pprint(blackedBuyerApi({"saleChannel": "Nocnoc", "accountNumber": "13089398756@163.com-ID",
                                   "customerName": "Diogo Montes Ribeiro Saramago", "blackedType": "1",
                                   "recipientName": "Diogo Montes Ribeiro Saramago"}))
    pass