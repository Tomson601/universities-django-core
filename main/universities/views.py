from universities import models, serializers
from rest_framework.viewsets import ModelViewSet
from django.views.generic import TemplateView, ListView
from universities import models
from django.db.models import Q
from django.shortcuts import render


def get_data(request):
    
    my_data = models.University.objects.all()
    
    context={
      'my_data':my_data,
    } 
    return render(request, 'universities_list.html', context)


class UniversityViewSet(ModelViewSet):
    queryset = models.University.objects.all()
    serializer_class = serializers.UniversitySerializer
    lookup_field = "identifier"
    lookup_url_kwarg = "identifier"
    http_method_names = ["get"]


class CountryViewSet(ModelViewSet):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer
    lookup_field = "identifier"
    lookup_url_kwarg = "identifier"
    http_method_names = ["get"]


class HomePageView(TemplateView):
    template_name = 'home_page.html'


class UniversityView(TemplateView):
    template_name = 'universities_list.html'


class SearchResultsView(ListView):
    model = models.University
    template_name = 'search_results.html'
    #queryset = models.University.objects.filter(country=49)

    def get_queryset(self): # new
        query = self.request.GET.get("q")
        object_list = models.University.objects.filter(
            Q(code=query)
        )
        return object_list
