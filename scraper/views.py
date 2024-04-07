from django.shortcuts import HttpResponse
from Generalscrapers.spiders import AltexSpider, EmagParse
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from Generalscrapers import settings as my_settings
import json
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from scraper.models import Item


spiders_dict = {
    "altex_parse" : AltexSpider,
    "emag_parse" : EmagParse
}

def index(request):
    return HttpResponse("ok")

@csrf_exempt
def scrape_url(request):
    
    if request.method == "POST":
        
        parser = request.POST.get("parser")
        url = request.POST.get("url")

        crawler_settings = Settings()
        crawler_settings.setmodule(my_settings)
        
        process = CrawlerProcess(settings=crawler_settings)

        body = json.loads(request.body.decode('utf-8'))    
        
        process.crawl(spiders_dict.get(parser), start_urls = [url])
        process.start(stop_after_crawl=True, install_signal_handlers=False)      
        process.stop()

        return HttpResponse("URL has been scraped")
    
def home_view(request):
    template = loader.get_template("land_page_scraper.html")
    return HttpResponse(template.render())

def load_table(request):

    template = loader.get_template("scraper_list.html")

    items= Item.objects.all().values()
    header_list = Item._meta.fields
    return(HttpResponse(template.render({"header_list" : header_list, "items": items})))

def options_bar(request):

    template = loader.get_template("scrape_options.html")

    options = [
        {"name" : "Altex", "value" : "altex_parse"},
        {"name" : "Emag", "value" : "emag_parse"}
    ]

    return(HttpResponse(template.render({"options": options})))