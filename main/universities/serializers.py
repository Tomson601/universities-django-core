from rest_framework import serializers
from universities import models


class UniversitySerializer(serializers.ModelSerializer):
    code = serializers.ReadOnlyField()
    country = serializers.ReadOnlyField()
    state_province = serializers.ReadOnlyField()
    domains = serializers.ReadOnlyField()
    name = serializers.ReadOnlyField()
    web_pages = serializers.ReadOnlyField()

    class Meta:
        model = models.University
        fields = ("identifier", "code", "country", "state_province", "domains", "name", "web_pages")
