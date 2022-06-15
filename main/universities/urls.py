from django.urls import re_path
from . import views
from universities.views import get_data

urlpatterns = [
    re_path("search/", views.SearchResultsView.as_view(), name="search_results"),
    re_path("home/", views.HomePageView.as_view(), name="home"),
    re_path('universities/', get_data, name='universities'),
]