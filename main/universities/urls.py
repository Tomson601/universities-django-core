from django.urls import include, re_path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r"university", views.UniversityViewSet, basename="university")

urlpatterns = [
    re_path(r"^", include(router.urls)),
]