# -*- coding:utf-8 -*-
#!/usr/bin/python3

import redis
import itertools
from rediscluster import RedisCluster

nodes_release = [{"host": "10.100.1.181", "port": 6379},
                 {"host": "10.100.1.182", "port": 6379},
                 {"host": "10.100.1.183", "port": 6379},
                 {"host": "10.100.1.184", "port": 6379},
                 {"host": "10.100.1.185", "port": 6379},
                 {"host": "10.100.1.186", "port": 6379}]
nodes_release_info = {"username": "readonly", "password": "!QAZxsw2"}

nodes_test = [{"host": "192.168.3.5", "port": 8001},
              {"host": "192.168.3.5", "port": 8002},
              {"host": "192.168.3.5", "port": 8003},
              {"host": "192.168.3.6", "port": 8004},
              {"host": "192.168.3.6", "port": 8005},
              {"host": "192.168.3.6", "port": 8006}]
nodes_test_info = {"username": "redis_admin", "password": "halfj$$1/2red"}

class Redis_User():
    def __init__(self, nodes, username='redis_admin',
                 password='halfj$$1/2red', decode_responses=True):
        self.nodes = nodes
        self.username = username
        self.password = password
        self.decode_responses = decode_responses

    # 对节点redis进行增删改查
    def redis_operate(self, method='get', key=None, name=None, value=None):
        self.key = key
        self.name = name
        self.value = value
        self.method = method
        redis_value_lis = []
        for node in self.nodes:
            # 连接redis
            redis_conn = redis.StrictRedis(host=node['host'],
                                           port=node['port'],
                                           username=self.username,
                                           password=self.password,
                                           decode_responses=self.decode_responses)
            if self.method == 'get':
                try:
                    return redis_conn.get(self.key)
                except:
                    continue
            elif self.method == 'hget':
                try:
                    return redis_conn.hget(self.name, self.key)
                except:
                    continue
            elif self.method == 'set':
                try:
                    return redis_conn.set(self.name, self.value)
                except:
                    continue
            elif self.method == 'hset':
                try:
                    return redis_conn.hset(self.name, self.key, self.value)
                except:
                    continue
            elif self.method == 'del':
                try:
                    return redis_conn.delete(self.name)
                except:
                    continue
            elif self.method == 'hdel':
                try:
                    return redis_conn.hdel(self.name, self.key)
                except:
                    continue
            elif self.method == 'keys':
                redis_value = redis_conn.keys(self.key)
                if redis_value != None:
                    redis_value_lis.append(redis_value)
        redis_value_list = [i for i in itertools.chain(*redis_value_lis)]
        return redis_value_list



if __name__ == '__main__':
    values = Redis_User(nodes_test, username=nodes_test_info['username'],
                        password=nodes_test_info['password']).redis_operate(name='redis:demo',
                                                                            key='170479',
                                                                            method='hdel')
    print(values)