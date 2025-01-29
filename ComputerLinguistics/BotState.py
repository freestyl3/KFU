from aiogram.fsm.state import StatesGroup, State

class BotState(StatesGroup):
    loading_text = State()
    text_is_ready = State()