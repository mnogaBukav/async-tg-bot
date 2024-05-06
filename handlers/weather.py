from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

from buttons.kb_common import menu_markup
from buttons.kb_weather import weather_btn, weather_markup
from modules.weather_client import WeatherClient
from states.current_weather import CurrentWeather
from utils.config import OPEN_WEATHER_API_URL

router = Router()


@router.message(StateFilter(None), F.text == weather_btn.text)
async def weather_command_handler(msg: Message, state: FSMContext) -> None:
    await msg.answer(
        "Send geolocation or send city name or send coordinates",
        reply_markup=weather_markup
    )
    await state.set_state(CurrentWeather.choosing_cur_geo_or_city_name)


@router.message(CurrentWeather.choosing_cur_geo_or_city_name)
async def handle_city(msg: Message, state: FSMContext, 
                      weather_client: WeatherClient) -> None:
    if not msg.location:
        if not msg.text:
            await msg.answer('Incorrect data entered.')
            return
        
        text_list = msg.text.split(',')
        size = len(text_list)
        if size == 1:
            location = {'q': text_list[0]}
        elif size == 2:
            location = {'lat': str(text_list[0]), 'lon': str(text_list[1])}
        else:
            await msg.answer('Incorrect data entered.')
            return

    else:
        location = {'lat': str(msg.location.latitude), 
                    'lon': str(msg.location.longitude)}
        
    await msg.answer(
        await weather_client.get_current(OPEN_WEATHER_API_URL, location),
        reply_markup=menu_markup
    )
    await state.clear()
