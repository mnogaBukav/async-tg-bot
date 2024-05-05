from asyncio import run

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from handlers import common, weather, games
from utils.config import BOT_TOKEN


async def main() -> None:
    bot = Bot(token=BOT_TOKEN, 
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_routers(
        common.router, weather.router, games.router
    )
    try:
        await dp.start_polling(bot)
    finally:
        await common.http_session.close()


if __name__ == '__main__':
    run(main())
