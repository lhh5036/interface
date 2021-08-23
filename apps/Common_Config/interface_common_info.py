'''
@File: interface_common_info.py
@time:2021/8/4
@Author:quanliu 181324
@Desc:公共接口配置文件
'''

import requests
import json

class InterfaceCommonInfo:

    # 测试环境接口地址
    common_url = "http://192.168.3.162:80"

    # 预生产环境接口地址
    # common_url = "http://10.100.1.1:32100"

    # 生产环境接口地址
    # common_url = "http://10.100.1.1:31100"

    # 公共token
    token_currency = "5df26666b185fbf0b3437482125d340e"

    # 公共请求头参数
    common_header = {"Content-Type":"application/json","Authorization":token_currency}


'''
获取新旧用户系统token
'''
def GetLoginToken(method):
    header = {'Content-Type': 'application/json',
              'Authorization': InterfaceCommonInfo.token_currency}
    form = {"method": "string","args": "{\"userName\":\"170110\",\"password\":\"123456abc\"}"}
    form_new = {"args": "{\"employeeNo\":\"170110\",\"password\":\"MTIzNDU2YWJj\"}", "time": "1623037336864",
            "signature": "bf8daed69ec2e5287e4515889abe361b"}
    if method == 'new':
        url = InterfaceCommonInfo.common_url + "/usermgt-n/login"
        r = requests.post(url, headers=header, data=json.dumps(form_new))
        try:
            results =  r.json()["result"]['accessToken']
            return results
        except KeyError:
            return "员工账号不存在或密码错误"
    elif method == 'old':
        url = InterfaceCommonInfo.common_url + "/usermgt/login"
        r = requests.post(url, headers=header, data=json.dumps(form))
        try:
            results =  r.json()["result"]['accessToken']
            return results
        except KeyError:
            return "员工账号不存在或密码错误"


if __name__ == '__main__':
    tokens = GetLoginToken('new')
    print(tokens)