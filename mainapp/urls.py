from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    # path('rss/', views.parse_and_save_rss, name = "parse")
    path('rss/', views.rand, name = "parse")
]
