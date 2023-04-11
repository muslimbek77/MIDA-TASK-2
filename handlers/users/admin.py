import asyncio
from aiogram.dispatcher import FSMContext
from aiogram import types
from keyboards.default.admin_menu import adminmenu
import io
from data.config import ADMINS
from loader import dp, db, bot
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows


@dp.message_handler(commands="admin", user_id=ADMINS)
async def admin_page(message: types.Message):
  await message.answer("Выберите опцию", reply_markup=adminmenu)




@dp.message_handler(text="Выгрузить пользователей", user_id=ADMINS)
async def users_xls(message: types.Message):
    df = db.select_all_users()

    # create a pandas dataframe by selecting data from a table
    df =db.convert_all_users()

    # create a new workbook
    workbook = Workbook()

    # select the active worksheet
    worksheet = workbook.active

    # write the dataframe to the worksheet
    for r in dataframe_to_rows(df, index=False, header=True):
        worksheet.append(r)

    # save the workbook to a bytes buffer
    buffer = io.BytesIO()
    workbook.save(buffer)
    buffer.seek(0)
    file = types.InputFile(buffer, filename='users.xlsx')

    # send the file to the user
    await message.answer_document(document=file)

  

@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    print(users[0][0])
    await message.answer(users)



@dp.message_handler(text="/cleandb", user_id=ADMINS)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("База очищена!")







@dp.message_handler(text="Отправить сообщение пользователям")
async def send_ad_command(message: types.Message, state: FSMContext):
    await message.answer("Введите сообщение...")
    await state.set_state("advertisement")


@dp.message_handler(state = "advertisement", content_types=types.ContentType.ANY)
async def sending_advert(message: types.Message, state: FSMContext):
    await state.finish()
    users =  db.select_all_users()
    count = db.count_users()
        
    for user in users:
        user_id = user[0]
        try:
            await bot.copy_message(user_id, message.chat.id, message.message_id, reply_markup=message.reply_markup)
            await asyncio.sleep(0.05)
        except:
            pass

    await message.answer(f"Объявления отправлены {count[0]} пользователям.")
        

# Reklama yuborish  