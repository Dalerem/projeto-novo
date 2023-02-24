import scrapy

class Tjsp1Spider(scrapy.Spider):
    name = "tjsp1"
    start_urls = ["https://esaj.tjsp.jus.br/esaj/portal.do?servico=190090"]

    def parse(self, response):
        for consultas in response.css('.esajTabelaServico'):
            yield {
                'titulos': consultas.css('.esajCelulaDescricaoServicos a::text').get()
            }

