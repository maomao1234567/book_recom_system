# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem


class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/top250']

    def parse(self, response):
        book_list = response.xpath("//div[@class='article']//table")

        for i_item in book_list:
            douban_item = DoubanItem()
            '''normalize-space（去除xpath中的换行符）'''
            book_name = i_item.xpath(
                "normalize-space(.//div[@class='pl2']/a/text())"
            ).extract_first()
            douban_item['book_name'] = "".join(book_name)
            douban_item['author'] = i_item.xpath(
                ".//p[@class='pl']/text()").extract_first().split('/')[0]
            douban_item['introduce'] = i_item.xpath(
                ".//span[@class='inq']/text()").extract_first()
            douban_item['star'] = i_item.xpath(
                ".//span[@class='rating_nums']/text()").extract_first()

            yield douban_item
            
            '''下一次迭代时，从上一次迭代遇到的yield后面的代码(下一行)开始执行'''
        next_link = response.xpath(
            "//span[@class='next']/link/@href").extract()
        print(next_link)

        if next_link:
            next_link1 = next_link[0]
            yield scrapy.Request(next_link1, callback=self.parse)

