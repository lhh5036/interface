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
import pprint
from copy import deepcopy
from apps.get_page_content_by_requests import get_page_content_by_requests
from loggerUtils import MyLog
from apps.Common_Config.interface_common_info import Common_TokenHeader
from apps.AllSystemData.UsermgtSystem.usermgt_api.usermgtSystem_interface_url import UsermgtApiUrl
# 实例化日志类
logger = MyLog("operate_api_data").getlog()
'''接口参数拼接装饰器'''
class Splicing_Params():
    def __init__(self, params_list, paramMap=None):
        self.params_list = params_list
        self.paramMap = paramMap
        self.params_list_deepcopy = deepcopy(self.params_list)

    def splicing_param(self):
        if self.paramMap == None:
            return self.params_list_deepcopy[len(self.params_list_deepcopy)-1]
        else:
            if type(self.paramMap) == list:
                return self.paramMap
            else:
                for paramMap_key in self.paramMap.keys():
                    self.params_list_deepcopy[len(self.params_list_deepcopy)-1][paramMap_key] = self.paramMap[paramMap_key]
                return self.params_list_deepcopy[len(self.params_list_deepcopy)-1]

    def splicing_params(self):
        if type(self.paramMap) == list:
            return self.splicing_param()
        else:
            if len(self.params_list_deepcopy) == 1:
                return self.splicing_param()
            elif len(self.params_list_deepcopy) == 2:
                self.params_list_deepcopy[0]['args'] = json.dumps(self.splicing_param())
                return self.params_list_deepcopy[0]
            elif len(self.params_list_deepcopy) == 3:
                self.params_list_deepcopy[1]['search'] = self.splicing_param()
                self.params_list_deepcopy[0]['args'] = json.dumps(self.params_list_deepcopy[1])
                return self.params_list_deepcopy[0]

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

'''拼接請求參數（新）'''
def api_assemble_new(login_method="new", api_method="post", api_header="", employeeNo='181324'):
    def wraager(func):
        def demo(*args):
            if api_header != "":
                api_header_use = api_header # 如果api_header不为空则使用该api_header
            else: 
                if login_method == "new":
                    # 如果api_header为空则使用公共header
                    api_header_use = Common_TokenHeader().common_header
                elif login_method == 'old':
                    api_header_use = Common_TokenHeader().token_header(login_method, employeeNo)
            api_url, api_param = func(*args) # 获取接口请求的地址和请求参数
            resp = get_page_content_by_requests(api_url, api_header_use, api_param, api_method)
            if resp.status_code == 200:
                logger.info("接口请求的地址:{0}".format(api_url))
                logger.info("接口请求参数:{0}".format(api_param))
            else:
                logger.error("接口请求的地址:{0}".format(api_url))
                logger.error("接口请求参数:{0}".format(api_param))
            return [resp.status_code, resp.json()] # 返回接口状态码和响应结果
        return demo
    return wraager

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
            logger.info(form)
            if api_method == 'post':
                url = api_url
                if params == True:
                    resp = requests.post(url, headers=header,
                                         data=json.dumps(form))
                    result = [resp.status_code, resp.json()]
                    print(result)
                    return result
                elif params == False:
                    resp = requests.post(url, headers=header)
                    result = [resp.status_code, resp.json()]
                    return result
            elif api_method == 'get':
                url = api_url.format(params)
                resp = requests.get(url, headers=header)
                result = [resp.status_code, resp.json()]
                return result
        return demo
    return wragger

@api_assemble(UsermgtApiUrl.listNextEmployeeByDeptId_url)
@splicing_params_new()
def test():
    return [[{"args": ""}], {'args': '50841235'}]

if __name__ == '__main__':
    params_list = [{"args": ""},
                   {"employeeNo": "",
                    "servicePlatform": ""}]
    pprint.pprint(Splicing_Params(params_list, paramMap={"employeeNo": "3381", "servicePlatform": "SMT平台"}).splicing_params())
    pass