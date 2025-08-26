# -*- coding: utf-8 -*-
import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load .env file
API_KEY = os.getenv("OPENWEATHER_API_KEY") 

def get_weather(city):
    """
    Enhanced to return more weather data
    """
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        feels_like = data["main"]["feels_like"]
        
        return {
            "description": desc,
            "temperature": temp,
            "humidity": humidity,
            "wind_speed": wind_speed,
            "feels_like": feels_like,
            "city": city,
            "full_string": f"It's currently {temp}°C (feels like {feels_like}°C) with {desc} in {city}. Humidity: {humidity}%, Wind: {wind_speed} m/s."
        }
        
    except requests.exceptions.RequestException as e:
        return {"error": f"Sorry, I couldn't fetch the weather for {city}. Error: {str(e)}"}
    except KeyError:
        return {"error": "Sorry, the weather data format was unexpected."}