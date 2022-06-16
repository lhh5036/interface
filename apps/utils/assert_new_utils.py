'''
@File: assert_new_utils.py
@time:2022/6/15
@Author:quanliu 181324
@Desc:断言用法
'''
import logging
from deepdiff import DeepDiff

def new_assert_utils(resp_result,assertResp_result): # 接口返回的数据和期望的数据 [状态码,响应结果数据]
    if len(resp_result) < 2:
        return "需要断言的数据不全，请检查!"
    if len(assertResp_result) < 2:
        return "期望的数据不全，请检查!"

    resp_statusCode = resp_result[0] # 接口返回响应状态码
    resp_json = resp_result[1] # 接口返回响应结果
    exp_resp_statusCode = assertResp_result[0] # 接口期望状态码
    exp_resp_json = assertResp_result[1] # 接口期望返回的结果
    try:
        compare_statusCode = assert_statusCode(resp_statusCode,exp_resp_statusCode)
        if compare_statusCode != None:
            return True
    except AssertionError as e: # 断言失败
        logging.error("接口报错,statu_code:{0}".format(resp_statusCode))
        return False

    diff_json = assert_respJson(resp_json,exp_resp_json)
    if diff_json == {}:
        logging.info("接口响应结果与期望一致")
        return True
    else:
        logging.error("接口响应结果与期望结果不一致,请检查:{0}".format(diff_json))
        return False

# 断言响应状态码
def assert_statusCode(resp_statusCode,exp_resp_statusCode):
    assert resp_statusCode == exp_resp_statusCode,"接口状态码与期望状态码不一致!"

# 断言响应结果，默认都会按照JSON格式来校验
def assert_respJson(resp_json,exp_resp_json):
    if resp_json == {} or exp_resp_json == {}:
        return "需要校验的数据或者期望数据结果为空，请检查!"
    ddiff = DeepDiff(resp_json,exp_resp_json,ignore_string_case=True,ignore_order=True )
    return ddiff


if __name__ == '__main__':
    t1 = [200,{"status": "1", "aa": "2"}]
    t2 = [500,{"status":1,"a":2}]
    print(new_assert_utils(t1,t2))
