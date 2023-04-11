from aiogram.types import ReplyKeyboardMarkup,KeyboardButton



adminmenu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Выгрузить пользователей'),
            KeyboardButton(text='Отправить сообщение пользователям'),
        ],
    ],
    resize_keyboard=True
)