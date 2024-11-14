import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/smartphone-8gb-ram"]

    

    def parse(self, response):

        produtos = response.css('div.ui-search-result__wrapper')

        for produto in produtos:
            
            yield{
                'brand': produto.css('span.poly-component__brand::text').get()
            }