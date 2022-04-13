# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: operate_api_data
@time:2022/4/12
@Author:majiaqin 170479
@Desc:拼接api参数和请求接口装饰器
'''

import pprint
import requests
import json
from apps.Common_Config.interface_common_info import InterfaceCommonInfo, Common_TokenHeader

'''接口参数拼接装饰器'''
def splicing_params(value_dict, params_key1='args', params_key2='search'):
    def wragger(func):
        def demo(*args):
            if len(func(*args)) == 1:
                result = func(*args)[0]
                for k in value_dict:
                    result[k] = value_dict[k]
                    return result
            elif len(func(*args)) == 2:
                result01 = func(*args)[1]
                for k in value_dict:
                    result01[k] = value_dict[k]
                result02 = func(*args)[0]
                try:
                    result02[params_key1] = str(result01)
                    return result02
                except KeyError:
                    raise KeyError
            elif len(func(*args)) == 3:
                result01 = func(*args)[2]
                for k in value_dict:
                    result01[k] = value_dict[k]
                result02 = func(*args)[1]
                try:
                    result02[params_key2] = str(result01)
                except KeyError:
                    raise KeyError
                try:
                    result03 = func(*args)[0]
                    result03[params_key1] = str(result02)
                    return result03
                except KeyError:
                    raise KeyError
        return demo
    return wragger

'''接口请求拼接装饰器'''
def api_assemble(api_url, api_method='post'):
    def wragger(func):
        def demo(*args):
            global true, false, null
            true = True
            false = False
            null = None
            url = InterfaceCommonInfo.common_url + api_url
            header = Common_TokenHeader.common_header
            form = func(*args)
            if api_method == 'post':
                resp = requests.post(url, headers=header,
                                     data=json.dumps(form))
                result = resp.json()
                return result
            elif api_method == 'get':
                resp = requests.get(url, headers=header)
                result = resp.json()
                return result
        return demo
    return wragger

if __name__ == '__main__':
    pass