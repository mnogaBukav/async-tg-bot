"""
Module for accessing environment variables and defining API URLs.

This module retrieves API keys and tokens from environment variables and
defines URLs for accessing external APIs.
"""

from os import getenv

# Retrieve API keys and tokens from environment variables
API_KEY: str = getenv('API_KEY')
BOT_TOKEN: str = getenv('BOT_TOKEN')

# Define URL for OpenWeatherMap API
OPEN_WEATHER_API_URL: str = f'https://api.openweathermap.org/data/2.5/weather'
