# import asyncio
# from aiogram import Bot, Dispatcher, types, F
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
# from dotenv import load_dotenv
# import os

# load_dotenv()

# TOKEN = os.getenv("TOKEN")

# bot = Bot(TOKEN)
# dp = Dispatcher()

# keyboard = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="btn 1"), KeyboardButton(text="btn 2")],
#         [KeyboardButton(text="btn 3"), KeyboardButton(text="btn 4")]
#     ],
#     resize_keyboard=True
# )

# inline_keyboard = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text="btn 1", callback_data="btn1"),
#             InlineKeyboardButton(text="btn 2", callback_data="btn2")
#         ],
#         [
#             InlineKeyboardButton(text="btn 3", callback_data="btn3"),
#             InlineKeyboardButton(text="btn 4", callback_data="btn4")
#         ]
#     ]
# )

# @dp.message(F.text == '/start')
# async def start_bot(message: types.Message):
#     await message.answer("Choice: ", reply_markup=inline_keyboard)

# @dp.message(F.text == "btn 1")
# async def handle_btn_1(message: types.Message):
#     await message.answer('Pressed btn 1')

# @dp.callback_query(F.data == "btn1")
# async def handle_inline_btn_1(callback: types.CallbackQuery):
#     await callback.answer()
#     await callback.message.answer('Pressed inline btn 1')

# async def main():
#     await dp.start_polling(bot)

# if __name__ == '__main__':
#     asyncio.run(main())



import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from dotenv import load_dotenv
import os

class Form(StatesGroup):
    name = State()
    age = State()

load_dotenv()

TOKEN = os.getenv("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(F.text == '/start')
async def start(message: types.Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer("What is your name?")

@dp.message(Form.name)
async def get_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Form.age)
    await message.answer("How old are you?")

@dp.message(Form.age)
async def get_age(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(f'Your name is: {data['name']}, your age is: {message.text}')
    await state.clear()

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())