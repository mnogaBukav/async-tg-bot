from typing import Any, Dict
from aiohttp import ClientSession, ClientResponseError


class WeatherAPI:
    @staticmethod
    async def get_weather(url: str, params: Dict[str, str]) -> str:
        async with ClientSession() as s:
            async with s.get(url, params=params) as r:
                try:
                    print(r.status)
                    r.raise_for_status()
                except ClientResponseError:
                    return ''
                return __class__.__json_parse(await r.json())

    @staticmethod
    def __json_parse(json: Dict[str, Any]) -> str:
        return (f'city: {json['name']}\n'
                f'temp: {json['main']['temp']}\n'
                f'feels like: {json['main']['feels_like']}\n'
                f'weather: {json['weather'][0]['description']}\n'
                f'clouds: {json['clouds']['all']}%\n'
                f'wind: {json['wind']['speed']}\n'
                f'humidity: {json['main']['humidity']}\n'
                f'pressure: {json['main']['pressure']}\n'
                f'sunrise: {json['sys']['sunrise']}\n'
                f'sunset: {json['sys']['sunset']}\n')
