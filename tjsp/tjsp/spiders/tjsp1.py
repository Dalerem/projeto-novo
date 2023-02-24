import scrapy

class Tjsp1Spider(scrapy.Spider):
    name = "tjsp1"
    start_urls = ["https://esaj.tjsp.jus.br/esaj/portal.do?servico=190090"]

    # Função resposta
    def parse(self, response):
        for consultas in response.css('.esajTabelaServico'):
            # Coletar os titulos
            yield {
                'titulos': consultas.css('.esajCelulaDescricaoServicos a::text').get()
            }

