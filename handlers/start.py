from aiogram import Router, F, types
from aiogram.filters import Command


start_router = Router()

@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    msg = f"Здравствуйте, {name}"
    await message.answer(msg)



















# from aiogram import Router
# from aiogram.types import Message 
# from aiogram.filters import Command
# from aiogram.fsm.context import FSMContext 
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# from aiogram.fsm.state import State, StatesGroup

# def group_keyboard():
#     keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.add('group 47-1', 'group 47-2', 'group 48-1', 'group 48-2')
#     return keyboard

# class homework(StatesGroup):
#     name = State()
#     group = State()
#     homework_num = State()
#     git_link = State()


# async def cmd_start(self,message: Message ):
#     await message.answer('привет.я бот для отправки дз . введи команду /send_homework')

# async def start_homework (self,message: Message, state: FSMContext):
#     await state.update_data(name=message.text)
#     await state.set_state(homework.name)
#     await message.answer('введите имя :')


# async def process_name(self,message: Message, state: FSMContext):
#     await state.update_data(name=message.text)
#     await state.set_state(homework.group)
#     await message.answer ('выберите вашу группу :', reply_markup=group_keyboard())


# async def process_homework_number(self,message: Message,state: FSMContext):
#     homework_number = int(message.text)
#     if homework_number < 1 or homework_number >8 :
#         await message.answer('номер дз должен быть от 1 до 8')
#         return 
#     await state.update_data(homework_number=homework_number)
#     await state.set_state(homework.git_link)
#     await message.answer('введите ссылку на репозиторий')


