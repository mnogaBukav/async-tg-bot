from aiogram.fsm.state import State, StatesGroup


class GameState(StatesGroup):
    choosing_game = State()
    choosing_bet = State()
    roll_dices = State()

    
