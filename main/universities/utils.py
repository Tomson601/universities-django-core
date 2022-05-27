from universities import models
import requests


def get_universities_json():
    url = 'http://universities.hipolabs.com/search?country=Poland'
    response = requests.get(url)
    data = response.json()

    keys = ["web_pages", "name", "alpha_two_code", "state-province",  "domains", "country"]
    poland = models.Country.objects.get(country_name="Poland")

    for school in data:
        university = models.University.objects.create(
            code = str(school["alpha_two_code"]),
            country = models.Country.objects.get(country_name="Poland"),
            state_province = school["state-province"],
            domains = str(school["domains"]),
            name = str(school["name"]),
            web_pages = str(school["web_pages"])
        )
        university.save()
    return "SUCCESS"
