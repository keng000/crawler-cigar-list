# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from w3lib import html


class ProductsSpider(CrawlSpider):
    name = "products"
    allowed_domains = ["cubancigarwebsite.com"]
    # start_urls = ['http://www.cubancigarwebsite.com/']
    # start_urls = ['https://www.cubancigarwebsite.com/brands/']
    start_urls = [
        "https://www.cubancigarwebsite.com/brand/cohiba",
        "https://www.cubancigarwebsite.com/brand/h-upmann",
        "https://www.cubancigarwebsite.com/brand/hoyo-de-monterrey",
        "https://www.cubancigarwebsite.com/brand/montecristo",
        "https://www.cubancigarwebsite.com/brand/partagas",
        "https://www.cubancigarwebsite.com/brand/romeo-y-julieta",
        "https://www.cubancigarwebsite.com/brand/bolivar",
        "https://www.cubancigarwebsite.com/brand/punch",
        "https://www.cubancigarwebsite.com/brand/ramon-allones",
        "https://www.cubancigarwebsite.com/brand/trinidad",
        "https://www.cubancigarwebsite.com/brand/jose-l-piedra",
        "https://www.cubancigarwebsite.com/brand/quintero",
        "https://www.cubancigarwebsite.com/brand/vegueros",
        "https://www.cubancigarwebsite.com/brand/cuaba",
        "https://www.cubancigarwebsite.com/brand/diplomaticos",
        "https://www.cubancigarwebsite.com/brand/el-rey-del-mundo",
        "https://www.cubancigarwebsite.com/brand/fonseca",
        "https://www.cubancigarwebsite.com/brand/juan-lopez",
        "https://www.cubancigarwebsite.com/brand/la-flor-de-cano",
        "https://www.cubancigarwebsite.com/brand/la-gloria-cubana",
        "https://www.cubancigarwebsite.com/brand/por-larranaga",
        "https://www.cubancigarwebsite.com/brand/quai-dorsay",
        "https://www.cubancigarwebsite.com/brand/rafael-gonzalez",
        "https://www.cubancigarwebsite.com/brand/saint-luis-rey",
        "https://www.cubancigarwebsite.com/brand/san-cristobal",
        "https://www.cubancigarwebsite.com/brand/sancho-panza",
        "https://www.cubancigarwebsite.com/brand/vegas-robaina",
        "https://www.cubancigarwebsite.com/brand/belinda",
        "https://www.cubancigarwebsite.com/brand/club",
        "https://www.cubancigarwebsite.com/brand/guantanamera",
        "https://www.cubancigarwebsite.com/brand/mini",
        "https://www.cubancigarwebsite.com/brand/puritos",
        "https://www.cubancigarwebsite.com/brand/troya",
        "https://www.cubancigarwebsite.com/brand/cubatabaco",
        "https://www.cubancigarwebsite.com/brand/edmundo-dantes",
        "https://www.cubancigarwebsite.com/brand/habanos",
        "https://www.cubancigarwebsite.com/brand/cabanas",
        "https://www.cubancigarwebsite.com/brand/caney",
        "https://www.cubancigarwebsite.com/brand/cifuentes",
        "https://www.cubancigarwebsite.com/brand/davidoff",
        "https://www.cubancigarwebsite.com/brand/dunhill",
        "https://www.cubancigarwebsite.com/brand/gispert",
        "https://www.cubancigarwebsite.com/brand/la-corona",
        "https://www.cubancigarwebsite.com/brand/la-escepcion",
        "https://www.cubancigarwebsite.com/brand/la-flor-del-caney",
        "https://www.cubancigarwebsite.com/brand/los-statos-de-luxe",
        "https://www.cubancigarwebsite.com/brand/maria-guerrero",
        "https://www.cubancigarwebsite.com/brand/san-luis-rey",
        "https://www.cubancigarwebsite.com/brand/siboney",
    ]
    # rules = (
    #     Rule(LinkExtractor(allow=r'\/brand\/.*'), callback='parse', follow=True),
    # )

    # def parse_start_url(serf, response):
    #     for url in response.css(".brandImage").css("a::attr('href')").extract():
    #         yield response.follow(url, callable=serf.parse)

    def parse(self, response):
        for _i in response.css('div[itemtype="http://schema.org/Product"]'):
            item = {}
            item["brand"] = _i.css('[itemtype="http://schema.org/Brand"]').css("::text").extract_first().strip()
            item["name"] = _i.css(".cigarDetailsName::text").extract_first().strip()
            item["shape"] = html.remove_tags(_i.css(".cigarDetailsCommonName").get()).strip()
            path = _i.css("img::attr('src')").get()
            item["img"] = f"https://www.cubancigarwebsite.com{path}"
            yield item
