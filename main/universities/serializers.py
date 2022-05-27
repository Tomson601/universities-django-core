from rest_framework import serializers
from universities import models


class UniversitySerializer(serializers.ModelSerializer):
    code = serializers.CharField()
    country = serializers.CharField()
    state_province = serializers.CharField()
    domains = serializers.CharField()
    name = serializers.CharField()
    web_pages = serializers.CharField()

    class Meta:
        model = models.University
        fields = ["id", "code", "country", "state_province", "domains", "name", "web_pages"]


class CountrySerializer(serializers.ModelSerializer):
    country_name = serializers.CharField()

    class Meta:
        model = models.Country
        fields = ["id", "country_name"]
