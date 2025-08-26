from src.services.weather_api import get_weather
from src.parsers.event_parser import parse_event
from src.services.llm_handler import get_suggestion
import re

def extract_temperature(weather_string):
    """
    Extract temperature from your formatted weather string.
    Example: "It's currently 15°C with..." → returns 15
    """
    try:
        # Pattern to find temperature value (digits before °C)
        match = re.search(r'currently\s+(-?\d+)', weather_string)
        if match:
            return float(match.group(1))
        
        # Alternative pattern if first one fails
        match = re.search(r'(-?\d+)°C', weather_string)
        if match:
            return float(match.group(1))
            
    except (ValueError, AttributeError):
        pass
    
    return None

def main():
    print("Hello, I am your personal shopper. How can I assist you today?")
    
    # Initialize variables
    city = None
    event_type = None
    weather_result = None
    temperature = None
    
    # Keep asking until we get valid location and weather
    while True:
        # Get user input
        user_input = input("\n> ")
        
        # Parse input for event details
        city, start_date, end_date, event_type = parse_event(user_input)
        
        # If city not detected, ask specifically
        if not city:
            city = input("I couldn't detect the city. Please enter it: ")
        
        # If event type not detected, ask specifically
        if not event_type:
            event_type = input("What type of event is this? (wedding/business/casual/skiing): ").lower()
        
        # Get weather information
        weather_result = get_weather(city)
        
        # Check if weather API call was successful
        if "Sorry" not in weather_result and "Error" not in weather_result:
            print(weather_result)
            
            # Extract temperature from weather result
            temperature = extract_temperature(weather_result)
            
            if temperature is not None:
                break  # Exit loop if we have all required data
            else:
                print("I got the weather, but couldn't determine the temperature. Please try again.")
        else:
            print(weather_result)
            print("Please provide a valid city name.")
        
        # Reset for next iteration if failed
        city = None
        event_type = None
    
    # Get AI-powered outfit suggestions
    print("Generating outfit suggestions...")
    suggestions = get_suggestion(weather_result, event_type, temperature)
    
    print("\nOutfit Suggestions:")
    print(suggestions)

if __name__ == "__main__":
    main()