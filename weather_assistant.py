"""
Python Weather Assistant
Fetches the current weather and rain chance for a city using WeatherAPI,
prints a report, and reads it aloud using text-to-speech.

Requires a free API key from https://www.weatherapi.com, set as an
environment variable named WEATHER_API_KEY (see README for setup).
"""

import os
import json
import requests
import pyttsx3


def speak(engine, text):
    engine.setProperty('rate', 160)
    engine.say(text)
    engine.runAndWait()


def get_weather(city, api_key):
    url = f"https://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=1"
    return requests.get(url, timeout=10)


def main():
    engine = pyttsx3.init()

    api_key = os.getenv("WEATHER_API_KEY")
    if not api_key:
        print("Error: WEATHER_API_KEY environment variable is not set.")
        print("Get a free key from https://www.weatherapi.com and set it before running.")
        return

    city = input("Enter the name of the city: ")

    try:
        response = get_weather(city, api_key)
        wdic = response.json()
    except requests.exceptions.RequestException:
        print("Could not connect to the weather service. Check your internet connection.")
        return
    except json.JSONDecodeError:
        print("Unexpected response from the weather service.")
        return

    if "error" in wdic:
        print("Error:", wdic["error"]["message"])
        speak(engine, "City not found. Please try again.")
        return

    try:
        temp = wdic["current"]["temp_c"]
        condition = wdic["current"]["condition"]["text"]
        humidity = wdic["current"]["humidity"]
        rain_chance = wdic["forecast"]["forecastday"][0]["day"]["daily_chance_of_rain"]
    except KeyError:
        print("Unexpected data format from the weather service.")
        return

    print("----------------------------------------")
    print(f"Weather Report for: {city}")
    print("----------------------------------------")
    print(f"Temperature: {temp} degree C")
    print(f"Condition: {condition}")
    print(f"Humidity: {humidity}%")
    print(f"Rain Chance: {rain_chance}%")
    print("----------------------------------------")

    speech_text = (
        f"The weather in {city} is {condition}. "
        f"The temperature is {temp} degrees Celsius, "
        f"with a {rain_chance} percent chance of rain."
    )
    speak(engine, speech_text)


if __name__ == "__main__":
    main()
