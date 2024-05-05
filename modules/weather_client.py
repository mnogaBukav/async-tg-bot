from typing import Dict
from datetime import datetime as dt

from aiohttp import ClientSession


class WeatherClient:
    """
    Class for fetching weather data.
    """
    def __init__(self, client_session: ClientSession) -> None:
        """
        Initialize the weather client.
        """
        self.__session = client_session

    async def get_current(
        self, 
        url: str, 
        params: Dict[str, str]
    ) -> str:
        """
        Fetch current weather data from the provided URL.
        """
        async with self.__session.get(url, params=params) as response:
            if response.status == 200:
                json = await response.json()
                format = '%d-%m-%y, %H:%M'
                sr = dt.fromtimestamp(json['sys']['sunrise'])
                ss = dt.fromtimestamp(json['sys']['sunset'])
                return (
                    f'Current time: {dt.now().strftime(format)}\n'
                    f'City: {json['name']}\n'
                    f'Temp: {json['main']['temp']}°C\n'
                    f'Feels like: {json['main']['feels_like']}°C\n'
                    f'Weather: {json['weather'][0]['description']}\n'
                    f'Clouds: {json['clouds']['all']}%\n'
                    f'Wind: {json['wind']['speed']} m/s\n'
                    f'Humidity: {json['main']['humidity']}%\n'
                    f'Pressure: {json['main']['pressure']} mm Hg\n'
                    f'Sunrise: {sr.strftime(format)}\n'
                    f'Sunset: {ss.strftime(format)}\n'
                    f'Length of day: {ss - sr}'
                )

            return 'Error with receiving a weather forecast.'
