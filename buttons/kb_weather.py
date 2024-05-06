from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from .kb_common import cancel_btn

weather_btn = KeyboardButton(text='Weather')
user_geo_btn = KeyboardButton(
    text='My current location', request_location=True
)
weather_markup = ReplyKeyboardMarkup(keyboard=[
    [user_geo_btn, cancel_btn]
], resize_keyboard=True)
