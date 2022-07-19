# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: tariffCountryApi
@time:2022/7/18
@Author:majiaqin 170479
@Desc:查询资费国家
'''
import pprint
from apps.AllSystemData.SaleSystem.sale_api.saleSystem_interface_url import SaleApiUrl
from apps.AllSystemData.SaleSystem.sale_api.saleSystem_interface_param import SaleApiInputParam
from apps.Common_Config.operate_api_data import api_assemble_new, Splicing_Params

@api_assemble_new()
def tariffCountryApi(paramMap=None):
    url = SaleApiUrl.tariffCountry_url
    params_list = [SaleApiInputParam.tariffCountry_param01,
                   SaleApiInputParam.tariffCountry_param02,
                   SaleApiInputParam.tariffCountry_param03]
    api_params = Splicing_Params(params_list, paramMap).splicing_params()
    return url, api_params

if __name__ == '__main__':
    pprint.pprint(tariffCountryApi({"name": "chineseName",
                                    "inputText": "阿塞拜疆共和国"}))
    pass