from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from universities.views import get_data

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path("", include("universities.urls")),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),
    path('universities/', get_data, name='universities'),
]
