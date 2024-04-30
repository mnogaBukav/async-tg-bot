from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

cancel_btn = KeyboardButton(text='Cancel')
weather_btn = KeyboardButton(text='Weather')
user_geo_btn = KeyboardButton(
    text='My current location', request_location=True
)

play_dice_btn = KeyboardButton(text='Play game')
dice_btn = KeyboardButton(text='🎲')
dart_btn = KeyboardButton(text='🎯')
basketball_btn = KeyboardButton(text='🏀')
football_btn = KeyboardButton(text='⚽') 
bowling_btn = KeyboardButton(text='🎳')
slots_btn = KeyboardButton(text='🎰')

games_markup = ReplyKeyboardMarkup(keyboard=[
    [dice_btn, dart_btn, basketball_btn],
    [football_btn, bowling_btn, slots_btn],
    [cancel_btn]
], resize_keyboard=True)

start_markup = ReplyKeyboardMarkup(keyboard=[
    [weather_btn, play_dice_btn],
], resize_keyboard=True)

weather_markup = ReplyKeyboardMarkup(
    keyboard=[[user_geo_btn, cancel_btn]], 
    resize_keyboard=True
)
