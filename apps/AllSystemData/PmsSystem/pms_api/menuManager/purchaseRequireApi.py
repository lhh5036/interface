# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: purchaseRequireApi
@time:2022/7/15
@Author:majiaqin 170479
@Desc:查询采购需求分页列表
'''
import pprint
from apps.AllSystemData.PmsSystem.pms_api.pmsSystem_interface_url import PmsApiUrl
from apps.AllSystemData.PmsSystem.pms_api.pmsSystem_interface_param import PmsApiInputParam
from apps.Common_Config.operate_api_data import api_assemble_new, Splicing_Params

@api_assemble_new()
def purchaseRequireApi(paramMap=None):
    url = PmsApiUrl.purchaseRequire_url
    params_list = [PmsApiInputParam.purchaseRequire_param01,
                   PmsApiInputParam.purchaseRequire_param02,
                   PmsApiInputParam.purchaseRequire_param03]
    requestJson = Splicing_Params(params_list, paramMap).splicing_params()
    return url, requestJson

if __name__ == '__main__':
    pprint.pprint(purchaseRequireApi())
    pass