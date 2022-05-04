# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: operate_api_data
@time:2022/4/12
@Author:majiaqin 170479
@Desc:拼接api参数和请求接口装饰器
'''

import requests
import json
from apps.Common_Config.interface_common_info import InterfaceCommonInfo, Common_TokenHeader

'''接口参数拼接装饰器'''
def splicing_params(params_key1='args', params_key2='search'):
    def wragger(func):
        def demo(*args):
            if type(func(*args)[0][0]) == list:
                result01 = func(*args)[0][0]
                for k in func(*args)[1]:
                    result01[0] = func(*args)[1][k]
                return result01
            else:
                if len(func(*args)[0]) == 1:
                    result = func(*args)[0][0]
                    for k in func(*args)[1]:
                        result[k] = func(*args)[1][k]
                        return result
                elif len(func(*args)[0]) == 2:
                    result01 = func(*args)[0][1]
                    for k in func(*args)[1]:
                        result01[k] = func(*args)[1][k]
                    result02 = func(*args)[0][0]
                    try:
                        result02[params_key1] = str(result01)
                        return result02
                    except KeyError:
                        raise KeyError
                elif len(func(*args)[0]) == 3:
                    result01 = func(*args)[0][2]
                    for k in func(*args)[1]:
                        result01[k] = func(*args)[1][k]
                    result02 = func(*args)[0][1]
                    try:
                        result02[params_key2] = str(result01)
                    except KeyError:
                        raise KeyError
                    try:
                        result03 = func(*args)[0][0]
                        result03[params_key1] = str(result02)
                        return result03
                    except KeyError:
                        raise KeyError
        return demo
    return wragger

# 拼接接口参数
def splicing_params_new(params_key1='search', params_key2='args'):
    def wragger(func):
        def demo(*args):
            if type(func(*args)[0][0]) == list:
                result01 = func(*args)[0][0]
                for k in func(*args)[1]:
                    result01[k] = func(*args)[1][k]
                return result01
            else:
                result01 = func(*args)[0][0] # 获取最内层数据
                for k in func(*args)[1]:
                    result01[k] = func(*args)[1][k]
                try:
                    result02 = func(*args)[0][1] # 获取倒数第二层数据
                except:
                    return result01
                result02[params_key2] = str(result01) # 填充倒数第二层数据
                try:
                    result01 = func(*args)[0][2] # 获取最外层数据
                except:
                    return result02
                result01[params_key1] = str(result02)
                return result01
        return demo
    return wragger

'''将splicing_params_new或splicing_params装饰器解析的字典格式参数转为list'''
def params_list(func):
    def wragger(*args):
        result = []
        result.append(func(*args))
        return result
    return wragger

'''接口请求拼接装饰器'''
def api_assemble(api_url, api_method='post', params=True):
    def wragger(func):
        def demo(*args):
            global true, false, null
            true = True
            false = False
            null = None
            header = Common_TokenHeader.common_header
            form = func(*args)
            if api_method == 'post':
                url = api_url
                if params == True:
                    resp = requests.post(url, headers=header,
                                         data=json.dumps(form))
                    result = resp.json()
                    return result
                elif params == False:
                    resp = requests.post(url, headers=header)
                    result = resp.json()
                    return result
            elif api_method == 'get':
                url = api_url.format(params)
                resp = requests.get(url, headers=header)
                result = resp.json()
                return result
        return demo
    return wragger

@splicing_params_new({'ids': 333})
def test():
    return [['']]

if __name__ == '__main__':
    print(test())
    pass