import scrapy
from Generalscrapers.items import GeneralscrapersItem
import datetime
import json

class AltexSpider(scrapy.Spider):
    name = 'Altex_parser'
    allowed_domains = ['altex.ro']
    start_urls = ["https://altex.ro/casuta-gradina-keter-oakland-754-duotech-210-x-124-8-x-253-cm-bej-maro-inchis/cpd/MDE246956/"]

    def parse(self, response):

        fields = GeneralscrapersItem()

        json_ld = json.loads(response.xpath("//script[contains(text(),'Product')]/text()").get())

        link = response.url
        fields["link"] = link

        name = json_ld['name']
        fields["name"] = name

        time_scraped = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        fields["time_scraped"] = time_scraped

        price = response.xpath("//span[@class='Price-int leading-none']/text()").get().replace(".", "")
        fields["price"] = price

        description= response.xpath("//meta[@name='description']/@content").get()
        fields["description"] = description

        attributes = response.xpath("//div[@id='additional']//tr").getall()
        attribute_json = {}
        for attr in attributes:
            key = attr.xpath("./th/text()").get()
            value = attr.xpath("./td/text()").get()
            attribute_json[key] = value

        fields["attributes"] = json.dumps(attribute_json)

        is_available = True if price else False
        fields["is_available"] = is_available

        yield fields

