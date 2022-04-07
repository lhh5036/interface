'''
@File: mysql_handleOperator.py
@time:2021/8/19
@Author:quanliu 181324
@Desc:MySQL数据库操作工具类
'''


from apps.Common_Config.db_config import Mysql_Db_Config
from apps.FmisSystem.fmis_common_settting import Fmis_Common_Setting
import pymysql
import pprint
import itertools

# mysql数据库具体操作实现类
class Mysql_handleOperator():
    def __init__(self, sqlinfo):    # sqlinfo为各系统通过db_config全局配置解析出来的数据库信息元组
        self.sqlinfo = sqlinfo
        self.host = self.sqlinfo[1]
        self.user = self.sqlinfo[2]
        self.password = self.sqlinfo[3]
        self.database = self.sqlinfo[0]
        self.port = 3306
        self.charset = "utf8"

        # # 连接数据库
        self.con = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port,
            charset=self.charset)

    def data_sql(self, methods, sql):
        self.methods = methods      # 声明增删改查哪种操作(insert/delete/update/select)
        self.sql = sql              # sql语句

        # 一次性查询数据库数据
        if self.methods == 'select':
            cursor = self.con.cursor() # 创建一个游标
            cursor.execute(self.sql)
            results = cursor.fetchall() # 返回全部结果
            cursor.close()
            self.con.close() # 关闭数据库连接
            return results

        # 新增修改删除数据库数据
        elif self.methods == 'insert' or self.methods == 'update' or self.methods == 'delete':
            cursor = self.con.cursor()
            try:
                cursor.execute(self.sql)
                self.con.commit()
            except:
                self.con.rollback() # 出现异常回滚
            cursor.close()
            self.con.close() # 关闭数据库连接

    # 使用流式游标分批次查询数据表数据
    def data_cursor_sql(self, sql):
        self.sql = sql  # sql语句

        cursor = pymysql.cursors.SSCursor(self.con)
        cursor.execute(self.sql)
        results = []
        while True:
            result = cursor.fetchone()
            results.append(result)
            # print(result)
            if not result:
                break
        results = [i for i in results if i != None]
        cursor.close()
        self.con.close()
        return results

class MySql_operator():
    # 一次性查询数据表全部数据
    def data_sql(self, con, sql, methods='select'):
        self.con = con
        self.methods = methods  # 声明增删改查哪种操作(insert/delete/update/select)
        self.sql = sql  # sql语句

        # 查询数据库数据
        if self.methods == 'select':
            cursor = self.con.cursor()
            cursor.execute(self.sql)
            results = cursor.fetchall()
            cursor.close()
            return results

        # 新增修改删除数据库数据
        elif self.methods == 'insert' or self.methods == 'update' or self.methods == 'delete':
            cursor = self.con.cursor()
            cursor.execute(self.sql)
            cursor.close()
            self.con.commit()

# 连接数据库
def controlDatebase(config_info, methods='select', port=3306, charset='utf8'):
    def wragger(func):
        def demo(*args):
            conn = pymysql.connect(host=config_info[1],
                                   user=config_info[2],
                                   password=config_info[3],
                                   database=config_info[0],
                                   port=port,
                                   charset=charset)
            sql_list = func(conn, *args)
            data_list = []
            for i in sql_list:
                data = MySql_operator().data_sql(conn, i, methods)
                datas = [info for info in itertools.chain(*data)]
                data_list.append(datas)
            conn.close()
            return data_list
        return demo
    return wragger

# 获取数据库数据
def get_data(config_info, method="select"):
    def wragger(func):
        def demo(*args):
            try:
                data = Mysql_handleOperator(config_info).data_sql(method, func(*args))
                return data
            except:
                raise Exception
        return demo
    return wragger

# 将元组数据转为列表
def convert_list(func):
    def wragger(*args):
        try:
            lis = [i for i in itertools.chain(*func(*args))]
            return lis
        except:
            return 0
    return wragger

if __name__ == '__main__':
    pass