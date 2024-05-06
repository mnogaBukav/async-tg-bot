import asyncio

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram.types import Message, CallbackQuery

from buttons.kb_common import play_games_btn
from buttons.kb_games import games_markup, dice_markup, change_bet_btn, game_kb
from states.games_states import GameState

router = Router()


@router.message(StateFilter(None), F.text == play_games_btn.text)
async def play_games_handler(msg: Message, state: FSMContext) -> None:
    await msg.answer(
        "What game do you want to play?", 
        reply_markup=games_markup
    )
    await state.set_state(GameState.choosing_game)


@router.message(GameState.choosing_game)
async def play_dice_handler(msg: Message, state: FSMContext) -> None:    
    try:
        kb = game_kb[msg.text]
    except KeyError:
        await msg.answer('Game not found!')
        return
    await msg.answer(
        "bet: ur value will be",
        reply_markup=kb
    )
    await state.set_state(GameState.choosing_bet)
    await state.set_data({'game': msg.text})


@router.callback_query(GameState.choosing_bet, F.data.startswith("bet_"))
async def callbacks_bet(callback: CallbackQuery, state: FSMContext) -> None:
    action = callback.data.split("_")[1]
    await callback.answer()
    await state.set_state(GameState.roll_dices)
    await state.set_data({'action': action})
    await callback.message.answer(
        f'your bet is: {action}\nRoll the dice!', 
        reply_markup=dice_markup
    )


@router.message(GameState.roll_dices)
async def roll_dices(msg: Message, state: FSMContext) -> None:
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


@router.message(GameState.roll_dices, F.text == change_bet_btn.text)
async def change_bet(msg: Message, state: FSMContext) -> None:
    await msg.answer(
        f'Your bet is: none\nRoll the dice!', 
        reply_markup=dice_markup
    )
    await state.set_state(GameState.roll_dices)