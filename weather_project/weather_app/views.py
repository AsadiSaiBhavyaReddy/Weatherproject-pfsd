from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Admin,User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login  # renamed the function
import requests

import requests
def weather(request):
    return render(request,"weather.html")

def logout(request):
    return render(request,"login.html")

def checkadminlogin(request):
    adminuname = request.POST["uname"]
    adminpwd = request.POST["pwd"]

    flag=Admin.objects.filter(Q(username=adminuname) & Q(password=adminpwd))
    print(flag)

    if flag:
        return redirect('weather')

    else:
        return HttpResponse("Login Failed")


from django.shortcuts import render
from django.http import HttpResponse
import requests

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
import requests

from django.shortcuts import render
import requests





def weather(request):
    temperature_unit = request.POST.get('temperature_unit', 'celsius')
    weather_data = None
    three_day_forecast = []
    past_temperature_celsius = None
    past_temperature_fahrenheit = None
    past_description = None  # Initialize past_description

    if request.method == 'POST':
        city = request.POST['city']
        api_key = '2036123b8e33228f996f8cfda6c85902'

        # For current weather
        current_weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
        response = requests.get(current_weather_url)
        data = response.json()

        if data.get('cod') == 404:  # Corrected '404' to 404 (integer)
            error_message = data.get('message', 'City not found.')
            return render(request, 'weather.html', {'error_message': error_message})

        temperature_celsius = data.get('main', {}).get('temp')
        if temperature_celsius is not None:
            temperature_fahrenheit = (temperature_celsius * 9/5) + 32
        else:
            temperature_fahrenheit = None

        description = data.get('weather')[0].get('description') if data.get('weather') else None
        icon = data.get('weather')[0].get('icon') if data.get('weather') else None

        weather_data = {
            'city': city,
            'temperature_celsius': temperature_celsius,
            'temperature_fahrenheit': temperature_fahrenheit,
            'description': description,
            'icon': icon
        }

        # For 5-day forecast
        forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={api_key}"
        forecast_response = requests.get(forecast_url)
        forecast_data = forecast_response.json()

        for entry in forecast_data.get('list', [])[:8]:  # Taking 8 entries for 3 days approx
            temp_celsius = entry['main']['temp']
            if temp_celsius is not None:
                temp_fahrenheit = (temp_celsius * 9/5) + 32
            else:
                temp_fahrenheit = None
            day_data = {
                'time': entry.get('dt_txt'),
                'temperature_celsius': temp_celsius,
                'temperature_fahrenheit': temp_fahrenheit,
                'description': entry['weather'][0]['description'],
                'icon': entry['weather'][0]['icon']
            }
            three_day_forecast.append(day_data)

        # Fetch past weather data
        past_temperature, past_description = get_past_weather(city, 3, api_key)
        past_temperature_celsius = past_temperature
        if past_temperature_celsius is not None:
            past_temperature_fahrenheit = (past_temperature_celsius * 9/5) + 32
        else:
            past_temperature_fahrenheit = None

    return render(request, 'weather.html', {
        'weather_data': weather_data,
        'three_day_forecast': three_day_forecast,
        'past_temperature_celsius': past_temperature_celsius,
        'past_temperature_fahrenheit': past_temperature_fahrenheit,
        'past_description': past_description,  # Add past_description to the context
        'temperature_unit': temperature_unit
    })

def get_past_weather(city, past_days, api_key):
    # Make an API request to fetch past weather data
    base_url = "http://api.openweathermap.org/data/2.5/past-weather"  # Replace with the actual API endpoint
    params = {
        'q': city,
        'cnt': past_days,
        'appid': api_key
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        past_data = response.json()
        # Extract and return relevant past weather information
        past_temperature = past_data.get('main', {}).get('temp')
        past_description = past_data.get('weather')[0].get('description')
        return past_temperature, past_description
    else:
        # Handle API request errors
        return None,"APIError"









