# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: getEmplUserIdByEmplNo
@time:2022/8/11
@Author:majiaqin 170479
@Desc:根据工号获取用户钉钉id
'''
import pprint
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgtSystem_interface_url import UsermgtApiUrl
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgtSystem_interface_param import UsermgtApiInputParam
from apps.Common_Config.operate_api_data import Splicing_Params, api_assemble_new

@api_assemble_new()
def getEmplUserIdByEmplNoApi(paramMap=None):
    url = UsermgtApiUrl.getEmplUserIdByEmplNo_url
    params_list = [UsermgtApiInputParam.getEmplUserIdByEmplNo_param01]
    api_params = Splicing_Params(params_list, paramMap).splicing_params()
    return url, api_params

if __name__ == '__main__':
    pprint.pprint(getEmplUserIdByEmplNoApi({"idList": [8825],
                                            "employeeNoList": ["170478"]}))
    pass