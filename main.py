from asyncio import run

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiohttp import ClientSession

from modules.weather_client import WeatherClient
from handlers import common, weather, games
from utils.config import BOT_TOKEN


async def main() -> None:
    bot = Bot(token=BOT_TOKEN, 
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))    
    
    client_session = ClientSession()
    dp = Dispatcher(
        client_session=client_session,
        weather_client=WeatherClient(client_session),
    )
    
    dp.include_routers(
        common.router, weather.router, games.router
    )
      
    try:
        await dp.start_polling(bot)
    finally:
        await client_session.close()


if __name__ == '__main__':
    run(main()) 
