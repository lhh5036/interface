'''
@File: get_page_content_by_requests.py
@time:2022/5/30
@Author:
@Desc:
'''
import requests, json

def get_page_content_by_requests(url, headers, inParam, methods="post", timeout=5000):
    try:
        if methods == "get":
            resp = requests.get(url=url, headers=headers, params=json.dumps(inParam), timeout=timeout)
            return resp
        if methods == "post":
            resp = requests.post(url=url, headers=headers, data=json.dumps(inParam), timeout=timeout)
            return resp
    except Exception as e:
        return Exception, e


