from django.shortcuts import render
import requests
from .models import City
# Create your views here.

def index(request):

    appid = 'd731ec31aa625c0a8a10db99f6b32f8e'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    cities = City.objects.all()

    all_cities = []
    for city in cities:
        res = requests.get(url.format(city.name))
        if res.status_code == 404:
            continue
        city_weather = res.json()
        city_info = {
            'city': city.name,
            'temp': city_weather["main"]["temp"],
            'icon': city_weather["weather"][0]["icon"]
        }
        all_cities.append(city_info)

    context = {'all_info': all_cities}
    return render(request, 'weather/weather.html', context)



#
# You don't check that the data for the specific city is found.
# You loop through all cities in your database, and try to get the weather for each one;
# but you don't check that the result is actually returned. You should do:
# for city in cities:
#     response = requests.get(url.format(city))
#     if response.status_code == 404:
#         continue
#     city_weather = response.json()
#
#Also, you should check that you are formatting your URL properly.
# As it stands, you are inserting your City object directly into the URL
# - this will only work if you have defined a __str__ method that returns only the city name.
# It would be better to use the name directly:
#     response = requests.get(url.format(city.name))


