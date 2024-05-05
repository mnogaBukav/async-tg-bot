from aiogram.fsm.state import State, StatesGroup


class GameChoice(StatesGroup):
    
    choosing_game = State()
    roll_dices = State()

    dice_game = State()
    dart_game = State()
    basketball_game = State()
    football_game = State()
    bowling_game = State()
    slots_game = State()
