# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import log
import pymysql


class DoubanPipeline(object):

    def process_item(self, item, spider):
        conn = pymysql.connect(host="localhost", user="root",
                               password="299521", port=3306, db='douban')
        cur = conn.cursor()
        sql = "insert into books(author, book_name, introduce, star) " \
              "values (%s, %s, %s, %s)"
        author = item['author']
        book_name = item['book_name']
        introduce = item['introduce']
        star = item['star']
        values = (author, book_name, introduce, star)
        cur.execute(sql, values)
        conn.commit()
        return item
