import asyncio
from aiogram import Router, html, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram.types import Message, CallbackQuery

from states.games_states import GameChoice
from buttons.kb_buttons import (
    games_markup, start_markup, bet_markup, dice_markup, 
    play_games_btn, cancel_btn, change_bet_btn,
    dice_btn, dart_btn, basketball_btn, 
    football_btn, bowling_btn, slots_btn
)

router = Router()

@router.message(StateFilter(None), F.text == play_games_btn.text)
async def play_games_handler(msg: Message, state: FSMContext):
    await msg.answer(
        "What game do you want to play?", 
        reply_markup=games_markup
    )

@router.message(StateFilter(None), F.text == dice_btn.text)
async def play_dice_handler(msg: Message, state: FSMContext):
    await msg.answer(
        "bet: ur value will be", 
        reply_markup=bet_markup()
    )

@router.callback_query(F.data.startswith("bet_"))
async def callbacks_bet(callback: CallbackQuery, state: FSMContext):
    action = callback.data.split("_")[1]
    await callback.answer()
    await state.set_state(GameChoice.roll_dices)
    await state.set_data({'action': action})
    await callback.message.answer(
        f'your bet is: {action}\nRoll the dice!', 
        reply_markup=dice_markup
    )

@router.message(GameChoice.roll_dices)
async def roll_dices(msg: Message, state: FSMContext):
    if msg.dice is None or msg.dice.emoji != '🎲':
        await msg.answer("This is not a dice, send message again!")
        return
    
    bot_result = await msg.answer_dice()
    action = (await state.get_data())['action']
    if (
        (msg.dice.value > bot_result.dice.value and action == "higher") or
        (msg.dice.value < bot_result.dice.value and action == "lower") or
        (msg.dice.value == bot_result.dice.value and action == "equal")
    ):
        game_result = "user won"
    else:
        game_result = "bot won"

    await asyncio.sleep(4)
    await msg.answer(game_result)

# TODO
@router.message(GameChoice.roll_dices, F.text == change_bet_btn.text)
async def change_bet(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer(
        f'your bet is: none\nRoll the dice!', 
        reply_markup=dice_markup
    )
    await state.set_state(GameChoice.roll_dices)