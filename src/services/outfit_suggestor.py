# src/services/outfit_suggestor.py
import os
from dotenv import load_dotenv

load_dotenv()

def suggest_outfit(weather_condition, event_type=None, location=None, dates=None):
    """
    Enhanced outfit suggestion using LLM or fallback to basic logic
    Accepts: weather_condition, event_type, location, dates
    """
    # Fallback to simple logic if LLM not configured
    if not os.getenv("OPENAI_API_KEY"):
        return basic_outfit_suggestion(weather_condition, event_type)
    
    # Use LLM if available
    try:
        from src.services.llm_handler import outfit_llm
        return outfit_llm.generate_outfit_suggestion(
            weather_condition, 
            event_type, 
            location, 
            dates
        )
    except ImportError:
        return basic_outfit_suggestion(weather_condition, event_type)

def basic_outfit_suggestion(weather_condition, event_type):
    """Fallback basic suggestions when LLM is not available"""
    # Weather-based suggestions
    weather_keywords = {
        "rain": "Bring a waterproof jacket and boots. ",
        "snow": "Wear thermal layers and a heavy coat. ",
        "sun": "Wear light fabrics and sunscreen. ",
        "cloud": "Layers are recommended for changing conditions. ",
        "wind": "A windbreaker would be useful. ",
        "hot": "Light, breathable fabrics are essential. ",
        "cold": "Warm layers and a insulated jacket needed. ",
        "humid": "Moisture-wicking fabrics recommended. ",
        "storm": "Waterproof gear and sturdy shoes advised. "
    }
    
    # Event-based suggestions
    event_suggestions = {
        "wedding": "Formal attire with elegant layers",
        "business": "Business casual with a professional jacket",
        "vacation": "Comfortable casual wear with versatile pieces",
        "beach": "Light clothing, swimwear, and sun protection",
        "hiking": "Moisture-wicking fabrics and sturdy shoes",
        "skiing": "Thermal layers, waterproof pants, and goggles",
        "party": "Stylish evening wear with comfortable shoes",
        "dinner": "Smart casual attire for dining out",
        "sightseeing": "Comfortable walking shoes and daypack"
    }
    
    # Analyze weather for advice
    weather_advice = ""
    for keyword, advice in weather_keywords.items():
        if keyword in weather_condition.lower():
            weather_advice = advice
            break
    
    # Get event-specific advice
    event_advice = event_suggestions.get(event_type, "Casual comfortable clothing")
    
    # Construct final suggestion
    if event_type:
        return f"For your {event_type}: {event_advice}. {weather_advice}"
    else:
        return f"Travel recommendation: {event_advice}. {weather_advice}"

# Optional: Test function if run directly
if __name__ == "__main__":
    # Test the basic suggestion - REPLACE THE DEGREE SYMBOL!
    test_weather = "It's currently 30\u00B0C with sun in Jamaica"  # ← FIXED HERE
    test_event = "beach"
    print(basic_outfit_suggestion(test_weather, test_event))