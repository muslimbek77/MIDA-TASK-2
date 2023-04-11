from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.menu import start_menu,gruppa_menu,da_net,main_menu
from loader import dp,db,bot
import sqlite3
from data.config import ADMINS
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Добавить пользователя в базу
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)

    await message.answer(text="Привет! Я бот, который поможет тебе выбрать группу по твоим интересам",reply_markup=start_menu)


interes_gr = {
    "Психология":("Вы психолог?","https://t.me/psyhologyiseasy"),
    "Криптовалюта":("Вы торгуете криптовалютой?","https://t.me/kriptovalyuta_efir"),
    "Стартапы":("Вы создаете стартап?","https://t.me/business_startapp")
}

gr_spisok = InlineKeyboardMarkup(inline_keyboard = [
        [InlineKeyboardButton(text=i,url=j[1]) for i,j in interes_gr.items()],
        [
        InlineKeyboardButton(text='Вернуться в меню',callback_data='menu')]
        ]
        )


@dp.callback_query_handler()
async def call_back_query(call:types.CallbackQuery):
    call_data = call.data
    # print(call_data)
    if call_data == "Podobrat-gruppu":
        await call.message.edit_text("Чем вы интересуетесь?",reply_markup=gruppa_menu)
    elif call_data.startswith("gr"):
        text = interes_gr.get(call.data.split('-')[-1])[0]
        await call.message.edit_text(text=text,reply_markup=da_net)
    elif call_data in ['da' ,'net']:
        text = call.message.text
        gr_name = [i for i,j in interes_gr.items() if j[0]==text][0]
        link = interes_gr.get(gr_name)[1]

        await call.message.edit_text(f"Ссылка на чат для <a href='{link}'>{gr_name}</a>",reply_markup=main_menu)
    elif call_data=="menu":
        await call.message.edit_text(text="Привет! Я бот, который поможет тебе выбрать группу по твоим интересам",reply_markup=start_menu)
    elif call_data == "spisok-grupp":
        await call.message.edit_text("Список групп",reply_markup=gr_spisok)




