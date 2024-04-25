from aiohttp import ClientSession

from utils.config import API_KEY


class WeatherRequester:
    def __init__(self) -> None:
        pass
    
    def get_api_url(self, city: str, api_key: str) -> str:
        return (f'https://api.openweathermap.org/data/'
                f'2.5/weather?q={city}&appid={api_key}&units=metric')
    
    async def get_weather(self, city: str, api_key: str = API_KEY):
        async with ClientSession() as session:
            async with session.get(self.get_api_url(city, api_key)) as response:
                response.raise_for_status()
                print(self.json_parse(await response.json()))