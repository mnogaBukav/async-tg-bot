from asyncio import run

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from handlers.common import common_router
from utils.config import BOT_TOKEN


async def main() -> None:
    bot = Bot(token=BOT_TOKEN, 
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    
    dp = Dispatcher()
    dp.include_routers(
        common_router,
    )

    await dp.start_polling(bot)


if __name__ == '__main__':
    run(main())
