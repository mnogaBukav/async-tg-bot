"""
Module defining custom reply keyboard markups for Telegram bot.

This module defines custom reply keyboard markups using aiogram's 
KeyboardButton and ReplyKeyboardMarkup.
"""

from aiogram.types import KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup

# Define KeyboardButtons
cancel_btn = KeyboardButton(text='Cancel')
weather_btn = KeyboardButton(text='Weather')
user_geo_btn = KeyboardButton(text='My current location', request_location=True)
play_dice_btn = KeyboardButton(text='Play game')
dice_btn = KeyboardButton(text='🎲')
dart_btn = KeyboardButton(text='🎯')
basketball_btn = KeyboardButton(text='🏀')
football_btn = KeyboardButton(text='⚽') 
bowling_btn = KeyboardButton(text='🎳')
slots_btn = KeyboardButton(text='🎰')

# Define ReplyKeyboardMarkups
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