import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    start = State()


class Keyboards():

    def __init__(self):
        pass

    def add_inl_button(self, kb, text, cb):
        button = InlineKeyboardButton(text=text, callback_data=cb)
        kb.add(button)

    def normal(self):
        self.keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

        btn1 = KeyboardButton(text="Рассчитать")
        btn2 = KeyboardButton(text="Информация")
        btn3 = KeyboardButton(text="Купить")

        self.keyboard.add(btn1)
        self.keyboard.add(btn2)
        self.keyboard.add(btn3)
        return self.keyboard

    def inline(self):
        self.in_kb = InlineKeyboardMarkup()

        button2 = InlineKeyboardButton(text = 'Формулы расчёта', callback_data='formulas')
        button = InlineKeyboardButton(text = 'Рассчитать норму калорий', callback_data='calories')

        self.in_kb.add(button)
        self.in_kb.add(button2)
        return self.in_kb

    def buy(self):
        self.buy_ = InlineKeyboardMarkup()

        for i in range(1,5):
            self.add_inl_button(kb=self.buy_, text=f"Product{i}", cb="product_buying")

        return self.buy_


kb = Keyboards()


with open(".api", "r") as key: api = key.read()

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb.normal())


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer("Рады вас видеть!", reply_markup = kb.inline())

@dp.message_handler(text='Купить')
async def get_buying_list(message):


    async def send(img, text):
        with open(img, "rb") as file:
            await message.answer_photo(file, text)

    for i in range(1,5):
        await send(os.path.join("images", f"img_{i}.png"), f"Название: Product{1} | Описание: описание {1} | Цена: {i*100}")

    await message.answer("Выберите товар:", reply_markup=kb.buy())


@dp.callback_query_handler(text = 'formulas')
async def get_formulas(call):
    await call.message.answer("для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5")

@dp.callback_query_handler(text = 'product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")


@dp.callback_query_handler(text = 'calories')
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
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
