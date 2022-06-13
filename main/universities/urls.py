from django.urls import include, re_path
from rest_framework import routers
from . import views


# router = routers.DefaultRouter()
# router.register(r"universities", views.UniversityViewSet, basename="universities")
# router.register(r"country", views.CountryViewSet, basename="country")

urlpatterns = [
    #re_path(r"^", include(router.urls)),
    re_path("search/", views.SearchResultsView.as_view(), name="search_results"),
    re_path("home/", views.HomePageView.as_view(), name="home"),
    re_path("universities/", views.UniversityView.as_view(), name="universities"),
    # re_path("uni/", views.UniversityViewSet.as_view(), name="universities"),
    # re_path("country/", views.CountryViewSet.as_view(), name="country")
]