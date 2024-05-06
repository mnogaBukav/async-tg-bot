from aiogram import Router, html, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from buttons.kb_buttons import cancel_btn, start_markup

router = Router()

@router.message(CommandStart())
async def command_start_handler(msg: Message, state: FSMContext) -> None:
    """This handler receives messages with `/start` command"""
    await msg.answer(f"Hello, {html.bold(msg.from_user.full_name)}!", 
                         reply_markup=start_markup)
    await state.clear()

@router.message(F.text == cancel_btn.text)
async def cancel_handler(msg: Message, state: FSMContext) -> None:
    await msg.answer("Menu:", reply_markup=start_markup)
    await state.clear()
