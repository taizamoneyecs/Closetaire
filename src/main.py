from src.services.weather_api import get_weather
from src.parsers.event_parser import parse_event
from src.services.llm_handler import get_suggestion
import re

def extract_temperature(weather_string):
    """
    Improved temperature extraction from weather API response
    """
    try:
        # Multiple patterns to catch different weather string formats
        patterns = [
            r'currently\s+([-\d]+\.?\d*)°?C',  # "currently 19.84°C"
            r'([-\d]+\.?\d*)°?C',              # "19.84°C"
            r'temperature[^\d]+([-\d]+\.?\d*)' # "temperature: 19.84"
        ]
        
        for pattern in patterns:
            match = re.search(pattern, weather_string)
            if match:
                return float(match.group(1))
                
    except (ValueError, AttributeError):
        pass
    
    return None

def main():
    print("Hello, I am your personal shopper. How can I assist you today?")
    user_input = input("> ")
    
    city, start_date, end_date, event_type = parse_event(user_input)
    
    if not city:
        city = input("I couldn't detect the city. Please enter it: ")
    if not event_type:
        event_type = input("What type of event is this? (wedding/business/casual/skiing/beach): ").lower()

    weather_data = get_weather(city)

    if "error" in weather_data and "404" in weather_data["error"]:
        print(f"Sorry, '{city}' doesn't seem to be a valid city. Please try again.")
        city = input("Enter a valid city: ")
        weather_data = get_weather(city)

    if "error" in weather_data:
        print(weather_data["error"])
        return

    print(f"\n  Weather for {city}:")
    print(f"   Temperature: {weather_data['temperature']}°C (feels like {weather_data['feels_like']}°C)")
    print(f"   Conditions: {weather_data['description']}")
    print(f"   Humidity: {weather_data['humidity']}%")
    print(f"   Wind: {weather_data['wind_speed']} m/s")
    
    real_temperature = weather_data["temperature"]
    
    print("\n Generating outfit suggestions...")
    suggestions = get_suggestion(weather_data['full_string'], event_type, real_temperature)
    
    print("\n Outfit Suggestions:")
    print("-" * 50)
    print(suggestions)
    print("-" * 50)

if __name__ == "__main__":
    main()