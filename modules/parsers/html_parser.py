from typing import Any, Dict


def json_parse(json: Dict[str, Any]) -> str:
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

