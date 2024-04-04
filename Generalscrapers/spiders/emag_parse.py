import scrapy
from Generalscrapers.items import GeneralscrapersItem
import datetime
import json
import re

class EmagParse(scrapy.Spider):
    name = 'Emag_parser'
    allowed_domains = ['emag.ro']
    start_urls = ["https://www.emag.ro/statie-de-andocare-usb-c-13-in-1-port-gigabit-ethernet-de-1000-mbps-4k-hdmi-port-vga-usb3-0-usb2-0-port-de-date-usb-c-slot-pentru-card-sd-card-tf-3-5-mm-audio-mic-vaxiuja-universal-argint-20-sshytzw/pd/DX5K9TYBM/?ref=profiled_categories_campaign_1_1&provider=rec&recid=rec_94_bd883080eb6ee6a1469c513185a604a61d8ab3ca8ff1d61b5c6f732e01d44bfc_1711413105&scenario_ID=94"]

    def parse(self, response):

        fields = GeneralscrapersItem()

        json_ld = json.loads(response.xpath("//script[contains(text(),'Product')]/text()").get())

        link = response.url
        fields["url"] = link

        name = json_ld['name']
        fields["name"] = name

        time_scraped = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        fields["time_scraped"] = time_scraped

        price = json_ld["offers"]["price"]
        fields["price"] = round(float(price),2)

        description= response.xpath("//meta[@name='description']/@content").get()
        fields["description"] = description
        
        categories = response.xpath("//ol[@class='breadcrumb']/li//text()").getall()
        fields["category"] = "/".join(categories)

        attributes = response.xpath("//table[@class='table table-striped specifications-table']//tr").getall()
        attribute_json = {}
        for attr in attributes:
            key = attr.xpath("./td[1]/text()").get()
            value = attr.xpath("./td[2]/text()").get()
            attribute_json[key] = value

        # print(attribute_json)

        fields["attributes"] = json.dumps(attribute_json)

        is_available = True if json_ld["availability"] == "http://schema.org/InStock" else False
        fields["is_available"] = is_available

        yield fields

