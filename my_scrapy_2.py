# p60 带规则的爬取
# 2020.3.7

from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

class ArticleSpider(CrawlSpider):
    name = 'articles'
    allowd_domains = ['baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E5%8C%97%E4%BA%AC/128981']
    rules = [Rule(LinkExtractor(allow=r'.*'), callback='parse_items', follow=True)]

    def parse_items(self, response):
        url = response.url
        title = response.css('h1::text').extract_first()
        text = response.xpath('//div[@class="lemma-summary"]//text()').extract()
        print('URL is:{}'.format(url))
        print("Title is: {}".format(title))
        print("Text is: {}".format(text))