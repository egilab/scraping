import scrapy


class SiScrapy(scrapy.Spider):
    name = "siscrapy"
    allowed_domains = ['45.77.40.141']
    start_urls = ['http://45.77.40.141/toko/web/login']

    def parse(self, response):
        title = response.css('title::text').get()
        yield {"title": title}
