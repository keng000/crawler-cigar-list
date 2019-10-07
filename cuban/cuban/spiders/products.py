# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from w3lib import html

class ProductsSpider(CrawlSpider):
    name = 'products'
    allowed_domains = ['www.cubancigarwebsite.com']
    # start_urls = ['http://www.cubancigarwebsite.com/']
    start_urls = ['https://www.cubancigarwebsite.com/brands/']

    # rules = (
    #     Rule(LinkExtractor(allow=r'/brand/.*'), callback='parse_item', follow=True),
    # )

    def parse_start_url(serf, response):
        for url in response.css(".brandImage").css("a::attr('href')").extract():
            yield response.follow(url, callable=serf.parse)

    def parse(self, response):
        for _i in response.css('div[itemtype="http://schema.org/Product"]'):
            item = {}
            item['brand'] = _i.css('[itemtype="http://schema.org/Brand"]').css('::text').extract_first().strip()
            item['name'] = _i.css('.cigarDetailsName::text').extract_first().strip()
            item['shape'] = html.remove_tags(_i.css('.cigarDetailsCommonName').get()).strip()
            path = _i.css("img::attr('src')").get()
            item['img'] = f"{response.url}{path}"
            yield item
