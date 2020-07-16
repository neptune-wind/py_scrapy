# p59 简单爬取网页和标题
# 2020.3.7

import scrapy
from urllib.parse import quote

url1 = 'https://baike.baidu.com/item/%E9%9D%92%E5%B2%9B/60244'
url2 = 'https://baike.baidu.com/item/%E5%8E%A6%E9%97%A8'
url3 = 'https://baike.baidu.com/item/%E4%B8%8A%E6%B5%B7/114606'

class ArticleSpider(scrapy.Spider):
    name = 'article'

    def start_requests(self):
        urls = \
        [
            url1, url2, url3
        ]
        return[scrapy.Request(url=url, callback=self.parse)
               for url in urls]

    def parse(self, response):
        url = response.url
        title = response.css('h2::text').extract_first()
        print('URL is:{}'.format(url))
        print("Title is: {}".format(title))