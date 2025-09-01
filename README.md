# Closetaire

Closetaire is an outfit recommendation program built with React Native and Flask that helps users to decide what to wear based on the location and type of event inputted.  

## Features developed
-  Real-time weather integration (temperature, humidity, wind, etc.)
-  AI/LLM-based outfit suggestions 
-  Event & location parsing from natural language input
-  Frontend powered by React Native
-  Backend built with Flask API

## Tech Stack
- **Frontend:** React Native / Expo  
- **Backend:** Python, Flask, REST API  
- **AI:** OpenAI API integration (optional, fallback included)  
- **Weather Data:** OpenWeather API  

### Backend (Flask) Terminal Commands
cd Closetaire
python -m venv venv
venv\Scripts\activate  
pip install -r requirements.txt
python app.py

### Frontend (React-native) Terminal Commands
cd frontend
npm install
npm start

### Environment Variables
OPENAI_API_KEY=your_openai_key
OPENWEATHER_API_KEY=your_weather_key


