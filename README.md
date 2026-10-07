# Python Weather Assistant

A command-line weather assistant that fetches live weather data for any city and reads the report aloud using text-to-speech.

## Features
- Real-time temperature, condition, humidity, and rain chance via the WeatherAPI
- Voice output using offline text-to-speech
- Handles invalid city names, network errors, and unexpected API responses gracefully instead of crashing

## Tech used
Python 3, [`requests`](https://pypi.org/project/requests/) (API calls), [`pyttsx3`](https://pypi.org/project/pyttsx3/) (text-to-speech)

## Setup
1. Get a free API key from [weatherapi.com](https://www.weatherapi.com).
2. Set it as an environment variable (never hardcode it in the script):

   **Windows (PowerShell):**
   ```
   setx WEATHER_API_KEY "your_key_here"
   ```
   **Mac/Linux:**
   ```
   export WEATHER_API_KEY="your_key_here"
   ```
3. Install dependencies and run:
   ```bash
   pip install -r requirements.txt
   python weather_assistant.py
   ```

## Example
```
Enter the name of the city: Lahore
Weather Report for: Lahore
Temperature: 34 degree C
Condition: Sunny
Humidity: 40%
Rain Chance: 10%
(speaks the report aloud)
```

## Note on security
This project deliberately reads the API key from an environment variable instead of hardcoding it in the source file, so the key is never exposed if this repo is public.
