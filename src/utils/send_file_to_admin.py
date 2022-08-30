from os import path

from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton 
from loguru import logger

from config import ADMINS_ID
from loader import bot


'''
Ф-ция отправки файла с настройками админу 
'''
@logger.catch
async def send_to_admin(id: int) -> bool:
    file_path = f'./data/settings/{id}.json'
    if not path.exists(file_path):
        logger.error(f'{file_path} not exist')
        return False

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='Ответить', callback_data=f'{id}'))

    with open(file_path, 'r') as file:
        await bot.send_document(ADMINS_ID, file)
        await bot.send_message(ADMINS_ID, f'{id}', reply_markup=markup)

    logger.success(f'{id} settings send')

    return True