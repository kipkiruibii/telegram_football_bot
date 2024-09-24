import scrapy


class ThecrawlerSpider(scrapy.Spider):
    name = "thecrawler"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        yield response.css('')
