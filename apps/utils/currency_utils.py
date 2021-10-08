# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: currency_utils
@time:2021/10/8
@Author:majiaqin 170479
@Desc:通用工具类
'''



'''判断某个键是否存在于响应数据中'''
class Json_Get():
    def __init__(self, response):
        self.response = response

    def json_get(self, k):
        self.k = k
        if self.k in self.response:
            return "True"
        for key, value in self.response.items():
            if isinstance(value, dict):
                return Json_Get(value).json_get(self.k)
            if isinstance(value, list):
                for i in range(0, len(value)):
                    if isinstance(value[i], dict):
                        return Json_Get(value[i]).json_get(self.k)
        else:
            return "False"

if __name__ == '__main__':
    pass