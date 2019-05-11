# -*- coding: utf-8 -*-
import scrapy
#导入CrawlSpider模块 需改写原来的def parse(self,response)方法
from scrapy.spiders import CrawlSpider ,Rule

#导入链接提取模块
from scrapy.linkextractors import LinkExtractor
from Urus.items import UrusItem

class urusSpider(CrawlSpider):
    name = 'urus'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/2775.html']

    #如需要进行页面解释则使用callback回调函数 因为有下一页，所以我们需要跟进，这里使用follow令其为True
    rules = {
        Rule(LinkExtractor(allow=r'https://car.autohome.com.cn/pic/series/2775.+'), callback= 'parse_page', follow=True),
    }

    def parse_page(self, response):
        catagory = response.xpath('//div[@class = "uibox"]/div/text()').get()
        srcs = response.xpath('//div[contains(@class,"uibox-con")]/ul/li//img/@src').getall()
        #获取xpath地址，可使用谷歌浏览器直接复制

        #map(函数，参数二)，将参数二中的每个都进行函数计算并返回一个列表
        srcs = list(map(lambda x:x.replace('t_',''),srcs))
        srcs = list(map(lambda x:response.urljoin(x),srcs))
        yield UrusItem(catagory=catagory, image_urls = srcs)