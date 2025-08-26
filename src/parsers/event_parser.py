from dateutil import parser
import re

def parse_event(user_input):
    words = user_input.split()
    
    city = None
    start_date = None
    end_date = None
    event_type = None

    # Find location prepositions first
    location_words = ['in', 'at', 'to', 'for', 'near', 'around']
    preposition_positions = []
    
    for i, word in enumerate(words):
        if word.lower() in location_words:
            preposition_positions.append(i)

    # Try to find city starting from each preposition
    for pos in preposition_positions:
        if pos + 1 >= len(words):
            continue
            
        # Build potential city name from words after preposition
        potential_city_parts = []
        current_pos = pos + 1
        
        # Collect words until we hit a non-city-looking word
        while current_pos < len(words):
            current_word = words[current_pos]
            
            # Stop at common non-city words
            stop_words = ['next', 'this', 'for', 'a', 'the', 'week', 'weekend', 'month', 'tomorrow', 'today']
            if current_word.lower() in stop_words:
                break
                
            # Stop at dates or other indicators
            if '-' in current_word or current_word.isdigit():
                break
                
            potential_city_parts.append(current_word)
            current_pos += 1
            
            # Limit to 3 words for city names (e.g., "rio de janeiro")
            if len(potential_city_parts) >= 3:
                break
        
        if potential_city_parts:
            potential_city = ' '.join(potential_city_parts)
            # Basic validation: city should have at least one word with >2 chars
            if any(len(part) > 2 for part in potential_city_parts):
                city = potential_city
                break

    # Event type detection
    event_types = ["wedding", "business", "casual", "skiing", "beach", "party", "conference", "dinner"]
    lower_input = user_input.lower()
    for event in event_types:
        if event in lower_input:
            event_type = event
            break

    # Date detection
    for i, word in enumerate(words):
        if "-" in word:
            try:
                dates = word.split("-")
                start_date = parser.parse(dates[0])
                end_date = parser.parse(dates[1])
            except:
                pass

    return city, start_date, end_date, event_type