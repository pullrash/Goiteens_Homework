import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from dotenv import load_dotenv
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher()

class Calculate(StatesGroup):
    num_1 = State()
    operation = State()
    num_2 = State()

keyboard_1 = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="1"), KeyboardButton(text="2"), KeyboardButton(text="3")],
    [KeyboardButton(text="4"), KeyboardButton(text="5"), KeyboardButton(text="6")],
    [KeyboardButton(text="7"), KeyboardButton(text="8"), KeyboardButton(text="9")],
    [KeyboardButton(text="0")]],
    resize_keyboard=True
)

keyboard_2 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="+"), KeyboardButton(text="-")],
        [KeyboardButton(text="*"), KeyboardButton(text="/")]
    ]
)


@dp.message(Command("calc"))
async def start_calc(message: types.Message, state: FSMContext):
    await state.set_state(Calculate.num_1)
    await message.answer("введіть перше число", reply_markup=keyboard_1)


@dp.message(Calculate.num_1)
async def first_num(message: types.Message, state: FSMContext):
    await state.update_data(num_1=message.text)
    await state.set_state(Calculate.operation)
    await message.answer("виберіть операцію", reply_markup=keyboard_2)


@dp.message(Calculate.operation)
async def op(message: types.Message, state: FSMContext):
    await state.update_data(operation=message.text)
    await state.set_state(Calculate.num_2)
    await message.answer("виберіть друге число", reply_markup=keyboard_1)


@dp.message(Calculate.num_2)
async def finish_calc(message: types.Message, state: FSMContext):
    await state.update_data(num_2=message.text)
    data = await state.get_data()
    
    result = eval(f"{data['num_1']}{data['operation']}{data['num_2']}")
    
    await message.answer(f"Результат: {result}", reply_markup=types.ReplyKeyboardRemove())
    await state.clear()

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())