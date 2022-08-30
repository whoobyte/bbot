from re import match

from aiogram import types
from loguru import logger

from config.messages import SELECT_USER_SUCCESS
from config import ADMINS_ID
from loader import user_recipient
from loader import dp


'''
По нажатию на кнопку 
Запись id пользователя, которому файл будет отправлен
'''
@logger.catch
@dp.callback_query_handler(lambda call: match(r'^\d{9}$', call.data))
async def _(callback: types.CallbackQuery):
    recipient_id = callback.data

    logger.info(f'ADMIN choose {callback.data}')

    await dp.bot.send_message(
        ADMINS_ID, SELECT_USER_SUCCESS % recipient_id)

    user_recipient[0] = recipient_id
