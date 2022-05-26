from universities import models

country = models.Country.objects.create(country_name="Poland")

country.save()
