from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from buttons.kb_common import cancel_btn, menu_markup

router = Router()

@router.message(CommandStart())
async def command_start_handler(msg: Message, state: FSMContext) -> None:
    """This handler receives messages with `/start` command"""
    await msg.answer(f"Hello!", 
                     reply_markup=menu_markup)
    await state.clear()

@router.message(F.text == cancel_btn.text)
async def cancel_handler(msg: Message, state: FSMContext) -> None:
    await msg.answer("Menu:", reply_markup=menu_markup)
    await state.clear()
