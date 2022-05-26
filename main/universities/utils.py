from universities import models
import requests
import json

def get_universities_json():
    url = 'http://universities.hipolabs.com/search?country=Poland'
    response = requests.get(url)
    data = response.json()

    for school in data:
        print(school)

    return data