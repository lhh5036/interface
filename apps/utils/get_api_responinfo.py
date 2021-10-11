'''
@File: get_api_respontime
@time:2021/9/25
@Author:majiaqin 170479
@Desc:获取接口各种格式的响应时间
'''

import requests

class Get_Api_Respontime():
    def __init__(self, resp):   # resp为接口返回数据
        self.resp = resp

    def get_api_respontime(self, index):
        self.index = index

        # 获取时分秒毫秒
        if self.index == 'hmsms':
            result = self.resp.elapsed
        # 获取毫秒
        elif self.index == 'ms':
            result = self.resp.elapsed.total_seconds()
        # 四舍五入到秒
        elif self.index == 's':
            result = self.resp.elapsed.seconds

        return result
