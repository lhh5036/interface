'''
@File: fmis_db_config.py
@time:2021/8/3
@Author:Administrator
@Desc:解析数据库配置文件
'''

import configparser
import os
import logging


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
            elif env == "product" or env == "PRODUCT":
                return parseEsFile(cf,"es_product")
        elif dbtype == "mysql":
            configPath = os.path.join(proDir, "mysql_sources_config.ini")
            cf.read(os.path.abspath(configPath))
            if env == "test_case" or env == "TEST": # 当前环境为test
                if projectname == "das":  # 项目名称为数据分析系统
                    return parseMySqlFile(cf,"erp_das_test")
                elif projectname == "fmis": # 项目名称为财务系统
                    return parseMySqlFile(cf,"erp_fmis_test")
            elif env == "product" or env == "PRODUCT": # 当前环境为product
                if projectname == "das":
                    return parseMySqlFile(cf,"erp_das_product")
                elif projectname == "fmis":
                    return parseMySqlFile(cf,"erp_fmis_product")


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