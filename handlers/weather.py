from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from buttons.kb_buttons import start_markup
from modules.weather_client import WeatherClient
from states.current_weather import CurrentWeather
from utils.config import API_KEY, OPEN_WEATHER_API_URL


router = Router()

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
