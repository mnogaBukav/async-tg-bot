"""
Module defining custom reply keyboard markups for Telegram bot.

This module defines custom reply keyboard markups using aiogram's 
KeyboardButton and ReplyKeyboardMarkup.
"""
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import (
    KeyboardButton, 
    InlineKeyboardButton, 
    ReplyKeyboardMarkup,
)

# Define KeyboardButtons
cancel_btn = KeyboardButton(text='Cancel')
weather_btn = KeyboardButton(text='Weather')
user_geo_btn = KeyboardButton(text='My current location', request_location=True)
play_games_btn = KeyboardButton(text='Play game')
dice_btn = KeyboardButton(text='dice 🎲')
change_bet_btn = KeyboardButton(text='change bet')
dice_emoji = KeyboardButton(text='🎲')
dart_btn = KeyboardButton(text='🎯')
basketball_btn = KeyboardButton(text='🏀')
football_btn = KeyboardButton(text='⚽') 
bowling_btn = KeyboardButton(text='🎳')
slots_btn = KeyboardButton(text='🎰')

higher_btn = InlineKeyboardButton(text='higher', callback_data="bet_higher")
lower_btn = InlineKeyboardButton(text='lower', callback_data="bet_lower")
equal_btn = InlineKeyboardButton(text='equal', callback_data="bet_equal")

# Define ReplyKeyboardMarkups
dice_markup = ReplyKeyboardMarkup(keyboard=[
    [dice_emoji, change_bet_btn,
    cancel_btn]
], resize_keyboard=True)

games_markup = ReplyKeyboardMarkup(keyboard=[
    [dice_btn, dart_btn, basketball_btn],
    [football_btn, bowling_btn, slots_btn],
    [cancel_btn]
], resize_keyboard=True)


start_markup = ReplyKeyboardMarkup(keyboard=[
    [weather_btn, play_games_btn],
], resize_keyboard=True)

weather_markup = ReplyKeyboardMarkup(
    keyboard=[[user_geo_btn, cancel_btn]], 
    resize_keyboard=True
)

def bet_markup():
    builder = InlineKeyboardBuilder()
    builder.add(higher_btn, lower_btn, equal_btn)
    return builder.as_markup()
