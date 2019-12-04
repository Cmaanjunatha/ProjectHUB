from django.shortcuts import render, redirect
from .models import register

# Create your views here.
def home(request):

    return render(request, 'home.html', {})




def about(request):
    import json
    import requests

    #city = input('City Name :')
    url = 'https://api.openweathermap.org/data/2.5/weather?q=delhi&appid=c024db4252df483d3b82b661c1c4bb7f'
    api = requests.get(url)
    api = api.json()
    # print(json_data)
    #print(format_add)
    return render(request, 'about.html', {'api': api})



def location(request):
    import requests
    import json
    #city = input('City Name :')
    url = 'https://api.openweathermap.org/data/2.5/weather?q=delhi&appid=c024db4252df483d3b82b661c1c4bb7f'
    api = requests.get(url)
    api = api.json()
    return render(request, 'location.html', {'api': api})


'''

def form_submission(request):
    city = cityinfo()
    city= cityinfo.city
    #city_name = request.POST["city"]
    #city_info = cityinfo(city_name='city_name')
    #city_info.save()
    print(city)
    return render(request, 'home.html', {'city': city})
    
'''
