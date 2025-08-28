# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
from flask_cors import CORS
from src.services.weather_api import get_weather
from src.parsers.event_parser import parse_event
from src.services.outfit_suggestor import suggest_outfit  # handles LLM/fallback internally

app = Flask(__name__)
CORS(app)

@app.route("/api/chat", methods=["POST"])
def chat():
    try:
        user_input = request.json.get("message")
        if not user_input:
            return jsonify({"response": "No input provided"}), 400

        # Parse event from user input
        event_info = parse_event(user_input)
        print("Parsed event info:", event_info, type(event_info))

        # Support tuple or dict output
        if isinstance(event_info, dict):
            city = event_info.get("City")
            event_type = event_info.get("Event type")
        elif isinstance(event_info, tuple):
            if len(event_info) >= 2:
                city, event_type = event_info[:2]
            else:
                return jsonify({"response": "Failed to parse city and event type."}), 500
        else:
            return jsonify({"response": "Unexpected format from event parser."}), 500

        # Fetch weather data
        weather_data = get_weather(city)
        print("Weather data:", weather_data, type(weather_data))

        # Check if API returned an error
        if not isinstance(weather_data, dict) or "error" in weather_data:
            return jsonify({"response": weather_data.get("error", "Failed to fetch weather data.")})

        # Safely get weather info with defaults
        description = weather_data.get("description", "Unknown weather")
        temperature = weather_data.get("temperature", "N/A")
        full_string = weather_data.get("full_string", "Weather info unavailable")

        # Generate outfit suggestion
        suggestion = suggest_outfit(
            weather_condition=description,
            event_type=event_type,
            location=city,
            dates=None
        )

        response_text = f"{suggestion}\n\nWeather info: {full_string}"
        return jsonify({"response": response_text})

    except Exception as e:
        print("=== Error in /api/chat ===")
        print(e)
        return jsonify({"response": "Sorry, no suggestion was generated."}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
