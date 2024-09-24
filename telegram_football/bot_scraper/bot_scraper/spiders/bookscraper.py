import scrapy
from scrapy_playwright.page import PageMethod
from scrapy.crawler import CrawlerProcess

class BookscraperSpider(scrapy.Spider):
    name = "bookscraper"
    # allowed_domains = ["books.toscrape.com"]
    # start_urls = ["https://books.toscrape.com/"]

    def start_requests(self):
        yield scrapy.Request("https://books.toscrape.com/", meta={
            "playwright": True,
            "playwright_page_methods": [
                # PageMethod("wait_for_selector", '.filters__tab'),
            ],
        }, )

    def parse(self, response):
        # items = response.css('.filters__tab')
        yield {
            'title': 'items'

        }

