'''
@File: assert_new_utils.py
@time:2022/6/15
@Author:quanliu 181324
@Desc:断言用法
'''
import logging
from deepdiff import DeepDiff

def new_assert_utils(func): # 接口返回的数据和期望的数据 [状态码,响应结果数据]
    def wragger(*args, **kwargs):
        resp_result,expResp_result = func(*args, **kwargs) # 获取结果
        if len(resp_result) < 2:
            logging.error("需要断言的数据不全，请检查!")
            return False
        if len(expResp_result) < 2:
            logging.error("期望的数据不全，请检查!")
            return False

        resp_statusCode = resp_result[0] # 接口返回响应状态码
        resp_json = resp_result[1] # 接口返回响应结果
        exp_resp_statusCode = expResp_result[0] # 接口期望状态码
        exp_resp_json = expResp_result[1] # 接口期望返回的结果
        comp_code = assert_statusCode(resp_statusCode,exp_resp_statusCode)
        if comp_code == False:
            return False
        comp_json = assert_respJson(resp_json, exp_resp_json)
        if comp_json == False:
            return False
    return wragger

# 断言响应状态码
def assert_statusCode(resp_statusCode, exp_resp_statusCode):
    if resp_statusCode != exp_resp_statusCode:
        logging.error("接口状态码与期望状态码不一致!接口状态码为:{0}".format(resp_statusCode))
        return False
    else:
        logging.info("接口状态码与期望状态码一致")
        return True

# 断言响应结果，默认都会按照JSON格式来校验
def assert_respJson(resp_json, exp_resp_json):
    if resp_json == {} or exp_resp_json == {}:
        return "需要校验的数据或者期望数据结果为空，请检查!"
    ddiff = DeepDiff(resp_json, exp_resp_json, ignore_string_case=True, ignore_order=True)
    if ddiff == {}:
        logging.info("接口响应结果与期望一致")
        return True
    else:
        logging.error("接口响应结果与期望结果不一致,请检查:{0}".format(ddiff))
        return False
