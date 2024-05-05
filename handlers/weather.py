from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

from modules.weather_client import WeatherClient
from buttons.kb_buttons import start_markup, weather_btn, weather_markup
from handlers.common import http_session
from states.current_weather import CurrentWeather
from utils.config import API_KEY, OPEN_WEATHER_API_URL


router = Router()

@router.message(StateFilter(None), F.text == weather_btn.text)
async def weather_command_handler(msg: Message, state: FSMContext):
    """This handler receives messages with `/weather` comman   d"""
    await msg.answer("Enter location or send your geolocation", reply_markup=weather_markup)
    await state.set_state(CurrentWeather.choosing_cur_geo_or_city_name)

@router.message(CurrentWeather.choosing_cur_geo_or_city_name)
async def handle_city(msg: Message, 
                      state: FSMContext, 
                      weather_client: WeatherClient):
    if msg.location:
        location = {'lat': str(msg.location.latitude),
                    'lon': str(msg.location.longitude)}
    else:
        text_list = msg.text.split(',')
        if len(text_list) == 2:
            location = {'lat': str(text_list[0]),   
                        'lon': str(text_list[1])}
        else:
            location = {'q': text_list[0]}
    
    data = {'appid': API_KEY, 'units': 'metric'}
    data.update(location)
    await msg.answer(
        await weather_client.get_current(OPEN_WEATHER_API_URL, data),
        reply_markup=start_markup
    )
    await state.clear()
