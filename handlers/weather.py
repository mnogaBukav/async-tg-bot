from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from buttons.kb_buttons import start_markup
from handlers.common import http_client
from modules.weather.open_weather_client import OpenWeatherClient
from states.current_weather import CurrentWeather
from utils.config import API_KEY, OPEN_WEATHER_API_URL

router = Router()
weather_client = OpenWeatherClient(http_client)

@router.message(CurrentWeather.choosing_cur_geo_or_city_name)
async def handle_city(msg: Message, state: FSMContext):
    data = {'appid': API_KEY, 'units': 'metric'}
    if msg.location:
        location = {'lat': str(msg.location.latitude),
                    'lon': str(msg.location.longitude)}
    else:
        location = {'q': msg.text or ''}
    data.update(location)

    await msg.answer(
        await weather_client.get_current_weather(OPEN_WEATHER_API_URL, data),
        reply_markup=start_markup
    )
    await state.clear()