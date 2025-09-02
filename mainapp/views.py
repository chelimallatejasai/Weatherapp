# main/views.py
from django.shortcuts import render
import requests

def index(request):
    weather_data = {}
    error_message = None

    if request.method == "POST":
        city = request.POST.get('city')  # get city from form input
        api_key = "4d017260473a636a424c320f85044ba8"  # 🔑 replace with your OpenWeatherMap API key
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        try:
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                weather_data = {
                    "city": data["name"],
                    "temperature": data["main"]["temp"],
                    "humidity": data["main"]["humidity"],
                    "pressure": data["main"]["pressure"],
                    "description": data["weather"][0]["description"].capitalize(),
                    "icon": data["weather"][0]["icon"],  # for weather icon
                }
            else:
                error_message = data.get("message", "Something went wrong. Try again!")

        except Exception as e:
            error_message = str(e)

    return render(request, "mainapp/weather.html", {"weather_data": weather_data, "error_message": error_message})
