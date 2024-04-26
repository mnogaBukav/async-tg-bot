from typing import Any, Dict
from datetime import datetime

from aiohttp import ClientSession, ClientResponseError


class WeatherAPI:
    @staticmethod
    async def get_weather(url: str, params: Dict[str, str]) -> str:
        async with ClientSession() as s:
            async with s.get(url, params=params) as r:
                try:
                    r.raise_for_status()
                except ClientResponseError:
                    return 'Error with receiving a weather forecast.'
                return __class__.__json_parse(await r.json())

    @staticmethod
    def __json_parse(json: Dict[str, Any]) -> str:
        sunrise = datetime.fromtimestamp(json['sys']['sunrise'])
        sunset = datetime.fromtimestamp(json['sys']['sunset'])
        return (f'Current time: {datetime.now().strftime('%y-%m-%d %H:%M')}\n'
                f'City: {json['name']}\n'
                f'Temp: {json['main']['temp']}°C\n'
                f'Feels like: {json['main']['feels_like']}°C\n'
                f'Weather: {json['weather'][0]['description']}\n'
                f'Clouds: {json['clouds']['all']}%\n'
                f'Wind: {json['wind']['speed']} m/s\n'
                f'Humidity: {json['main']['humidity']}%\n'
                f'Pressure: {json['main']['pressure']} mm Hg\n'
                f'Sunrise: {sunrise}\n'
                f'Sunset: {sunset}\n'
                f'Length of day: {sunset - sunrise}')
