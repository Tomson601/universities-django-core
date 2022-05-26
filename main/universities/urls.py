from django.urls import include, re_path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r"universities", views.UniversityViewSet, basename="universities")
router.register(r"country", views.CountryViewSet, basename="country")

urlpatterns = [
    re_path(r"^", include(router.urls)),
]