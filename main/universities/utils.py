from universities import models
import requests

MAIN_URL = 'http://universities.hipolabs.com/search?'

def get_universities_json():
    response = requests.get(MAIN_URL)
    data = response.json()

    for school in data:
        university = models.University.objects.create(
            code = str(school["alpha_two_code"]),
            country = models.Country.objects.get(country_name=school["country"]),
            state_province = school["state-province"],
            domains = str(school["domains"]),
            name = str(school["name"]),
            web_pages = str(school["web_pages"])
        )
        university.save()
    return "SUCCESS"

def get_countries():
    response = requests.get(MAIN_URL)
    data = response.json()

    for school in data:
        if models.Country.objects.filter(country_name=school["country"]).exists() == True:
            continue
        else:
            country = models.Country.objects.create(
                country_name = str(school["country"])
            )
            country.save()
    return "SUCCESS"

def update_database():
    get_countries()
    get_universities_json()
    return "SUCCESS"

# TODO: Fix Republic of Congo model