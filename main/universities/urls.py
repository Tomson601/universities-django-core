from django.urls import re_path
from rest_framework import routers
from . import views


urlpatterns = [
    re_path("search/", views.SearchResultsView.as_view(), name="search_results"),
    re_path("home/", views.HomePageView.as_view(), name="home"),
]