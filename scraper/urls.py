from django.urls import path

from . import views
    
urlpatterns = [
    path("", views.home_view, name="index"),
    path("scrape_url", views.scrape_url, name="scrape_url"),
    path("load_table", views.load_table, name="load_table")
]