from aiogram.fsm.state import State, StatesGroup


class CurrentWeather(StatesGroup):
    choosing_cur_geo_or_city_name = State()
