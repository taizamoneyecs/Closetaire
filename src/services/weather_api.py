# -*- coding: utf-8 -*-
import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load .env file
API_KEY = os.getenv("OPENWEATHER_API_KEY") 

def get_weather(city):
    """
    Fetch weather data for a given city from OpenWeatherMap API.
    Returns formatted weather string or error message.
    """
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise exception for bad status codes
        
        data = response.json()
        desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        
        return f"It's currently {temp}\u00B0C with {desc} in {city}. Humidity: {humidity}%."
        
    except requests.exceptions.RequestException as e:
        return f"Sorry, I couldn't fetch the weather for {city}. Error: {str(e)}"
    except KeyError:
        return "Sorry, the weather data format was unexpected."