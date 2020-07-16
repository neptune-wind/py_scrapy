# p63 带规则的爬取
# 通过正则表达式筛选希望爬取的部分网站——这里是词条item
# 通过Rule()中的cb_kwargs参数向回调函数传入参数
# 2020.3.7

from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

class ArticleSpider(CrawlSpider):
    name = 'articles'
    allowd_domains = ['baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E5%8C%97%E4%BA%AC/128981']
    rules = [
        Rule(LinkExtractor(allow=r'^(https://baike.baidu.com/item).*'), callback='parse_items', follow=True,
             cb_kwargs={'is_item': True}),
        Rule(LinkExtractor(allow='.*'), callback='parse_items',
             cb_kwargs={'is_item': False}),
    ]

    def parse_items(self, response, is_item):
        print(response.url)
        title = response.css('h1::text').extract_first()
        if is_item:
            url = response.url
            text = response.xpath('//div[@class="lemma-summary"]//text()').extract()
            print("Title is: {}".format(title))
            print("Text is: {}".format(text))
        else:
            print('This is not an item: {}'.format(title))
