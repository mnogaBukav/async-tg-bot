from typing import Any, Dict
from datetime import datetime

from aiohttp import ClientResponseError
from requests.async_http_client import AsyncHTTPClient


class OpenWeatherClient:
    def __init__(self, client: AsyncHTTPClient) -> None:
        self.__client = client
    
    async def get_current_weather(
        self, url: str, params: Dict[str, str]
    ) -> str:
        text = ''
        async with self.__client.get(url, params=params) as r:
            try:
                r.raise_for_status()
            except ClientResponseError:
                text = 'Error with receiving a weather forecast.'
            text = self.__json_parse(await r.json())
        return text
    
    @staticmethod
    def __json_parse(json: Dict[str, str]) -> str:
        format = '%d-%m-%y, %H:%M'
        sr = datetime.fromtimestamp(json['sys']['sunrise']).strftime(format)
        ss = datetime.fromtimestamp(json['sys']['sunset']).strftime(format)
        return (f'Current time: {datetime.now().strftime(format)}\n'
                f'City: {json['name']}\n'
                f'Temp: {json['main']['temp']}°C\n'
                f'Feels like: {json['main']['feels_like']}°C\n'
                f'Weather: {json['weather'][0]['description']}\n'
                f'Clouds: {json['clouds']['all']}%\n'
                f'Wind: {json['wind']['speed']} m/s\n'
                f'Humidity: {json['main']['humidity']}%\n'
                f'Pressure: {json['main']['pressure']} mm Hg\n'
                f'Sunrise: {sr}\n'
                f'Sunset: {ss}\n'
                f'Length of day: {ss - sr}')
