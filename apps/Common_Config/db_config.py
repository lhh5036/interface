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
def parseMySqlFile(cf, databasename):
    _host = cf.get(databasename, "mysql_host")
    _user = cf.get(databasename, "mysql_user")
    _password = cf.get(databasename, "mysql_password")
    _database = cf.get(databasename, "mysql_database")
    return [_host, _user, _password, _database]

'''解析es_sources_config.ini文件中ES配置'''
def parseEsFile(cf, databasename):
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

if __name__ == '__main__':
    pass

