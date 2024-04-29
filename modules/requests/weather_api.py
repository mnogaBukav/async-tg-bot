from typing import Any, Dict
from datetime import datetime

from aiohttp import ClientSession, ClientResponseError
from requests.async_http_client import AsyncHTTPClient


class OpenWeatherClient:
    def __init__(self, client: AsyncHTTPClient) -> None:
        self.__client = client
    
    async def get_weather(url: str, params: Dict[str, str]) -> str:
        async with ClientSession() as s:
            async with s.get(url, params=params) as r:
                try:
                    r.raise_for_status()
                except ClientResponseError:
                    return 'Error with receiving a weather forecast.'
                return __class__.__json_parse(await r.json())

    def __json_parse(json: Dict[str, Any]) -> str:
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
