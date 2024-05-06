from asyncio import run

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiohttp import ClientSession

from modules.weather_client import WeatherClient
from handlers import routers
from utils.config import BOT_TOKEN


async def main() -> None:
    bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)
    
    client_session = ClientSession()
    dp = Dispatcher(
        client_session=client_session,
        weather_client=WeatherClient(client_session),
    )
    
    dp.include_routers(routers)

    await bot.delete_webhook(drop_pending_updates=True)

    try:
        await dp.start_polling(bot)
    finally:
        await client_session.close()


if __name__ == '__main__':
    run(main()) 
