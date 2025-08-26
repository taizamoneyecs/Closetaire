import re
from dateutil import parser

def parse_event(user_input):
    """
    Parse user input to extract city, dates, and event type.
    Returns: city, start_date, end_date, event_type
    """
    # Initialize with default values
    city = None
    start_date = None
    end_date = None
    event_type = None

    # Extract city (title case words that might be locations)
    city_match = re.search(r'\b[A-Z][a-z]+\b', user_input)
    if city_match:
        city = city_match.group(0)

    # Extract dates (simple pattern for now)
    date_pattern = r'(\d{1,2}(?:st|nd|rd|th)?\s+\w+\s*-\s*\d{1,2}(?:st|nd|rd|th)?\s+\w+)'
    date_match = re.search(date_pattern, user_input)
    
    if date_match:
        try:
            date_range = date_match.group(1)
            dates = date_range.split('-')
            start_date = parser.parse(dates[0].strip())
            end_date = parser.parse(dates[1].strip())
        except:
            # If parsing fails, keep dates as None
            pass

    # Extract event type
    event_types = ["wedding", "business", "vacation", "skiing", "beach", "hiking", "party"]
    words = user_input.lower().split()
    for word in words:
        if word in event_types:
            event_type = word
            break

    return city, start_date, end_date, event_type