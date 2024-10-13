import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import crud_functions as cf
cf.initiate_db()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    start = State()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()

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
        btn4 = KeyboardButton(text="Регистрация")

        self.keyboard.add(btn1)
        self.keyboard.add(btn2)
        self.keyboard.add(btn3)
        self.keyboard.add(btn4)
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
        await message.answer_photo(img, text)

    for i in cf.get_all_products():
        await send(i[4], f"Название: {i[1]} | Описание: {i[2]}  | Цена: {i[3]}")

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




@dp.message_handler(text='Регистрация')
async def sing_up(message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):

    if cf.is_included(message.text):
        await message.answer("Пользователь существует, введите другое имя")
        await RegistrationState.username.set()
        return
    await state.update_data(username=str(message.text))
    await message.answer("Введите свой email:")
    await RegistrationState.email.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=str(message.text))
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):

    try:
        await state.update_data(age=int(message.text))
    except:
        await message.answer("Нужно из цифр!")
        await RegistrationState.age.set()
        return

    data = await state.get_data()
    print(data["username"], data["email"], data["age"])
    try:
        cf.add_user(data["username"], data["email"], str(data["age"]))
    except Exception as E:
        await message.answer(f"Ошибка при обработке данных! {E}")
    await state.finish()
    await message.answer(f"Регистрация прошла успешно!")


@dp.message_handler()
async def any_msg(message):
    await message.answer("Введите команду /start, чтобы начать общение.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
 # username = State()
 #    email = State()
 #    age = State()
 #    balance = State()
