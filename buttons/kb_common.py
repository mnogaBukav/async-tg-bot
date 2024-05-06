from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

cancel_btn = KeyboardButton(text='Cancel')
weather_btn = KeyboardButton(text='Weather')
play_games_btn = KeyboardButton(text='Play game')

menu_markup = ReplyKeyboardMarkup(keyboard=[
    [weather_btn, play_games_btn],
], resize_keyboard=True)
