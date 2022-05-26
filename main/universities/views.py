from universities import models, serializers
from rest_framework.viewsets import ModelViewSet


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
