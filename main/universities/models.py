from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=150, null=False)

    def __str__(self):
        return {
            self.country_name
            }

class University(models.Model):
    code = models.CharField(max_length=25)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, related_name="country", null=False)
    state_province = models.CharField(max_length=200, null=True)
    domains = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    web_pages = models.CharField(max_length=300)

    def __str__(self):
        return {
            self.name,
            self.country.name
        }
