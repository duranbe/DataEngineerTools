import scrapy

class ChurchillQuotesSpider(scrapy.Spider):
    name = "citations de Churchill"
    start_urls = ["http://evene.lefigaro.fr/citations/winston-churchill",]

    def parse(self, response):
        author = response.xpath('//div[@class="figsco__fake__col-9"]')
        
        for cit in response.xpath('//div[@class="figsco__quote__text"]'):
            text_value = cit.xpath('a/text()').extract_first()
            text_value = text_value.replace(u"\u201C",'').replace(u"\u201D",'')
            current_author=author.pop().xpath('a/text()').extract_first()
            yield { 'text' : text_value, 'author':current_author }