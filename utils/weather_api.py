import requests
import os
from dotenv import load_dotenv

load_dotenv()  # loads .env file

def get_weather(city="Tirur"):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return "No API key found. Please set OPENWEATHER_API_KEY."

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            return f"Weather in {city}: {temp}°C, {desc}"
        else:
            return f"Error fetching weather: {data.get('message', 'Unknown error')}"
    except Exception as e:
        return f"Weather API failed: {e}"
