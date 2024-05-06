from aiogram.fsm.state import State, StatesGroup


class GameState(StatesGroup):
    choosing_game: State = State()
    choosing_bet: State = State()
    roll_dices: State = State()

    
