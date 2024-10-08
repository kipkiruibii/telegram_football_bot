import scrapy
from scrapy_playwright.page import PageMethod
from scrapy.crawler import CrawlerProcess


class BookscraperSpider(scrapy.Spider):
    name = "bookscraper"

    # allowed_domains = ["books.toscrape.com"]
    # start_urls = ["https://books.toscrape.com/"]

    def start_requests(self):
        yield scrapy.Request("https://www.flashscore.co.ke/", meta={
            "playwright": True,
            'playwright_page': {'timeout': 90000},
            "playwright_page_methods": [
                PageMethod("wait_for_selector", '.filters__tab'),
            ],
        }, )

    def parse(self, response):
        items = response.css('.filters__tab')
        for i in items:
            print(i)
        # for item in items:
        #     yield {
        #         'tab': item.css('.filters__text::text').get()
        #
        #     }
