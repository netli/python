# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class XunyeePipeline(object):
#     def process_item(self, item, spider):
#         return item
#
#
from twisted.enterprise import adbapi  # 导入twisted的包
import MySQLdb
import MySQLdb.cursors
from scrapy import log

class XunyeePipeline(object):
    """docstring for MySQLstor"""

    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
                                            host='192.168.0.250',
                                            db='python',
                                            user='ysy_data',
                                            passwd='aaaaa888',
                                            cursorclass=MySQLdb.cursors.DictCursor,
                                            charset='utf8',
                                            use_unicode=True
                                            )

    def process_item(self, item, spider):
        print spider
        # run db query in thread pool
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)

        return item

    def _conditional_insert(self, tx, item):


            if item.get('name'):

              names = item.get('name')
              places = item.get('place')
              amounts = item.get('amount')
              for indexNames in range(len(names)):
                 tx.execute( \
                    "insert into move (name, place, amount)\
                    values (%s, %s, %s)",
                    (names[indexNames],
                     places[indexNames],
                     amounts[indexNames]
                      )
                 )

    def handle_error(self, e):
        log.err(e)