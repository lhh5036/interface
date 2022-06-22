# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: threeLevelEmployee
@time:2022/6/17
@Author:majiaqin 170479
@Desc:三级查询组织架构
'''

import pprint
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgtSystem_interface_url import UsermgtApiUrl
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgtSystem_interface_param import UsermgtApiInputParam
from apps.Common_Config.operate_api_data import Splicing_Params, api_assemble_new

@api_assemble_new()
def threeLevelEmployeeApi(paramMap=None):
    url = UsermgtApiUrl.threeLevelEmployee_url
    params_list = [UsermgtApiInputParam.threeLevelEmployee_param01]
    api_params = Splicing_Params(params_list, paramMap).splicing_params()
    return url, api_params

if __name__ == '__main__':
    pprint.pprint(threeLevelEmployeeApi({"servicePlatform": "AMAZON平台",
                                         "employeeNo": "075"}))
    pass