from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

weather_btn = KeyboardButton(text="Weather")
user_geo_btn = KeyboardButton(text="My current location", 
                              request_location=True)

start_markup = ReplyKeyboardMarkup(keyboard=[
    [weather_btn]
], resize_keyboard=True)
weather_markup = ReplyKeyboardMarkup(keyboard=[[user_geo_btn]],
                                     resize_keyboard=True)