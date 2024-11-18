import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/smartphone-8gb-ram"]

    

    def parse(self, response):

        produtos = response.css('div.ui-search-result__wrapper')
        page_max = 1

        for produto in produtos:

            precos = produto.css('span.andes-money-amount__fraction::text').getall()
            
            yield{
                'brand': produto.css('span.poly-component__brand::text').get(),
                'nome': produto.css('h2.poly-box.poly-component__title a::text').get(),
                'preco_antigo': precos[0] if len(precos) > 0 else None,
                'preco_novo': precos[1] if len(precos) > 0 else None,
                'rating': produto.css('span.poly-reviews__rating::text').get(),
                'qtd_review': produto.css('span.poly-reviews__total::text').get()
            }

        while page_max < 10:
            next_page = response.css('li.andes-pagination__button.andes-pagination__button--next a::attr(href)').get()
            yield scrapy.Request(next_page, callback=self.parse)
            page_max += 1