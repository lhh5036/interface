'''
@File: es_handleOperator.py
@time:2021/8/19
@Author:quanliu
@Desc:ES数据库操作工具类
'''
from elasticsearch6 import Elasticsearch
from apps.Common_Config.db_config import Es_Db_Config

# ES数据库具体操作实现类
class Es_handleOperator():
    # 初始化
    def __init__(self,esInfo):
        # 连接对应系统的数据库
        self.hosts = esInfo[0]
        self.port = esInfo[1]
        self.timeout = esInfo[2]

    # 获取数据（数据量不大情况下使用）
    def data_es(self, index, querys):
        self.index = index              # es表(索引)
        self.query = querys             # 查询语句

        es = Elasticsearch(hosts=self.hosts, port=self.port, timeout=self.timeout)
        query = self.query
        allDoc = es.search(index=self.index, body=query)
        if allDoc['hits']['total'] == 0:
            return 0
        else:
            return allDoc['hits']

    # 按游标获取数据(解决获取一百万以上数据导致数据库报错的问题)
    def data_es_new(self, method: object, index: object, querys: object, scroll: object = '20m',
                    nsize: object = 1000) -> object:
        self.method = method  # total获取表数据数量 data获取表全部数据
        self.index = index  # es表(索引)
        self.query = querys  # 查询语句
        self.scroll = scroll  # 通过此参数可以获取es表中的scroll_id
        self.nsize = nsize  # 设置游标查询条目数

        es = Elasticsearch(hosts=self.hosts, port=self.port, timeout=self.timeout)
        query = self.query
        allDoc = es.search(index=self.index, body=query, scroll=self.scroll, size=self.nsize)
        if self.method == 'total':
            return allDoc['hits']['total']
        elif self.method == 'data':
            # 游标用于输出es查询出的所有结果
            scroll_id = allDoc['_scroll_id']
            results = []
            results = allDoc['hits']['hits']
            for j in range(0, int(allDoc['hits']['total'] / self.nsize) + 1):
                result = es.scroll(scroll_id=scroll_id, scroll=self.scroll)
                if len(result['hits']['hits']) == 0:
                    pass
                else:
                    results = results + result['hits']['hits']
            return results

    # 计算总量
    def data_es_count(self, index, querys):
        self.index = index  # es表(索引)
        self.query = querys  # 查询语句

        es = Elasticsearch(hosts=self.hosts, port=self.port, timeout=self.timeout)
        query = self.query
        allDoc = es.search(index=self.index, body=query)
        if allDoc['hits']['total'] == 0:
            return 0
        else:
            return allDoc['hits']['total']

'''获取查询条目数'''
def get_data_num(es_info, index):
    def wragger(func):
        def demo(*args):
            total = Es_handleOperator(es_info).data_es_count(index, func(*args))
            return total
        return demo
    return wragger

'''获取ES数据'''
def get_es_data(es_info, index):
    def wragger(func):
        def demo(*args):
            data = Es_handleOperator(es_info).data_es_new("data", index, func(*args))
            return data
        return demo
    return wragger

if __name__ == '__main__':
    pass