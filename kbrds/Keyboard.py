from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

KeyboardHelp = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Главное меню'), KeyboardButton(text='Информация')],
    [KeyboardButton(text='Задать вопрос❓')]
], resize_keyboard=True)

KeyboardStart = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Помощь'), KeyboardButton(text='Информация')],
    [KeyboardButton(text='Задать вопрос❓')]
], resize_keyboard=True)

KeyboardInfo = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Помощь'), KeyboardButton(text='Главное меню')],
    [KeyboardButton(text='Задать вопрос❓')]
], resize_keyboard=True)

KeyboardDel = ReplyKeyboardRemove()