from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    start = State()

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = KeyboardButton(text="Рассчитать")
btn2 = KeyboardButton(text="Информация")
keyboard.add(btn1)
keyboard.add(btn2)

with open(".api", "r") as key: api = key.read()

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=keyboard)


@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    await message.answer("Введите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=int(message.text))
    await message.answer("Введите свой вес:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    try:
        male_bmr = 10 * data["weight"] + 6.25 * data["growth"] - 5 * data["age"] + 5
        await message.answer(f"Подсчет калорий: {male_bmr}")
    except:
        await message.answer(f"Были введены неверные данные!")
    await state.finish()


@dp.message_handler()
async def any_msg(message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
