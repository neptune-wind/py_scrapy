# p63 创建item
# 3中的代码，结合items.py文件，用item组织已经收集到的信息
# 2020.3.8

from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from PythonScrapy.items import BaiduSpiderItem

class ArticleSpider(CrawlSpider):
    name = 'articleItems'
    allowd_domains = ['baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E5%8C%97%E4%BA%AC/128981']
    rules = [
        Rule(LinkExtractor(allow=r'^(https://baike.baidu.com/item).*'), callback='parse_items', follow=True,
             cb_kwargs={'is_item': True}),
        Rule(LinkExtractor(allow='.*'), callback='parse_items',
             cb_kwargs={'is_item': False}),
    ]

    def parse_items(self, response, is_item):
        if is_item:
            Item = BaiduSpiderItem()

            title = response.css('h1::text').extract_first()
            url = response.url
            text = response.xpath('//div[@class="lemma-summary"]//text()').extract()
            Item['title'] = title
            Item['url'] = url
            text_temp = ""
            for sentence in text:
                if sentence == "\n":
                    pass
                else:
                    text_temp += sentence
            Item['text'] = text_temp
            return Item

