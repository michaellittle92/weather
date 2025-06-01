import datetime
import calendar
from dotenv import load_dotenv
import os
import requests
from weather_element import weather_element


def get_weather_data():
    response = call_openweathermap()
    weather_elements = []

    for day in response:
        date = convert_from_epoch(day["dt"]).date()
        weekday = get_day_from_date(convert_from_epoch(day["dt"]))
        max_temp = convert_kelvin_to_celsius(day["temp"]["max"])
        min_temp = convert_kelvin_to_celsius(day["temp"]["min"])
        description = day["weather"][0]["description"]
        icon = get_icon_url(day["weather"][0]["icon"])
        weather_elements.append(weather_element(date, weekday, max_temp, min_temp, description, icon))

    return weather_elements

def call_openweathermap():
    load_dotenv()
    api_key = os.environ["WEATHER_API"]
    lat = -37.9504939
    lon = 145.3678563
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={api_key}"
    resp = requests.get(url).json()
    daily = resp["daily"]
    return daily

def convert_from_epoch(epoch_time):
    dt = datetime.datetime.fromtimestamp(epoch_time)
    return dt

def get_day_from_date(dt):
    index = dt.weekday()
    return calendar.day_name[index]

def convert_kelvin_to_celsius(kelvin_temp):
    return round(kelvin_temp - 273.15, 1)

def get_icon_url(icon_code):
    return f"https://openweathermap.org/img/wn/{icon_code}.png"
