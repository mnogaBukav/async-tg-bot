from aiogram import Router, html
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


common_router = Router()

@common_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """This handler receives messages with `/start` command"""
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!\n"
                         f"I'm here to help you find out the weather in any city.")

@common_router.message(Command('weather'))
async def weather_command_handler(message: Message):
    """This handler receives messages with `/weather` command"""
    city = 'Minsk'
    weather_service = WeatherService()
    try:
        weather_info = await weather_service.get_weather(city)
        await message.answer(weather_info)
    except Exception as e:
        print(e)
        await message.answer("Произошла ошибка при получении информации о погоде.")
