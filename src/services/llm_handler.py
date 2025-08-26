import os
import requests
from dotenv import load_dotenv

load_dotenv()

class GroqAPI:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")  # Changed to Groq
        self.base_url = "https://api.groq.com/openai/v1/chat/completions"  # Groq endpoint
    
    def get_outfit_suggestion(self, weather_condition, event_type, temperature):
       
        
        prompt = f"""
            As a personal fashion assistant, suggest 3 appropriate outfits for:
            - Event: {event_type}
            - Weather: {weather_condition}
            - Temperature: {temperature}°C

            Provide practical, weather-appropriate suggestions. Consider:
            - Layering for temperature changes
            - Fabric choices for comfort
            - Footwear suitability for conditions

            Format clearly with numbered suggestions and brief explanations.
            """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "llama-3.1-8b-instant",  # Groq's free model
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 500
        }
        
        try:
            response = requests.post(self.base_url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        except Exception as e:
            return f"Sorry, I couldn't generate suggestions. Error: {str(e)}"

# Mock version for testing (unchanged)
def mock_outfit_suggestion(weather_condition, event_type, temperature):
    """Free mock responses for development"""
    suggestions = {
        "wedding": [
            "Formal suit with light layers",
            "Elegant dress with matching jacket",
            "Classic outfit with weather-appropriate accessories"
        ],
        "business": [
            "Professional suit with comfortable shoes",
            "Blouse with tailored pants and blazer", 
            "Business dress with layered options"
        ],
        "casual": [
            "Casual jeans with comfortable top",
            "Shorts and t-shirt for warm weather",
            "Light jacket with casual pants"
        ]
    }
    
    event_suggestions = suggestions.get(event_type, suggestions["casual"])
    
    base = f"Based on {weather_condition} at {temperature}°C for {event_type}:\n\n"
    return base + "\n".join([f"{i+1}. {suggestion}" for i, suggestion in enumerate(event_suggestions)])

# Main function to get suggestions (now uses Groq)
def get_suggestion(weather_condition, event_type, temperature):
    if os.getenv("GROQ_API_KEY"):  # Changed to Groq
        return GroqAPI().get_outfit_suggestion(weather_condition, event_type, temperature)
    else:
        return mock_outfit_suggestion(weather_condition, event_type, temperature)