from aiogram import Router, html, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from buttons.kb_buttons import start_markup, weather_btn, weather_markup
from modules.requests.async_http_client import AsyncHTTPClient
from states.current_weather import CurrentWeather

http_client = AsyncHTTPClient()
router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """This handler receives messages with `/start` command"""
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", 
                         reply_markup=start_markup)

@router.message(StateFilter(None), F.text == weather_btn.text)
async def weather_command_handler(message: Message, state: FSMContext):
    """This handler receives messages with `/weather` command"""
    await message.answer("Choose location:", reply_markup=weather_markup)
    await state.set_state(CurrentWeather.choosing_cur_geo_or_city_name)
