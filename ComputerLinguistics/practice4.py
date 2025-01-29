import asyncio
import logging
import os
from urllib import request

from aiogram import Bot, Dispatcher, types
from aiogram.filters import StateFilter
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from bs4 import BeautifulSoup
from deeppavlov import configs, build_model
from dotenv import load_dotenv

from BotState import BotState

logging.basicConfig(level=logging.INFO)
load_dotenv()

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()
model = build_model('squad_ru_bert', install=True)
print("Model builded!")

@dp.message(Command('start'))
async def start_message(message: types.Message):
    await message.answer(f'/text - Загрузить текст\n')

@dp.message(Command('text'))
async def set_load_text_state(message: types.Message, state: FSMContext):
    await state.set_state(BotState.loading_text)
    await message.answer('Введите текст')

@dp.message(StateFilter(BotState.loading_text))
async def load_text(message: types.Message, state: FSMContext):
    await state.update_data(text=message.text)
    await state.set_state(BotState.text_is_ready)
    await message.answer('Текст загружен!')

@dp.message(StateFilter(BotState.text_is_ready))
async def test_function(message: types.Message, state: FSMContext):
    data = await state.get_data()
    text = data['text']
    question = message.text
    answer = model([text], [question])
    await message.answer(answer[0][0])


if __name__ == '__main__':
    asyncio.run(dp.start_polling(bot, skip_updates=True))