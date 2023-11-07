from scrapy_djangoitem import DjangoItem
from scraper.models import Item

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()

# from django.core.management import call_command

class GeneralscrapersItem(DjangoItem):
    django_model = Item