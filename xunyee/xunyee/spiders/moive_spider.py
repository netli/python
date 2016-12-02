# -*- coding: utf-8 -*-


from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from ..items import *

class MoiveSpider(CrawlSpider):
    name="xymoive"
    allowed_domains=["www.xunyee.cn"]
    # allowed_domains=["www.xunyee.cn"]
    # start_urls=["http://www.yishengyue.cn"]
    start_urls=["http://www.xunyee.cn/rank-teleplay-play.html"]
    # rules=[
    #     Rule(SgmlLinkExtractor(allow=(r'http://movie.douban.com/top250\?start=\d+.*'))),
    #     Rule(SgmlLinkExtractor(allow=(r'http://movie.douban.com/subject/\d+')),callback="parse_item"),
    # ]



    def parse(self, response):

        sel= Selector(response)
        moves = sel.xpath('//*[@id="rank_left_content"]/div/div[2]/div')
        items = []
        for  move in moves:
         item = XYmoiveItem()
         item['place']= move.xpath('a/span[1]/span/i/text()').extract()
         item['name']=moves.xpath('a/span[2]/text()').extract()
         item['amount']=moves.xpath('a/span[3]/b/text()').extract()
         # print  item
         items.append(item)
         return items


