from aiogram.fsm.state import State, StatesGroup


class ImageGenerator(StatesGroup):
    waiting_for_prompt = State()