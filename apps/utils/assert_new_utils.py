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
        checkResult = True # 默认校验通过
        resp_result,expResp_result = func(*args, **kwargs) # 获取结果
        if len(resp_result) < 2:
            logging.error("需要断言的数据不全，请检查!")
            checkResult = False
            return checkResult
        if len(expResp_result) < 2:
            logging.error("期望的数据不全，请检查!")
            checkResult = False
            return checkResult

        resp_statusCode = resp_result[0] # 接口返回响应状态码
        resp_json = resp_result[1] # 接口返回响应结果
        exp_resp_statusCode = expResp_result[0] # 接口期望状态码
        exp_resp_json = expResp_result[1] # 接口期望返回的结果
        comp_code = assert_statusCode(resp_statusCode,exp_resp_statusCode)
        if checkResult != comp_code: # 如果校验状态码的结果与期望结果不一致
            checkResult = False
            return checkResult
        else:
            comp_json = assert_respJson(resp_json, exp_resp_json)
            if checkResult == comp_json:
                return checkResult
            else:
                checkResult = False
                return checkResult
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
    ddiff = DeepDiff(resp_json,exp_resp_json, ignore_string_case=True, ignore_order=True, view="tree")
    if ddiff == {}:
        logging.info("接口响应结果与期望一致")
        return True
    else:
        logging.error("接口响应结果与期望结果不一致,请检查:{0}".format(ddiff))
        return False

# 传入要校验的值，接口响应结果，期望值(SQL查询结果)
def concat_assert_data(func):
    def wragger(*args):
        keysList, resp_json, exp_select_result = func(*args) # resp_json--》接口响应状态码和响应结果；exp_select_result-->期望状态码和SQL查询结果
        check_json_list = [] # 需要校验的值
        expact_json_list = [] # 期望的结果
        if len(keysList) <= 0 or len(resp_json) < 2 or len(exp_select_result) < 2:
            logging.error("没有需要校验的key")
            return check_json_list, expact_json_list
        check_code = resp_json[0] # 响应状态码
        check_json = resp_json[1] # 响应结果
        result_check_json = {}
        for key in keysList:
            value_list = []
            value_list.append(check_json[key])
            result_check_json[key] = value_list  # 将需要校验的key单独存，且value为List
        # 拼接需要获取需要校验的数据
        check_json_list.append(check_code)
        check_json_list.append(result_check_json)

        # 处理期望值
        expact_code = exp_select_result[0] # 期望状态码
        expact_json = exp_select_result[1] # 期望SQL查询结果
        if len(expact_json) <= 0:
            logging.error("期望结果为空")
            return check_json_list, expact_json_list
        m = 0
        expact_json_dict = {}
        for k in keysList:
            expact_json_dict[k] = []
            for i in range(len(expact_json)):
                expact_json_dict[k].append(expact_json[i][m])
            m += 1
        # 拼接期望数据
        expact_json_list.append(expact_code)
        expact_json_list.append(expact_json_dict)
        return check_json_list, expact_json_list
    return wragger

@new_assert_utils
@concat_assert_data
def test():
    t1 = ["a","b"]
    t2 = [200,{"a":"1","b":2,"c":3}]
    t3 = [500,((1,2),)]

    return t1,t2,t3

if __name__ == '__main__':
    print(test())