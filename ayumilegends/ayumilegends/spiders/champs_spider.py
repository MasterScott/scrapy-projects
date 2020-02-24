import scrapy
import re


class ChampItem(scrapy.Item):
    # Overview
    Champion = scrapy.Field()
    Faction = scrapy.Field()
    Rarity = scrapy.Field()
    Role = scrapy.Field()
    Affinity = scrapy.Field()

    # Stats
    HP = scrapy.Field()
    ATK = scrapy.Field()
    DEF = scrapy.Field()
    SPD = scrapy.Field()
    CRATE = scrapy.Field()
    CDMG = scrapy.Field()
    RESIST = scrapy.Field()
    ACC = scrapy.Field()


class ChampSpider(scrapy.Spider):
    name = "champs"
    allowed_domains = ["ayumilove.net"]
    start_urls = ["https://ayumilove.net/"
                  "raid-shadow-legends-list-of-champions-by-rarity/"]

    def parse(self, response):
        links = response.css('div.entry-content ol li a::attr(href)').extract()
        for link in links:
            yield scrapy.Request(link, callback=self.parse_attr)

    def parse_attr(self, response):
        item = ChampItem()
        h1_text = response.css('h1::text').get()
        h1_text = h1_text.replace('Raid Shadow Legends ', '')
        h1_text = h1_text.replace(' Skill Mastery Equip Guide', '')
        item['Champion'] = h1_text

        overview = response.xpath("//td[contains(., \
                                  'Overview')]").css('a::text').getall()

        item['Faction'] = overview[0]
        item['Rarity'] = overview[1]
        item['Role'] = overview[2]
        item['Affinity'] = overview[3]

        stats = response.xpath("//td[contains(., \
                               'Total Stats')]").css('p::text').getall()

        item['HP'] = re.split('\:\s', stats[0])[1].replace(',', '').strip()
        item['ATK'] = re.split('\:\s', stats[1])[1].replace(',', '').strip()
        item['DEF'] = re.split('\:\s', stats[2])[1].replace(',', '').strip()
        item['SPD'] = re.split('\:\s', stats[3])[1].strip()
        item['CRATE'] = re.split('\:\s', stats[4])[1].strip()
        item['CDMG'] = re.split('\:\s', stats[5])[1].strip()
        item['RESIST'] = re.split('\:\s', stats[6])[1].strip()
        item['ACC'] = re.split('\:\s', stats[7])[1].strip()

        return item
