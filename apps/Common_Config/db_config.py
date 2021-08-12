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


# 解析每个系统中的db_sources文件得到ES/MYSQL配置
class ReadConfig:
    def getDbConfig(env,projectname,dbtype): # 环境、项目名称、数据库类型（ES/mysql）
        if env == "" or projectname == "" or dbtype == "":
            logging.error("env or projectName or dbType is empty!")
            return
        configPath = ""
        cf = configparser.ConfigParser()
        proDir = os.path.dirname(os.path.abspath(__file__))
        if dbtype == "es":
            configPath = os.path.join(proDir, "es_sources_config.ini")
            cf.read(os.path.abspath(configPath))
            if env == "test_case" or env == "TEST":
                return parseEsFile(cf,"es_test")
            elif env == "release" or env == "RELEASE":
                return parseEsFile(cf,"es_release")
        elif dbtype == "mysql":
            configPath = os.path.join(proDir, "mysql_sources_config.ini")
            cf.read(os.path.abspath(configPath))
            if env == "test_case" or env == "TEST": # 当前环境为test
                if projectname == "das":  # 项目名称为数据分析系统
                    return parseMySqlFile(cf,"erp_das_test")
                elif projectname == "fmis": # 项目名称为财务系统
                    return parseMySqlFile(cf,"erp_fmis_test")
                elif projectname == "erp_usermgt": # 旧用户系统
                    return parseMySqlFile(cf,"erp_usermgt_test")
                elif projectname == "erp_usermgt_new": # 新用户系统
                    return parseMySqlFile(cf,"erp_usermgt_new_test")
            elif env == "release" or env == "RELEASE": # 当前环境为release
                if projectname == "das":
                    return parseMySqlFile(cf,"erp_das_release")
                elif projectname == "fmis":
                    return parseMySqlFile(cf,"erp_fmis_release")
                elif projectname == "erp_usermgt":
                    return parseMySqlFile(cf,"erp_usermgt_release")
                elif projectname == "erp_usermgt_new":
                    return parseMySqlFile(cf,"erp_usermgt_new_release")


'''
redis调用类
'''
# redis生产环境集群
nodes_release = [{"host": "10.100.1.91", "port": 6379},
                 {"host": "10.100.1.93", "port": 6379},
                 {"host": "10.100.1.95", "port": 6379}]

# redis测试环境集群
nodes_test = [{"host": "192.168.3.4", "port": 7001},
              {"host": "192.168.3.4", "port": 7002},
              {"host": "192.168.3.5", "port": 7003},
              {"host": "192.168.3.5", "port": 7004}]

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
    def redis_cluster(self, nodes, keys):           # nodes为redis集群
        self.nodes = nodes
        self.keys = keys
        self.nodes = nodes
        r = RedisCluster(startup_nodes=self.nodes, decode_responses=self.decode_responses)
        get_values = r.get(self.keys)
        return get_values

    def redis_zscore(self, nodes, name, value):     # nodes为redis集群
        self.nodes = nodes
        self.name = name
        self.value = value
        r = RedisCluster(startup_nodes=self.nodes, decode_responses=self.decode_responses)
        get_values = r.zscore(self.name, self.value)
        return get_values


# 解析es_sources_config.ini文件中ES配置
def parseEsFile(cf,databasename):
    _host = cf.get(databasename,"es_host")
    _port = cf.get(databasename,"es_port")
    _timeout = int(cf.get(databasename,"es_timeout"))
    return _host,_port,_timeout


# 解析mysql_sources_config文件中MYSQL配置
def parseMySqlFile(cf,databasename):
    _database = cf.get(databasename, "mysql_database")
    _host = cf.get(databasename, "mysql_host")
    _user = cf.get(databasename, "mysql_user")
    _password = cf.get(databasename, "mysql_password")
    return _database,_host,_user,_password