from aiogram import Router, html
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from modules.requests.weather_api import WeatherAPI


common_router = Router()

@common_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """This handler receives messages with `/start` command"""
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")

@common_router.message(Command('weather'))
async def weather_command_handler(message: Message):
    """This handler receives messages with `/weather` command"""
    try:
        await message.answer(
            await WeatherAPI.get_weather(message.text.split()[1])
        )
    except Exception:
        await message.answer("Error with receiving weather forecast")
