from aiogram import Router, html, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from buttons.kb_buttons import cancel_btn, start_markup, weather_btn, weather_markup, play_dice_btn, games_markup
from modules.requests.async_http_client import AsyncHTTPClient
from states.current_weather import CurrentWeather

http_client = AsyncHTTPClient()
router = Router()


@router.message(CommandStart())
async def command_start_handler(msg: Message) -> None:
    """This handler receives messages with `/start` command"""
    await msg.answer(f"Hello, {html.bold(msg.from_user.full_name)}!", 
                         reply_markup=start_markup)

@router.message(F.text == cancel_btn.text)
async def cancel_handler(msg: Message, state: FSMContext):
    await msg.answer("Menu:", reply_markup=start_markup)
    await state.clear()

@router.message(StateFilter(None), F.text == play_dice_btn.text)
async def play_dice_handler(msg: Message):
    await msg.answer("What game do you want to play?", reply_markup=games_markup)

@router.message(StateFilter(None), F.text == weather_btn.text)
async def weather_command_handler(msg: Message, state: FSMContext):
    """This handler receives messages with `/weather` command"""
    await msg.answer("Enter location or send your geolocation", reply_markup=weather_markup)
    await state.set_state(CurrentWeather.choosing_cur_geo_or_city_name)
