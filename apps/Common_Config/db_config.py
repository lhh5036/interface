'''
@File: fmis_db_config.py
@time:2021/8/3
@Author:Administrator
@Desc:解析数据库配置文件
'''

import configparser
import os
import logging
import redis
from rediscluster import RedisCluster

'''解析mysql_sources_config文件中MYSQL配置'''
def parseMySqlFile(cf,databasename):
    _host = cf.get(databasename, "mysql_host")
    _user = cf.get(databasename, "mysql_user")
    _password = cf.get(databasename, "mysql_password")
    _database = cf.get(databasename, "mysql_database")
    return [_host, _user, _password, _database]

'''解析es_sources_config.ini文件中ES配置'''
def parseEsFile(cf,databasename):
    _host = cf.get(databasename, "es_host")
    _port = cf.get(databasename, "es_port")
    _timeout = int(cf.get(databasename, "es_timeout"))
    return _host, _port, _timeout

'''获取配置文件中所有生产环境的数据库配置'''
class Get_Db_Info():
    def __init__(self):
        pass

    @staticmethod
    def get_mysqldb_info(env, database_config="mysql_sources_config.ini"):
        cf = configparser.ConfigParser()
        prodir = os.path.dirname(os.path.abspath(__file__))
        configpath = os.path.join(prodir, database_config)
        cf.read(os.path.join(configpath), encoding='utf-8')
        return parseMySqlFile(cf, env)

    @staticmethod
    def get_esdb_info(env, database_config="es_sources_config.ini"):
        cf = configparser.ConfigParser()
        prodir = os.path.dirname(os.path.abspath(__file__))
        configpath = os.path.join(prodir, database_config)
        cf.read(os.path.join(configpath), encoding='utf-8')
        return parseEsFile(cf, env)

    def __del__(self):
        message = "close "
        logging.info(message)
        return message

'''获取Mysql数据库配置'''
def Mysql_Db_Config(env):
    config = Get_Db_Info().get_mysqldb_info(env)
    return [config[i] for i in range(len(config))]

'''获取ES数据库配置'''
def Es_Db_Config(env):
    es_config = Get_Db_Info().get_esdb_info(env)
    return [es_config[i] for i in range(len(es_config))]

'''
redis调用类
'''
# redis生产环境集群
nodes_release = [{"host": "10.100.1.91", "port": 6379},
                 {"host": "10.100.1.93", "port": 6379},
                 {"host": "10.100.1.95", "port": 6379}]

# redis测试环境集群
nodes_test = [{"host": "192.168.3.5", "port": 8001,
               "user": "redis_admin",
               "password": "halfj$$1/2red"},
              {"host": "192.168.3.5", "port": 8002,
               "user": "redis_admin",
               "password": "halfj$$1/2red"},
              {"host": "192.168.3.5", "port": 8003,
               "user": "redis_admin",
               "password": "halfj$$1/2red"},
              {"host": "192.168.3.6", "port": 8004,
               "user": "redis_admin",
               "password": "halfj$$1/2red"},
              {"host": "192.168.3.6", "port": 8005,
               "user": "redis_admin",
               "password": "halfj$$1/2red"},
              {"host": "192.168.3.6", "port": 8006,
               "user": "redis_admin",
               "password": "halfj$$1/2red"}]

# redis连接
class Redis_User():
    def __init__(self, host, port=6379, decode_responses=True):
        self._host = host
        self._port = port
        self._decode_responses = decode_responses

    # 取出键对应的值(单节点)
    def redis_get(self, keys):
        self._keys = keys
        # 创建连接的进程池
        poll = redis.ConnectionPool(host=self._host, port=self._port)
        # 选择需要连接的进程池
        r = redis.Redis(connection_pool=poll)
        get_value = r.get(self._keys)
        return get_value

    # 取出键对应的值(集群)
    def redis_cluster(self, nodes, keys):           # nodes为redis集群
        self._nodes = nodes
        self._keys = keys
        r = RedisCluster(startup_nodes=self._nodes, decode_responses=self._decode_responses)
        get_values = r.get(self._keys)
        return get_values

    def redis_zscore(self, nodes, name, value):     # nodes为redis集群
        self._nodes = nodes
        self._name = name
        self._value = value
        r = RedisCluster(startup_nodes=self._nodes, decode_responses=self._decode_responses)
        get_values = r.zscore(self._name, self._value)
        return get_values

# 解析redis_sources_config文件中REDIS配置
class parseRedisFile():
    def __init__(self, cf, databasename):
        self.cf = cf
        self.databasename = databasename

    def host(self):
        _host = self.cf.get(self.databasename, "redis_host")
        return _host
    def port(self):
        _port = self.cf.get(self.databasename, "redis_port")
        return _port


if __name__ == '__main__':
    pass

