from aiogram.enums import DiceEmoji
from aiogram.types import (
    KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup,
)

from .kb_common import cancel_btn

change_bet_btn = KeyboardButton(text='change bet')
dice_btn = KeyboardButton(
    text='Dice ' + DiceEmoji.DICE.value
)
dart_btn = KeyboardButton(
    text='Dart ' + DiceEmoji.DART.value
)
basketball_btn = KeyboardButton(
    text='Basketball ' + DiceEmoji.BASKETBALL.value
)
football_btn = KeyboardButton(
    text='Football' + DiceEmoji.FOOTBALL.value
) 
bowling_btn = KeyboardButton(
    text='Bowling ' + DiceEmoji.BOWLING.value
)
slots_btn = KeyboardButton(
    text='Slots ' + DiceEmoji.SLOT_MACHINE.value
)

higher_btn = InlineKeyboardButton(
    text='higher', callback_data="bet_higher"
)
lower_btn= InlineKeyboardButton(
    text='lower', callback_data="bet_lower"
)
equal_btn = InlineKeyboardButton(
    text='equal', callback_data="bet_equal"
)

games_markup = ReplyKeyboardMarkup(keyboard=[
    [dice_btn, dart_btn, basketball_btn],
    [football_btn, bowling_btn, slots_btn],
    [cancel_btn]
], resize_keyboard=True)

dice_markup = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=DiceEmoji.DICE.value), change_bet_btn, cancel_btn]
], resize_keyboard=True)

game_kb = {
    dice_btn.text: dice_markup, 
    dart_btn.text: dice_markup, 
    basketball_btn.text: dice_markup, 
    football_btn.text: dice_markup, 
    bowling_btn.text: dice_markup, 
    slots_btn.text: dice_markup,
}
