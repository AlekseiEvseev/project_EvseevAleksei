# Задача 2: собрать данные об авторах и названиях книг

import scrapy

class LitresSpider(scrapy.Spider):
    name = 'litres_parser'
    start_urls = ['https://www.litres.ru/genre/knigi-detektivy-5022/']


# запрос к shell
# response.xpath('//div[@class="art-item__info"]/div/a/text()').get()

    def parse(self, response):
        for book in response.xpath('//div[@class="art-item__info"]'):
            name = book.xpath('div[@class="art-item__name"]/a/text()').get()
            author = book.xpath('div[@class="art-item__author"]/a/text()').get()

            yield {
                'name': name,
                'author': author,
            }
