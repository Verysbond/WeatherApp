from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    appid = 'd731ec31aa625c0a8a10db99f6b32f8e'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    city = "Minsk"
    res = requests.get(url.format(city)).json()
    city_info = {
        'city': city,
        'temp': res['main']['temp'],
        'icon': res['weather'][0]['icon']
    }
    context = {'info': city_info}
    return render(request, 'weather/weather.html', context)
