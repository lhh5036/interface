'''
@File: es_handleOperator.py
@time:2021/8/19
@Author:quanliu
@Desc:Redis数据库操作工具类
'''

import redis
from rediscluster import RedisCluster

class Redis_User():
    def __init__(self, host, port=6379, decode_responses=True):
        self.host = host
        self.port = port
        self.decode_responses = decode_responses

    # 取出键对应的值(单节点)
    def redis_get(self, keys):
        self.keys = keys
        # 创建连接的进程池
        poll = redis.ConnectionPool(host=self.host, port=self.port)
        # 选择需要连接的进程池
        r = redis.Redis(connection_pool=poll)
        get_value = r.get(self.keys)
        return get_value

    # 取出键对应的值(集群)
    def redis_cluster(self, nodes, keys):
        self.nodes = nodes
        self.keys = keys
        self.nodes = nodes
        r = RedisCluster(startup_nodes=self.nodes, decode_responses=self.decode_responses)
        get_values = r.get(self.keys)
        return get_values

    def redis_zscore(self, nodes, name, value):
        self.nodes = nodes
        self.name = name
        self.value = value
        r = RedisCluster(startup_nodes=self.nodes, decode_responses=self.decode_responses)
        get_values = r.zscore(self.name, self.value)
        return get_values

if __name__ == '__main__':
    pass