from django.urls import path, include
from .views import scrape
urlpatterns = [
    path('webscrap',scrape)
]