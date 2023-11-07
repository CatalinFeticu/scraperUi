from django.db import models
from django.utils import timezone

import datetime

class Item(models.Model):
    name = models.CharField(max_length=500)
    link = models.URLField(max_length=500)
    time_scraped = models.DateTimeField("Date scraped",auto_now=True)
    price = models.FloatField()
    original_price = models.FloatField(null=True,blank=True)
    description = models.CharField(max_length=500)
    attributes = models.JSONField()
    category = models.JSONField(null=True,blank=True)
    is_available = models.BooleanField()
    data = models.JSONField(null=True,blank=True)

    def __str__(self):
        return self.link
    
    def is_promotion(self):
        return bool(self.original_price and self.price != self.original_price)
            

class Link(models.Model):
    link = models.URLField(max_length=500)
    time_scraped = models.DateTimeField("Date scraped", auto_now=True)
    is_new = models.BooleanField()
    data = models.JSONField(null=True,blank=True)
    def __str__(self):
        return self.link
