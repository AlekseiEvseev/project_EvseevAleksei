# стягивает всю страницу

import scrapy

class FullPageSpider(scrapy.Spider):

    name = 'full_page'
    start_urls = ['https://www.litres.ru/genre/knigi-detektivy-5022/']

    def parse(self, response):
        filename = response.url.split('/')[-1] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
            