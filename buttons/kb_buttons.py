"""
Module defining custom reply keyboard markups for Telegram bot.

This module defines custom reply keyboard markups using aiogram's 
KeyboardButton and ReplyKeyboardMarkup.
"""
from aiogram.types import (
    KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, 
    ReplyKeyboardMarkup,
)

# Define KeyboardButtons
cancel_btn: KeyboardButton = KeyboardButton(text='Cancel')
weather_btn: KeyboardButton = KeyboardButton(text='Weather')
user_geo_btn: KeyboardButton = KeyboardButton(
    text='My current location', request_location=True
)
play_games_btn: KeyboardButton = KeyboardButton(text='Play game')
dice_btn: KeyboardButton = KeyboardButton(text='dice 🎲')
change_bet_btn: KeyboardButton = KeyboardButton(text='change bet')
dice_emoji: KeyboardButton = KeyboardButton(text='🎲')
dart_btn: KeyboardButton = KeyboardButton(text='🎯')
basketball_btn: KeyboardButton = KeyboardButton(text='🏀')
football_btn: KeyboardButton = KeyboardButton(text='⚽') 
bowling_btn: KeyboardButton = KeyboardButton(text='🎳')
slots_btn: KeyboardButton = KeyboardButton(text='🎰')


# Define InlineKeyboardButtons
higher_btn: InlineKeyboardButton = InlineKeyboardButton(
    text='higher', callback_data="bet_higher"
)
lower_btn: InlineKeyboardButton = InlineKeyboardButton(
    text='lower', callback_data="bet_lower"
)
equal_btn: InlineKeyboardButton = InlineKeyboardButton(
    text='equal', callback_data="bet_equal"
)


# Define ReplyKeyboardMarkups
dice_markup: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[
    [dice_emoji, change_bet_btn, cancel_btn]
], resize_keyboard=True)

games_markup: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[
    [dice_btn, dart_btn, basketball_btn],
    [football_btn, bowling_btn, slots_btn],
    [cancel_btn]
], resize_keyboard=True)

start_markup: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[
    [weather_btn, play_games_btn],
], resize_keyboard=True)

weather_markup: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[
    [user_geo_btn, cancel_btn]
], resize_keyboard=True)


# Define InlineKeyboardMarkups
dice_markup: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[
    [higher_btn, lower_btn, equal_btn]
])


game_kb: dict[str, InlineKeyboardMarkup] = {
    '🎲': dice_markup, 
    '🎯': dice_markup, 
    '🏀': dice_markup, 
    '⚽': dice_markup, 
    '🎳': dice_markup, 
    '🎰': dice_markup,
}
