from universities import models

country = models.Country.objects.get(country_name="Poland")
universities = models.University.objects.filter(country=country)
university_list = []
for school in universities:
    university_list.append(school)

for school in university_list:
    print(school)
