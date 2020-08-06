import scrapy


class WithscrapySpider(scrapy.Spider):
    name = 'withscrapy'
    allowed_domains = ['45.77.40.141']
    start_urls = ['http://45.77.40.141/toko/web/login']

    def parse(self, response):
        data = {
            "email": "egi@egi.com",
            "password": "123"
        }
        return scrapy.FormRequest(
            url="http://45.77.40.141/toko/web/masuk",
            formdata=data,
            callback=self.after_login
        )

    def after_login(self, response):
        products = response.xpath('//div[@class="snipcart-thumb"]')
        all_data = []
        data = {}
        for d in products:
            data['link'] = d.xpath('.//a/@href').get()
            data['title'] = d.xpath('.//p/text()').get()
            yield data

        # products = response.css('.products-right .col-md-4 .snipcart-thumb a::attr(href)').getall()
        # for d in products:
        #     yield response.follow(d, callback=self.parse_detail)

    # def parse_detail(self, response):
    #     title = response.xpath('//h2/text()').get()
    #     desc = response.xpath('//div[@class="w3agile_description"]/p/text()').getall()
    #     return {
    #         "title": title,
    #         "desc": desc
    #     }
